import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_skill  # noqa: E402


class FrontmatterTests(unittest.TestCase):
    def test_required_metadata_is_present_and_consistent(self):
        data = validate_skill.frontmatter(ROOT / "SKILL.md")
        self.assertEqual(data["name"], "vibe-coding")
        self.assertTrue(data["description"])
        self.assertIn("metadata", data)

    def test_skill_body_uses_progressive_reference_routing(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/security.md", text)
        self.assertIn("Any meaningful change | [security applicability]", text)
        self.assertIn("Medium/high risk or unclear acceptance criteria | [requirements]", text)
        self.assertIn("[security applicability](references/security.md)", text)
        self.assertIn("references/verification.md", text)
        self.assertLess(len(text.splitlines()), 220)
