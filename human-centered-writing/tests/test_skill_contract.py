"""Structural and deterministic checks for the skill corpus.

These tests validate skill assets and test specifications. They do not claim to
measure subjective prose quality or execute any external model.
"""

from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "tests" / "test-cases" / "writing_cases.json"
REQUIRED_CONTEXTS = {
    "casual conversation", "professional email", "professional German email",
    "German B1 communication", "job application", "academic explanation",
    "scientific paragraph", "software documentation", "programming explanation",
    "marketing advertisement", "social media caption", "no-change",
    "financial data", "citations and quotations", "strict formatting",
}
PROTECTED_CASES = {
    "software-docs": "`npm test`",
    "numbers": "€1,250.50",
    "citations": "(Lee, 2025, p. 4)",
    "strict-format": "| Item | Value |",
}


def load_cases() -> list[dict[str, str]]:
    """Load the local, declarative representative case corpus."""
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))


class SkillContractTests(unittest.TestCase):
    """Verify required coverage and deterministic preservation fixtures."""

    def test_case_corpus_has_at_least_thirty_cases(self) -> None:
        self.assertGreaterEqual(len(load_cases()), 30)

    def test_case_ids_are_unique_and_complete(self) -> None:
        cases = load_cases()
        identifiers = [case["id"] for case in cases]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        for case in cases:
            self.assertEqual(set(case), {"id", "context", "operation", "input", "expectation"})
            self.assertIn(case["operation"], {"generate", "humanize"})
            self.assertTrue(case["input"].strip())
            self.assertTrue(case["expectation"].strip())

    def test_required_contexts_are_represented(self) -> None:
        contexts = {case["context"] for case in load_cases()}
        self.assertTrue(REQUIRED_CONTEXTS.issubset(contexts))

    def test_protected_fixture_strings_are_present(self) -> None:
        cases = {case["id"]: case for case in load_cases()}
        for identifier, protected_text in PROTECTED_CASES.items():
            self.assertIn(protected_text, cases[identifier]["input"])

    def test_editorial_claims_are_labeled_as_non_automated(self) -> None:
        rubric = (ROOT / "references" / "quality-rubric.md").read_text(encoding="utf-8")
        self.assertIn("not a scientific detector", rubric)
        self.assertIn("Do not infer authorship", rubric)


if __name__ == "__main__":
    unittest.main()
