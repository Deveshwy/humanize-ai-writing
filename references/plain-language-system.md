# Plain-language editing system

Use this reference when the user asks for plain English, an Orwell-style edit, a detailed rewrite audit, or concise prose for documentation, PRs, landing pages, or progress reports.

This is a writing system, not a detector and not a list of forbidden words. It adapts George Orwell's six 1946 prose rules into practical editing tests. The software and marketing applications draw from [Vox's July 19, 2026 thread](https://x.com/Voxyz_ai/status/2078857039116156978).

## Contents

- [Order of authority](#order-of-authority)
- [The six tests](#the-six-tests)
- [Audit and rewrite workflow](#audit-and-rewrite-workflow)
- [Surface checks](#surface-checks)
- [Failure modes](#failure-modes)

## Order of authority

1. Preserve the fidelity ledger: facts, meaning, uncertainty, attribution, commitments, quotations, citations, and required markup.
2. Preserve the writer's useful voice, including deliberate rhythm, technical vocabulary, and unusual but apt phrasing.
3. Apply the six plain-language tests.
4. Break a test whenever following it would damage accuracy, clarity, tone, or humanity.

The tests govern prose. Never rewrite code, commands, API names, identifiers, file paths, quotations, citations, or fixed product names. Keep a technical term when the everyday substitute is less exact; explain the term if the audience needs it.

## The six tests

### 1. Stale image

Flag metaphors, similes, and figures of speech that arrive preassembled rather than from the writer's observation. State the point directly, use a concrete example, or write a fresh image that fits the subject.

Do not strip out every figure of speech. Keep one that is precise, memorable, and true to the voice.

### 2. Shorter word

Replace a long or formal word when a shorter, familiar word means the same thing in context.

Do not trade a precise word for a vague one. “Use” is often better than “utilize,” but a technical term may be the clearest choice for an expert reader.

### 3. Cuttable word

Ask what each word contributes: fact, logic, qualification, tone, rhythm, or emphasis. Cut it if it contributes none of these.

Common cuts include throat-clearing, duplicated adjectives, generic intensifiers, recap phrases, and claims that merely praise the sentence's subject.

### 4. Visible actor

Prefer active voice when it reveals responsibility or makes the action easier to follow.

Keep passive voice when the actor is unknown, unimportant, obvious, deliberately withheld, or less important than the object or event. Never invent an actor to satisfy the test.

### 5. Everyday equivalent

Replace jargon, imported phrasing, inflated abstractions, and unnecessary scientific wording when everyday English keeps the meaning. Name the actor and action instead of hiding both inside a nominalization.

Keep terms of art when they carry information that the plain substitute would lose.

### 6. Meaning over rules

Ignore any rule that produces stiff, ugly, misleading, childish, or less natural prose. The point is readable thought, not mechanical brevity.

## Audit and rewrite workflow

When the user asks only for a rewrite, return the clean copy first. Do not make them read the diagnosis before the result.

When the user asks for an audit and rewrite:

1. Quote only the smallest useful snippet.
2. Label the material issue: stale phrase, inflated word, cuttable word, passive construction, or jargon.
3. Give the specific edit and explain any meaning or tone it preserves.
4. Then give the full rewrite.

Do not count every article, auxiliary verb, or passive construction as a violation. Report patterns and edits that change the quality of the prose.

Example:

> Comprehensive error handling has been implemented across all API endpoints to ensure robust and reliable performance.

- “has been implemented” -> passive construction -> name the actor if known, or lead with the change
- “comprehensive,” “robust,” and “reliable” -> unsupported achievement language -> cut unless the draft proves each claim
- “to ensure” -> overclaim -> state the behavior the error handling actually provides

Rewrite: “We added error handling to every API endpoint.”

## Surface checks

### README files, documentation, commits, and PRs

- State what changed and why.
- Prefer the exact component, behavior, and consequence over praise.
- Cut “successfully,” “comprehensive,” “robust,” and similar achievement language unless the sentence supplies evidence and the distinction matters.
- Make the first paragraph sufficient for a reviewer to understand the change.

### Landing pages

- Give each unit of copy one concrete claim.
- Name the product behavior, mechanism, customer, constraint, proof, or outcome already supported by the source.
- Run the swap test after rewriting: if a competitor could use the line unchanged, make it specific. If the source offers no supporting detail, delete the line.
- Never replace one generic benefit with a synonymized generic benefit. Keep the strongest supported line even if the section becomes much shorter.
- Do not manufacture specificity. A placeholder or narrower claim is better than invented proof.

### Progress and completion reports

- Lead with the outcome.
- State what changed, what failed or remains uncertain, and what comes next.
- Start with a few plain sentences. Add detail only when it changes a decision or next action.
- Avoid ceremonial checkmarks, “successfully,” “perfect,” inflated achievement language, and walls of bullets.

## Failure modes

- **Ban-list editing:** deleting conspicuous words while leaving the generic thought and template structure intact
- **Mechanical shortening:** cutting qualifiers, causality, or useful rhythm to reduce the word count
- **Forced active voice:** inventing responsibility or making the sentence awkward
- **Jargon substitution:** replacing an exact term with a longer, vaguer explanation
- **Generic synonym swap:** exchanging one inflated phrase for another without adding an actor, action, constraint, or proof
- **Competitor specificity:** adding unsupported product claims merely to pass the landing-page swap test
