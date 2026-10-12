"""Tests for the local, offline project validator."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from scripts.validate_skill import REQUIRED_CORE_PHRASES, REQUIRED_FILES, validate_project


class ValidateProjectTests(unittest.TestCase):
    """Verify structural and safety-oriented validation behavior."""

    def test_current_project_is_valid(self) -> None:
        """The shipped project should satisfy its own required structure."""
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(validate_project(root), [])

    def test_missing_required_file_is_reported(self) -> None:
        """A missing file must result in a clear validation error."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            errors = validate_project(Path(temporary_directory))
        self.assertIn(f"Missing required file: {REQUIRED_FILES[0]}", errors)

    def test_missing_core_instruction_is_reported(self) -> None:
        """A structurally complete but incomplete skill must fail validation."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for relative_path in REQUIRED_FILES:
                path = root / relative_path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("placeholder", encoding="utf-8")
            errors = validate_project(root)
        self.assertIn(f"Core skill instruction is missing: {REQUIRED_CORE_PHRASES[0]}", errors)


if __name__ == "__main__":
    unittest.main()
