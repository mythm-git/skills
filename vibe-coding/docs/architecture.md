# Architecture

One canonical `SKILL.md` contains shared triggers, risk gates, routing, and delivery contract. `references/` contains conditional operational knowledge; `templates/` provides reusable artifacts; `scripts/` implements deterministic release checks; `tests/` verifies the package's meaningful invariants; `examples/` illustrates usage. `agents/openai.yaml` is an optional OpenAI UI adapter, not a second source of workflow truth.
