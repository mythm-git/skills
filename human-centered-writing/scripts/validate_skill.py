"""Validate the local skill structure without network access or third-party dependencies."""

from __future__ import annotations

import logging
from pathlib import Path
import sys

LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    ".gitignore",
    ".env.example",
    "pyproject.toml",
    "CHANGELOG.md",
    "LICENSE",
    "docs/research-notes.md",
    "docs/model-testing.md",
    "scripts/run_model_comparisons.py",
    "scripts/package_skill.py",
    "tests/test_model_comparisons.py",
    "tests/test-cases/model_comparison_cases.json",
    "references/configuration.md",
    "references/ai-writing-patterns.md",
    "references/punctuation-and-formatting.md",
    "references/style-profiles.md",
    "references/voice-preservation.md",
    "references/quality-rubric.md",
    "examples/before-after.md",
    "tests/test-cases/writing_cases.json",
    "adapters/codex/SKILL.md",
    "adapters/claude-code/SKILL.md",
)
REQUIRED_CORE_PHRASES = (
    "## Purpose and activation",
    "Generation mode",
    "Humanization mode",
    "## Core workflow",
    "## Voice and semantic integrity",
    "## Quality gate",
    "## Safety boundary",
    "Do not optimize text to avoid AI detectors",
)


def configure_logging() -> None:
    """Configure concise local logging without recording document content."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def validate_project(root: Path) -> list[str]:
    """Return validation errors for the project rooted at *root*."""
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (root / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        content = skill_path.read_text(encoding="utf-8")
        for phrase in REQUIRED_CORE_PHRASES:
            if phrase not in content:
                errors.append(f"Core skill instruction is missing: {phrase}")

    return errors


def main() -> int:
    """Run validation and return a process status without exposing user text."""
    configure_logging()
    errors = validate_project(PROJECT_ROOT)
    if errors:
        for error in errors:
            LOGGER.error(error)
        return 1
    LOGGER.info("Skill structure validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
