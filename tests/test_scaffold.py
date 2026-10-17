import importlib.util
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('scaffold', ROOT / 'scripts/scaffold.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ScaffoldTests(unittest.TestCase):
    def test_all_profiles_share_tracking_and_keep_platform_boundaries(self):
        for profile, platform in [('component', None), *[('mobile', p) for p in MODULE.PLATFORMS]]:
            with self.subTest(profile=profile, platform=platform), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / 'sample'
                MODULE.scaffold(profile, 'sample-app', target, platform=platform, display_name='Sample App')
                for name in ('backlog.md', 'implementation-plan.md', 'work-tracking.md'):
                    self.assertEqual((target / 'docs' / name).read_bytes(), (ROOT / 'base/docs' / name).read_bytes())
                agents = (target / 'AGENTS.md').read_text()
                self.assertIn('Shared Cortext Working Conventions', agents)
                self.assertIn('transient', agents)
                self.assertTrue((target / 'specs/decisions').is_dir())
                for file in target.rglob('*'):
                    if file.is_file():
                        self.assertNotIn('{{', file.read_text(), str(file))
                if profile == 'component':
                    self.assertTrue((target / 'src/sample_app/cli.py').is_file())
                    self.assertFalse((target / 'app').exists())
                else:
                    self.assertFalse((target / 'pyproject.toml').exists())
                    self.assertTrue((target / 'profile/README.md').is_file())
                    self.assertTrue((target / 'specs/security-privacy.md').is_file())
                    for layout in MODULE.PLATFORMS[platform]:
                        self.assertTrue((target / layout).is_dir())
                    result = subprocess.run([sys.executable, 'scripts/verify_repo.py'],
                                            cwd=target, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_provenance_is_identical_across_destinations_and_portable(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = [MODULE.scaffold('component', 'sample', Path(tmp) / name) for name in ('one', 'two')]
            self.assertEqual(results[0], results[1])
            self.assertNotIn(tmp, json.dumps(results))
            self.assertEqual(len(results[0]['source_digest']), 64)

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
            (source / 'base/docs/backlog.md').write_text('shared')
            (source / 'profiles/component/docs/backlog.md').write_text('override')
            target = Path(tmp) / 'output'
            with self.assertRaisesRegex(ValueError, 'collides'):
                MODULE.scaffold('component', 'sample', target, template_root=source)
            self.assertFalse(target.exists())


if __name__ == '__main__':
    unittest.main()
