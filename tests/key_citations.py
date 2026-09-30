"""Scores a store against the quotes the answer key cites.

    python tests/key_citations.py output/abstraction.sqlite [more stores]

For each store: how many of the key's cited quotes (section 7, the five
answers) a claim holds on the cited line, with the speaker the key gives.
This reads the key, so it lives with the checks and not in backbone/.
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CITATION = re.compile(r'(D\d{3}) line (\d+): "([^"]+)"')


def score(store_path: Path, section: str = "## 7. The five answers", until: str = "## 8. Problem questions") -> dict:
    key = (ROOT / "answer-key.md").read_text(encoding="utf-8")
    part = key[key.index(section): key.index(until)]
    connection = sqlite3.connect(store_path)
    connection.row_factory = sqlite3.Row
    claims = connection.execute(
        "SELECT c.line, c.quote, c.type, c.value, d.declared_id FROM claims c JOIN documents d USING (doc_hash)"
    ).fetchall()
    connection.close()
    matched, missing, speaker = 0, [], []
    for line in part.split("\n"):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        who = cells[1] if len(cells) >= 4 and cells[1] in ("Patient", "Clinician") else None
        for cite in CITATION.finditer(line):
            document, number, quote = "BH-" + cite.group(1), int(cite.group(2)), cite.group(3)
            hits = [c for c in claims if c["declared_id"] == document and c["line"] == number and (quote in c["quote"] or c["quote"] in quote)]
            if not hits:
                missing.append(f"{document} line {number}")
                continue
            if who:
                speakers = {json.loads(c["value"]).get("speaker") for c in hits if c["type"] == "observation"}
                if who.lower() not in speakers:
                    speaker.append(f"{document} line {number} (key {who}, store {', '.join(sorted(s for s in speakers if s))})")
                    continue
            matched += 1
    return {"store": str(store_path), "matched": matched, "cited": matched + len(missing) + len(speaker), "missing": missing, "speaker_differs": speaker}


if __name__ == "__main__":
    for path in sys.argv[1:]:
        result = score(Path(path))
        print(f"{result['store']}: {result['matched']} of {result['cited']} cited quotes held with the same speaker")
        if result["missing"]:
            print("  no claim holds: " + ", ".join(result["missing"]))
        if result["speaker_differs"]:
            print("  speaker differs: " + ", ".join(result["speaker_differs"]))
