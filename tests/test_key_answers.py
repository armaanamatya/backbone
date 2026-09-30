"""Check 14 in full: the five answers against section 7 of the key, by figure
and by source, not by wording.

The comparison rests on the results behind each answer, which the tests in
`test_answers.py` do not look at. The key's cited lines for DEV-05 are read
from `answer-key.md` itself. No model is called.
"""

import json
from pathlib import Path

from key_citations import CITATION

KEY = json.loads((Path(__file__).parent / "answer_key.json").read_text(encoding="utf-8"))["answers"]
ROOT = Path(__file__).resolve().parent.parent


def result(answer, function, **arguments):
    found = [r for r in answer["results"] if r["function"] == function and all(r["arguments"].get(k) == v for k, v in arguments.items())]
    assert found, f"no {function} result with {arguments}"
    return found[0]


def cited(answer) -> set:
    return {(s["document"], s["line"]) for r in answer["results"] for s in r["sources"]}


def documents_of(rows) -> set:
    return {d for row in rows for d in row["documents"]}


# ---- DEV-01 ------------------------------------------------------------------------


def test_dev_01_figures(answers):
    expected = KEY["DEV-01"]
    care = result(answers["DEV-01"], "care_delivered", group_by="class")
    assert answers["DEV-01"]["patient"]["patient"] == expected["patient"]
    assert (care["period"]["start"], care["period"]["end"]) == tuple(expected["period"])
    assert {t["sessions"] for t in care["totals"]} == {expected["sessions"]}
    assert {t["days"] for t in care["totals"]} == {expected["days"]}
    for name, count in expected["by_class"].items():
        assert {t["by_class"][name]["sessions"] for t in care["totals"]} == {count}, name
    assert sorted(r["encounter"] for r in care["contributed"]) == expected["contributed"]
    assert sorted(r["encounter"] for r in care["excluded"]) == expected["excluded"]
    assert care["not_read"] == expected["not_read"]


def test_dev_01_sources(answers):
    """Each counted contact cites every document that describes it, and the
    records the key names as duplicate or ineligible risks are all named."""
    expected = KEY["DEV-01"]
    care = result(answers["DEV-01"], "care_delivered", group_by="class")
    by_encounter = {r["encounter"]: r for r in care["contributed"]}
    for encounter, documents in expected["duplicate_risk"].items():
        assert set(documents) <= set(by_encounter[encounter]["documents"]), encounter
        assert len(by_encounter[encounter]["sources"]) >= 1
    assert expected["copy"] in by_encounter["HG-E110"]["copies"]
    for encounter, row in by_encounter.items():
        assert row["sources"], encounter
        assert all(s["verified"] for s in care["sources"])
    not_counted = result(answers["DEV-01"], "not_counted")
    named = documents_of(not_counted["rows"]) | {d["document"] for d in not_counted["documents_without_encounter"]}
    assert set(expected["ineligible_documents"]) <= named


def test_dev_01_the_open_conflict_changes_no_count(answers):
    care = result(answers["DEV-01"], "care_delivered", group_by="class")
    assert len(care["conflicts"]) == 1
    assert len({(t["sessions"], t["days"]) for t in care["totals"]}) == 1
    assert len({t["minutes"] for t in care["totals"]}) == 2


# ---- DEV-02 ------------------------------------------------------------------------


def test_dev_02_figures(answers):
    expected = KEY["DEV-02"]
    care = result(answers["DEV-02"], "care_delivered")
    assert sorted(t["minutes"] for t in care["totals"]) == expected["minutes"]
    assert sorted(t["hours"] for t in care["totals"]) == expected["hours"]
    weekly = result(answers["DEV-02"], "care_delivered", group_by="week") if any(r["arguments"].get("group_by") == "week" for r in answers["DEV-02"]["results"] if r["function"] == "care_delivered") else None
    goal = next((r for r in answers["DEV-02"]["results"] if r["function"] == "goal_status"), None)
    assert weekly or goal, "the answer holds no weekly figures"
    if weekly:
        found = {g["start"]: sorted(t["minutes"] for t in g["totals"]) for g in weekly["groups"]}
    else:
        found = {w["start"]: w["minutes"] for w in goal["weeks"]}
    assert found == expected["weeks"]
    assert [c["conflict_id"] for c in care["conflicts"]] == expected["not_settled"]
    assert care["not_read"] == expected["not_read"]


def test_dev_02_exclusions(answers):
    expected = KEY["DEV-02"]
    care = result(answers["DEV-02"], "care_delivered")
    removed = {r["encounter"]: [list(pair) for pair in r["removed"]] for r in care["contributed"] if r["removed"]}
    assert removed == expected["removed"]
    without = {r["encounter"]: r["minutes_without_patient"] for r in care["contributed"] if r["minutes_without_patient"]}
    assert without == expected["without_patient"]
    assert sorted(r["encounter"] for r in care["excluded"]) == KEY["DEV-01"]["excluded"]


# ---- DEV-03 ------------------------------------------------------------------------


def test_dev_03_figures(answers):
    expected = KEY["DEV-03"]
    goal = result(answers["DEV-03"], "goal_status")
    assert {w["start"]: w["verdict"] for w in goal["weeks"]} == expected["verdicts"]
    assert len(goal["plans"]) == expected["plans"] and goal["plan_changes"] == expected["plan_changes"]
    needs = {r["measure"]: r["minimum"] for r in goal["plans"][0]["requirements"]}
    assert needs == expected["goal"]
    last = goal["weeks"][-1]
    assert last["depends_on"] == [expected["week_4_depends_on"]] and last["partial"] == expected["week_4_partial"]
    assert all(not w["depends_on"] for w in goal["weeks"][:-1])
    assert goal["not_read"] == expected["not_read"]


def test_dev_03_the_goal_is_cited_from_the_plan(answers):
    goal = result(answers["DEV-03"], "goal_status")
    source = KEY["DEV-03"]["goal_source"]
    assert (source["document"], source["line"]) in {(s["document"], s["line"]) for s in goal["sources"] if s["type"] == "plan_rule"}


# ---- DEV-04 ------------------------------------------------------------------------


def test_dev_04_figures_and_sources(answers):
    for on in ("2026-01-19", "2026-01-21"):
        expected = KEY["DEV-04"][on]
        detail = result(answers["DEV-04"], "date_detail", date=on)
        assert detail["counts"]["therapy_contacts"] == expected["therapy_contacts"], on
        assert sorted(t["minutes"] for t in detail["totals"]) == expected["minutes"], on
        therapy = [c for c in detail["contacts"] if c["counts"]]
        if "per_contact" in expected:
            assert {c["encounter"]: c["minutes"] for c in therapy} == expected["per_contact"]
        if "present" in expected:
            assert therapy[0]["present"] == expected["present"] and [list(p) for p in therapy[0]["removed"]] == expected["removed"]
        if "modality" in expected:
            assert therapy[0]["modality"] == expected["modality"]
        assert set(expected["documents"]) <= documents_of(therapy), on
        assert detail["conflicts"] == KEY["DEV-04"]["not_settled"], on
        assert detail["not_read"] == KEY["DEV-04"]["not_read"]


def test_dev_04_the_correction_and_the_copy(answers):
    expected = KEY["DEV-04"]["correction"]
    detail = result(answers["DEV-04"], "date_detail", date="2026-01-19")
    group = next(c for c in detail["contacts"] if c["encounter"] == "HG-E110")
    conflict = next(c for c in group["conflicts"] if c["conflict_id"] == expected["conflict"])
    assert conflict["status"] == "settled" and conflict["outcome"] == expected["outcome"]
    old = next(a for a in conflict["alternatives"] if a["value"] == expected["replaced"])
    assert sorted(old["documents"]) == expected["replaced_in"]
    assert "BH-D104" in group["copies"]


# ---- DEV-05 ------------------------------------------------------------------------


def test_dev_05_figures(answers):
    expected = KEY["DEV-05"]
    scores = result(answers["DEV-05"], "assessments")
    assert [[r["score"][0], r["completed_date"]] for r in scores["rows"]] == expected["scores"]
    assert [c["change"] for c in scores["changes"]] == expected["changes"]
    assert scores["overall_change"] == expected["overall"]
    copies = {c["document"]: r["completed_date"] for r in scores["rows"] for c in r["copies"]}
    mentions = {m["document"]: r["completed_date"] for r in scores["rows"] for m in r["mentions"]}
    assert copies == expected["copies"] and mentions == expected["mentions"]
    assert scores["conflicts"] == expected["not_settled"]
    assert scores["not_read"] == expected["not_read"]


def test_dev_05_the_reason_for_the_added_contact_is_cited(answers):
    lines = cited(answers["DEV-05"])
    for document, line in KEY["DEV-05"]["reason_sources"]:
        assert (document, line) in lines, f"{document} line {line}"


def test_dev_05_cites_every_line_the_key_cites(answers):
    """The key's tables for DEV-05 cite lines of the record. Each is among the
    sources behind the answer, by document and line. Whether the quote and the
    speaker match too is scored by `key_citations.py`, and the count is in
    `output/comparison/models-and-efforts.md`."""
    key = (ROOT / "answer-key.md").read_text(encoding="utf-8")
    part = key[key.index("### DEV-05") : key.index("## 8. Problem questions")]
    wanted = {("BH-" + m.group(1), int(m.group(2))) for m in CITATION.finditer(part)}
    assert len(wanted) >= 25, "the key section was not found"
    lines = cited(answers["DEV-05"])
    missing = sorted(f"{d} line {n}" for d, n in wanted - lines)
    assert missing == KEY["DEV-05"]["cited_lines_not_in_the_answer"]
