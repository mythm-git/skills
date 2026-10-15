#!/usr/bin/env python3
"""Deterministic security posture checks for this skill repository, not applications."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="skill directory")
    args = parser.parse_args()
    root = args.root.resolve()
    checks = {
        ".gitignore excludes .env": ".env" in (root / ".gitignore").read_text(encoding="utf-8"),
        ".gitignore permits .env.example": "!.env.example" in (root / ".gitignore").read_text(encoding="utf-8"),
        "security reference rejects embedded instruction trust": "untrusted" in (root / "references/risk-assessment.md").read_text(encoding="utf-8").lower(),
        "authentication reference requires server-side authorization": "server-side" in (root / "references/authentication.md").read_text(encoding="utf-8").lower(),
        "verification reference prohibits blanket secure claims": "blanket" in (root / "references/verification.md").read_text(encoding="utf-8").lower(),
    }
    failed = [name for name, result in checks.items() if not result]
    print("SECURITY AUDIT: checked repository hygiene and explicit skill safeguards.")
    for name, result in checks.items():
        print(f"- {'PASS' if result else 'FAIL'}: {name}")
    if failed:
        return 1
    print("Note: this is not a dependency, runtime, or deployment vulnerability scanner.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
