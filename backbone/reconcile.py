"""Matches documents to contacts and applies the conflict rules (piece 5 of the build list).

Everything here is code. No model is called, and no fact about any patient is
written here: the rules run on the claims the documents gave.

The rules are the 16 in `decisions.md`. The ones applied in this file:

     1  documents that share a number, or a patient, date, class and time, describe one contact
     3  minutes come from actual times; a scheduled time is never counted
     4  only intervals with the patient present count
     5  an interval a document says had no therapy is removed
     6  an interval runs up to its end time and does not include it
     7  different documents can each supply a different detail of one contact
     8  a signed correction replaces the value it names
     9  a copy carries the authority and date of its original
    10  attendance is established by an attendance record or a signed clinical note
    11  records of equal standing that disagree stay open, as alternatives
    13  an assessment is identified by patient, instrument and completion time
    14  stated minutes are checked against clock times
    15  two names are one person only when a document links them
"""

from __future__ import annotations

import itertools
import re
from collections import Counter, defaultdict

ESTABLISHING = "establishing"
OTHER = "other"

ENCOUNTER = "encounter"
ADMINISTRATIVE = "administrative"
# Classes that are records of administration and not encounters (D-16, D-17, D-40).
ADMINISTRATIVE_CLASSES = {"scheduling_contact", "questionnaire_review"}

ATTENDED = {"attended", "attended_part"}
NOT_ATTENDED = {"absent", "no_show", "cancelled_by_patient", "cancelled_by_clinic"}
SPECIFIC_ABSENCE = ("cancelled_by_clinic", "cancelled_by_patient", "no_show")
PATIENT_TIMES = {"patient_present", "patient_arrival", "patient_departure"}

WOULD_SETTLE = {
    "start": "An arrival or check-in record, or a correction by the author of the record being changed.",
    "end": "A departure or check-out record, or a correction by the author of the record being changed.",
    "attendance": "A signed attendance record, or a correction by the author of the record being changed.",
    "interruption": "A correction by the author of one of the records.",
    "minutes": "A correction by the author of the record, giving the times or the minutes.",
    "status": "A correction by the author of one of the records.",
    "score": "The original form, or a correction by the author of one of the records.",
}

_CLOCK = re.compile(r"(?<![\d:])([01]?\d|2[0-3]):([0-5]\d)(?![\d:])")


def clock(text: str | None) -> int | None:
    """Minutes after midnight for "HH:MM", or None."""
    if not text:
        return None
    match = _CLOCK.search(text)
    return int(match.group(1)) * 60 + int(match.group(2)) if match else None


def written(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def merged(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for start, end in sorted(interval for interval in intervals if interval[1] > interval[0]):
        if result and start <= result[-1][1]:
            result[-1] = (result[-1][0], max(result[-1][1], end))
        else:
            result.append((start, end))
    return result


def without(start: int, end: int, removed: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """The interval from start up to end, less the parts of `removed` that fall
    inside it (rules 5 and 6)."""
    kept = []
    cursor = start
    for low, high in merged(removed):
        low, high = max(low, start), min(high, end)
        if high <= low:
            continue
        if low > cursor:
            kept.append((cursor, low))
        cursor = max(cursor, high)
    if cursor < end:
        kept.append((cursor, end))
    return kept


def length(intervals: list[tuple[int, int]]) -> int:
    return sum(end - start for start, end in intervals)


def person(name: str | None) -> str | None:
    """A name without the credentials after it. Names are compared as written
    and are never merged on likeness (rule 15)."""
    if not name:
        return None
    return " ".join(name.split(",")[0].split()) or None


def is_signed(section: dict) -> bool:
    if section.get("is_copy"):
        return bool(section.get("original_signed_by"))
    return section.get("signature") == "signed"


def standing(section: dict | None) -> str:
    """Whether a section can establish attendance (rule 10). A copy stands as
    its original does (rule 9). An attendance record counts whether or not the
    extract itself is signed (R-31)."""
    if not section:
        return OTHER
    if section["kind"] == "attendance_record":
        return ESTABLISHING
    if section["kind"] in ("clinical_note", "correction") and is_signed(section):
        return ESTABLISHING
    return OTHER


def moment(date: str | None, time: str | None) -> str | None:
    return f"{date}T{time or '00:00'}" if date else None


def authority(claim: dict, section: dict | None) -> str | None:
    """When the statement was signed. For a copy, when its original was (rule 9)."""
    if not section:
        return None
    if section.get("is_copy"):
        return moment(section.get("original_signed_date"), section.get("original_signed_time"))
    value = claim["value"]
    if value.get("entry_signed_date"):
        return moment(value["entry_signed_date"], value.get("entry_signed_time"))
    if section.get("signature") == "signed":
        return moment(section.get("signed_date"), section.get("signed_time"))
    return None


# --------------------------------------------------------------------------
# Rule 1: which references describe the same contact
# --------------------------------------------------------------------------


class Groups:
    def __init__(self, keys):
        self.parent = {key: key for key in keys}

    def find(self, key):
        while self.parent[key] != key:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key

    def join(self, first, second):
        first, second = self.find(first), self.find(second)
        if first != second:
            low, high = sorted((first, second))
            self.parent[high] = low


def _spans(claims: list[dict]) -> list[tuple[int, int]]:
    spans = []
    for claim in claims:
        if claim["type"] != "time":
            continue
        start, end = clock(claim["value"].get("start")), clock(claim["value"].get("end"))
        if start is None and end is None:
            continue
        spans.append((start if start is not None else end, end if end is not None else start))
    return spans


def _overlap(first: list[tuple[int, int]], second: list[tuple[int, int]]) -> bool:
    return any(a[0] <= b[1] and b[0] <= a[1] for a in first for b in second)


def group_references(claims: list[dict]) -> list[list[dict]]:
    """Puts the claims into groups, one group for each contact (rule 1, D-41)."""
    nodes: dict[tuple, list[dict]] = defaultdict(list)
    for claim in claims:
        if claim["contact_ref"] is not None:
            nodes[(claim["doc_hash"], claim["contact_ref"])].append(claim)
    keys = sorted(nodes)
    groups = Groups(keys)

    def first(key, field):
        return next((claim[field] for claim in nodes[key] if claim[field]), None)

    identity = {
        key: {
            # A number is a number, whichever field a document printed it in.
            "numbers": {claim["encounter_id"] for claim in nodes[key] if claim["encounter_id"]}
            | {claim["appointment_id"] for claim in nodes[key] if claim["appointment_id"]},
            "date": first(key, "service_date"),
            "class": first(key, "service_class"),
            "spans": _spans(nodes[key]),
        }
        for key in keys
    }

    by_number = defaultdict(list)
    for key in keys:
        for number in identity[key]["numbers"]:
            by_number[number].append(key)
    for same in by_number.values():
        for key in same[1:]:
            groups.join(same[0], key)

    def members(root):
        return [key for key in keys if groups.find(key) == root]

    def fits(key, root):
        """Same date and class as every dated, classed member of the group."""
        mine = identity[key]
        return any(
            identity[other]["date"] == mine["date"] and identity[other]["class"] == mine["class"]
            for other in members(root)
        )

    def group_spans(root):
        return [span for other in members(root) for span in identity[other]["spans"]]

    unnumbered = [key for key in keys if not identity[key]["numbers"] and identity[key]["date"]]
    timed = [key for key in unnumbered if identity[key]["spans"]]
    untimed = [key for key in unnumbered if not identity[key]["spans"]]

    # A reference with a time joins the contact whose times it overlaps.
    for key in timed:
        roots = sorted(
            {groups.find(other) for other in keys if other != key and groups.find(other) != groups.find(key)}
        )
        matches = [
            root for root in roots if fits(key, root) and _overlap(identity[key]["spans"], group_spans(root))
        ]
        numbered = [root for root in matches if any(identity[other]["numbers"] for other in members(root))]
        chosen = numbered if numbered else matches
        if len(chosen) == 1:
            groups.join(key, chosen[0])

    # A reference with no time joins the one contact of its date and class (D-41).
    for key in untimed:
        roots = sorted(
            {
                groups.find(other)
                for other in keys
                if other not in untimed and groups.find(other) != groups.find(key)
            }
        )
        matches = [root for root in roots if fits(key, root)]
        if len(matches) == 1:
            groups.join(key, matches[0])
            continue
        if not matches:
            for other in untimed:
                same = identity[other]["date"] == identity[key]["date"]
                if other != key and same and identity[other]["class"] == identity[key]["class"]:
                    if not any(identity[member]["numbers"] for member in members(groups.find(other))):
                        groups.join(key, other)

    gathered: dict[tuple, list[dict]] = defaultdict(list)
    for key in keys:
        gathered[groups.find(key)].extend(nodes[key])
    return [gathered[root] for root in sorted(gathered)]


def _describes(claim: dict) -> bool:
    """Whether a claim says something about a contact beyond naming it."""
    if claim["type"] in ("contact",):
        return False
    if claim["type"] == "participant":
        return claim["value"].get("presence") not in (None, "not_stated")
    return True


# --------------------------------------------------------------------------
# One contact
# --------------------------------------------------------------------------


def _most_common(values: list):
    counted = Counter(value for value in values if value is not None)
    if not counted:
        return None
    best = max(counted.values())
    return sorted(value for value, count in counted.items() if count == best)[0]


def _candidate(value: int, claim: dict, section: dict | None) -> dict:
    return {
        "value": value,
        "claim": claim["claim_id"],
        "document": claim["document"],
        "authority": authority(claim, section),
        "copy": bool(section and section.get("is_copy")),
    }


def _alternatives(candidates: list[dict], notes: dict[int, str] | None = None) -> list[dict]:
    result = []
    for value in sorted({candidate["value"] for candidate in candidates}):
        same = [candidate for candidate in candidates if candidate["value"] == value]
        result.append(
            {
                "value": written(value),
                "claims": sorted(candidate["claim"] for candidate in same),
                "documents": sorted({candidate["document"] for candidate in same}),
                "copies": sorted({candidate["document"] for candidate in same if candidate["copy"]}),
                "note": (notes or {}).get(value),
            }
        )
    return result


def _apply_corrections(field: str, candidates: list[dict], corrections: list[dict], contact_id: str):
    """Rule 8, then rule 9. Returns the candidates left, and a conflict if a
    value was replaced."""
    names = {"start": ("arrival", "start"), "end": ("departure", "end")}[field]
    before = list(candidates)
    replaced: dict[int, str] = {}
    used = []
    for correction in corrections:
        value = correction["claim"]["value"]
        if value.get("field") not in names:
            continue
        old, new = clock(value.get("old_value")), clock(value.get("new_value"))
        if old is None or new is None:
            continue
        signed = correction["authority"]
        kept = []
        for candidate in candidates:
            later = candidate["authority"] is not None and signed is not None and candidate["authority"] > signed
            if candidate["value"] == old and candidate["claim"] != correction["claim"]["claim_id"] and not later:
                replaced[old] = f"replaced by the correction in {correction['claim']['document']}"
                continue
            kept.append(candidate)
        candidates = kept
        if not any(candidate["value"] == new for candidate in candidates):
            candidates.append(_candidate(new, correction["claim"], correction["section"]))
        used.append(correction)
    if not replaced:
        return candidates, None
    removed = [candidate for candidate in before if candidate["value"] in replaced]
    rule = "8, then 9" if any(candidate["copy"] for candidate in removed) else "8"
    left = sorted({candidate["value"] for candidate in candidates})
    conflict = {
        "conflict_id": f"{contact_id}:{'departure' if field == 'end' else 'arrival'}",
        "contact_id": contact_id,
        "field": "departure" if field == "end" else "arrival",
        "alternatives": _alternatives(before + [c for c in candidates if c not in before], replaced),
        "status": "settled" if len(left) == 1 else "open",
        "rule": rule if len(left) == 1 else f"{rule}, then 11",
        "outcome": written(left[0]) if len(left) == 1 else None,
        "would_settle": None if len(left) == 1 else WOULD_SETTLE[field],
    }
    return candidates, conflict


def build_contact(patient_key: str, claims: list[dict], sections: dict) -> dict | None:
    """Works out one contact from the claims of every document that describes it.

    Returns the contact with its conflicts and findings, or None for a mention.
    """
    numbers = sorted({claim["encounter_id"] for claim in claims if claim["encounter_id"]})
    appointments = sorted({claim["appointment_id"] for claim in claims if claim["appointment_id"]})
    if not numbers and not appointments and not any(_describes(claim) for claim in claims):
        return None
    # A reference with no number and no date cannot be matched or placed (D-41).
    if not numbers and not appointments and not any(claim["service_date"] for claim in claims):
        return None

    def section_of(claim):
        return sections.get((claim["doc_hash"], claim["section"]))

    strong = [claim for claim in claims if standing(section_of(claim)) == ESTABLISHING]
    weak = [claim for claim in claims if standing(section_of(claim)) != ESTABLISHING]
    references = [claim for claim in claims if claim["type"] == "contact"] or claims

    service_date = _most_common([claim["service_date"] for claim in references])
    service_class = _most_common([c["service_class"] for c in references if c in strong]) or _most_common(
        [claim["service_class"] for claim in references]
    )
    as_written = _most_common([c["service_as_written"] for c in references if c["service_class"] == service_class])
    times = sorted(_spans(claims))
    label = numbers[0] if numbers else (appointments[0] if appointments else None)
    if label is None:
        label = f"{service_date}/{service_class}" + (f"/{written(times[0][0])}" if times else "")
    contact_id = f"{patient_key}/{label}"
    record_kind = ADMINISTRATIVE if service_class in ADMINISTRATIVE_CLASSES else ENCOUNTER

    conflicts: list[dict] = []
    findings: list[dict] = []
    notes: list[str] = []

    def of_type(group, kind):
        return [claim for claim in group if claim["type"] == kind]

    def usable(claim):
        """Rule 3, D-36, D-38: in a record that can establish attendance, a
        time counts unless it is labelled scheduled."""
        return claim["time_label"] != "scheduled"

    # ---- Did the patient attend (rules 4 and 10, D-42) -------------------
    def says_attended(group):
        found = [c for c in of_type(group, "attendance") if c["value"]["status"] in ATTENDED]
        found += [
            c
            for c in of_type(group, "participant")
            if c["value"]["role"] == "patient" and c["value"]["presence"] in ("present", "present_part")
        ]
        found += [c for c in of_type(group, "time") if c["value"]["what"] in PATIENT_TIMES and usable(c)]
        found += [
            c
            for c in of_type(group, "stated_minutes")
            if c["value"]["of"] == "patient_present" and c["value"]["minutes"] > 0
        ]
        return found

    def says_absent(group):
        found = [c for c in of_type(group, "attendance") if c["value"]["status"] in NOT_ATTENDED]
        found += [
            c
            for c in of_type(group, "participant")
            if c["value"]["role"] == "patient" and c["value"]["presence"] == "absent"
        ]
        found += [c for c in of_type(group, "statement") if c["value"]["says"] == "no_patient_contact"]
        return found

    strong_yes, strong_no = says_attended(strong), says_absent(strong)
    weak_yes = [c for c in says_attended(weak) if c["type"] != "time"]
    weak_no = says_absent(weak)
    held_evidence = (
        [
            c
            for c in of_type(strong, "time")
            if usable(c) and c["value"]["what"] in PATIENT_TIMES | {"contact_interval", "patient_absent_interval"}
        ]
        + [c for c in of_type(strong, "attendance") if c["value"]["status"] in ATTENDED | {"completed"}]
        + [c for c in of_type(strong, "participant") if c["value"]["presence"] in ("present", "present_part")]
    )

    def absence(group):
        named = [c["value"]["status"] for c in of_type(group, "attendance")]
        return [status for status in SPECIFIC_ABSENCE if status in named]

    def sides(yes, no):
        def side(value, group):
            return {
                "value": value,
                "claims": sorted(claim["claim_id"] for claim in group),
                "documents": sorted({claim["document"] for claim in group}),
                "kinds": sorted({section_of(claim)["kind"] for claim in group if section_of(claim)}),
            }

        return [side("attended", yes), side("did not attend", no)]

    attendance_open = None
    if record_kind == ADMINISTRATIVE:
        status, present = "recorded", "not_applicable"
    elif strong_yes and strong_no:
        status, present = "unsettled", "unsettled"
        attendance_open = f"{contact_id}:attendance"
        conflicts.append(
            {
                "conflict_id": attendance_open,
                "contact_id": contact_id,
                "field": "attendance",
                "alternatives": sides(strong_yes, strong_no),
                "status": "open",
                "rule": "11",
                "outcome": None,
                "would_settle": WOULD_SETTLE["attendance"],
            }
        )
    elif strong_no:
        named = absence(strong) or absence(weak)
        if len(named) > 1:
            notes.append("the records name more than one reason for the absence: " + ", ".join(named))
        status = named[0] if named else ("held_without_patient" if held_evidence else "absent")
        present = "no"
        if weak_yes:
            conflicts.append(
                {
                    "conflict_id": f"{contact_id}:attendance",
                    "contact_id": contact_id,
                    "field": "attendance",
                    "alternatives": sides(weak_yes, strong_no),
                    "status": "settled",
                    "rule": "10",
                    "outcome": "did not attend",
                    "would_settle": None,
                }
            )
    elif strong_yes or held_evidence:
        # D-39: with no word of absence, a contact that was held had the patient in it.
        status, present = "held", "yes"
        if weak_no:
            conflicts.append(
                {
                    "conflict_id": f"{contact_id}:attendance",
                    "contact_id": contact_id,
                    "field": "attendance",
                    "alternatives": sides(strong_yes or held_evidence, weak_no),
                    "status": "settled",
                    "rule": "10",
                    "outcome": "attended",
                    "would_settle": None,
                }
            )
    elif weak_no:
        named = absence(weak)
        if len(named) > 1:
            notes.append("the records name more than one reason for the absence: " + ", ".join(named))
        status, present = (named[0] if named else "absent"), "no"
    else:
        status, present = "not_established", "no"
        if weak_yes:
            notes.append("a record says the patient attended, and none that can establish attendance does")

    # ---- The session itself -------------------------------------------------
    scheduled = [
        (clock(c["value"].get("start")), clock(c["value"].get("end")))
        for c in of_type(claims, "time")
        if c["value"]["what"] == "contact_interval" and c["time_label"] == "scheduled"
    ]
    actual = [
        (clock(c["value"].get("start")), clock(c["value"].get("end")), c)
        for c in of_type(strong, "time")
        if c["value"]["what"] == "contact_interval" and usable(c)
    ]
    actual = [entry for entry in actual if entry[0] is not None and entry[1] is not None]
    scheduled = [entry for entry in scheduled if entry[0] is not None and entry[1] is not None]
    session = None
    if scheduled:
        session = {"start": written(_most_common(scheduled)[0]), "end": written(_most_common(scheduled)[1]), "kind": "scheduled"}
    elif actual:
        chosen = _most_common([(start, end) for start, end, _ in actual])
        session = {"start": written(chosen[0]), "end": written(chosen[1]), "kind": "actual"}

    # ---- When the patient was present (rules 3, 7, 8, 9, 11) --------------
    alternatives: list[dict] = []
    removed_rows: list[dict] = []
    away = merged(
        [
            (clock(c["value"].get("start")), clock(c["value"].get("end")))
            for c in of_type(strong, "time")
            if c["value"]["what"] == "patient_absent_interval"
            and usable(c)
            and clock(c["value"].get("start")) is not None
            and clock(c["value"].get("end")) is not None
        ]
    )
    if present in ("yes", "unsettled"):
        starts, ends, implied = [], [], []
        stretches = defaultdict(list)
        for claim in of_type(strong, "time"):
            if not usable(claim):
                continue
            what = claim["value"]["what"]
            start, end = clock(claim["value"].get("start")), clock(claim["value"].get("end"))
            if what == "patient_arrival" and start is not None:
                starts.append(_candidate(start, claim, section_of(claim)))
            elif what == "patient_departure" and end is not None:
                ends.append(_candidate(end, claim, section_of(claim)))
            elif what == "patient_present":
                if start is not None and end is not None:
                    stretches[(claim["doc_hash"], claim["section"])].append((start, end, claim))
                elif start is not None:
                    starts.append(_candidate(start, claim, section_of(claim)))
                elif end is not None:
                    ends.append(_candidate(end, claim, section_of(claim)))
        for stretch in stretches.values():
            stretch.sort(key=lambda entry: (entry[0], entry[1]))
            starts.append(_candidate(stretch[0][0], stretch[0][2], section_of(stretch[0][2])))
            last = max(stretch, key=lambda entry: entry[1])
            ends.append(_candidate(last[1], last[2], section_of(last[2])))
            covered = merged([(start, end) for start, end, _ in stretch])
            for (_, gap_start), (gap_end, _) in zip(covered, covered[1:]):
                implied.append((gap_start, gap_end, stretch[0][2]))

        # D-39: no document gives the patient's own times, so the contact's do.
        from_contact = []
        if not starts:
            starts = [_candidate(start, claim, section_of(claim)) for start, _, claim in actual]
            from_contact.append("start")
        if not ends:
            ends = [_candidate(end, claim, section_of(claim)) for _, end, claim in actual]
            from_contact.append("end")
        in_words = [c for c in strong_yes if c["type"] != "time"]
        if from_contact and (starts or ends) and not in_words:
            # The note is for a contact where nothing says in words that the
            # patient was there (D-39, R-63).
            notes.append("the patient's presence is taken from the interval of the contact")

        corrections = [
            {"claim": claim, "section": section_of(claim), "authority": authority(claim, section_of(claim))}
            for claim in of_type(claims, "correction")
            if section_of(claim) and is_signed(section_of(claim))
        ]
        corrections.sort(key=lambda entry: (entry["authority"] or "", entry["claim"]["claim_id"]))
        for entry in corrections:
            if entry["claim"]["value"].get("field") not in ("arrival", "start", "departure", "end"):
                # Rule 11: what the rules do not recognize stays open.
                conflicts.append(
                    {
                        "conflict_id": f"{contact_id}:correction:{entry['claim']['claim_id']}",
                        "contact_id": contact_id,
                        "field": entry["claim"]["value"].get("field") or "other",
                        "alternatives": [
                            {"value": entry["claim"]["value"].get("old_value"), "claims": [], "documents": []},
                            {
                                "value": entry["claim"]["value"].get("new_value"),
                                "claims": [entry["claim"]["claim_id"]],
                                "documents": [entry["claim"]["document"]],
                            },
                        ],
                        "status": "open",
                        "rule": "11",
                        "outcome": None,
                        "would_settle": "A rule for corrections of this field. None is built.",
                    }
                )
        open_fields = {}
        for field, candidates in (("start", starts), ("end", ends)):
            candidates, conflict = _apply_corrections(field, candidates, corrections, contact_id)
            if conflict:
                conflicts.append(conflict)
            values = sorted({candidate["value"] for candidate in candidates})
            if len(values) > 1 and not (conflict and conflict["status"] == "open"):
                conflict = {
                    "conflict_id": f"{contact_id}:{field}",
                    "contact_id": contact_id,
                    "field": field,
                    "alternatives": _alternatives(candidates),
                    "status": "open",
                    "rule": "11",
                    "outcome": None,
                    "would_settle": WOULD_SETTLE[field],
                }
                conflicts.append(conflict)
            if len(values) > 1:
                open_fields[field] = conflict["conflict_id"]
            if field == "start":
                starts = candidates
            else:
                ends = candidates

        # Rule 5: intervals a record says had no therapy. The label does not
        # matter: a break the note calls scheduled is still a break the note
        # says had no therapy.
        stated = defaultdict(list)
        for claim in of_type(strong, "time"):
            if claim["value"]["what"] != "no_therapy_interval":
                continue
            start, end = clock(claim["value"].get("start")), clock(claim["value"].get("end"))
            if start is not None and end is not None and end > start:
                stated[claim["doc_hash"]].append((start, end, claim))
        for start, end, claim in implied:
            # A gap between two stretches of presence, unless the record states it.
            if not any((start, end) == (s, e) for s, e, _ in stated[claim["doc_hash"]]):
                stated[claim["doc_hash"]].append((start, end, claim))
        per_document = {document: merged([(s, e) for s, e, _ in rows]) for document, rows in stated.items()}
        removal_sets = sorted({tuple(rows) for rows in per_document.values()})
        clash = any(
            a != b and a[0] < b[1] and b[0] < a[1]
            for first, second in itertools.combinations(removal_sets, 2)
            for a in first
            for b in second
        )
        if clash:
            conflict_id = f"{contact_id}:interruption"
            conflicts.append(
                {
                    "conflict_id": conflict_id,
                    "contact_id": contact_id,
                    "field": "interruption",
                    "alternatives": [
                        {
                            "value": ", ".join(f"{written(s)}–{written(e)}" for s, e in rows),
                            "claims": sorted(
                                claim["claim_id"]
                                for document, found in stated.items()
                                if tuple(per_document[document]) == rows
                                for _, _, claim in found
                            ),
                            "documents": sorted(
                                {
                                    claim["document"]
                                    for document, found in stated.items()
                                    if tuple(per_document[document]) == rows
                                    for _, _, claim in found
                                }
                            ),
                        }
                        for rows in removal_sets
                    ],
                    "status": "open",
                    "rule": "11",
                    "outcome": None,
                    "would_settle": WOULD_SETTLE["interruption"],
                }
            )
            removal_options = [(list(rows), {conflict_id: ", ".join(f"{written(s)}–{written(e)}" for s, e in rows)}) for rows in removal_sets]
        else:
            everything = merged([interval for rows in removal_sets for interval in rows])
            removal_options = [(everything, {})]
        seen = set()
        for rows in stated.values():
            for start, end, claim in rows:
                if (start, end, claim["claim_id"]) in seen:
                    continue
                seen.add((start, end, claim["claim_id"]))
                removed_rows.append(
                    {
                        "start": written(start),
                        "end": written(end),
                        "why": (
                            "between two stretches of presence"
                            if claim["value"]["what"] == "patient_present"
                            else claim["value"].get("detail") or "no therapy"
                        ),
                        "claim": claim["claim_id"],
                        "document": claim["document"],
                    }
                )
        removed_rows.sort(key=lambda row: (row["start"], row["end"], row["claim"]))

        start_values = sorted({candidate["value"] for candidate in starts})
        end_values = sorted({candidate["value"] for candidate in ends})
        if start_values and end_values:
            for start, end, (removal, removal_choice) in itertools.product(start_values, end_values, removal_options):
                if end <= start:
                    continue
                choices = dict(removal_choice)
                if "start" in open_fields:
                    choices[open_fields["start"]] = written(start)
                if "end" in open_fields:
                    choices[open_fields["end"]] = written(end)
                if attendance_open:
                    choices[attendance_open] = "attended"
                kept = without(start, end, list(removal) + away)
                alternatives.append(
                    {
                        "present": True,
                        "start": written(start),
                        "end": written(end),
                        "intervals": [[written(a), written(b)] for a, b in kept],
                        "minutes": length(kept),
                        "choices": choices,
                        "start_claims": sorted(c["claim"] for c in starts if c["value"] == start),
                        "end_claims": sorted(c["claim"] for c in ends if c["value"] == end),
                    }
                )
        else:
            alternatives.append(
                {
                    "present": True,
                    "start": None,
                    "end": None,
                    "intervals": [],
                    "minutes": None,
                    "choices": {attendance_open: "attended"} if attendance_open else {},
                    "start_claims": [],
                    "end_claims": [],
                }
            )
            notes.append("no clock times are given for the patient's presence")

        # Rule 14: stated minutes are checked against the clock times.
        for claim in of_type(strong, "stated_minutes"):
            if claim["value"]["of"] != "patient_present":
                continue
            minutes = claim["value"]["minutes"]
            own = [
                option
                for option in alternatives
                if option["minutes"] is not None
                and (
                    any(c.startswith(claim["doc_hash"][:12]) for c in option["start_claims"] + option["end_claims"])
                    or not any(
                        c["claim"].startswith(claim["doc_hash"][:12]) for c in starts + ends
                    )
                )
            ]
            timed = [option for option in alternatives if option["minutes"] is not None]
            if not timed:
                for option in alternatives:
                    option["minutes"] = minutes
                    option["minutes_from"] = claim["claim_id"]
                notes.append("the minutes are as stated; no clock times are given to check them against")
            elif minutes not in {option["minutes"] for option in (own or timed)}:
                conflict_id = f"{contact_id}:minutes:{claim['claim_id']}"
                conflicts.append(
                    {
                        "conflict_id": conflict_id,
                        "contact_id": contact_id,
                        "field": "minutes",
                        "alternatives": [
                            {
                                "value": str(option["minutes"]),
                                "claims": option["start_claims"] + option["end_claims"],
                                "documents": [],
                                "note": "from the clock times",
                            }
                            for option in (own or timed)
                        ]
                        + [
                            {
                                "value": str(minutes),
                                "claims": [claim["claim_id"]],
                                "documents": [claim["document"]],
                                "note": "as stated",
                            }
                        ],
                        "status": "open",
                        "rule": "14, then 11",
                        "outcome": None,
                        "would_settle": WOULD_SETTLE["minutes"],
                    }
                )
                extra = []
                for option in own or timed:
                    option["choices"] = {**option["choices"], conflict_id: f"{option['minutes']} from the clock times"}
                    extra.append(
                        {**option, "minutes": minutes, "choices": {**option["choices"], conflict_id: f"{minutes} as stated"}}
                    )
                alternatives.extend(extra)

        if attendance_open:
            alternatives.append(
                {
                    "present": False,
                    "start": None,
                    "end": None,
                    "intervals": [],
                    "minutes": 0,
                    "choices": {attendance_open: "did not attend"},
                    "start_claims": [],
                    "end_claims": [],
                }
            )

    # ---- Attended in part ---------------------------------------------------
    partial = False
    attended = [option for option in alternatives if option["present"] and option["start"]]
    if present == "yes":
        if any(c["value"]["status"] == "attended_part" for c in of_type(strong, "attendance")):
            partial = True
        if session and attended:
            if all(clock(option["start"]) > clock(session["start"]) for option in attended):
                partial = True
                notes.append("arrived after the start" if session["kind"] == "scheduled" else "joined after the start")
            if all(clock(option["end"]) < clock(session["end"]) for option in attended):
                partial = True
                notes.append("left before the end")

    # ---- Time in the contact without the patient ----------------------------
    without_patient = list(away)
    if present == "no" and status == "held_without_patient":
        without_patient += [(start, end) for start, end, _ in actual]
    minutes_without_patient = length(merged(without_patient)) if without_patient else None

    # ---- Stated minutes for the contact as a whole (rule 14) ----------------
    for claim in of_type(strong, "stated_minutes"):
        if claim["value"]["of"] != "contact_total" or not actual:
            continue
        lengths = {end - start for start, end, _ in actual}
        if claim["value"]["minutes"] not in lengths:
            conflicts.append(
                {
                    "conflict_id": f"{contact_id}:contact_minutes:{claim['claim_id']}",
                    "contact_id": contact_id,
                    "field": "minutes of the contact",
                    "alternatives": [
                        {"value": str(value), "claims": [c["claim_id"] for _, _, c in actual], "documents": [], "note": "from the clock times"}
                        for value in sorted(lengths)
                    ]
                    + [{"value": str(claim["value"]["minutes"]), "claims": [claim["claim_id"]], "documents": [claim["document"]], "note": "as stated"}],
                    "status": "open",
                    "rule": "14, then 11",
                    "outcome": None,
                    "would_settle": WOULD_SETTLE["minutes"],
                }
            )

    # ---- People, and how the contact was held (rule 7) ----------------------
    sources = strong or claims
    clinicians = sorted(
        {
            person(c["value"].get("name"))
            for c in of_type(sources, "participant")
            if c["value"]["role"] == "clinician" and person(c["value"].get("name"))
        }
    )
    people = [c["value"] for c in of_type(sources, "participant") if c["value"]["role"] not in ("clinician", "patient")]
    named_roles = {value["role"] for value in people if person(value.get("name"))}
    others = sorted(
        {
            (person(value.get("name")) or value.get("role_as_written") or value["role"], value["role"])
            for value in people
            # "the partner" adds nothing where a document names the partner.
            if person(value.get("name")) or value["role"] not in named_roles
        }
    )
    modality = _most_common([c["value"]["modality"] for c in of_type(sources, "modality")])

    # ---- Findings (rule 10) ---------------------------------------------------
    for claim in of_type(claims, "charge"):
        if present != "yes":
            findings.append(
                {
                    "finding_id": f"{contact_id}:charge:{claim['value'].get('charge_id') or claim['claim_id']}",
                    "kind": "charge_without_attendance",
                    "contact_id": contact_id,
                    "detail": (
                        f"A charge ({claim['value'].get('charge_id') or 'no number'},"
                        f" {claim['value'].get('description') or 'no description'}) is posted for a contact"
                        f" whose status is {status.replace('_', ' ')}. This is an inconsistency between"
                        " documentation and billing. The record does not show whether the charge was later"
                        " reviewed or reversed. It is not a finding of improper billing."
                    ),
                    "claims": [claim["claim_id"]] + sorted(c["claim_id"] for c in strong_no),
                }
            )
    for claim in of_type(claims, "statement"):
        section = section_of(claim)
        if claim["value"]["says"] == "made_before_the_service" and section and section["kind"] == "draft_note":
            findings.append(
                {
                    "finding_id": f"{contact_id}:draft:{claim['claim_id']}",
                    "kind": "draft_made_before_the_service",
                    "contact_id": contact_id,
                    "detail": "A draft note for this contact was made before the service it describes.",
                    "claims": [claim["claim_id"]],
                }
            )
    late = set()
    for claim in references:
        section = section_of(claim)
        if not section or section["kind"] != "clinical_note" or section.get("is_copy"):
            continue
        signed = section.get("signed_date")
        if section.get("signature") == "signed" and signed and service_date and signed > service_date:
            if (claim["doc_hash"], claim["section"]) not in late:
                late.add((claim["doc_hash"], claim["section"]))
                findings.append(
                    {
                        "finding_id": f"{contact_id}:signed_later:{claim['document']}:{claim['section']}",
                        "kind": "note_signed_after_the_service_date",
                        "contact_id": contact_id,
                        "detail": f"The note in {claim['document']} was signed on {signed}, after the service date {service_date}.",
                        "claims": [claim["claim_id"]],
                    }
                )

    contact = {
        "contact_id": contact_id,
        "record_kind": record_kind,
        "encounter_id": numbers[0] if numbers else None,
        "appointment_id": appointments[0] if appointments else None,
        "service_date": service_date,
        "service_class": service_class,
        "service_as_written": as_written,
        "status": status,
        "patient_present": present,
        "partial": partial,
        "modality": modality,
        "clinicians": clinicians,
        "participants": [{"name": name, "role": role} for name, role in others],
        "session": session,
        "presence": alternatives,
        "removed": removed_rows,
        "minutes": [
            {"minutes": option["minutes"], "present": option["present"], "choices": option["choices"]}
            for option in alternatives
        ],
        "minutes_without_patient": minutes_without_patient,
        "notes": sorted(set(notes)),
        "documents": sorted({claim["document"] for claim in claims}),
        "claims": sorted(claim["claim_id"] for claim in claims),
    }
    if len(numbers) > 1:
        contact["notes"].append("more than one encounter number: " + ", ".join(numbers))
    return {"contact": contact, "conflicts": conflicts, "findings": findings}


# --------------------------------------------------------------------------
# Plan rules and assessments
# --------------------------------------------------------------------------


def plan_rules(claims: list[dict], sections: dict) -> list[dict]:
    """The rules of each plan, read from the plan itself and from nothing else (D-37)."""
    rows = []
    by_document = defaultdict(list)
    for claim in claims:
        section = sections.get((claim["doc_hash"], claim["section"]))
        if claim["type"] == "plan_rule" and section and section["kind"] == "plan":
            by_document[claim["doc_hash"]].append((claim, section))
    for doc_hash, found in by_document.items():
        episode = next((c["value"] for c, _ in found if c["value"]["rule"] == "episode_period"), {})
        for claim, section in found:
            rows.append(
                {
                    "rule_id": claim["claim_id"],
                    "doc_hash": doc_hash,
                    "rule": claim["value"]["rule"],
                    "value": {
                        **{k: v for k, v in claim["value"].items() if k != "rule" and v not in (None, [])},
                        "document": claim["document"],
                        "signed": moment(section.get("signed_date"), section.get("signed_time")),
                    },
                    # D-13: a plan is in effect from the start of its episode.
                    "effective_from": episode.get("start_date"),
                    "effective_to": episode.get("end_date"),
                    "claim_id": claim["claim_id"],
                }
            )
    return sorted(rows, key=lambda row: row["rule_id"])


def _instrument(name: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", name.upper())


def assessments(patient_key: str, claims: list[dict], sections: dict) -> tuple[list[dict], list[dict]]:
    """Distinct assessments (rule 13). Copies and mentions add none (rule 9)."""
    scores = [claim for claim in claims if claim["type"] == "score"]
    clusters: list[dict] = []
    order = {"completion": 0, "copy": 1, "mention": 2}

    def relation(claim):
        section = sections.get((claim["doc_hash"], claim["section"]))
        if section and section.get("is_copy") and claim["value"]["relation"] == "completion":
            return "copy"
        return claim["value"]["relation"]

    for claim in sorted(scores, key=lambda c: (order[relation(c)], c["claim_id"])):
        value = claim["value"]
        key = (_instrument(value["instrument"]), value.get("completed_date"))
        home = None
        if value.get("completed_date"):
            for cluster in clusters:
                if cluster["key"] != key:
                    continue
                forms = {cluster["form_id"], value.get("form_id")} - {None}
                times = {cluster["completed_time"], value.get("completed_time")} - {None}
                if len(forms) <= 1 and len(times) <= 1:
                    home = cluster
                    break
        if home is None:
            home = {"key": key, "instrument": value["instrument"], "form_id": None, "completed_time": None, "claims": []}
            clusters.append(home)
        home["form_id"] = home["form_id"] or value.get("form_id")
        home["completed_time"] = home["completed_time"] or value.get("completed_time")
        home["claims"].append((relation(claim), claim))

    rows, conflicts = [], []
    for cluster in clusters:
        totals = [(kind, claim) for kind, claim in cluster["claims"] if claim["value"].get("item_number") is None]
        best = min((order[kind] for kind, _ in totals), default=None)
        values = sorted({claim["value"]["score"] for kind, claim in totals if order[kind] == best})
        date = cluster["key"][1]
        assessment_id = f"{patient_key}/{cluster['key'][0]}/{date or 'undated'}" + (
            f"/{cluster['form_id']}" if cluster["form_id"] else ""
        )
        if date is None:
            assessment_id += f"/{cluster['claims'][0][1]['claim_id']}"
        items = {}
        for kind, claim in cluster["claims"]:
            if claim["value"].get("item_number") is not None:
                items[str(claim["value"]["item_number"])] = claim["value"]["score"]
        if len(values) > 1:
            conflicts.append(
                {
                    "conflict_id": f"{assessment_id}:score",
                    "contact_id": None,
                    "field": "score",
                    "alternatives": [
                        {
                            "value": str(value),
                            "claims": sorted(c["claim_id"] for k, c in totals if c["value"]["score"] == value),
                            "documents": sorted({c["document"] for k, c in totals if c["value"]["score"] == value}),
                        }
                        for value in values
                    ],
                    "status": "open",
                    "rule": "11",
                    "outcome": None,
                    "would_settle": WOULD_SETTLE["score"],
                }
            )
        rows.append(
            {
                "assessment_id": assessment_id,
                "instrument": cluster["instrument"],
                "score": values,
                "completed_date": date,
                "completed_time": cluster["completed_time"],
                "form_id": cluster["form_id"],
                "items": items,
                "claims": sorted(c["claim_id"] for k, c in cluster["claims"] if k == "completion"),
                "copies": sorted(c["claim_id"] for k, c in cluster["claims"] if k == "copy"),
                "mentions": sorted(c["claim_id"] for k, c in cluster["claims"] if k == "mention"),
            }
        )
    rows.sort(key=lambda row: (row["completed_date"] or "", row["assessment_id"]))
    return rows, conflicts


# --------------------------------------------------------------------------
# Everything for one patient
# --------------------------------------------------------------------------


def conclude(patient_key: str, claims: list[dict], sections: dict) -> dict[str, list[dict]]:
    """The conclusions for one patient, from all of that patient's claims."""
    contacts, conflicts, findings = [], [], []
    taken = set()
    for group in group_references(claims):
        built = build_contact(patient_key, group, sections)
        if built is None:
            continue
        # Two contacts may still share a label. The store needs each id once.
        base, number = built["contact"]["contact_id"], 2
        while built["contact"]["contact_id"] in taken:
            built["contact"]["contact_id"] = f"{base}#{number}"
            number += 1
        taken.add(built["contact"]["contact_id"])
        contacts.append(built["contact"])
        conflicts.extend(built["conflicts"])
        findings.extend(built["findings"])
    found, more = assessments(patient_key, claims, sections)
    conflicts.extend(more)
    contacts.sort(key=lambda row: (row["service_date"] or "", row["contact_id"]))
    return {
        "contacts": contacts,
        "conflicts": sorted(conflicts, key=lambda row: row["conflict_id"]),
        "findings": sorted(findings, key=lambda row: row["finding_id"]),
        "plan_rules": plan_rules(claims, sections),
        "assessments": found,
    }
