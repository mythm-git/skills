#!/usr/bin/env python3
"""Validate the portable structure and constrained YAML frontmatter of this skill."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter delimiters")
    values: dict[str, str] = {}
    lines = match.group(1).splitlines()
    for index, line in enumerate(lines):
        if not line.strip() or line.startswith(" "):
            continue  # nested metadata is allowed but not required by the standard.
        key, separator, value = line.partition(":")
        if not separator or not key:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        if not value.strip() and not any(next_line.startswith(" ") for next_line in lines[index + 1 : index + 2]):
            raise ValueError(f"empty frontmatter value: {line!r}")
        values[key.strip()] = value.strip().strip('"')
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="skill directory (default: repository root)")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    for relative in ("SKILL.md", "README.md", "SUMMARY.md", "LICENSE", ".gitignore", ".env.example"):
        if not (root / relative).is_file():
            errors.append(f"missing required release file: {relative}")
    skill = root / "SKILL.md"
    if skill.is_file():
        try:
            data = frontmatter(skill)
            for key in ("name", "description"):
                if not data.get(key):
                    errors.append(f"frontmatter missing {key}")
            if data.get("name") != root.name:
                errors.append(f"frontmatter name must equal directory name ({root.name})")
            if data.get("name") and not NAME_RE.fullmatch(data["name"]):
                errors.append("frontmatter name must be lowercase hyphen-case")
            if len(data.get("name", "")) > 64:
                errors.append("frontmatter name exceeds 64 characters")
        except ValueError as exc:
            errors.append(f"SKILL.md: {exc}")
    required_refs = {"requirements.md", "architecture.md", "security.md", "testing.md", "verification.md", "delivery.md"}
    present_refs = {item.name for item in (root / "references").glob("*.md")} if (root / "references").is_dir() else set()
    errors.extend(f"missing required reference: references/{name}" for name in sorted(required_refs - present_refs))
    if errors:
        print("VALIDATION FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("VALIDATION PASSED: skill structure and frontmatter are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
