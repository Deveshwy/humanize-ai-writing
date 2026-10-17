# Direct-response copy blacklist

Apply this negative style guide only when writing or auditing direct-response copy, or when the user explicitly requests a blacklist review. Script findings are review flags, not automatic defects; quoted examples and deliberate repetition may be valid.

## Hard bans

Remove:

- False contrast stacks such as "It's not X. It's not Y. It's Z."
- Three consecutive short sentences with matching punch-line rhythm.
- Generic rhetorical section openers such as "But what does that actually mean?"
- Self-interview lines such as "Honestly?" "Sound familiar?" and "Crazy, right?" unless they are a genuine question hook or invite a real response.
- Manufactured-intimacy openers that ask permission to be honest instead of stating the admission.
- Generic fantasy openings such as "Imagine waking up to..."
- Repeated openers or sentence skeletons used as artificial emphasis.
- Filler transitions such as "Let's dive in," "Here's the thing," "At the end of the day," "More on that later," and "But wait, there's more."
- Dramatic colon reveals such as “The best part: it learns” or “The real secret: distribution.”
- Emoji or exclamation-point overload.
- Dense paragraphs that ignore the intended reading pace.

## Repetition and momentum

Reject consecutive frames such as:

- "Same close rate. Same conversion. Different result."
- "More leads. More calls. More revenue."
- "No inspections. No appraisals. No banks."

Rewrite with progression. Each line should add evidence, raise the stakes, deepen the implication, or move the argument forward.

## Claims

Remove empty compound hedges such as "could potentially" or "in many cases." Replace them with the strongest version the source supports.

If proof is missing:

- State the limit.
- Narrow the claim.
- Mark the claim for verification.
- Remove it.

Never invent testimonials, performance data, customer outcomes, deadlines, scarcity, or guarantees.

## Formatting

- Use line breaks to support pacing, not to create a stack of dramatic fragments.
- Use emojis only when explicitly requested and appropriate to the platform.
- Let urgency come from proof, timing, stakes, offer structure, or a real deadline.
- Prefer readable paragraphs over a sequence of isolated slogans.
- Delete fake-profound kicker lines instead of rewriting them into a stronger slogan. End on the last concrete point, supported takeaway, or next action.

## Final check

1. Scan for banned transitions and rhetorical openers.
2. Check adjacent lines and sentences for repeated openings or syntax.
3. Check for three short punchy sentences in a row.
4. Verify that every strong claim has support or a stated limit.
5. Break dense paragraphs where the reading experience requires it.
6. Run `scripts/audit_blacklist.py` and manually review every flag in context.
7. Check the ending for recap, sloganized wisdom, or an unnecessary mic drop.
8. For spoken copy, run the breath, mouth, ad-read, self-interview, and timing checks in `spoken-delivery.md`.

Do not mention the blacklist review unless the user asks for it.
