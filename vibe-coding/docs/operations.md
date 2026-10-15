# Operations

Run validators from the skill root. A failure is actionable: fix the referenced file, rerun the affected script, then run the suite. `check_secrets.py` redacts suspected values; investigate locally without pasting credentials into tickets or logs.

When updating instructions, keep `SKILL.md` routing-focused and put detailed conditional material in references. Update examples and tests for changed behavior, run all checks, update the changelog, and reconsider compatibility status only after a real platform test.
