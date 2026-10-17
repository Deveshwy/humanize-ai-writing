---
name: humanize-ai-writing
description: Rewrite or audit AI-generated, AI-assisted, overly polished, generic, formulaic, needlessly complex, or written-for-the-page prose while preserving meaning, facts, voice, citations, uncertainty, and commitments. Use for requests to humanize or de-AI text, remove AI slop, write in plain or Simple English, make prose sound natural or less robotic, apply Simplified Technical English or ASD-STE100-style constraints, prepare technical text for non-native readers or translation, make scripts sound spoken rather than written, match a supplied voice, diagnose AI-writing signals, enforce a direct-response blacklist, or revise scripts, VSLs, speaker notes, marketing, email, Wikipedia, encyclopedic, informational, documentation, README, runbook, procedure, error-message, release-note, incident-report, API-guide, article-draft, and editor-comment prose.
---

# Humanize AI Writing

Improve the writing itself. Optimize for clarity, specificity, source fidelity, and an owned voice.

## Choose the mode

- **Light clean:** Preserve order, structure, and most phrasing. Remove obvious filler, inflation, repetition, and synthetic rhythm.
- **Full rewrite:** Rebuild the piece around its strongest supported claim while preserving its substance.
- **Voice match:** Follow the sample's cadence, vocabulary, punctuation, directness, and degree of polish without copying distinctive phrases.
- **Pattern audit:** Identify observable patterns without rewriting. Quote the smallest useful snippet, name the pattern, and give a concrete fix. Do not score the draft, guess whether AI wrote it, or treat a lone phrase as proof of anything.
- **Spoken delivery:** Rewrite scripts, VSLs, speaker notes, podcast copy, dialogue, and other performed text for a real mouth and a specific speaker.
- **Direct-response blacklist:** Apply strict negative constraints to sales pages, emails, VSLs, advertorials, webinars, launch assets, and related copy.
- **Wikipedia/editorial:** Review encyclopedic or informational prose, wikitext, sourcing, neutrality, citations, markup, and editor comments.
- **Controlled technical English:** Rewrite documentation, procedures, error messages, runbooks, release notes, incident reports, API guides, or translation-ready text with pragmatic or strict ASD-STE100-style constraints.

Use the lightest mode that satisfies the request. Preserve structure when the user asks to polish, clean, tighten, or lightly humanize. Rebuild only when the user asks for a rewrite or the existing structure is the main problem. If the request is ambiguous, make a reasonable choice and edit; ask only when the choice would materially change the result.

## Establish the fidelity contract

Before changing prose, make a short internal ledger:

- purpose, audience, surface, and desired action
- claims, names, dates, numbers, chronology, quotes, and attribution
- promises, deadlines, citations, links, and markup
- material uncertainty, disagreement, and unresolved questions
- voice traits or quirks that should survive

Treat this ledger as locked. Keep the facts, attribution, commitments, and ask intact. If a needed fact is missing, remove the claim, request the source, or use a clearly labeled placeholder when it helps the user finish the draft.

## Core workflow

1. Identify the mode and build the fidelity ledger.
2. Diagnose root problems before polishing sentences. Look for unsupported claims, vague attribution, generic significance, promotional tone, broken citations or markup, empty abstractions, template architecture, synthetic rhythm, and page-written sentences that will be awkward to perform.
3. Load only the references routed below. For a substantial draft, run the appropriate audit script before or after editing; treat its output as leads for human review, not pass/fail truth.
4. Rewrite in passes:
   - Make the minimum effective edit. Leave strong, distinctive sentences alone; unevenness is not automatically a defect.
   - Cut generic setup, recap loops, fake suspense, and performance of helpfulness.
   - Restore concrete actors, actions, constraints, proof, and consequences already supported by the source.
   - Replace inflated wording and nominalizations with precise nouns and verbs.
   - Vary sentence length because the thought requires it; do not manufacture fragments or fake imperfection.
   - Preserve useful quirks, bluntness, humor, profanity, self-interruptions, honest admissions, and necessary uncertainty when they belong to the writer.
   - Front-load the point only when the existing setup adds no context, tension, evidence, or character. Do not force every paragraph into the same conclusion-first shape.
5. Run the plain-language pass below. Treat it as a set of editing tests, not a word-ban list. For controlled technical English, use its separate reference and do not blend strict constraints into other surfaces.
6. Compare the result against the fidelity ledger sentence by sentence. Correct drift in meaning, facts, attribution, citations, tone, uncertainty, commitments, or formatting.
7. Read for voice and rhythm. Remove edits that merely swap one generic phrase for another.
8. Return the requested artifact, not a performance report.

## Run the plain-language pass

Apply these tests to prose, not to code, commands, identifiers, quoted text, citations, or technical terms that lose precision when simplified:

1. **Stale image:** Replace a familiar metaphor, simile, or stock phrase with a direct statement or a fresh image that belongs to this writer.
2. **Shorter word:** Prefer the shorter, familiar word when it carries the same meaning and tone.
3. **Cuttable word:** Remove any word that does no factual, logical, rhythmic, or emotional work.
4. **Visible actor:** Prefer active voice when it clarifies who did what. Keep passive voice when the actor is unknown, irrelevant, deliberately withheld, or less important than the action.
5. **Everyday equivalent:** Replace jargon, foreign phrasing, scientific wording, and abstract nouns when plain English keeps the precision. Keep necessary terms and explain them if the audience needs help.
6. **Meaning over rules:** Break any rule that would make the sentence less accurate, less natural, less humane, or harder to read.

Compression never outranks the fidelity contract. Do not delete a qualifier, caveat, attribution, or term of art merely to make a sentence shorter. Do not force active voice by inventing an actor.

## Route the references

- For a substantial general rewrite, read `references/rewrite-playbook.md`.
- For a plain-language audit, documentation or PR prose, landing-page specificity, or progress-report cleanup, read `references/plain-language-system.md`.
- For Simplified Technical English, ASD-STE100, translation-ready technical text, non-native technical readers, or tightly controlled procedures and documentation, read `references/simplified-technical-english.md`. Use pragmatic mode unless the user explicitly requests STE, ASD-STE100, or compliance.
- For voice matching, read `references/voice-calibration.md` and infer traits from at least two representative samples when available.
- For scripts, VSLs, speaker notes, podcast copy, dialogue, or anything meant to be performed, read `references/spoken-delivery.md`. Run `scripts/ai_style_audit.py --spoken` on substantial drafts.
- For a style audit or broad pattern inventory, read `references/ai-slop-patterns.md` and run `scripts/ai_style_audit.py` on long drafts.
- For Wikipedia, documentation, informational prose, markup, citations, or editor comments, read `references/ai-writing-signals.md`.
- For direct-response copy or an explicit blacklist review, read `references/direct-response-blacklist.md` and run `scripts/audit_blacklist.py`.
- Read `references/research-basis.md` only when maintaining the skill or explaining the evidentiary limits of signal-based review.

Do not load every reference by default. Do not run scripts on a sentence or short paragraph when manual review is faster and clearer.

## Apply surface-specific rules

### Direct-response copy

Apply the blacklist only to direct-response copy or when the user explicitly asks for it. Treat script findings as review flags: quoted text, intentional examples, and deliberate repetition can be valid. Keep every claim and proof point aligned with the source.

For landing pages, make each headline, subhead, bullet, and proof block carry one concrete claim. Run the swap test after rewriting: if a competitor could paste a line onto its page unchanged, add a supported product, customer, mechanism, constraint, or outcome. If the source provides none, delete the line. Do not rescue a vague claim by swapping in vague synonyms; a shorter page with one real claim is better than a complete-looking page filled with benefit fog.

### Spoken scripts and read-aloud copy

Write for a specific speaker, audience, setting, and performance length. When a useful reference script or transcript is supplied, map its functional beats and pacing before rewriting; do not copy distinctive wording or import its claims. Ground the new version in the user's facts, proof, offer, and voice.

Run a read-aloud pass at likely performance speed. Fix lines that exhaust the breath, catch the mouth, sound like written ad copy, or make the speaker interview themselves with canned questions. Preserve roughness already present in real samples—contractions, repeated words, blunt asides, fragments, local vocabulary—but do not manufacture stutters, filler words, slang, or fake intimacy to simulate humanity.

### Documentation and operational prose

For README files, documentation, commit messages, and PR descriptions, state what changed and why in plain words. Remove achievement language such as “successfully implemented,” broad claims such as “comprehensive” or “robust,” and adjectives that the evidence does not earn. A reviewer should understand the change in one read.

For progress and completion reports, lead with the outcome. Then state what changed, what failed or remains uncertain, and what comes next. Start with a few plain sentences; add bullets or detail only when they help the reader decide or act. Avoid ceremonial checkmarks, self-congratulation, and walls of status bullets.

When controlled technical English is active, first classify each passage as procedural or descriptive. Keep one name for each item, put required conditions before commands, write one instruction per procedural sentence, and preserve code, identifiers, commands, paths, product names, and quoted errors exactly. Apply strict sentence and vocabulary rules only through `references/simplified-technical-english.md`; they are not defaults for general documentation.

### Wikipedia and informational writing

Prioritize verifiability, neutral point of view, no original research, source-text alignment, named attribution, valid markup, and citation integrity. Verify citations when tools and sources are available. Otherwise preserve them exactly and flag uncertainty. Fix the editorial defect rather than merely removing its visible tell.

For editor comments, replace canned assurances and generic policy language with concise reasoning tied to the actual edit, source, or policy question.

### General prose and voice matching

Preserve effective quirks, including unevenness that belongs to the writer. Keep strong opinions, blunt language, humor, profanity, fragments, self-interruptions, and honest admissions when the samples support them. Do not professionalize the writer by default. Match observable traits rather than caricaturing a person or copying memorable phrasing. Do not invent anecdotes, emotions, sensory details, quotes, credentials, statistics, or lived experience.

Do not rotate precise terms merely to create lexical variety. If `agent`, `invoice`, or `review` is the right word, repeat it. At the ending, cut recap paragraphs and fake-profound kicker lines that turn the point into an aphorism or decorative metaphor. End on the last concrete point, supported takeaway, or next action; do not manufacture closure when the draft does not need it.

## Return the result

- **Rewrite:** Give the clean revision first. Add a brief note only for meaningful choices, unresolved facts, or preserved constraints.
- **Pattern audit:** List only material findings as `snippet -> named pattern -> concrete fix`. Do not rewrite unless asked, assign a score, or claim to determine authorship.
- **Plain-language audit:** Group material violations by stale phrase, inflated word, cuttable word, passive construction, or jargon; then give the rewrite. Do not inventory harmless preferences.
- **Before/after:** Show only the most instructive changes.
- **Unsupported claims:** Request a source, soften the claim, add a labeled placeholder, or remove it. Never invent specificity.

Do not preface a revision with a long explanation. Do not list every small edit. Do not claim that a script “passed” the writing unless the user requested audit details.

## Quality bar

The result should sound situated and owned. Its structure should follow the writer's purpose. It should name the thing directly, preserve source integrity, carry real constraints and judgment, and avoid generic certainty, fake intimacy, theatrical contrast, templated punchiness, decorative formatting, recap endings, and over-polished assistant rhythm. The writer should still recognize the draft as theirs.
