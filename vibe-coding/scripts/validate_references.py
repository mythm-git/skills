#!/usr/bin/env python3
"""Check repository-local Markdown links and portable internal paths."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="skill directory")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    referenced: set[Path] = set()
    excluded_runtime_roots = {
        ("verification", "fixtures"), ("verification", "workspaces"),
        ("verification", "logs"), ("verification", "artifacts"),
        ("verification", "agent-home"),
    }
    for document in root.rglob("*.md"):
        relative_parts = document.relative_to(root).parts
        if any(part.startswith(".") for part in relative_parts) or any(relative_parts[:len(prefix)] == prefix for prefix in excluded_runtime_roots):
            continue
        text = document.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if "://" in target or target.startswith("#"):
                continue
            if "\\" in target or Path(target).is_absolute():
                errors.append(f"{document.relative_to(root)} uses non-portable link: {target}")
                continue
            resolved = (document.parent / target).resolve()
            if not resolved.is_file():
                errors.append(f"{document.relative_to(root)} has broken link: {target}")
            else:
                referenced.add(resolved)
    reference_dir = root / "references"
    if reference_dir.is_dir():
        for item in reference_dir.glob("*.md"):
            if item.resolve() not in referenced and item.name not in {"coding-standards.md"}:
                errors.append(f"orphaned reference: references/{item.name}")
    if errors:
        print("REFERENCE VALIDATION FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("REFERENCE VALIDATION PASSED: internal links resolve and paths are portable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
