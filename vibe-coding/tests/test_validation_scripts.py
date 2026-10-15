import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ValidationScriptTests(unittest.TestCase):
    def test_help_is_available(self):
        for script in ["validate_skill.py", "validate_references.py", "check_secrets.py", "security_audit.py"]:
            result = subprocess.run([sys.executable, f"scripts/{script}", "--help"], cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, script)

    def test_all_repository_validators_succeed(self):
        for script in ["validate_skill.py", "validate_references.py", "check_secrets.py", "security_audit.py"]:
            result = subprocess.run([sys.executable, f"scripts/{script}"], cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, f"{script}: {result.stdout}{result.stderr}")
