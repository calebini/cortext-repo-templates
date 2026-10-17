#!/usr/bin/env python3
"""Check the seed repository's authoritative mobile-app structure."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", "README.md", "profile/README.md", "specs/repo-standard.md",
    "specs/overview.md", "specs/architecture.md", "specs/interfaces.md",
    "specs/lifecycle.md", "specs/security-privacy.md", "specs/testing.md",
    "specs/release.md", "specs/accessibility-localization.md",
    "specs/compatibility.md", "contracts/README.md", "SECURITY.md",
)


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))
    unresolved = []
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                continue
            if "{" * 2 in text or "}" * 2 in text:
                unresolved.append(str(path.relative_to(ROOT)))
    if unresolved:
        raise SystemExit("Unresolved template tokens: " + ", ".join(unresolved))
    print("repository structure verification passed")


if __name__ == "__main__":
    main()
