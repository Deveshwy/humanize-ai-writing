# AI-Writing Signal Taxonomy

Source: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing, revision 1361516048, last changed 2026-06-28T11:52:27Z.

Use this as an editorial signal map. Visible tells should prompt deeper checks for sourcing, neutrality, attribution, specificity, markup, and citation integrity.

## Contents

- [Content signals](#content-signals)
- [Language and grammar signals](#language-and-grammar-signals)
- [Style and formatting signals](#style-and-formatting-signals)
- [User-facing communication signals](#user-facing-communication-signals)
- [Markup signals](#markup-signals)
- [Citation signals](#citation-signals)
- [Miscellaneous edit signals](#miscellaneous-edit-signals)
- [Comment signals](#comment-signals)
- [Review checklist](#review-checklist)

## Content Signals

Prioritize these because they often reveal unsupported or source-level problems:

- Generic significance, legacy, importance, transformation, cultural heritage, broad trend, or impact claims that do not add specific facts.
- Canned notability and attribution language: repetitive emphasis on media coverage, independent sources, public recognition, or "documented" importance.
- Superficial analysis that sounds interpretive but does not connect to cited evidence.
- Promotional or travel-guide tone, especially praise-heavy language around places, products, companies, people, or cultural topics.
- Vague attribution: unnamed experts, observers, critics, industry reports, or broad publications where the actual source should be named.
- Outline-like conclusions about challenges, opportunities, future prospects, or broader implications.
- Leads that treat a broad list title or category-like topic as a proper-noun entity.

Useful revision moves:

- Replace generic importance with a specific, sourced fact.
- Attribute opinions to named sources or remove them.
- Delete empty impact/legacy language unless the source itself supports that frame.
- Convert source-bragging into normal inline citations or concise attribution.

## Language and Grammar Signals

These are weaker alone but useful in clusters:

- Dense clusters of common AI-ish vocabulary, especially abstract evaluative words.
- Avoidance of plain "is" and "are" phrasing in favor of inflated verbs.
- Negative parallelisms such as "not just X, but Y", "not X but Y", and "X rather than Y".
- Repeated three-part sentence structures or triads.
- Forced lexical variety where a normal writer would repeat the precise term.

Useful revision moves:

- Prefer the exact noun or verb over elegant variation.
- Use plain "is" or "are" when the sentence is defining, identifying, or describing.
- Break formulaic contrasts and triads unless the structure carries real meaning.

## Style and Formatting Signals

These often indicate copy-pasted model output or generated wiki text:

- Title case headings where the local style expects sentence case.
- Excessive boldface, especially outside lead definitions.
- Vertical lists with inline headers where prose or standard bullets would be clearer.
- Heavy or unusual em dash use.
- Tables used for prose-like summaries rather than tabular data.
- Curly quotation marks or apostrophes in contexts that normally use straight marks.
- Skipped heading levels or thematic breaks before headings.

Useful revision moves:

- Normalize headings, emphasis, and list structure to the local style.
- Use tables only for genuinely comparable data.
- Keep punctuation consistent with the surrounding document.

## User-Facing Communication Signals

These matter in talk-page comments, edit summaries, reviews, support replies, and agent-authored messages:

- Collaborative helper phrasing that sounds addressed to a user rather than to the page or issue.
- Knowledge-cutoff throat-clearing, speculation about unavailable sources, or self-referential model limitations.
- Placeholder templates, instruction-like remnants, or phrasing that describes how an answer should be written instead of answering.

Useful revision moves:

- Replace helper framing with the actual editorial judgment.
- Remove model self-reference.
- Fill or delete placeholders before publishing.

## Markup Signals

Treat these as concrete defects, not merely style issues:

- Markdown in wikitext or another markup system that does not accept it.
- Broken wikitext, mismatched brackets, malformed refs, or generated citation syntax.
- Search-result artifacts such as `turn0search0` or links to searches rather than sources.
- Generated citation tokens such as `contentReference`, `oaicite`, `oai_citation`, `attached_file`, `grok_card`, or similar tool residue.
- Nonexistent or out-of-place categories, templates, policy links, or shortcuts.

Useful revision moves:

- Convert Markdown to the target markup.
- Replace search links with actual sources.
- Remove generated tool tokens and repair citations manually.
- Verify categories, templates, and shortcuts before keeping them.

## Citation Signals

These are high priority because they can hide fabricated or unsupported claims:

- Broken external links.
- Invalid DOI or ISBN values.
- DOI links that resolve to unrelated works.
- Book citations without page numbers or usable access details when the claim needs them.
- Reference tags used incorrectly or unconventionally.
- Tracking parameters such as `utm_source=` in citations.
- Named references declared in a reference section but unused in the article body.

Useful revision moves:

- Open and verify cited sources when the claim matters.
- Add page numbers, archive links, or stable identifiers where appropriate.
- Remove unrelated or unusable citations rather than decorating unsupported claims.

## Miscellaneous Edit Signals

- A pronounced shift in style inside one page or document.
- Overly exhaustive edit summaries that read like generated changelogs.
- AfC-style "submission statements" embedded in drafts.
- Pre-placed maintenance templates or permission-gaming language.
- Sudden differences that line up with known model habits or tool artifacts.

## Comment Signals

For Wikipedia/editor comments and review replies, watch for:

- Canned assurances of quality, good faith, neutrality, policy adherence, or willingness to improve.
- Generic offers to receive constructive criticism.
- Calls to focus on content rather than conduct when they do not address the concrete issue.
- Complaints that accusations are speculative without explaining the edit.
- Subject lines or section titles pasted as plain text.
- Nonexistent policies, guidelines, or shortcuts.
- Article maintenance banners transcluded into discussion.
- Over-formal wikilawyering or misused policy shortcuts.
- Emoji or decorative formatting where local norms do not support it.
- Confusion over why a draft was declined.
- Generic requests for source assessment without naming the source question.

Useful revision moves:

- State the specific edit, source, policy, or factual question.
- Keep the comment short and humanly accountable.
- Avoid generic virtue claims; show the reasoning instead.

## Review Checklist

1. Does the passage make claims that are specific, attributed, and source-supported?
2. Are praise, legacy, impact, or trend claims necessary and backed by the source?
3. Are opinions attributed to named sources?
4. Are citations valid, relevant, and formatted for the target surface?
5. Does the prose use formulaic contrasts, triads, or inflated verbs where simpler wording is better?
6. Are markup, headings, emphasis, lists, tables, and punctuation consistent with local style?
7. If commenting, does the comment explain the actual editorial judgment rather than promising quality?
8. Would removing only the visible AI tell leave the deeper problem untouched? If yes, fix the deeper problem first.
