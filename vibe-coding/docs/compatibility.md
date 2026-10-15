# Compatibility Matrix

Status labels distinguish documentation review from live evidence. The sanitized public summary is in [COMPATIBILITY_REPORT.md](../COMPATIBILITY_REPORT.md); private runtime traces are not part of the release.

| Platform | Format | Documentation | Installation | Discovery | Invocation | Behavioral task | Functional/security result | End-to-end | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Agent Skills ecosystem | Specification-compatible | Documentation-reviewed | N/A | N/A | N/A | N/A | N/A | N/A | Canonical source uses `SKILL.md` and relative resources. |
| OpenAI Codex CLI | Specification-compatible | Documentation-reviewed | PASS | PASS | PASS | PASS for local synthetic scenarios | PARTIAL | Historical verification used Codex CLI 0.162.1 and repo-scope `.agents/skills`; current results are in the public compatibility report. |
| ChatGPT Skills | Specification-compatible | Documentation-reviewed | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | No authenticated import surface/tool was available. |
| Claude Code | Specification-compatible | Documentation-reviewed | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | `claude` was not installed on PATH. |
| Claude | Specification-compatible | Documentation-reviewed | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | No authenticated product automation was available. |

Manual verification records should capture platform/version, install method, invocation prompt, permissions, scripts run, result, and limitation. Sources: [Agent Skills](https://agentskills.io/specification), [OpenAI Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), [Claude custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
