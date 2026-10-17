# Simplified Technical English

Use this reference for technical prose when the user names Simplified Technical English, STE, ASD-STE100, translation readiness, non-native readers, or tightly controlled documentation. It also applies when a runbook, procedure, error message, release note, incident report, or API guide needs unusually low ambiguity.

This is a specialized mode inside the broader humanization workflow. It is not the default for marketing, blog writing, scripts, speaker notes, personal voice, or persuasive copy. Controlled language deliberately removes expressive range.

## Select the mode

- **Pragmatic controlled English:** Use by default for technical clarity. Apply the structural rules while keeping necessary domain words such as `idempotent`, `webhook`, `deploy`, and `compile`.
- **Strict STE:** Use only when the user explicitly names STE, ASD-STE100, or compliance. Apply the full constraints below and explain that true compliance also requires the official ASD-STE100 dictionary.

Do not claim certification or guaranteed compliance. This reference is an unofficial editing aid.

## Classify before editing

Classify each passage before applying the rules:

| Passage | Purpose | Preferred verb form | Sentence limit | Unit |
|---|---|---|---|---|
| Procedural | Tell the reader what to do | Imperative | 20 words | One instruction per sentence |
| Descriptive | Explain what a thing is or does | Simple present, past, or future | 25 words | One topic per paragraph; six sentences maximum |

Do not mix a command and an explanation in the same sentence. A note inside a procedure is descriptive and uses the 25-word limit.

## Lock facts and terminology

Extend the fidelity ledger with a terminology map before drafting:

- Choose one name for each item. Do not alternate between `config`, `configuration`, `settings`, and `options` unless they name different things.
- Choose one verb for each action. Do not rotate `check`, `verify`, `confirm`, and `validate` for variety.
- Give a domain term one meaning and one part of speech within the document.
- Keep technical terms when a plain substitute loses precision. Explain them if the audience needs help.
- Break long noun chains with prepositions. Prefer “the timeout value for the connection pool” to “the connection pool timeout configuration value.”

Terminology consistency outranks lexical variety in this mode.

## Protect untouchable text

Preserve these exactly, even when they break a language rule:

- code blocks and inline code
- identifiers, commands, flags, and file paths
- product names, API endpoints, and configuration keys
- quoted errors and log lines
- numbers with units

Do not rewrite a literal to make the surrounding sentence shorter.

## Write procedural text

- Use the imperative: “Run the migration.”
- Give one instruction per sentence unless two actions must happen at the same time.
- Put a required condition before the command: “If the build fails, read the log.”
- Put warnings and cautions before the dangerous step. State the action first and the consequence second.
- Use `WARNING` for a risk of injury and `CAUTION` for a risk of damage or data loss.
- Keep notes informational. Do not hide instructions inside a note.
- Use a vertical list when several instructions or alternatives would overload one sentence.

Example:

Before: “You will want to get the API key before configuring the client, which you can do under Settings.”

After:

1. Get the API key under Settings.
2. Configure the client with this key.

## Write descriptive text

- Give one new fact per sentence.
- Keep one topic per paragraph.
- Use no more than six sentences in a paragraph.
- Prefer simple present, simple past, or simple future.
- Use active voice when it reveals the actor. Keep passive voice only when the actor is unknown or unimportant.
- Give pronouns clear referents. Prefer “this request” to a bare “this.”
- Connect related sentences with direct words such as “Then” or “As a result” when the relationship would otherwise be unclear.

## Control verbs and sentence structure

In strict mode:

- Use the infinitive, imperative, simple present, simple past, or simple future.
- Use a past participle as an adjective only when its role is clear, as in “the cached response.”
- Avoid present perfect, progressive constructions, and indirect forms such as “is to be installed.”
- Describe an action with a verb, not a noun. Write “compress the file,” not “perform compression of the file.”
- Prefer `can`, `will`, and `must`. Resolve `should`, `would`, `may`, `might`, and `could` according to their actual meaning instead of replacing them mechanically.
- Do not remove articles or necessary instances of `that` to meet the word limit.
- Do not use contractions in strict mode.
- Avoid semicolons. Split the sentence.

Never delete meaningful uncertainty merely because strict STE limits modal verbs. If the source is uncertain, restate the uncertainty accurately or explain that the strict constraint conflicts with the fidelity contract.

## Use plain, complete words

Replace inflated phrasing only when the shorter wording keeps the meaning:

| Instead of | Prefer |
|---|---|
| leverage, utilize | use |
| in order to | to |
| prior to | before |
| it is worth noting that | delete the setup |
| enables you to, allows you to | you can |
| is designed to, aims to | state what it does |
| in the event that | if |
| due to the fact that | because |
| out of the box | by default |
| under the hood | internally |
| e.g. | for example |
| i.e. | that is |
| etc. | name the items or end the list |

Delete unsupported praise such as `robust`, `powerful`, `comprehensive`, `seamless`, and `state-of-the-art`, or replace it with a measurable property already supported by the source.

Do not use this table as a blind ban list. A word can be correct in context.

## Apply surface patterns

### Error messages

State what happened in simple past. Give the cause if it is known. Then give the fix as an imperative. Remove “Oops,” apology filler, and vague “please ensure” language.

### Runbooks and procedures

Use numbered imperative steps. Put each condition before its command. Put warnings before the step that creates the risk.

### Incident reports

Use simple past and concrete measurements. Preserve the timeline, impact, uncertainty, and attribution. Prefer “Between 14:02 and 14:31 UTC, 12% of requests failed” to vague impact language when those facts are supported.

### Release notes

State the change, the affected user or component, and the required action. Treat breaking changes like cautions: give the action before the consequence.

### Agent instructions

Treat prompts and `AGENTS.md` files as procedures. Use one instruction per sentence, put conditions first, and use `must` only for real requirements.

### Translation preparation

Use one name per item, complete grammar, explicit referents, and direct conditions. Avoid slang, regional expressions, unexplained abbreviations, phrasal verbs with ambiguous meanings, and Latin abbreviations.

## Audit and self-check

For a rewrite, run these checks before delivery:

1. Count the words in the three longest prose sentences. Split procedural sentences over 20 words and descriptive sentences over 25 words.
2. Search for contractions, semicolons, `has been`, `have been`, `should`, and progressive verb forms. Review each hit in context.
3. Inspect every `if` and `when` in procedural text. Put a required condition before its command.
4. Search for unused synonyms from the terminology map. Replace accidental term rotation.
5. Confirm that code, identifiers, paths, commands, product names, and quoted errors are unchanged.
6. Compare the result with the fidelity ledger. Restore any lost fact, qualifier, uncertainty, attribution, or commitment.

For an audit-only request, report each material finding as `offending text -> applicable rule -> compliant rewrite`. Cite only rules that appear in this reference. Do not invent ASD-STE100 rule numbers from memory.

## Limits and source

Strict STE is unsuitable for marketing, blog voice, literary prose, and most spoken copy. If the user requests STE for one of those surfaces, explain the tradeoff and keep the broader humanization mode unless they confirm that controlled language matters more than voice.

This reference adapts AminBlg's MIT-licensed [SimpleEnglish skill](https://github.com/AminBlg/SimpleEnglish/blob/379728b51981b6d2ee1de0f201164483a9648972/skills/simple-english/SKILL.md), copyright 2026 AminBlg. It paraphrases the source's ASD-STE100 Issue 9 workflow for this package and preserves the source's practical limits. The official ASD-STE100 dictionary and official rule wording are not included.

MIT permission notice: Permission is granted, free of charge, to use, copy, modify, merge, publish, distribute, sublicense, and sell the software, provided that the copyright and permission notice are included in substantial copies. The software is provided without warranty.
