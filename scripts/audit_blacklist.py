#!/usr/bin/env python3
"""Flag direct-response copy patterns that require manual review."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BANNED_PHRASES = [
    "let's dive in",
    "here's the thing",
    "at the end of the day",
    "in today's fast-paced digital world",
    "more on that later",
    "but wait, there's more",
]

BANNED_HEDGES = [
    "could potentially",
    "in many cases",
]

RHYTHM_OPENERS = [
    "same",
    "more",
    "less",
    "no",
    "people",
]

RHETORICAL_OPENERS = [
    r"\bbut what does that actually mean\?",
    r"\bso,?\s+how does it work\?",
    r"\bwhat does this mean for you\?",
]

COLON_REVEALS = [
    r"\bthe\s+(?:best|worst|real|hard|scary|funny|important)\s+(?:part|thing|detail|reason|problem|point|truth|answer)\s*:\s+[a-z]",
    r"\bthe\s+(?:detail|move|change)\s+that\s+(?:makes|made)\s+it\s+work\s*:\s+[a-z]",
]

FAUX_INSIGHT_SETUPS = [
    r"\bwhat\s+(?:most\s+people|nobody|everyone)\s+(?:miss(?:es)?|get(?:s)?\s+wrong|tell(?:s)?\s+you|skip(?:s)?)\b",
    r"\bthis\s+is\s+the\s+part\s+(?:most\s+people|everyone)\s+(?:miss(?:es)?|skip(?:s)?)\b",
]

MANUFACTURED_INTIMACY = [
    r"\bcan\s+i\s+be\s+(?:real|honest)(?:\s+with\s+you)?(?:\s+for\s+a\s+(?:second|minute|sec))?\b",
    r"\bcan\s+we\s+be\s+(?:real|honest)\b",
    r"\blet\s+me\s+be\s+(?:real|honest)\b",
    r"\breal\s+talk\b",
]

SELF_INTERVIEW_QUESTIONS = [
    r"\b(?:honestly|seriously|sound\s+familiar|crazy,?\s+right|guess\s+what|the\s+(?:best|worst|craziest)\s+part)\s*\?",
    r"\byou\s+know\s+what(?:'?s|\s+is)\s+(?:crazy|wild|funny)\s*\?",
]


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def emit(findings: list[str], message: str) -> None:
    findings.append(message)


def find_exact_patterns(text: str, findings: list[str]) -> None:
    lowered = text.lower()

    for phrase in BANNED_PHRASES:
        start = 0
        while True:
            index = lowered.find(phrase, start)
            if index == -1:
                break
            emit(findings, f"line {line_number(text, index)}: banned phrase: {phrase!r}")
            start = index + len(phrase)

    for hedge in BANNED_HEDGES:
        pattern = re.compile(rf"\b{re.escape(hedge)}\b", re.IGNORECASE)
        for match in pattern.finditer(text):
            emit(findings, f"line {line_number(text, match.start())}: vague hedge to review: {hedge!r}")

    for pattern in RHETORICAL_OPENERS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            emit(findings, f"line {line_number(text, match.start())}: rhetorical section opener")

    for pattern in COLON_REVEALS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            emit(findings, f"line {line_number(text, match.start())}: dramatic colon reveal")

    for pattern in FAUX_INSIGHT_SETUPS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            emit(findings, f"line {line_number(text, match.start())}: faux-insight setup")

    for pattern in MANUFACTURED_INTIMACY:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            emit(findings, f"line {line_number(text, match.start())}: manufactured-intimacy opener")

    for pattern in SELF_INTERVIEW_QUESTIONS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            emit(findings, f"line {line_number(text, match.start())}: self-interview question")

    for match in re.finditer(r"\bimagine\s+(if|waking|having|being|getting)\b", text, flags=re.IGNORECASE):
        emit(findings, f"line {line_number(text, match.start())}: generic imagine opener")


def sentence_split(text: str) -> list[tuple[int, str]]:
    pattern = re.compile(r"[^.!?\n][^.!?\n]*(?:[.!?]+|$)")
    return [(match.start(), match.group(0).strip()) for match in pattern.finditer(text) if match.group(0).strip()]


def first_word(value: str) -> str:
    match = re.search(r"[A-Za-z']+", value)
    return match.group(0).lower() if match else ""


def skeleton(value: str) -> str:
    words = re.findall(r"[A-Za-z']+", value.lower())
    if not words:
        return ""
    return " ".join(words[:3])


def find_repetition(text: str, findings: list[str]) -> None:
    lines = [(i + 1, line.strip()) for i, line in enumerate(text.splitlines()) if line.strip()]

    for (line_no_a, line_a), (line_no_b, line_b) in zip(lines, lines[1:]):
        word_a = first_word(line_a)
        word_b = first_word(line_b)
        if word_a and word_a == word_b:
            emit(findings, f"lines {line_no_a}-{line_no_b}: repeated line opener: {word_a!r}")
        if word_a in RHYTHM_OPENERS and word_b == word_a:
            emit(findings, f"lines {line_no_a}-{line_no_b}: parallel repetition stack")

    sentences = sentence_split(text)
    for (pos_a, sent_a), (pos_b, sent_b) in zip(sentences, sentences[1:]):
        if first_word(sent_a) and first_word(sent_a) == first_word(sent_b):
            emit(findings, f"line {line_number(text, pos_b)}: repeated sentence opener: {first_word(sent_b)!r}")
        if skeleton(sent_a) and skeleton(sent_a) == skeleton(sent_b):
            emit(findings, f"line {line_number(text, pos_b)}: repeated sentence skeleton: {skeleton(sent_b)!r}")

    for window in zip(sentences, sentences[1:], sentences[2:]):
        lengths = [len(re.findall(r"[A-Za-z']+", item[1])) for item in window]
        if all(1 <= length <= 5 for length in lengths):
            line = line_number(text, window[0][0])
            emit(findings, f"line {line}: possible triple short sentence stack")


def find_false_contrast(text: str, findings: list[str]) -> None:
    pattern = re.compile(
        r"\bit'?s\s+not\b[^.!?]*[.!?]\s*"
        r"\bit'?s\s+not\b[^.!?]*[.!?]\s*"
        r"\bit'?s\b[^.!?]*[.!?]",
        flags=re.IGNORECASE,
    )
    for match in pattern.finditer(text):
        emit(findings, f"line {line_number(text, match.start())}: false contrast stack")


def audit(text: str) -> list[str]:
    findings: list[str] = []
    find_exact_patterns(text, findings)
    find_false_contrast(text, findings)
    find_repetition(text, findings)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit copy for banned AI-writing patterns.")
    parser.add_argument("path", nargs="?", help="Text or Markdown file to audit. Reads stdin when omitted.")
    args = parser.parse_args()

    if args.path:
        text = Path(args.path).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    findings = audit(text)
    if findings:
        print("Blacklist review flags:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("No blacklist patterns found. Manual claim and context review is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
