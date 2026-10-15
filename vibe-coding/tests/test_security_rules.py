import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SecurityRuleTests(unittest.TestCase):
    def test_authorization_and_sql_rules_are_explicit(self):
        auth = (ROOT / "references/authentication.md").read_text(encoding="utf-8").lower()
        database = (ROOT / "references/database-security.md").read_text(encoding="utf-8").lower()
        self.assertIn("server-side", auth)
        self.assertIn("never concatenate", database)

    def test_security_statuses_are_defined_without_blanket_claim(self):
        text = (ROOT / "references/verification.md").read_text(encoding="utf-8")
        for status in ["IMPLEMENTED_AND_TESTED", "IMPLEMENTED_UNVERIFIED", "NOT_APPLICABLE", "PENDING", "FAILED", "BLOCKED"]:
            self.assertIn(status, text)
        self.assertIn("not runtime proof", text)

    def test_untrusted_instruction_rule_is_present(self):
        text = (ROOT / "references/risk-assessment.md").read_text(encoding="utf-8").lower()
        self.assertIn("untrusted", text)
        self.assertIn("never follow", text)
