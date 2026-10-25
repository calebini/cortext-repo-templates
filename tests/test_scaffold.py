import importlib.util
import json
import re
import ast
from pathlib import Path
import tempfile
import subprocess
import sys
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('scaffold', ROOT / 'scripts/scaffold.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ScaffoldTests(unittest.TestCase):
    def test_display_names_preserve_values_in_python_and_toml(self):
        names = ['My "Quoted" Service', "Owner's Service", 'Triple """ quote',
                 'Path \\ service', 'Line\nBreak\tService', 'Café 🚀', 'Delete\x7fCharacter']
        for name in names:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / 'sample'
                MODULE.scaffold('component', 'sample', target, display_name=name)
                metadata = tomllib.loads((target / 'pyproject.toml').read_text())
                self.assertEqual(metadata['project']['description'], name)
                for source in (target / 'src').rglob('*.py'):
                    ast.parse(source.read_text(), filename=str(source))
                cli = target / 'src/sample/cli.py'
                result = subprocess.run([sys.executable, '-X', 'utf8', str(cli)],
                                        capture_output=True, encoding='utf-8')
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, name + '\n')

    def test_all_profiles_share_tracking_and_keep_platform_boundaries(self):
        for profile, platform in [('component', None), ('go', None), *[('mobile', p) for p in MODULE.PLATFORMS]]:
            with self.subTest(profile=profile, platform=platform), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / 'sample'
                MODULE.scaffold(profile, 'sample-app', target, platform=platform, display_name='Sample App')
                for name in ('roadmap.md', 'implementation-plan.md', 'work-tracking.md'):
                    self.assertEqual((target / 'docs' / name).read_bytes(), (ROOT / 'base/docs' / name).read_bytes())
                agents = (target / 'AGENTS.md').read_text()
                self.assertIn('Shared Cortext Working Conventions', agents)
                self.assertIn('transient', agents)
                self.assertTrue((target / 'specs/decisions').is_dir())
                self.assertFalse((target / 'docs/backlog.md').exists())
                for name in ('README.md', 'AGENTS.md', 'specs/repo-standard.md',
                             'docs/work-tracking.md'):
                    self.assertIn('specs/HLD.md', (target / name).read_text(), name)
                # Every link in the generated workflow and HLD must resolve.
                for name in ('README.md', 'specs/HLD.md', 'docs/roadmap.md',
                             'docs/implementation-plan.md'):
                    source = target / name
                    for link in re.findall(r'\]\(([^)]+)\)', source.read_text()):
                        self.assertTrue((source.parent / link).exists(), (name, link))
                for file in target.rglob('*'):
                    if file.is_file():
                        self.assertNotIn('{{', file.read_text(), str(file))
                if profile == 'component':
                    self.assertTrue((target / 'src/sample_app/cli.py').is_file())
                    self.assertFalse((target / 'app').exists())
                elif profile == 'go':
                    for name in ('main.go', '.go-version', '.github/workflows/go.yml',
                                 'docs/development.md'):
                        self.assertTrue((target / name).is_file(), name)
                    for name in ('pyproject.toml', 'src', 'app', 'go.mod', 'go.sum',
                                 'contracts', 'internal', 'cmd'):
                        self.assertFalse((target / name).exists(), name)
                    self.assertIn('sample-app', (target / 'main.go').read_text())
                    self.assertTrue(agents.startswith((ROOT / 'base/AGENTS.md').read_text() + '\n'))
                    for source in target.rglob('*.md'):
                        for link in re.findall(r'\]\(([^)]+)\)', source.read_text()):
                            if '://' not in link and not link.startswith('#'):
                                self.assertTrue((source.parent / link.split('#')[0]).exists(),
                                                (source, link))
                else:
                    self.assertFalse((target / 'pyproject.toml').exists())
                    self.assertTrue((target / 'profile/README.md').is_file())
                    self.assertTrue((target / 'specs/security-privacy.md').is_file())
                    for layout in MODULE.PLATFORMS[platform]:
                        self.assertTrue((target / layout).is_dir())
                    result = subprocess.run([sys.executable, 'scripts/verify_repo.py'],
                                            cwd=target, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    # These are required documents, not optional HLD replacements.
                    for name in ('specs/HLD.md', 'docs/roadmap.md',
                                 'docs/implementation-plan.md', 'specs/lifecycle.md',
                                 'specs/security-privacy.md', 'specs/testing.md',
                                 'specs/release.md', 'specs/accessibility-localization.md',
                                 'specs/compatibility.md'):
                        document = target / name
                        content = document.read_bytes()
                        document.unlink()
                        result = subprocess.run([sys.executable, 'scripts/verify_repo.py'],
                                                cwd=target, capture_output=True, text=True)
                        self.assertNotEqual(result.returncode, 0, name)
                        self.assertIn(name, result.stdout + result.stderr)
                        document.write_bytes(content)

    def test_provenance_is_identical_across_destinations_and_portable(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = [MODULE.scaffold('component', 'sample', Path(tmp) / name) for name in ('one', 'two')]
            self.assertEqual(results[0], results[1])
            self.assertNotIn(tmp, json.dumps(results))
            self.assertEqual(len(results[0]['source_digest']), 64)

    def test_go_profile_provenance_tracks_profile_content(self):
        import shutil
        with tempfile.TemporaryDirectory() as tmp:
            template = Path(tmp) / 'template'
            shutil.copytree(ROOT / 'base', template / 'base')
            shutil.copytree(ROOT / 'profiles/go', template / 'profiles/go')
            (template / 'scripts').mkdir()
            shutil.copy(ROOT / 'scripts/scaffold.py', template / 'scripts/scaffold.py')
            shutil.copy(ROOT / 'VERSION', template / 'VERSION')
            first = MODULE.scaffold('go', 'sample', Path(tmp) / 'one', template_root=template)
            second = MODULE.scaffold('go', 'sample', Path(tmp) / 'two', template_root=template)
            self.assertEqual(first, second)
            self.assertEqual(first['profile'], 'go')
            self.assertIsNone(first['platform'])
            self.assertNotIn(tmp, json.dumps(first))
            (template / 'profiles/go/.go-version').write_text('1.27.4\n')
            third = MODULE.scaffold('go', 'sample', Path(tmp) / 'three', template_root=template)
            self.assertNotEqual(first['source_digest'], third['source_digest'])

    def test_language_options_are_scoped_to_their_profiles(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'output'
            for profile in ('go', 'mobile'):
                with self.subTest(profile=profile), self.assertRaisesRegex(ValueError, 'Package name'):
                    MODULE.scaffold(profile, 'sample', target, package_name='sample',
                                    platform='ios-swift' if profile == 'mobile' else None)
                self.assertFalse(target.exists())
            for profile in ('go', 'component'):
                with self.subTest(profile=profile), self.assertRaisesRegex(ValueError, 'platform'):
                    MODULE.scaffold(profile, 'sample', target, platform='ios-swift')
                self.assertFalse(target.exists())
            with self.assertRaisesRegex(ValueError, 'Python identifier'):
                MODULE.scaffold('component', 'class', target)
            # A Python keyword is an ordinary Go project slug.
            MODULE.scaffold('go', 'class', target)
            self.assertTrue((target / 'main.go').is_file())

    def test_refuses_existing_work_and_invalid_input_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'existing'
            target.mkdir()
            (target / 'precious').write_text('retain')
            with self.assertRaises(ValueError):
                MODULE.scaffold('component', 'sample', target)
            self.assertEqual(list(target.iterdir()), [target / 'precious'])
            for slug in ('../escape', '/absolute', 'bad/name', 'UPPER'):
                with self.assertRaises(ValueError):
                    MODULE.scaffold('component', slug, Path(tmp) / 'new')
            with self.assertRaises(ValueError):
                MODULE.scaffold('mobile', 'sample', Path(tmp) / 'new')
            self.assertFalse((Path(tmp) / 'new').exists())

    def test_profile_cannot_override_shared_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'template'
            (source / 'base/docs').mkdir(parents=True)
            (source / 'profiles/component/docs').mkdir(parents=True)
            (source / 'base/docs/roadmap.md').write_text('shared')
            (source / 'profiles/component/docs/roadmap.md').write_text('override')
            target = Path(tmp) / 'output'
            with self.assertRaisesRegex(ValueError, 'collides'):
                MODULE.scaffold('component', 'sample', target, template_root=source)
            self.assertFalse(target.exists())


if __name__ == '__main__':
    unittest.main()
