#!/usr/bin/env python3
"""Flag observable writing patterns for editorial review without inferring authorship."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List

PHRASE_PATTERNS: Dict[str, List[str]] = {
    "teacher_mode": [
        r"\blet'?s\s+(?:break\s+this\s+down|unpack|dive\s+in|delve\s+into|explore)\b",
        r"\bthink\s+of\s+it\s+as\b",
        r"\bit'?s\s+like\b",
    ],
    "filler_transitions": [
        r"\bit\s+is\s+(?:important|worth)\s+(?:to\s+note|noting)\b",
        r"\bit\s+bears\s+mentioning\b",
        r"\bnotably\b",
        r"\bimportantly\b",
        r"\binterestingly\b",
        r"\bin\s+conclusion\b",
        r"\bin\s+summary\b",
    ],
    "false_suspense": [
        r"\bhere'?s\s+(?:the\s+thing|the\s+kicker|where\s+it\s+gets\s+interesting|what\s+most\s+people\s+miss|the\s+deal)\b",
    ],
    "manufactured_intimacy": [
        r"\b(?:can\s+i\s+be\s+(?:real|honest)(?:\s+with\s+you)?(?:\s+for\s+a\s+(?:second|minute|sec))?|can\s+we\s+be\s+(?:real|honest)|let\s+me\s+be\s+(?:real|honest)|real\s+talk)\b",
    ],
    "self_interview": [
        r"\b(?:honestly|seriously|sound\s+familiar|crazy,?\s+right|guess\s+what|the\s+(?:best|worst|craziest)\s+part)\s*\?",
        r"\byou\s+know\s+what(?:'?s|\s+is)\s+(?:crazy|wild|funny)\s*\?",
    ],
    "audience_enumeration": [
        r"\bwhether\s+you(?:'re|\s+are)\s+[^.?!]{1,80}\s+or\s+[^.?!]{1,80}",
    ],
    "faux_insight_setup": [
        r"\bwhat\s+(?:most\s+people|nobody|everyone)\s+(?:miss(?:es)?|get(?:s)?\s+wrong|tell(?:s)?\s+you|skip(?:s)?)\b",
        r"\bthis\s+is\s+the\s+part\s+(?:most\s+people|everyone)\s+(?:miss(?:es)?|skip(?:s)?)\b",
    ],
    "colon_reveal": [
        r"\bthe\s+(?:best|worst|real|hard|scary|funny|important)\s+(?:part|thing|detail|reason|problem|point|truth|answer)\s*:\s+[a-z]",
        r"\bthe\s+(?:detail|move|change)\s+that\s+(?:makes|made)\s+it\s+work\s*:\s+[a-z]",
    ],
    "negative_parallelism": [
        r"\bnot\s+just\s+[^.?!;]{1,120}\s+but\s+(?:also\s+)?[^.?!;]{1,120}",
        r"\bnot\s+only\s+[^.?!;]{1,120}\s+but\s+(?:also\s+)?[^.?!;]{1,120}",
        r"\bthe\s+question\s+isn'?t\s+[^.?!;]{1,120}\b.*?\bthe\s+question\s+is\s+[^.?!;]{1,120}",
        r"\bnot\s+because\s+[^.?!;]{1,120}\s+but\s+because\s+[^.?!;]{1,120}",
    ],
    "rhetorical_punchline": [
        r"\b(?:the\s+)?(?:result|problem|catch|point|takeaway|worst\s+part|scary\s+part)\?",
    ],
    "false_ranges": [
        r"\bfrom\s+[^.?!\n]{1,80}\s+to\s+[^.?!\n]{1,80}",
    ],
    "grandiose_stakes": [
        r"\b(?:revolutionize|transform|reshape|redefine)\s+(?:the\s+)?(?:future|way|era|landscape)\b",
        r"\bchange\s+everything\b",
        r"\bnext\s+era\b",
        r"\bfundamentally\s+reshape\b",
    ],
    "vague_authority": [
        r"\bexperts\s+(?:say|argue|suggest|believe)\b",
        r"\bobservers\s+(?:say|argue|suggest|believe|note)\b",
        r"\bindustry\s+reports\s+suggest\b",
        r"\bstudies\s+show\b",
        r"\bmany\s+(?:believe|argue|say)\b",
    ],
    "serves_as": [
        r"\b(?:serves|served|serving)\s+as\b",
        r"\bstands\s+as\b",
        r"\bmarks\s+a\s+(?:pivotal|significant|critical)\b",
    ],
    "ai_vocab": [
        r"\b(?:delve|delves|delving|tapestry|landscape|realm|ecosystem|paradigm|synergy)\b",
        r"\b(?:leverage|leveraging|utilize|utilizing|harness|unlock|streamline|facilitate)\b",
        r"\b(?:robust|seamless|comprehensive|pivotal|crucial|intricate|meticulous|transformative|groundbreaking|multifaceted|dynamic)\b",
    ],
    "soft_analysis_tags": [
        r",\s+(?:highlighting|underscoring|reflecting|showcasing|demonstrating|emphasizing)\s+[^.?!]{1,120}",
    ],
    "dramatic_fragment": [
        r"\bthat'?s\s+it\.\s+that'?s\s+the\s+whole\s+thing\b",
        r"\bnot\s+[^.?!]{1,45}[.!?]\s+not\s+[^.?!]{1,45}[.!?]\s+(?:a|an|the|just)\s+[^.?!]{1,60}[.!?]",
    ],
}

WEIGHTS = {
    "teacher_mode": 3,
    "filler_transitions": 2,
    "false_suspense": 3,
    "manufactured_intimacy": 3,
    "self_interview": 3,
    "audience_enumeration": 2,
    "faux_insight_setup": 3,
    "colon_reveal": 2,
    "negative_parallelism": 4,
    "rhetorical_punchline": 3,
    "false_ranges": 2,
    "grandiose_stakes": 3,
    "vague_authority": 3,
    "serves_as": 2,
    "ai_vocab": 1,
    "soft_analysis_tags": 2,
    "dramatic_fragment": 3,
}

WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+|\n+")
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF]")


def read_text(args: argparse.Namespace) -> str:
    if args.text:
        return args.text
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("Provide --text, --file, or pipe text on stdin.")


def split_sentences(text: str) -> List[str]:
    parts = [p.strip() for p in SENTENCE_RE.split(text) if p.strip()]
    # Split very long newline-free blocks more cautiously on semicolons.
    sentences: List[str] = []
    for part in parts:
        if len(part) > 350 and ";" in part:
            sentences.extend([p.strip() for p in part.split(";") if p.strip()])
        else:
            sentences.append(part)
    return sentences


def tokenize(text: str) -> List[str]:
    return [m.group(0).lower() for m in WORD_RE.finditer(text)]


def count_pattern_hits(text: str) -> Dict[str, int]:
    hits = {}
    for category, patterns in PHRASE_PATTERNS.items():
        total = 0
        for pattern in patterns:
            total += len(re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL))
        hits[category] = total
    return hits


def sentence_start_repeats(sentences: Iterable[str]) -> Dict[str, int]:
    starts = []
    for sentence in sentences:
        words = tokenize(sentence)[:3]
        if len(words) >= 2:
            starts.append(" ".join(words))
    return {k: v for k, v in Counter(starts).items() if v > 1}


def markdown_tells(text: str) -> Dict[str, int]:
    lines = text.splitlines()
    bold_first = 0
    bullets = 0
    headings = 0
    bold_spans = 0
    for line in lines:
        if re.match(r"^\s*(?:[-*+]\s+|\d+\.\s+)\*\*[^*]+\*\*", line):
            bold_first += 1
        if re.match(r"^\s*(?:[-*+]\s+|\d+\.\s+)", line):
            bullets += 1
        if re.match(r"^\s{0,3}#{1,6}\s+", line):
            headings += 1
        bold_spans += len(re.findall(r"\*\*[^*\n]+\*\*", line))
    return {
        "bold_first_bullets": bold_first,
        "bold_spans": bold_spans,
        "bullet_lines": bullets,
        "heading_lines": headings,
        "em_dashes": text.count("—") + len(re.findall(r"\s--\s", text)),
        "unicode_arrows": len(re.findall(r"[→⇒➜➔]", text)),
        "emoji": len(EMOJI_RE.findall(text)),
        "smart_quotes": sum(text.count(ch) for ch in "“”‘’"),
    }


def short_sentence_stacks(sentences: List[str]) -> int:
    lengths = [len(tokenize(sentence)) for sentence in sentences]
    return sum(1 for window in zip(lengths, lengths[1:], lengths[2:]) if all(1 <= value <= 5 for value in window))


def ending_tells(text: str) -> List[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]
    if not paragraphs:
        return []
    ending = paragraphs[-1]
    findings: List[str] = []
    if re.match(r"^(?:in\s+conclusion|ultimately|overall)\b", ending, flags=re.IGNORECASE):
        findings.append("recap-style ending opener")
    if re.search(r"\bthat'?s\s+it\.\s+that'?s\s+the\s+whole\s+thing[.!]?\s*$", ending, flags=re.IGNORECASE):
        findings.append("dramatic mic-drop ending")
    return findings


def spoken_delivery_metrics(text: str, sentences: List[str], word_count: int) -> Dict[str, object]:
    sentence_lengths = [len(tokenize(sentence)) for sentence in sentences if tokenize(sentence)]
    long_lines = [
        index
        for index, line in enumerate(text.splitlines(), 1)
        if len(tokenize(line)) >= 32
    ]
    contraction_count = len(
        re.findall(
            r"\b(?:i'm|i've|i'll|i'd|you're|you've|you'll|you'd|we're|we've|we'll|"
            r"we'd|they're|they've|they'll|they'd|he's|she's|it's|that's|there's|"
            r"isn't|aren't|wasn't|weren't|don't|doesn't|didn't|can't|couldn't|"
            r"won't|wouldn't|shouldn't|haven't|hasn't|hadn't)\b",
            text,
            flags=re.IGNORECASE,
        )
    )
    return {
        "sentences_over_31_words": sum(1 for length in sentence_lengths if length >= 32),
        "lines_over_31_words": long_lines[:12],
        "contraction_count": contraction_count,
        "formal_register_flag": word_count >= 80 and contraction_count == 0,
        "manual_checks": ["breath", "mouth", "ad-read", "self-interview", "timing"],
    }


def compute_metrics(text: str, spoken: bool = False) -> Dict[str, object]:
    words = tokenize(text)
    sentences = split_sentences(text)
    sentence_lengths = [len(tokenize(s)) for s in sentences if tokenize(s)]
    unique_words = set(words)
    pattern_hits = count_pattern_hits(text)
    format_hits = markdown_tells(text)
    repeated_starts = sentence_start_repeats(sentences)
    fragment_stacks = short_sentence_stacks(sentences)
    ending_flags = ending_tells(text)

    avg_sentence = statistics.mean(sentence_lengths) if sentence_lengths else 0.0
    sentence_std = statistics.pstdev(sentence_lengths) if len(sentence_lengths) > 1 else 0.0
    burstiness = sentence_std / avg_sentence if avg_sentence else 0.0
    ttr = len(unique_words) / len(words) if words else 0.0

    metrics: Dict[str, object] = {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "avg_sentence_length_words": round(avg_sentence, 2),
        "sentence_length_stddev": round(sentence_std, 2),
        "burstiness_stddev_over_mean": round(burstiness, 3),
        "type_token_ratio": round(ttr, 3),
        "pattern_hits": pattern_hits,
        "formatting_hits": format_hits,
        "repeated_sentence_starts": repeated_starts,
        "short_sentence_stacks": fragment_stacks,
        "ending_flags": ending_flags,
    }
    if spoken:
        metrics["spoken_delivery"] = spoken_delivery_metrics(text, sentences, len(words))
    return metrics


def top_findings(metrics: Dict[str, object]) -> List[str]:
    findings: List[str] = []
    pattern_hits = metrics["pattern_hits"]
    formatting_hits = metrics["formatting_hits"]
    assert isinstance(pattern_hits, dict)
    assert isinstance(formatting_hits, dict)

    for category, count in sorted(pattern_hits.items(), key=lambda item: item[1] * WEIGHTS.get(item[0], 1), reverse=True):
        if count:
            findings.append(f"{category.replace('_', ' ')}: {count}")
    for category in ["bold_first_bullets", "em_dashes", "unicode_arrows", "emoji", "smart_quotes"]:
        count = formatting_hits.get(category, 0)
        if count:
            findings.append(f"{category.replace('_', ' ')}: {count}")
    bold_spans = formatting_hits.get("bold_spans", 0)
    if isinstance(bold_spans, int) and bold_spans > 3:
        findings.append(f"bold spans to review for decorative emphasis: {bold_spans}")
    repeats = metrics.get("repeated_sentence_starts", {})
    if isinstance(repeats, dict) and repeats:
        finding = ", ".join(f"'{k}' x{v}" for k, v in sorted(repeats.items())[:5])
        findings.append(f"repeated sentence starts: {finding}")
    fragment_stacks = metrics.get("short_sentence_stacks", 0)
    if isinstance(fragment_stacks, int) and fragment_stacks:
        findings.append(f"stacked short sentences to review in context: {fragment_stacks}")
    ending_flags = metrics.get("ending_flags", [])
    if isinstance(ending_flags, list):
        findings.extend(str(item) for item in ending_flags)
    word_count = metrics.get("word_count", 0)
    burstiness = metrics.get("burstiness_stddev_over_mean", 0)
    if isinstance(word_count, int) and word_count > 120 and isinstance(burstiness, (int, float)) and burstiness < 0.35:
        findings.append("sentence lengths are unusually uniform; review the rhythm in context")
    spoken = metrics.get("spoken_delivery")
    if isinstance(spoken, dict):
        long_count = spoken.get("sentences_over_31_words", 0)
        if isinstance(long_count, int) and long_count:
            findings.append(f"spoken lines likely to need a breath or mouth check: {long_count}")
        if spoken.get("formal_register_flag"):
            findings.append("no contractions in a substantial spoken draft; verify that this formal register belongs to the speaker")
    if not findings:
        findings.append("No strong surface patterns found. Check specificity, sourcing, and voice manually.")
    return findings[:12]


def print_markdown(metrics: Dict[str, object]) -> None:
    print("# Writing-pattern audit")
    print()
    print(f"- Words: {metrics['word_count']}")
    print(f"- Sentences: {metrics['sentence_count']}")
    print(f"- Average sentence length: {metrics['avg_sentence_length_words']} words")
    print(f"- Sentence rhythm / burstiness: {metrics['burstiness_stddev_over_mean']}")
    print(f"- Type-token ratio: {metrics['type_token_ratio']}")
    spoken = metrics.get("spoken_delivery")
    if isinstance(spoken, dict):
        print(f"- Spoken lines over 31 words: {spoken['sentences_over_31_words']}")
        print(f"- Contractions: {spoken['contraction_count']}")
    print()
    print("## Strongest findings")
    for item in top_findings(metrics):
        print(f"- {item}")
    print()
    print("## Edit priorities")
    print("- Remove generic setup and recap if present.")
    print("- Replace inflated vocabulary with exact verbs and nouns.")
    print("- Add real actors, constraints, examples, and tradeoffs where supported.")
    print("- Vary rhythm only where the thought calls for it.")
    print()
    print("These are review flags, not evidence of human or model authorship.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit text for observable writing patterns without inferring authorship.")
    parser.add_argument("file", nargs="?", help="Text file to audit")
    parser.add_argument("--text", help="Text to audit")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of Markdown")
    parser.add_argument("--spoken", action="store_true", help="Add performance-oriented review flags for scripts and read-aloud copy")
    args = parser.parse_args()

    text = read_text(args)
    metrics = compute_metrics(text, spoken=args.spoken)
    if args.json:
        print(json.dumps(metrics, indent=2, ensure_ascii=False))
    else:
        print_markdown(metrics)


if __name__ == "__main__":
    main()
