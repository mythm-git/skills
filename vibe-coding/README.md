# Vibe Coding Skill

Vibe Coding is a universal, risk-aware Agent Skill that guides coding agents through reliable software delivery: understand the project, use a proportionate plan, implement safely, verify what changed, and give an honest handoff. It supports BUILD, EXTEND, FIX, REFACTOR, REVIEW, SECURE, TEST, DEPLOY, and DOCUMENT work without requiring special commands.

## What it supports

The workflow is language-agnostic and applies the normal conventions of Python, JavaScript/TypeScript, C/C++, Java, Go, Rust, .NET, and other ecosystems. It protects against common engineering failures—unvalidated inputs, client-only authorization, secret leakage, unsafe SQL, untested regressions, and unsupported claims—while avoiding irrelevant controls for a local utility.

The canonical package is `SKILL.md` plus relative supporting files, following the open [Agent Skills specification](https://agentskills.io/specification). Details are loaded progressively: the entrypoint routes to specialized references only when needed.

## Use and modes

Ask naturally: “add a route,” “fix this regression,” “audit authorization,” or “prepare deployment.” The skill infers a mode; you can say `SECURE`, `FIX`, or another mode explicitly. Low-risk work gets focused implementation and checks. Medium-risk work gets a clear plan and regression/security review. High-risk work requires threat-aware tests, verification statuses, and explicit authorization before destructive or high-impact execution.

Security controls use an applicability matrix, so browser controls are not imposed on a local CLI, and RLS is not required where unavailable. See [references/security.md](references/security.md).

## Installation and activation

Follow the platform-specific, documentation-reviewed steps in [docs/installation.md](docs/installation.md). This repository has not been installed or invoked in a live Codex, Claude Code, Claude, or ChatGPT environment; see [docs/compatibility.md](docs/compatibility.md) for the exact status.

For a local quality check, use Python 3.10+ and run:

```powershell
python scripts/validate_skill.py
python scripts/validate_references.py
python scripts/check_secrets.py
python scripts/security_audit.py
python -m unittest discover -s tests -v
```

No external Python packages are required. Use `--help` on any script for its arguments.

## Configuration and customization

` .env.example` documents local placeholders only. Copy it to `.env` only when your host project needs it; never commit real credentials. Customize the workflow by editing the relevant reference or template while retaining verified-status terminology and safety boundaries.

## Operations, updates, and troubleshooting

Use [docs/operations.md](docs/operations.md) for update and troubleshooting procedures. Use [docs/limitations.md](docs/limitations.md) before relying on a platform or scanner outcome.

## Architecture

`SKILL.md` is the canonical routing and safety contract. It always directs meaningful work through the security applicability and verification references, then loads domain, planning, and architecture references only when the request calls for them. Supporting references, templates, examples, deterministic Python validators, and unit tests are portable and have no third-party runtime dependencies.

## Compatibility and project status

Version **0.2.0** is release-ready with disclosed limitations. Codex CLI has historical and current local execution evidence. Claude Code was unavailable on this machine; Claude and ChatGPT were not execution-tested. Read [COMPATIBILITY_REPORT.md](COMPATIBILITY_REPORT.md) and [RELEASE_READINESS.md](RELEASE_READINESS.md) before relying on platform behavior.

## Release and testing records

The public release includes concise, sanitized verification summaries: [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md), [TEST_RESULTS.md](TEST_RESULTS.md), [SECURITY_VERIFICATION.md](SECURITY_VERIFICATION.md), and [IMPROVEMENTS.md](IMPROVEMENTS.md). Private runtime traces and synthetic workspaces are deliberately excluded.

## License

Released under the [MIT License](LICENSE).
