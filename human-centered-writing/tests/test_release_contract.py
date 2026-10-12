"""Release-facing checks for public package content and documentation."""

from __future__ import annotations

from pathlib import Path

import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReleaseContractTests(unittest.TestCase):
    def test_release_version_is_consistent(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn("Version 0.3.1", readme)
        self.assertIn("## 0.3.1", changelog)
        self.assertIn('version = "0.3.1"', pyproject)

    def test_release_files_and_readme_commands_exist(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        expected = (
            "SKILL.md", "LICENSE", "references/configuration.md",
            "scripts/validate_skill.py", "scripts/run_model_comparisons.py",
            "scripts/package_skill.py", "docs/model-testing.md",
        )
        for relative_path in expected:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)
            self.assertIn(relative_path, readme)

    def test_public_docs_have_no_local_username_path(self) -> None:
        published_paths = (
            ROOT / "README.md", ROOT / "SKILL.md", ROOT / "CHANGELOG.md",
            ROOT / "docs" / "model-testing.md",
        )
        for path in published_paths:
            self.assertNotIn("C:\\\\Users\\\\maitham", path.read_text(encoding="utf-8"))
            self.assertNotIn("C:/Users/maitham", path.read_text(encoding="utf-8"))

    def test_mit_license_is_declared(self) -> None:
        self.assertTrue((ROOT / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"))


if __name__ == "__main__":
    unittest.main()
