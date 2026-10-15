#!/usr/bin/env python3
"""Conservative secret-pattern scan; findings are redacted and require review."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "generic assigned secret": re.compile(r"(?i)(?:api[_-]?key|secret|password|token)\s*[:=]\s*[\"'](?!replace_me|example|placeholder)[^\"'\s]{12,}"),
}
SKIP = {".git", "__pycache__", ".venv", "venv", "dist", "build"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="directory to scan")
    args = parser.parse_args()
    findings: list[str] = []
    for path in args.root.resolve().rglob("*"):
        if not path.is_file() or any(part in SKIP for part in path.parts) or path.suffix in {".pyc", ".pfx", ".p12"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in PATTERNS.items():
            for number, line in enumerate(text.splitlines(), 1):
                if pattern.search(line):
                    findings.append(f"{path.relative_to(args.root)}:{number}: possible {label} (value redacted)")
    if findings:
        print("SECRET SCAN FAILED: review and remove or explicitly suppress false positives.")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    print("SECRET SCAN PASSED: no configured secret patterns found (not a complete guarantee).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
