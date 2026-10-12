"""Run paired, reproducible model comparisons for the writing skill.

This script uses only the Python standard library. It needs an OpenAI-compatible
chat-completions endpoint and OPENAI_API_KEY; it never prints the key. Each case
uses the same model and request parameters for baseline and skill-enabled runs.
Results contain raw outputs plus deterministic protected-string checks. Editorial
scores remain a documented human review, not an authorship or detector claim.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "tests" / "test-cases" / "model_comparison_cases.json"
DEFAULT_OUTPUT = ROOT / "reports" / "model-comparison-results.json"
SYSTEM_BASELINE = "You are a helpful writing assistant. Follow the user's request accurately."
REFERENCE_NAMES = (
    "ai-writing-patterns.md",
    "punctuation-and-formatting.md",
    "style-profiles.md",
    "voice-preservation.md",
    "quality-rubric.md",
)


def load_cases() -> list[dict[str, Any]]:
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))


def skill_instruction() -> str:
    """Load the canonical skill and its revision-relevant guidance."""
    parts = [(ROOT / "SKILL.md").read_text(encoding="utf-8")]
    for name in REFERENCE_NAMES:
        parts.append((ROOT / "references" / name).read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def prompt_for(case: dict[str, Any]) -> str:
    return f"Context: {case['context']}\nOperation: {case['mode']}\n\n{case['request']}"


def protected_results(text: str, protected: list[str]) -> dict[str, bool]:
    return {item: item in text for item in protected}


def request_completion(
    *,
    endpoint: str,
    api_key: str,
    model: str,
    system: str,
    user: str,
    temperature: float,
    max_tokens: int,
) -> str:
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    request = Request(
        endpoint.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=90) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        raise RuntimeError(f"Model request failed with HTTP {error.code}.") from error
    except URLError as error:
        raise RuntimeError("Model endpoint was not reachable.") from error
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError("Model response did not contain a chat completion.") from error


def validate_cases(cases: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    identifiers: set[str] = set()
    for case in cases:
        required = {"id", "mode", "context", "request", "protected", "checks"}
        if set(case) != required:
            errors.append(f"{case.get('id', '<missing id>')}: invalid keys")
        if case.get("id") in identifiers:
            errors.append(f"{case['id']}: duplicate id")
        identifiers.add(case.get("id", ""))
        if case.get("mode") not in {"generate", "humanize"}:
            errors.append(f"{case['id']}: invalid mode")
        if not isinstance(case.get("protected"), list) or not isinstance(case.get("checks"), list):
            errors.append(f"{case['id']}: protected/checks must be lists")
    if len(cases) < 20:
        errors.append("At least 20 comparison cases are required.")
    return errors


def run(args: argparse.Namespace) -> int:
    cases = load_cases()
    errors = validate_cases(cases)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.check:
        print(f"Validated {len(cases)} paired comparison cases; no model call made.")
        return 0

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Model comparisons not run: OPENAI_API_KEY is not configured.", file=sys.stderr)
        return 2

    skill = skill_instruction()
    results: list[dict[str, Any]] = []
    for case in cases:
        user = prompt_for(case)
        baseline = request_completion(
            endpoint=args.endpoint, api_key=api_key, model=args.model, system=SYSTEM_BASELINE,
            user=user, temperature=args.temperature, max_tokens=args.max_tokens,
        )
        enabled = request_completion(
            endpoint=args.endpoint, api_key=api_key, model=args.model, system=skill,
            user=user, temperature=args.temperature, max_tokens=args.max_tokens,
        )
        results.append({
            "id": case["id"],
            "context": case["context"],
            "mode": case["mode"],
            "request": case["request"],
            "checks": case["checks"],
            "protected": case["protected"],
            "baseline": baseline,
            "with_skill": enabled,
            "baseline_protected": protected_results(baseline, case["protected"]),
            "with_skill_protected": protected_results(enabled, case["protected"]),
            "editorial_review": {
                "naturalness": None,
                "ai_associated_patterns": None,
                "punctuation_and_formatting": None,
                "sentence_structure": None,
                "vocabulary": None,
                "voice_preservation": None,
                "semantic_accuracy": None,
                "verdict": None,
                "notes": "Complete manually from the paired outputs and stated case checks.",
            },
        })

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({
        "model": args.model,
        "endpoint": args.endpoint,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "case_count": len(cases),
        "results": results,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(results)} paired model comparisons to {output}.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate corpus and prompts without a model call.")
    parser.add_argument("--model", default="gpt-4.1-mini")
    parser.add_argument("--endpoint", default="https://api.openai.com/v1")
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--max-tokens", type=int, default=350)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(run(parse_args()))
