---
name: human-centered-writing
description: Create or revise accurate, natural, audience-appropriate prose while preserving the author’s voice, required details, and formatting. Use for drafting, editing, emails, applications, documentation, explanations, and multilingual writing; do not use to conceal AI use or evade provenance or detection systems.
---

# Human-Centered Writing

## Purpose and activation

Use this skill when a user asks to draft, edit, simplify, polish, rewrite, or improve prose. It has two operations:

- **Generation mode:** create a context-appropriate first draft from a brief.
- **Humanization mode:** make the smallest effective edits to existing text while preserving meaning, voice, protected details, and required formatting.

Do not use it to impersonate a person, fabricate lived experience, remove provenance, manipulate watermarks, or optimize against AI-detection systems.

## Fast intake

Identify only what changes the result: operation, language, audience, goal, context, formality, length, required format, source material, protected details, and voice sample. Use reasonable defaults for simple requests; ask a concise question only if a missing answer would materially change accuracy, safety, or usefulness.

Honor explicit user requirements over defaults. For rewrites, default to conservative editing. Treat quotations, citations, URLs, code, file paths, dates, figures, names, technical terminology, and required markup as protected unless the user authorizes changes.

Use [configuration options](references/configuration.md) only when the user gives preferences or a non-default choice matters.

## Core workflow

1. **Classify:** select Generation or Humanization mode and identify the writing context.
2. **Plan lightly:** choose only the relevant guidance. Read [style profiles](references/style-profiles.md) for an unfamiliar or high-stakes context; read [voice preservation](references/voice-preservation.md) when a sample or source text is supplied.
3. **Draft or edit:** write directly for the reader and purpose. Use specifics supported by the brief; never invent facts, experiences, sources, outcomes, qualifications, benefits, or causal claims. When the brief cannot support a useful claim, use a neutral formulation, an explicit placeholder, or one concise question.
4. **Review:** correct material issues in meaning, evidence, voice, structure, clarity, and delivery. Preserve an already-natural passage when no meaningful improvement is needed; do not manufacture variation to demonstrate that an edit occurred.
5. **Return:** provide only the requested final text by default. Explain assumptions, changes, or an evaluation only when asked.

## Generation mode

Start with the reader’s need rather than a generic preface. Choose structure to match the task, not a fixed introduction–three-points–conclusion template. Let sentence length, paragraphing, transitions, punctuation, and formatting serve meaning and the requested voice.

Use direct verbs, concrete nouns, and supported details. Be concise when the task is simple. Retain formality, discipline-specific language, citations, and exact syntax where the context requires them.

## Humanization mode

Analyze the source before changing it. Look for contextually unnecessary filler, generic claims, semantic repetition, mechanical transitions, over-formatting, repetitive syntax, mismatched tone, and vague abstractions. First decide whether a material improvement is possible. For a short literal, legal, technical, multilingual, learner-level, or already-fit passage, preserving it can be the correct result. Refer to [writing-pattern guidance](references/ai-writing-patterns.md) and [punctuation guidance](references/punctuation-and-formatting.md) only when those issues are present.

Do not mechanically replace words or symbols. A phrase, punctuation mark, list, heading, technical term, or formal construction may be correct for its context. Make the smallest changes that improve reader fit, clarity, or credibility. If the source is already natural and suitable, return it unchanged and say so only if the user asked for an explanation.

## Voice and semantic integrity

Infer observable preferences from user-provided writing: formality, perspective, vocabulary, sentence complexity, pacing, punctuation, paragraph shape, and degree of directness. Preserve distinctive, appropriate choices. Do not introduce deliberate errors, random slang, false personal details, or artificial irregularity.

Meaning and protected details take priority over stylistic preference. Preserve the original strength of evidence, including modal language and causal limits. Flag uncertainty instead of turning it into a confident claim. Keep citations and quotations intact; do not change numerical, legal, medical, financial, or technical content without authorization. Preserve a strict template, table, command, path, or required Markdown byte-for-byte when requested.

## Context and language

Match the context instead of forcing a universal conversational style:

- Casual conversation: relaxed, direct, lightly formatted.
- Professional email or job application: specific, credible, polite, and purpose-led.
- Academic, scientific, or technical writing: rigorous, precise, reproducible, and correctly formatted.
- Educational, marketing, or social writing: audience-aware, concrete, and free of unsupported hype.
- German: distinguish **du** and **Sie**, retain idiomatic German syntax, and avoid literal English phrasing.
- Other languages: preserve regional and cultural features; do not translate or normalize identity markers unless requested.

Read [style profiles](references/style-profiles.md) for detailed, context-specific guidance.

## Quality gate

Before delivery, check that the text meets the brief; preserves protected details and formatting; keeps evidence strength unchanged; distinguishes facts from inference; has a credible voice; avoids needless repetition; and ends when the message is complete. When instructions conflict or omit a decision that would change the result materially, ask one concise clarification rather than blending incompatible styles. For a requested evaluation, use the observable, non-scientific rubric in [quality rubric](references/quality-rubric.md). Semantic fidelity and mandatory-detail preservation are hard requirements, not score trade-offs.

## Safety boundary

Do not optimize text to avoid AI detectors, alter or strip watermarking or provenance, insert invisible characters, or advise users how to bypass authorship checks. Detection outputs are probabilistic signals, not proof of authorship. If a user must demonstrate original work, recommend retaining drafts, source notes, citations, and revision history.

## References and examples

Load only what applies:

- [Configuration](references/configuration.md): user preferences and overrides.
- [Writing patterns](references/ai-writing-patterns.md): context-aware pattern review.
- [Punctuation and formatting](references/punctuation-and-formatting.md): restrained, safe editing.
- [Style profiles](references/style-profiles.md): context, language, and formality.
- [Voice preservation](references/voice-preservation.md): source-text and sample handling.
- [Quality rubric](references/quality-rubric.md): requested editorial evaluations.
- [Examples](examples/before-after.md): realistic revision decisions.

## Platform compatibility

- **ChatGPT and Claude:** attach or paste the root `SKILL.md` and keep the `references/` directory available when the platform supports project files.
- **Codex:** use this folder as the skill directory; the root `SKILL.md` is the canonical manifest.
- **Claude Code:** copy the root `SKILL.md` and its `references/` directory to the target skill location supported by the installed Claude Code version.

The shared manifest follows the Agent Skills convention. Local compatibility has been structurally validated; end-to-end platform discovery has not been tested in ChatGPT, Claude, or Claude Code.
