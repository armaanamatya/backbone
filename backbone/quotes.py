"""Finds each quote in its source and records the line (piece 3 of the build list).

A quote counts only if it is found, character for character, inside one line of
the document. A claim whose quote is not found is kept, marked unverified, and
is not used in a count.
"""

from __future__ import annotations

import re

VERIFIED = "verified"
LINE_CORRECTED = "verified_line_corrected"
UNVERIFIED = "unverified"

_PREFIX = re.compile(r"^\s*\d+\|\s?")


def split_lines(text: str) -> list[str]:
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def clean(quote: str) -> str:
    """Removes a line-number prefix the model may have copied, and outer spaces."""
    return _PREFIX.sub("", quote).strip()


def locate(lines: list[str], quote: str, line: int | None) -> tuple[int | None, str]:
    """Returns the line the quote is on (counting from 1) and how it was found."""
    quote = clean(quote or "")
    if not quote:
        return line, UNVERIFIED
    if line is not None and 1 <= line <= len(lines) and quote in lines[line - 1]:
        return line, VERIFIED
    found = [number for number, text in enumerate(lines, start=1) if quote in text]
    if not found:
        return line, UNVERIFIED
    if line is None:
        return found[0], LINE_CORRECTED
    return min(found, key=lambda number: abs(number - line)), LINE_CORRECTED
