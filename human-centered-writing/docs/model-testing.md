# Model Comparison Protocol and Results

## Status: not executed in this environment

No model comparison output is recorded in this package because this environment has no configured `OPENAI_API_KEY`, no OpenAI SDK, no local model runtime, and no available authenticated browser session. This is a verified access limitation, not a passing model result. No synthetic baseline, skill-enabled output, editorial score, or before-and-after claim has been substituted for a real model call.

## Reproducible paired test

`tests/test-cases/model_comparison_cases.json` contains 24 representative cases. For every case, `scripts/run_model_comparisons.py` sends the identical user request to the same model with identical `temperature` (default `0`) and `max_tokens` (default `350`):

1. Baseline system instruction: a minimal, generic writing-assistant instruction.
2. Skill-enabled system instruction: the root skill plus the relevant writing-pattern, punctuation, style, voice, and rubric references.

The script records both raw outputs, the model and settings, literal protected-detail checks, and a blank editorial-review record in `reports/model-comparison-results.json`. It does not transmit any package file and does not upload results.

## Evaluation criteria

For each pair, review:

- naturalness and reader fit;
- AI-associated generic framing, unsupported hype, mechanical transitions, and needless variation;
- punctuation and required formatting;
- sentence structure and vocabulary;
- voice preservation;
- semantic accuracy, evidence strength, protected facts, citations, code, and strict formatting.

Semantic fidelity, protected-detail preservation, and explicit constraints are hard requirements. Fail a case when either output violates a hard requirement; do not offset that failure with a stylistic score.

## Current result table

| Measure | Result |
|---|---:|
| Representative paired cases defined | 24 |
| Real model calls completed | 0 |
| Baseline outputs recorded | 0 |
| Skill-enabled outputs recorded | 0 |
| Editorial comparisons completed | 0 |
| Local corpus/harness checks | passed: 13 automated tests and 24-case corpus check |

## Run when model access is available

Set `OPENAI_API_KEY` only in the local shell, then run:

```powershell
python scripts/run_model_comparisons.py --model <model-id>
```

Review the generated JSON before treating any comparison as evidence. Re-run every case that fails a hard requirement after a skill change, retain the first and repeat outputs, and explain whether the change fixed the failure without causing regression elsewhere.
