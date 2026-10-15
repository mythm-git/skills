# Compatibility Report — v0.2.0

| Platform | Status | Evidence and limitation |
| --- | --- | --- |
| Agent Skills format | Documentation-reviewed | Canonical `SKILL.md`, frontmatter, and relative resources pass local structural checks. |
| OpenAI Codex CLI | PARTIAL | Historical discovery/invocation and behavior evidence exists. A fresh current session read installed v0.2.0 `SKILL.md`, but did not finish its greenfield task under the active tool policy. |
| Claude Code | BLOCKED | `claude` was not installed on PATH; no installation, authentication bypass, or software installation was attempted. Portable static format checks passed. |
| Claude | NOT TESTED | No authenticated product automation was available. |
| ChatGPT Skills | NOT TESTED | No authenticated import surface was available. |

Documentation instructions are provided in [docs/installation.md](docs/installation.md). No platform is claimed fully compatible without successful end-to-end execution evidence.
