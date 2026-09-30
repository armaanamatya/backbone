"""Lists every time, date and record number in a document, and checks that each
appears in what the model returned (R-49, R-51, check 16).

A value the model did not capture is listed for review. It does not block the read.
"""

from __future__ import annotations

import re

MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}
_MONTH = "|".join(sorted(MONTHS, key=len, reverse=True))
_DASH = "[-‐-―]"

TIME = re.compile(r"(?<![\d:.])([01]?\d|2[0-3]):([0-5]\d)(?![\d:])")
ISO_DATE = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2})(?!\d)")
# "March 3-14, 2025": the second day of a range has no month of its own.
RANGE_DATE = re.compile(
    rf"\b({_MONTH})\.?\s*(\d{{1,2}})\s*{_DASH}\s*(\d{{1,2}})(?!\d|:)(?:,?\s*(\d{{4}}))?",
    re.IGNORECASE,
)
WORD_DATE = re.compile(
    rf"\b({_MONTH})\.?\s*(\d{{1,2}})(?!\d|:)(?:(?:st|nd|rd|th)\b)?(?:,?\s+(\d{{4}})(?!\d))?",
    re.IGNORECASE,
)
IDENTIFIER = re.compile(r"\b[A-Z]{2,}(?:-[A-Z0-9]+)+\b")

CAPTURED = "captured"
OTHER_LINE = "captured_on_another_line"
QUOTED_ONLY = "quoted_only"
NOT_CAPTURED = "not_captured"


def values_in(text: str) -> list[tuple[str, tuple, str]]:
    """Every time, date and record number in a piece of text, as (kind, value, as written).

    A date is (year or None, month, day). A time is ("HH:MM",). A number is (text,).
    """
    found = []
    taken: list[tuple[int, int]] = []

    def free(match) -> bool:
        return all(match.end() <= start or match.start() >= end for start, end in taken)

    for match in ISO_DATE.finditer(text):
        year, month, day = (int(part) for part in match.groups())
        if 1 <= month <= 12 and 1 <= day <= 31:
            found.append(("date", (year, month, day), match.group(0)))
            taken.append(match.span())
    for match in RANGE_DATE.finditer(text):
        if not free(match):
            continue
        month = MONTHS[match.group(1).lower()]
        year = int(match.group(4)) if match.group(4) else None
        for day in (int(match.group(2)), int(match.group(3))):
            if 1 <= day <= 31:
                found.append(("date", (year, month, day), match.group(0)))
        taken.append(match.span())
    for match in WORD_DATE.finditer(text):
        if not free(match):
            continue
        month = MONTHS[match.group(1).lower()]
        day = int(match.group(2))
        year = int(match.group(3)) if match.group(3) else None
        if 1 <= day <= 31:
            found.append(("date", (year, month, day), match.group(0)))
            taken.append(match.span())
    for match in TIME.finditer(text):
        if not free(match):
            continue
        found.append(("time", (f"{int(match.group(1)):02d}:{match.group(2)}",), match.group(0)))
    for match in IDENTIFIER.finditer(text):
        if not free(match) or not any(character.isdigit() for character in match.group(0)):
            continue
        found.append(("number", (match.group(0),), match.group(0)))
    return found


def _same(kind: str, wanted: tuple, held: tuple) -> bool:
    if kind != "date":
        return wanted == held
    if wanted[0] is None or held[0] is None:
        return wanted[1:] == held[1:]
    return wanted == held


def _holdings(reading: dict):
    """What the result holds in its fields and in its quotes, with the line of each item."""
    fields: list[tuple[int | None, str, tuple]] = []
    quotes: list[tuple[str, tuple]] = []

    def take(item: dict, line: int | None):
        for name, value in item.items():
            if isinstance(value, str):
                if name == "quote":
                    quotes.extend((kind, held) for kind, held, _ in values_in(value))
                else:
                    fields.extend((line, kind, held) for kind, held, _ in values_in(value))

    take(reading.get("document", {}), None)
    for section in reading.get("sections", []):
        take({k: v for k, v in section.items() if k != "dates"}, section.get("signature_line"))
        for entry in section.get("dates", []):
            take(entry, entry.get("line"))
    for name, items in reading.items():
        if name in ("document", "sections") or not isinstance(items, list):
            continue
        for item in items:
            if isinstance(item, dict):
                take(item, item.get("line"))
    return fields, quotes


def check(lines: list[str], reading: dict) -> dict:
    """Compares the values in the document with the values in the result."""
    fields, quotes = _holdings(reading)
    rows = []
    for number, text in enumerate(lines, start=1):
        for kind, wanted, written in values_in(text):
            holders = [
                line
                for line, held_kind, held in fields
                if held_kind == kind and _same(kind, wanted, held)
            ]
            if any(line is None or line == number for line in holders):
                status = CAPTURED
            elif holders:
                status = OTHER_LINE
            elif any(held_kind == kind and _same(kind, wanted, held) for held_kind, held in quotes):
                status = QUOTED_ONLY
            else:
                status = NOT_CAPTURED
            rows.append({"line": number, "kind": kind, "value": written, "status": status})
    counts = {status: 0 for status in (CAPTURED, OTHER_LINE, QUOTED_ONLY, NOT_CAPTURED)}
    for row in rows:
        counts[row["status"]] += 1
    return {
        "values": len(rows),
        "counts": counts,
        "listed": [row for row in rows if row["status"] != CAPTURED],
    }
