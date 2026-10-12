# Human-Centered Writing Skill

**Version 0.3.1** · Instruction-based writing skill with local validation helpers.

## Overview

Human-Centered Writing helps an AI produce prose that fits a real reader, purpose, and voice. It is for drafting new text and revising existing text without flattening the writer’s meaning, style, facts, or required formatting.

The skill targets common weaknesses in generic AI paraphrasing: empty framing, unsupported hype, mechanical transitions, needless variation, repeated structure, and punctuation changes made for their own sake. It uses context and evidence to decide whether to edit; an already suitable passage may correctly remain unchanged.

It does **not** promise that a text is human-written, will evade an AI detector, or will receive any particular detector result. It does not remove provenance, impersonate people, invent experience, or turn weak evidence into stronger claims.

## Main capabilities

### Generation mode

Creates a first draft from a new instruction. It starts with the reader’s need, selects a fitting structure, and uses only supplied or supportable details. It is useful for emails, explanations, documentation, applications, academic prose, and short social copy.

### Humanization mode

Conservatively improves supplied text while preserving its meaning, voice, evidence strength, protected details, and required formatting. It does not mechanically swap “AI-sounding” words or punctuation. For a legal, technical, multilingual, learner-level, short, or already-natural passage, it can leave the text alone.

### Additional support

- Context-sensitive tone for casual, professional, academic, scientific, technical, educational, marketing, and social writing.
- English, German (including consistent **du**/**Sie**), and multilingual text without unwanted translation or normalization.
- Contextual review of generic framing, inflated vocabulary, repetition, transitions, sentence patterns, and unsupported claims.
- Restrained punctuation and formatting changes; commands, code, links, citations, numbers, tables, templates, and required Markdown stay protected.
- Voice preservation from an author’s supplied text or sample.

## How it works

This is primarily an **instruction-based skill**, not a standalone writing application. An AI model reads `SKILL.md` and the relevant references, then performs the reasoning and writing.

1. Understand the task, reader, language, context, goal, and protected details.
2. Analyze only the writing patterns relevant to the request.
3. Select an appropriate style rather than applying a universal conversational tone.
4. Generate a draft or revise the supplied text.
5. Review clarity, naturalness, structure, punctuation, and voice.
6. Verify semantic accuracy, evidence strength, figures, citations, code, and required formatting.
7. Return the finished text, with explanation only when requested.

The Python files do **not** write prose independently. They validate the package and, when an API key is supplied, can send matched baseline and skill-enabled prompts to an OpenAI-compatible model endpoint for recorded comparison.

## Installation

### Codex — documented local layout

For a user-scoped Codex skill, copy this complete folder to `%USERPROFILE%\.codex\skills\human-centered-writing\`. For a repository-scoped skill, place it at `.codex/skills/human-centered-writing/`. Keep `SKILL.md`, `references/`, and any needed scripts together. These layouts follow OpenAI’s documented Codex skill convention; this package has passed structural checks but has not had a separate end-to-end discovery test.

### Claude Code — documented project layout

From a project root, copy the complete folder to `.claude/skills/human-centered-writing/`, then invoke `/human-centered-writing` or ask Claude to use it when relevant. Claude Code documents project skills under `.claude/skills/<name>/SKILL.md`; this package’s activation has not been end-to-end tested in Claude Code.

### ChatGPT — supported where Skills are available

On eligible ChatGPT workspaces, open **Plugins** → **Skills**, select **Create**, then **Upload from your computer** and upload the prepared ZIP or folder as supported by that interface. Availability and permissions vary by plan, workspace, region, and administrator settings. This integration is documented by OpenAI but untested for this package.

### Claude — manual project use

Create a Claude Project, add `SKILL.md` and the relevant reference files to its knowledge, and paste the root instructions into Project Instructions when needed. Claude Projects support uploaded documents and project instructions; automatic Agent Skills discovery is not claimed for Claude.ai.

## Manual operation

You can use the skill without automatic discovery:

1. Open `SKILL.md` and copy its instructions into the AI system or project instruction field.
2. Choose **Generation mode** for a new draft or **Humanization mode** for a supplied passage.
3. Provide the reader, context, language, tone, length, source text, and any details that must remain unchanged.
4. Review the output against the original facts, formatting, and voice before sending it.

Useful local commands from this folder:

```powershell
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/run_model_comparisons.py --check
python scripts/package_skill.py
```

## Using it with AI

If automatic selection does not activate, name the skill explicitly. For example:

```text
Use the Human-Centered Writing Skill to rewrite this email naturally while preserving all details.

Generate a professional German email using the Human-Centered Writing Skill. Use Sie, keep it concise, and do not invent experience.

Humanize the following paragraph without changing its technical meaning, numbers, citations, Markdown, or code.
```

For Codex and Claude Code, you can also invoke the installed skill by name (`$human-centered-writing` or `/human-centered-writing` where the host exposes that command). In ChatGPT or Claude, attach or paste the instructions first, then use the same request pattern.

## Configuration

Preferences belong in the request; there is no runtime configuration file. The supported options are:

| Preference | Typical values | Default |
|---|---|---|
| Operation | `generate`, `humanize` | infer from request |
| Context | casual, email, application, academic, technical, educational, marketing, social | infer from request |
| Formality | low, medium, high | fit context |
| Concision | concise, balanced, detailed | fit request |
| Voice preservation | low, medium, high | high for rewrites |
| Editing intensity | conservative, substantial | conservative for rewrites |
| Formatting restraint | low, medium, high | medium |
| Punctuation | flexible, restrained, strict | flexible |
| Language / region | language and regional convention | preserve input |

Example: “Humanize this conservatively for a formal German email. Keep the **Sie** register, all figures, Markdown, and technical terms unchanged.” See [configuration guidance](references/configuration.md).

## Examples

### Remove empty framing

Before: “In today’s fast-paced world, planning is crucial.”

After: “Planning matters.”

The revision is direct, but it should not add a specific benefit unless the brief supports it.

### Preserve technical information

Before: “Run `npm test` after editing config.yaml.”

After: unchanged.

Commands and paths are protected; a rewrite would not improve this instruction.

### Preserve a natural work message

Before: “The report is due Friday. Please send the final PDF to Ana.”

After: unchanged.

No-change is a valid Humanization result when the text already fits its purpose.

More examples are in [examples/before-after.md](examples/before-after.md).

## Testing and verification

Python 3.10+ is required; there are no third-party package dependencies.

- `scripts/validate_skill.py` checks required files and core instructions.
- `python -m unittest discover -s tests -v` runs deterministic unit tests for structure, corpus coverage, preservation fixtures, and the model harness.
- `scripts/run_model_comparisons.py --check` validates the 24-case paired comparison corpus without network access.
- `scripts/run_model_comparisons.py --model <model-id>` runs paired comparisons only when `OPENAI_API_KEY` is configured locally. It writes raw outputs and literal protected-detail checks to `reports/model-comparison-results.json` for human editorial review.
- `scripts/package_skill.py` rebuilds `human-centered-writing-ready.zip` while excluding nested ZIPs, caches, reports, and Git metadata.

As of the v0.3.0 report, the 24 model-comparison cases were prepared but not executed because no configured model access was available. No model results have been fabricated. See [model-testing.md](docs/model-testing.md) for the protocol and current status.

## Limitations

- Naturalness is partly editorial judgment, not a scientific measurement.
- Output quality depends on the host model and the supplied context.
- Platform discovery, file upload, and skill invocation behavior can differ by product, plan, and configuration.
- AI-detector outcomes cannot be guaranteed or reliably predicted.
- Human review remains important for legal, medical, financial, safety-critical, academic, and externally published writing.

## Project structure

```text
human-centered-writing/
├── SKILL.md                 # canonical instructions and activation metadata
├── README.md                # this guide
├── CHANGELOG.md             # release history
├── LICENSE                  # MIT license
├── references/              # focused writing guidance
├── examples/                # before-and-after decisions
├── docs/                    # research notes and model-test protocol
├── scripts/                 # validator, comparison runner, packager
├── tests/                   # deterministic tests and case corpora
├── .env.example             # non-secret placeholder only
├── .gitignore               # prevents local artifacts from staging
└── pyproject.toml           # package metadata
```

## Version and license

Current version: **0.3.1**. See [CHANGELOG.md](CHANGELOG.md) for release history. This project is released under the [MIT License](LICENSE).

## Compatibility notes

The Codex and ChatGPT guidance above is based on [OpenAI’s skill documentation](https://developers.openai.com/api/docs/guides/tools-skills) and [ChatGPT Skills help](https://help.openai.com/en/articles/20001066-skills-in-chatgpt). The Claude guidance is based on [Claude Projects](https://support.anthropic.com/en/articles/9517075-what-are-projects) and [Claude Code Skills](https://code.claude.com/docs/en/skills). Documented layouts are distinguished from integrations that were not end-to-end tested.
