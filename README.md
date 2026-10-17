# Humanize AI Writing

An agent skill for making prose clear, natural, and specific while preserving facts, meaning, citations, uncertainty, commitments, and the writer's voice.

Use it to clean up a draft, rewrite it, match a supplied voice, prepare a spoken script, or audit writing patterns. It also includes guidance for direct-response copy, Wikipedia and informational writing, and controlled technical English.

## Install

Download this repository using **Code → Download ZIP**, then extract it. Put the entire `humanize-ai-writing` folder in your agent's skills directory. Keep `SKILL.md`, `references/`, `scripts/`, and `agents/` together so the skill can find its supporting files.

You can also clone this repository directly into your agent's skills directory. If your agent supports installing skills from GitHub, give it this repository's URL and ask it to install `humanize-ai-writing`.

For a tool without skill support, give it [SKILL.md](SKILL.md) and access to the referenced files. The main instructions explain which references to read for each task.

## Use

Ask your agent to use `humanize-ai-writing` and provide your draft, audience, and any constraints. For example:

```text
Use humanize-ai-writing to lightly clean this draft. Preserve the structure,
facts, citations, and my voice. Remove filler and awkward phrasing.
```

```text
Use humanize-ai-writing in pattern audit mode. Identify material writing
problems and suggest fixes without rewriting the draft.
```

```text
Use humanize-ai-writing in spoken delivery mode. Make this script easier
to say aloud while preserving the claims, offer, and call to action.
```

The available modes are light clean, full rewrite, voice match, pattern audit, spoken delivery, direct-response blacklist, Wikipedia/editorial, and controlled technical English.

## Files

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Main instructions, workflow, and reference routing |
| [agents/openai.yaml](agents/openai.yaml) | Display metadata and default prompt |
| [references/rewrite-playbook.md](references/rewrite-playbook.md) | Editing passes for substantial rewrites |
| [references/plain-language-system.md](references/plain-language-system.md) | Plain-language tests and surface checks |
| [references/simplified-technical-english.md](references/simplified-technical-english.md) | Pragmatic and strict controlled technical English |
| [references/voice-calibration.md](references/voice-calibration.md) | Voice matching from supplied samples |
| [references/spoken-delivery.md](references/spoken-delivery.md) | Scripts and read-aloud copy |
| [references/ai-slop-patterns.md](references/ai-slop-patterns.md) | Observable writing patterns to review |
| [references/ai-writing-signals.md](references/ai-writing-signals.md) | Editorial, sourcing, citation, and markup checks |
| [references/direct-response-blacklist.md](references/direct-response-blacklist.md) | Constraints for direct-response copy |
| [references/research-basis.md](references/research-basis.md) | Source credits and evidentiary limits |
| [scripts/ai_style_audit.py](scripts/ai_style_audit.py) | General and spoken writing-pattern flags |
| [scripts/audit_blacklist.py](scripts/audit_blacklist.py) | Direct-response copy flags |

## Optional audit scripts

The scripts use Python 3 and its standard library. No additional Python packages or API keys are required. Run them from the skill folder:

```bash
python3 scripts/ai_style_audit.py draft.md
python3 scripts/ai_style_audit.py --spoken draft.md
python3 scripts/ai_style_audit.py --json draft.md
python3 scripts/audit_blacklist.py draft.md
```

Both scripts also accept text through standard input. `audit_blacklist.py` returns exit code `1` when it finds review flags and `0` when it finds none.

The findings need human review. They do not establish whether AI wrote a text. Strict ASD-STE100 compliance also requires the official dictionary; the skill includes an unofficial editing aid.

## Sources and credits

The original skill instructions, nine references, two scripts, and agent metadata are preserved unchanged. See [research-basis.md](references/research-basis.md) for the skill's sources and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution and license notices.
