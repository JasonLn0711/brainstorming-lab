"""Token-vector similarity for dependency-free clustering."""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Any

from idea_os.models import idea_search_text


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "be",
    "by",
    "for",
    "from",
    "given",
    "how",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "under",
    "use",
    "with",
}


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-zA-Z0-9]+", text.lower())
    return [token for token in tokens if len(token) > 1 and token not in STOPWORDS]


def idea_vector(idea: dict[str, Any]) -> Counter[str]:
    vector: Counter[str] = Counter(tokenize(idea_search_text(idea)))
    for tag in idea.get("tags", []):
        for token in tokenize(str(tag)):
            vector[token] += 3
    for token in tokenize(str(idea.get("title", ""))):
        vector[token] += 2
    return vector


def cosine_similarity(left: Counter[str], right: Counter[str]) -> float:
    if not left or not right:
        return 0.0
    shared = set(left) & set(right)
    numerator = sum(left[token] * right[token] for token in shared)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return numerator / (left_norm * right_norm)


def idea_similarity(left: dict[str, Any], right: dict[str, Any]) -> float:
    return round(cosine_similarity(idea_vector(left), idea_vector(right)), 4)


def shared_tags(left: dict[str, Any], right: dict[str, Any]) -> list[str]:
    left_tags = {str(tag) for tag in left.get("tags", [])}
    right_tags = {str(tag) for tag in right.get("tags", [])}
    return sorted(left_tags & right_tags)
