from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
    def test_release_files_and_directories_exist(self):
        for name in ["SKILL.md", "README.md", "SUMMARY.md", "CHANGELOG.md", "LICENSE", ".gitignore", ".env.example", "references", "scripts", "templates", "tests", "examples", "docs"]:
            self.assertTrue((ROOT / name).exists(), name)

    def test_release_metadata_is_present(self):
        self.assertTrue((ROOT / "CHANGELOG.md").is_file())
        self.assertIn("[0.2.0]", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_ignore_file_protects_secrets_and_artifacts(self):
        ignored = (ROOT / ".gitignore").read_text(encoding="utf-8")
        for pattern in [".env", "!.env.example", "*.pem", "__pycache__/", "*.log"]:
            self.assertIn(pattern, ignored)
