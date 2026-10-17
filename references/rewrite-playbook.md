# Rewrite playbook

Use these passes in order for substantial edits.

## Contents

- [Pass 1: Lock the meaning](#pass-1-lock-the-meaning)
- [Pass 2: Cut machine scaffolding](#pass-2-cut-machine-scaffolding)
- [Pass 3: Replace abstraction with visible action](#pass-3-replace-abstraction-with-visible-action)
- [Pass 4: Restore human decision-making](#pass-4-restore-human-decision-making)
- [Pass 5: Fix sentence texture](#pass-5-fix-sentence-texture)
- [Pass 6: Rebuild structure](#pass-6-rebuild-structure)
- [Pass 7: Final human check](#pass-7-final-human-check)
- [Common transformations](#common-transformations)
- [Editing intensity](#editing-intensity)

## Pass 1: Lock the meaning

Before rewriting, identify:
- main claim
- audience
- desired action or feeling
- facts that must not change
- claims that need sourcing or removal

Do not add new facts to make the draft sound human.

Set the editing budget before rewriting. Make the minimum effective edit for the requested mode. Mark strong sentences, useful detours, and voice-bearing rough edges that should survive.

## Pass 2: Cut machine scaffolding

Remove generic openings before editing sentences.

Cut or rewrite:
- "In today's fast-paced world"
- "In an ever-evolving landscape"
- "It is important to note"
- "This article explores"
- "Let's dive into"
- "In conclusion"
- "By embracing X, we can unlock Y"
- "Whether you're X or Y"

Start where the actual point starts.

## Pass 3: Replace abstraction with visible action

Ask: who does what, to whom, with what consequence?

Weak: "The solution enables a more seamless customer experience."
Human: "Customers no longer have to repeat their address when they move from chat to phone support."

Weak: "This highlights the importance of cross-functional alignment."
Human: "The launch slipped because product and support were working from different dates."

## Pass 4: Restore human decision-making

AI often writes neutral summaries. Human writing makes choices.

Add, when supported by the text:
- what matters most
- what is uncertain
- what the writer would do next
- what does not matter
- what the tradeoff is
- what the reader should ignore

Avoid fake certainty. A grounded "probably" is more human than a hollow "clearly."

## Pass 5: Fix sentence texture

Use these edits:
- Swap nominalizations for verbs: "implementation of" -> "implement" or name the actor.
- Replace pompous linking verbs: "serves as" -> "is" or "works as."
- Break long parallel strings if they sound staged.
- Combine choppy fragments unless the genre supports them.
- Keep contractions only if they fit the speaker and context.
- Use plain punctuation. Keep em dashes only where they beat the alternatives.

## Pass 6: Rebuild structure

Choose the structure humans expect for the genre.

Rebuild only when the current structure blocks the piece's job. Lead with the conclusion when setup adds nothing, but keep a story, admission, aside, or delayed reveal when it supplies context, tension, evidence, or character. Do not impose the same point-detail-background pattern on every paragraph.

Email:
1. reason for writing
2. needed context
3. ask or decision
4. deadline or next step

Memo:
1. recommendation
2. reason
3. evidence
4. tradeoffs
5. next action

Blog/opinion:
1. concrete hook
2. claim
3. evidence or example
4. implication
5. ending that adds something, not a recap

Product/marketing:
1. user problem
2. product behavior
3. proof or example
4. clear call to action

Academic/professional prose:
1. claim
2. method or evidence
3. limitation
4. implication

## Pass 7: Final human check

Read the result out loud. Remove lines that sound like an assistant performing helpfulness.

Check for:
- one clear voice
- edits proportional to the actual problem
- strong human sentences left alone
- useful bluntness, humor, uncertainty, profanity, fragments, and digressions preserved
- no unsupported specifics
- no fake anecdote
- no generic recap or fake-profound kicker ending
- an ending on the last concrete point, supported takeaway, or next action
- consistent names for the same entity instead of synonym cycling
- no stack of inflated adjectives
- no repeated sentence openings
- no colon reveals, trailing fake-analysis clauses, or inflated proxy verbs
- no excessive markdown, decorative bold, or headings over tiny sections

For a pattern-only audit, quote the smallest useful snippet, name the observable pattern, and give the fix. Do not rewrite the draft, score it, or claim to determine whether a human or model wrote it.

## Common transformations

| AI-flavored draft | Better direction |
|---|---|
| "This serves as a testament to..." | Say what it proves, or cut it. |
| "It is important to note that..." | Delete the phrase; keep the point if useful. |
| "The ever-evolving landscape of..." | Name the actual field or change. |
| "Unlock new opportunities" | Name the opportunity. |
| "Seamless experience" | Describe the missing step or reduced friction. |
| "Robust framework" | Name the system, rule, or process. |
| "Not only X, but also Y" | Use "X and Y" unless the contrast matters. |
| "From X to Y" | Use a real sequence or list. |
| "Experts agree" | Name the source or remove the appeal. |
| "This underscores the need" | Say "This means we need" or name the action. |

## Editing intensity

Light clean:
- Keep order and most phrasing.
- Remove filler and obvious AI markers.
- Fix rhythm lightly.

Medium rewrite:
- Reorder paragraphs when helpful.
- Replace generic claims with concrete versions already implied by the draft.
- Tighten to the user's likely voice.

Full rewrite:
- Rebuild structure around the strongest claim.
- Remove template architecture.
- Preserve facts and intent.
- Add placeholders where missing human details are needed.
