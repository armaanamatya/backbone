"""Compares reads of the same documents by different models or efforts (O-36).

Each run is a settings file whose store was filled by `ingest`. The first is
the baseline. For each run the command reports what the tool charged, what
came back, and whether the rules reach the same conclusions as the baseline.
Calls no model.
"""

from __future__ import annotations

import glob
import json
from collections import Counter, defaultdict
from pathlib import Path

from . import counting, settings as settings_file, store

COUNT_BEARING = ("contacts", "times", "stated_minutes", "attendance", "scores", "corrections", "charges")


def usage(logs_dir: Path, model: str, effort: str, prompt_version: int) -> dict:
    """Cost, time and tokens of the reading calls of one run, from the logs."""
    found = {"calls": 0, "rejected": 0, "cost_usd": 0.0, "seconds": 0.0, "tokens_out": 0, "served_by": set()}
    for path in glob.glob(str(logs_dir / "*.jsonl")):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                event = json.loads(line)
                if event.get("event") != "model_call" or event.get("purpose") != "reading":
                    continue
                if (event.get("model"), event.get("effort"), event.get("prompt_version")) != (model, effort, prompt_version):
                    continue
                found["calls"] += 1
                found["rejected"] += 0 if event.get("accepted") else 1
                found["cost_usd"] += event.get("cost_usd") or 0
                found["seconds"] += event.get("wall_seconds") or 0
                found["tokens_out"] += event.get("output_tokens") or 0
                found["served_by"] |= set((event.get("models") or {}).keys())
    found["served_by"] = sorted(found["served_by"])
    return found


def facts(reading: dict) -> set:
    """The facts a count rests on, in one document's reading."""
    refs = {c["ref"]: c for c in reading["contacts"]}

    def who(item):
        contact = refs.get(item.get("contact")) or {}
        return contact.get("encounter_id") or contact.get("appointment_id") or contact.get("service_date")

    found = set()
    for c in reading["contacts"]:
        found.add(("contact", c.get("encounter_id") or c.get("appointment_id"), c.get("service_date"), c.get("service_class")))
    for t in reading["times"]:
        found.add(("time", who(t), t["what"], t.get("start"), t.get("end"), t["label"]))
    for m in reading["stated_minutes"]:
        found.add(("minutes", who(m), m["minutes"], m["of"]))
    for a in reading["attendance"]:
        found.add(("attendance", who(a), a["status"]))
    for x in reading["scores"]:
        found.add(("score", x["instrument"], x["score"], x.get("item_number"), x["completed_date"], x["relation"]))
    for x in reading["corrections"]:
        found.add(("correction", who(x), x["field"], x["old_value"], x["new_value"]))
    for x in reading["charges"]:
        found.add(("charge", who(x), x["charge_id"], x.get("quantity")))
    for section in reading["sections"]:
        found.add(("section", section["kind"], section["signature"], section.get("signed_date"), section["is_copy"]))
    return found


def readings(settings) -> dict[str, dict]:
    """The saved results of one run, by document hash."""
    found = {}
    stamp = f"__{settings.model}__{settings.effort}__v{settings.prompt_version}.json"
    for path in settings.readings.glob(f"*{stamp}"):
        record = json.loads(path.read_text(encoding="utf-8"))
        found[record["doc_hash"]] = record["reading"]
    return found


def describe(settings) -> dict:
    """What one run's store holds."""
    connection = store.connect(settings.store)
    try:
        documents = connection.execute("SELECT COUNT(*) FROM documents WHERE read_status = 'read'").fetchone()[0]
        claims = connection.execute("SELECT COUNT(*) FROM claims").fetchone()[0]
        quotes = dict(connection.execute("SELECT quote_status, COUNT(*) FROM claims GROUP BY 1").fetchall())
        by_type = dict(connection.execute("SELECT type, COUNT(*) FROM claims GROUP BY 1").fetchall())
        coverage = Counter()
        for row in connection.execute("SELECT not_captured FROM documents WHERE not_captured IS NOT NULL"):
            for status, count in json.loads(row[0])["counts"].items():
                coverage[status] += count
        conclusions = {}
        for patient in store.patients(connection):
            rules = store.rows_of(connection, "plan_rules", patient, "rule_id")
            contacts = store.rows_of(connection, "contacts", patient, "service_date, contact_id")
            weeks = store.rows_of(connection, "weekly_status", patient, "week_start")
            plans = counting.plans(rules)
            encounters = [c for c in contacts if c["record_kind"] == "encounter"]
            conclusions[patient] = {
                "encounters": len(encounters),
                "administrative": len(contacts) - len(encounters),
                "statuses": {c["encounter_id"] or c["contact_id"]: (c["status"], sorted(m["minutes"] for m in c["minutes"] if m["minutes"] is not None)) for c in encounters},
                "weeks": [(w["week_start"], w["verdict"], sorted(m["minutes"] for m in w["minutes"])) for w in weeks],
                "conflicts": [(c["conflict_id"], c["status"], c["rule"]) for c in store.rows_of(connection, "conflicts", patient, "conflict_id")],
                "findings": sorted(f["kind"] for f in store.rows_of(connection, "findings", patient, "finding_id")),
                "assessments": [(a["completed_date"], a["score"]) for a in store.rows_of(connection, "assessments", patient, "completed_date")],
                "totals": [
                    (row["sessions"], row["days"], row["minutes"])
                    for plan in plans
                    for row in sorted(counting.totals(contacts, rules, plan["start"], plan["end"]), key=lambda r: r["minutes"])
                ],
            }
        dumps = {table: store.dump(connection, (table,))[table] for table in store.CONCLUDES_TABLES}
    finally:
        connection.close()
    return {
        "documents": documents,
        "claims": claims,
        "quotes": quotes,
        "by_type": by_type,
        "coverage": dict(coverage),
        "conclusions": conclusions,
        "dumps": dumps,
    }


def compare(paths: list[str]) -> dict:
    runs = []
    for path in paths:
        settings = settings_file.load(Path(path))
        runs.append(
            {
                "settings": path,
                "model": settings.model,
                "effort": settings.effort,
                "prompt_version": settings.prompt_version,
                "usage": usage(settings.logs, settings.model, settings.effort, settings.prompt_version),
                "described": describe(settings),
                "readings": readings(settings),
            }
        )
    base = runs[0]
    base_readings = dict(base["readings"])
    base_dumps = dict(base["described"]["dumps"])
    base_conclusions = base["described"]["conclusions"]
    for run in runs:
        same = 0
        differing = []
        for doc_hash, reading in base_readings.items():
            other = run["readings"].get(doc_hash)
            if other is None:
                differing.append(reading["document"].get("declared_id"))
            elif facts(reading) == facts(other):
                same += 1
            else:
                differing.append(reading["document"].get("declared_id"))
        run["same_facts"] = same
        run["differing_documents"] = sorted(d for d in differing if d)
        run["same_conclusions"] = {
            table: base_dumps[table] == run["described"]["dumps"][table] for table in store.CONCLUDES_TABLES
        }
        run["same_figures"] = {
            patient: {
                key: base_conclusions[patient][key] == run["described"]["conclusions"].get(patient, {}).get(key)
                for key in ("encounters", "statuses", "weeks", "conflicts", "findings", "assessments", "totals")
            }
            for patient in base_conclusions
        }
        del run["readings"]
        del run["described"]["dumps"]
    return {"baseline": f"{base['model']} at {base['effort']}", "runs": runs}


def report(result: dict) -> str:
    runs = result["runs"]
    lines = [f"# Reads compared. Baseline: {result['baseline']}.", ""]
    lines += ["Everything here is measured. The rules ran on each run's saved results with no model.", ""]
    lines += ["## Cost and time", "", "| Run | Calls | Rejected | Cost | Seconds over the calls | Tokens out | Served by |", "|---|---|---|---|---|---|---|"]
    for run in runs:
        u = run["usage"]
        lines.append(f"| {run['model']} at {run['effort']} | {u['calls']} | {u['rejected']} | ${u['cost_usd']:.2f} | {u['seconds']:.0f} | {u['tokens_out']:,} | {', '.join(u['served_by'])} |")
    lines += ["", "## What came back", "", "| Run | Documents read | Claims | Quotes not found | Values not captured | Documents with the baseline's count-bearing facts |", "|---|---|---|---|---|---|"]
    for run in runs:
        d = run["described"]
        lines.append(
            f"| {run['model']} at {run['effort']} | {d['documents']} | {d['claims']} | {d['quotes'].get('unverified', 0)} |"
            f" {d['coverage'].get('not_captured', 0)} | {run['same_facts']} of {d['documents']} |"
        )
    lines += ["", "## What the rules make of it", ""]
    lines += ["| Run | Encounters | Statuses and minutes | Weekly verdicts and minutes | Conflicts | Findings | Assessments | Totals |", "|---|---|---|---|---|---|---|---|"]
    for run in runs:
        for patient, same in run["same_figures"].items():
            c = run["described"]["conclusions"].get(patient, {})
            mark = lambda key: "same" if same[key] else "DIFFERS"  # noqa: E731
            lines.append(
                f"| {run['model']} at {run['effort']} | {c.get('encounters')} ({mark('encounters')}) | {mark('statuses')} | {mark('weeks')} | {mark('conflicts')} | {mark('findings')} | {mark('assessments')} | {mark('totals')} |"
            )
    lines += ["", "## Weekly verdicts", ""]
    for run in runs:
        for patient, c in run["described"]["conclusions"].items():
            weeks = "; ".join(f"{start}: {verdict.replace('_', ' ')} ({' or '.join(str(m) for m in minutes)})" for start, verdict, minutes in c["weeks"])
            lines.append(f"- {run['model']} at {run['effort']}, {patient}: {weeks}")
    lines += ["", "## Where a run differs from the baseline", ""]
    for run in runs[1:]:
        for patient, same in run["same_figures"].items():
            c = run["described"]["conclusions"].get(patient, {})
            b = runs[0]["described"]["conclusions"][patient]
            if not same["statuses"]:
                for key in sorted(set(b["statuses"]) | set(c.get("statuses", {}))):
                    if b["statuses"].get(key) != c.get("statuses", {}).get(key):
                        lines.append(f"- {run['model']} at {run['effort']}, {key}: baseline {b['statuses'].get(key)}, this run {c.get('statuses', {}).get(key)}")
            for key in ("conflicts", "findings", "assessments", "totals"):
                if not same[key]:
                    lines.append(f"- {run['model']} at {run['effort']}, {key}: baseline {b[key]}, this run {c.get(key)}")
        if run["differing_documents"]:
            lines.append(f"- {run['model']} at {run['effort']}: count-bearing facts differ in {', '.join(run['differing_documents'])}")
    return "\n".join(lines) + "\n"
