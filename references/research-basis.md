# Research basis and maintenance notes

This skill is based on a mix of user-supplied AI-writing tropes and public research on AI-generated or AI-assisted writing. Use these notes to maintain the pattern inventory.

Its plain-language pass also adapts George Orwell's six prose rules from “Politics and the English Language” (1946). Treat those rules as editorial heuristics, not evidence of human or machine authorship. Their value is operational: they prompt the editor to test stale phrasing, word length, unnecessary words, passive voice, jargon, and the point at which a rule harms the sentence.

The July 2026 maintenance pass also drew practical editing and self-review ideas from Peter Yang's MIT-licensed [`no-ai-slop`](https://github.com/petergyang/no-ai-slop/tree/61c21c351da4dcb40946a11fead978f2078a2c65) skill. The useful additions were minimum-effective editing, observable-pattern audits without authorship claims, protection for rough voice, and checks for colon reveals, superficial analysis clauses, synonym cycling, manufactured endings, and decorative formatting. Treat this source as practitioner guidance, not research evidence or a universal ban list.

The July 29, 2026 maintenance pass reviewed Jimmy Slagle's [`anti-ai-slop-scriptwriting`](https://github.com/jimmyslagle/anti-ai-slop-scriptwriting/tree/4c3b6a4bb9b1dbf3ca5c146b7d22db2295abfd80) project for spoken-delivery methods. That project is PolyForm Noncommercial 1.0.0, so this package does not copy its files, examples, or linter implementation. The independently written additions here are the spoken-performance contract, structural reference adaptation, explicit breath/mouth/ad-read checks, and pattern coverage for manufactured intimacy and self-interview questions. Treat its corpus claims as practitioner observations, not independently verified performance evidence.

The August 1, 2026 maintenance pass integrated AminBlg's MIT-licensed [`SimpleEnglish`](https://github.com/AminBlg/SimpleEnglish/tree/379728b51981b6d2ee1de0f201164483a9648972) skill. Its controlled-technical-language workflow now lives in `simplified-technical-english.md`: classify procedural and descriptive text, keep terminology stable, put conditions before commands, protect technical literals, and use explicit sentence limits only when that mode is active. The integration preserves a boundary the source makes explicit: these constraints suit technical facts and instructions, not marketing or voice-led prose.

## Evidence-backed signals to keep

- Lexical and stylometric analysis commonly uses features such as lexical diversity, type-token ratio, hapax legomenon rate, sentence length, punctuation, contractions, subjectivity, named entities, and n-gram uniqueness.
- Several studies report that LLM-assisted writing can shift word choice toward terms such as delve, underscore, meticulous, intricate, realm, pivotal, crucial, and related excess vocabulary.
- Research on scientific communication has found LLM-modified passages may use longer or more complex words and lower lexical diversity.
- Model-specific signatures exist. Different LLMs can have distinct styles, and those styles can persist after paraphrase or translation.

## Maintenance rule

Update the pattern list by adding clusters, not single words. A single word can be normal in a human sentence. A cluster of inflated diction, template contrast, vague authority, smooth paragraph symmetry, and generic examples is a stronger signal that the prose needs revision.

Keep the positive system and the signal inventory separate. The plain-language tests improve prose; the signal inventory helps locate passages for review. Neither should override factual fidelity, meaningful uncertainty, technical precision, or the writer's real voice.

Do not convert the inventory into an AI detector. Report observable patterns and the writing problem they create. Do not assign an authorship probability, score the writer, or infer provenance from surface style.
