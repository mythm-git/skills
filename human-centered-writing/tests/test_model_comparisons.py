"""Deterministic tests for the paired model-comparison harness."""

from __future__ import annotations

import json
from pathlib import Path
import unittest

from scripts.run_model_comparisons import (
    CASES_PATH,
    SYSTEM_BASELINE,
    load_cases,
    prompt_for,
    protected_results,
    skill_instruction,
    validate_cases,
)


class ModelComparisonTests(unittest.TestCase):
    def test_corpus_has_representative_paired_cases(self) -> None:
        cases = load_cases()
        self.assertGreaterEqual(len(cases), 20)
        self.assertEqual(validate_cases(cases), [])
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertEqual({case["mode"] for case in cases}, {"generate", "humanize"})

    def test_cases_include_required_risk_coverage(self) -> None:
        cases = {case["id"]: case for case in load_cases()}
        for identifier in (
            "german-sie", "application-sparse", "software-command",
            "academic-qualification", "financial-values", "strict-table",
            "code-switching", "no-change", "conflicting-brief",
        ):
            self.assertIn(identifier, cases)

    def test_prompt_has_no_skill_instruction_in_baseline(self) -> None:
        case = load_cases()[0]
        prompt = prompt_for(case)
        self.assertIn(case["request"], prompt)
        self.assertNotIn("Human-Centered Writing", SYSTEM_BASELINE)
        self.assertIn("Human-Centered Writing", skill_instruction())

    def test_protected_string_checks_are_literal_and_auditable(self) -> None:
        self.assertEqual(protected_results("Run `npm test`.", ["`npm test`"]), {"`npm test`": True})
        self.assertEqual(protected_results("Run tests.", ["`npm test`"]), {"`npm test`": False})

    def test_case_file_is_json_array(self) -> None:
        self.assertIsInstance(json.loads(Path(CASES_PATH).read_text(encoding="utf-8")), list)


if __name__ == "__main__":
    unittest.main()
