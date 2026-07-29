#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PUBLIC_FILES = (
    ROOT / "profile" / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "SUPPORT.md",
    ROOT / "GOVERNANCE.md",
    ROOT / "CODE_OF_CONDUCT.md",
)
FORBIDDEN = (
    "CER-",
    "PR #",
    ".claude/",
    "localhost",
    "http://",
)
EXPECTED_PROFILE_LINKS = (
    "https://certiv.ai/",
    "https://certiv.ai/product/",
    "https://certiv.ai/tools/",
    "https://github.com/Certiv-ai/certiv-labs",
    "https://pypi.org/project/certiv/",
)


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def check_relative_links(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip()
            if (
                "://" in target
                or target.startswith("#")
                or target.startswith("mailto:")
            ):
                continue
            relative_target = target.split("#", 1)[0].split("?", 1)[0]
            resolved = (path.parent / relative_target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: relative link does not resolve: {target}"
                )


def check_public_copy(errors: list[str]) -> None:
    for path in PUBLIC_FILES:
        text = path.read_text(encoding="utf-8")
        for forbidden in FORBIDDEN:
            if forbidden in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: contains forbidden reference {forbidden!r}"
                )


def check_profile_destinations(errors: list[str]) -> None:
    profile = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    for expected in EXPECTED_PROFILE_LINKS:
        if expected not in profile:
            errors.append(f"profile/README.md: missing expected destination {expected}")


def main() -> int:
    errors: list[str] = []
    check_relative_links(errors)
    check_public_copy(errors)
    check_profile_destinations(errors)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"Validated {len(markdown_files())} Markdown files and organization profile destinations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
