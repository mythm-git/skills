import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReferenceTests(unittest.TestCase):
    def test_reference_validator_succeeds(self):
        result = subprocess.run([sys.executable, "scripts/validate_references.py"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_applicability_matrix_distinguishes_local_and_web(self):
        text = (ROOT / "references/security.md").read_text(encoding="utf-8")
        self.assertIn("Local CLI", text)
        self.assertIn("CORS", text)
        self.assertIn("REQUIRES_FURTHER_INFORMATION", text)
