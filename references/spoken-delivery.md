# Spoken delivery

Use this reference for scripts, VSLs, speaker notes, podcast copy, dialogue, video voiceover, and any text a person will perform.

## Contents

- [Set the performance contract](#set-the-performance-contract)
- [Choose the source hierarchy](#choose-the-source-hierarchy)
- [Adapt a reference without cloning it](#adapt-a-reference-without-cloning-it)
- [Rewrite for the mouth](#rewrite-for-the-mouth)
- [Run the read-aloud pass](#run-the-read-aloud-pass)
- [Avoid fake humanity](#avoid-fake-humanity)
- [Check the final script](#check-the-final-script)

## Set the performance contract

Lock these before editing:

- speaker and relationship to the audience
- delivery surface: camera, stage, webinar, podcast, voiceover, or conversation
- target runtime and likely speaking pace
- desired action or emotional landing point
- claims, proof, quotes, offer terms, and visual cues that cannot drift

Treat runtime as a constraint, not a reason to cut qualifiers or proof. If the piece is too long, remove redundant setup and repeated explanation first.

## Choose the source hierarchy

Use the most relevant evidence available:

1. the speaker's real recordings or transcripts
2. several representative samples from the same speaker and surface
3. the user's supplied reference script plus the speaker's written voice
4. written samples from the speaker
5. a neutral spoken register

Do not infer a whole voice from one polished sample when more material is available. For a serious voice match, compare at least two samples and note recurring pacing, diction, direct-address habits, humor, uncertainty, and closing style.

## Adapt a reference without cloning it

When the user supplies a useful script, identify the job of each beat:

- opener: what earns the next few seconds?
- setup: what situation or tension becomes concrete?
- turn: what changes the listener's understanding?
- proof: what earns belief?
- close: what should the listener do or feel?

Keep only the functional skeleton and pacing that fit the new task. Rewrite every claim and line from the user's source material. Do not carry over distinctive phrases, anecdotes, numbers, testimonials, urgency, or outcomes. If the reference is called “proven” but no evidence is supplied, treat it as a structural reference, not verified performance proof.

## Rewrite for the mouth

- Prefer words the speaker would actually say.
- Use contractions when the speaker uses them.
- Let sentence length change with the thought. Short beats can land; longer runs can carry explanation.
- Repeat the exact word when speech would repeat it. Do not cycle through synonyms to look polished.
- Use fragments and asides only when they fit the speaker and remain easy to follow.
- Replace abstract benefits with named actions, objects, constraints, body facts, dates, quantities, or consequences already supported by the source.
- Move to the next thought without announcing the transition.
- Make the close sound like the same person who delivered the body.

Line breaks should help performance. They should not turn every sentence into a dramatic fragment.

## Run the read-aloud pass

Read the full draft at likely performance speed.

1. **Breath:** Mark where a speaker naturally pauses. Break or reshape lines that demand too much air. If every pause lands at the same interval, vary the syntax where the thought allows it.
2. **Mouth:** Rewrite any cluster that causes a stumble, forces a restart, or only works when silently read.
3. **Ad-read:** Mark any line that suddenly sounds like a brochure, generic creator script, or stage direction disguised as dialogue. Replace it with the concrete point.
4. **Self-interview:** Remove canned questions the speaker asks only to answer immediately. Keep genuine questions addressed to the listener, deliberate question hooks, and questions that create a real pause or response.
5. **Timing:** Time the read when runtime matters. Edit against the actual read, not a generic words-per-minute assumption.

For substantial drafts, run:

```bash
python3 scripts/ai_style_audit.py --spoken <draft-file>
```

Treat the output as review leads. It cannot hear delivery or decide whether a phrase belongs to the speaker.

## Avoid fake humanity

Natural speech is not a bag of inserted imperfections.

- Preserve a speaker's real repetitions, hedges, slang, profanity, false starts, and filler when they help the performance.
- Do not add `um`, `like`, stutters, dropped letters, regional slang, or confessional openers merely to make a clean draft look human.
- Do not force fragments into a speaker whose real delivery is measured and grammatical.
- Do not use performed intimacy such as asking permission to “be honest.” State the honest thing.
- Do not mistake chaos for voice. A useful rough edge belongs to this speaker at this moment.

## Check the final script

- The facts, proof, uncertainty, offer, and ask still match the fidelity ledger.
- The speaker could say every line in one natural take.
- The pacing changes for a reason.
- Questions are real, not conversational decoration.
- Repetition is deliberate or voice-true.
- No line imports unsupported material from a reference.
- The ending lands on the actual action, proof point, or emotional beat instead of a slogan.
