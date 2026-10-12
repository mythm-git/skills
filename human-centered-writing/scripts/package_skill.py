"""Build the local distributable ZIP without generated caches or nested archives."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent / "human-centered-writing-ready.zip"
EXCLUDED_PARTS = {"__pycache__", "reports", ".git"}


def include(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return not any(part in EXCLUDED_PARTS for part in relative.parts) and path.suffix != ".zip"


def main() -> None:
    files = sorted(path for path in ROOT.rglob("*") if path.is_file() and include(path))
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())
    print(f"Packaged {len(files)} files to {OUTPUT}")


if __name__ == "__main__":
    main()
