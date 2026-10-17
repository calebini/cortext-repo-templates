#!/usr/bin/env python3
"""Compose a portable Cortext repository from shared base and one profile."""
from __future__ import annotations

import argparse
import hashlib
import json
import keyword
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = {
    'ios-swift': ('app/ios', 'core'),
    'android-kotlin': ('app/android', 'core'),
    'cross-platform': ('app/shared', 'app/ios', 'app/android', 'core'),
}
SKIP = {'.git', '__pycache__', '.pytest_cache', '.DS_Store'}
LINKS = '''
## Work Tracking

- [Backlog](docs/backlog.md): future ideas and pipeline work.
- [Implementation plan](docs/implementation-plan.md): durable delivery and next steps.
- [Decision records](specs/decisions/): choices, rationale and consequences.
- [Shared convention](docs/work-tracking.md): responsibilities and transient handoffs.
'''


def source_files(directory: Path) -> list[Path]:
    return sorted(p for p in directory.rglob('*')
                  if p.is_file() and not any(part in SKIP for part in p.relative_to(directory).parts))


def scaffold(profile: str, slug: str, destination: Path, *, platform: str | None = None,
             display_name: str | None = None, package_name: str | None = None,
             template_root: Path = ROOT) -> dict:
    if profile not in {'component', 'mobile'}:
        raise ValueError('Unknown profile')
    if not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', slug):
        raise ValueError('Slug must be lowercase words separated by hyphens')
    package = package_name or slug.replace('-', '_')
    if not package.isidentifier() or keyword.iskeyword(package):
        raise ValueError('Package name must be a Python identifier')
    if profile == 'mobile' and platform not in PLATFORMS:
        raise ValueError('Mobile profile requires a supported platform')
    if profile == 'component' and platform is not None:
        raise ValueError('Component profile does not take a platform')
    if profile == 'mobile' and package_name is not None:
        raise ValueError('Package name applies only to the component profile')
    if destination.is_symlink():
        raise ValueError('Destination cannot be a symlink')
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError('Refusing to write into a non-empty destination')
    tokens = {
        '{{component_slug}}': slug, '{{package_name}}': package,
        '{{Component Name}}': display_name or slug,
        '{{app_slug}}': slug, '{{App Name}}': display_name or slug,
        '{{platform_profile}}': platform or '',
    }

    def render(text: str) -> str:
        for token, value in tokens.items():
            text = text.replace(token, value)
        return text

    output: dict[str, bytes] = {}
    manifest = []
    for layer in ('base', f'profiles/{profile}'):
        directory = template_root / layer
        for source in source_files(directory):
            relative = source.relative_to(directory)
            if relative.parts[0] == 'profiles':
                continue
            if source.is_symlink():
                raise ValueError('Template symlinks are unsupported')
            raw = source.read_bytes()
            manifest.append({'path': f'{layer}/{relative.as_posix()}',
                             'sha256': hashlib.sha256(raw).hexdigest()})
            name = render(relative.as_posix())
            try:
                value = render(raw.decode('utf-8')).encode('utf-8')
            except UnicodeDecodeError:
                value = raw
            if name in output:
                if name != 'AGENTS.md':
                    raise ValueError(f'Profile collides with shared file: {name}')
                value = output[name] + b'\n' + value
            output[name] = value
    if profile == 'mobile':
        source = template_root / 'profiles/mobile/profiles' / str(platform) / 'README.md'
        raw = source.read_bytes()
        manifest.append({'path': f'profiles/mobile/profiles/{platform}/README.md',
                         'sha256': hashlib.sha256(raw).hexdigest()})
        output['profile/README.md'] = render(raw.decode()).encode()
        for layout in PLATFORMS[str(platform)]:
            output[f'{layout}/.gitkeep'] = b''
    output['specs/decisions/.gitkeep'] = b''
    output['README.md'] += LINKS.encode()
    version = (template_root / 'VERSION').read_text().strip()
    manifest.append({'path': 'VERSION', 'sha256': hashlib.sha256(version.encode()).hexdigest()})
    generator = template_root / 'scripts/scaffold.py'
    manifest.append({'path': 'scripts/scaffold.py',
                     'sha256': hashlib.sha256(generator.read_bytes()).hexdigest()})
    preimage = json.dumps(sorted(manifest, key=lambda x: x['path']),
                          sort_keys=True, separators=(',', ':')).encode()
    provenance = {'format_version': 1, 'template': 'cortext-repo-templates',
                  'template_version': version, 'profile': profile, 'platform': platform,
                  'source_digest': hashlib.sha256(preimage).hexdigest()}
    output['.cortext-template.json'] = (json.dumps(provenance, indent=2, sort_keys=True) + '\n').encode()
    # Validate all rendered paths before any output is created.
    for name in output:
        path = Path(name)
        if path.is_absolute() or '..' in path.parts or '{{' in name:
            raise ValueError('Invalid rendered template path')
    for name, raw in output.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream:
            stream.write(raw)
    return provenance


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profile', choices=['component', 'mobile'])
    parser.add_argument('slug')
    parser.add_argument('destination', type=Path)
    parser.add_argument('--platform', choices=sorted(PLATFORMS))
    parser.add_argument('--display-name')
    parser.add_argument('--package-name')
    args = parser.parse_args()
    try:
        result = scaffold(args.profile, args.slug, args.destination,
                          platform=args.platform, display_name=args.display_name,
                          package_name=args.package_name)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
