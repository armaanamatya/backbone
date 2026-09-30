"""Measures times, sizes, tokens and cost (stage 9, piece 9 of the build list).

Everything in `benchmark.md` is measured. The model's own time and cost come
from the logs of calls already made; the code's time is measured here, on
saved results, with no model. `--live` asks new questions end to end, which
is the only part that calls a model. `estimates.md` is a separate file: the
measured figures multiplied out to 500,000 documents, labelled as estimates.
"""

from __future__ import annotations

import dataclasses
import glob
import json
import os
import shutil
import statistics
import tempfile
import time
from datetime import datetime
from pathlib import Path

from . import ask, functions, ingest, reader, settings as settings_file, store
from .logs import NoLog, RunLog, now

PRODUCTION = 500_000
MILLION = 1_000_000


def _seconds(a: str, b: str) -> float:
    return (datetime.fromisoformat(b) - datetime.fromisoformat(a)).total_seconds()


def _events(logs_dir: Path):
    for path in sorted(glob.glob(str(logs_dir / "*.jsonl"))):
        with open(path, encoding="utf-8") as handle:
            lines = [json.loads(line) for line in handle]
        yield Path(path).name, lines


# --------------------------------------------------------------------------
# From the logs: what the model calls cost and took
# --------------------------------------------------------------------------


def reading_runs(settings) -> list[dict]:
    """Each ingest run that called the model under the current model, effort
    and prompt version: how many calls, how long the run took from its first
    event to its last, and what the calls cost."""
    stamp = (settings.model, settings.effort, settings.prompt_version)
    runs = []
    for name, lines in _events(settings.logs):
        calls = [e for e in lines if e.get("event") == "model_call" and e.get("purpose") == "reading" and (e.get("model"), e.get("effort"), e.get("prompt_version")) == stamp]
        if not calls:
            continue
        accepted = [e for e in calls if e.get("accepted")]
        runs.append(
            {
                "log": name,
                "started": lines[0]["at"],
                "calls": len(calls),
                "accepted": len(accepted),
                "documents_read": sum(1 for e in lines if e.get("event") == "document_read" and not e.get("reused")),
                "run_wall_seconds": round(_seconds(lines[0]["at"], lines[-1]["at"]), 1),
                "sum_of_call_seconds": round(sum(e.get("wall_seconds") or 0 for e in calls), 1),
                "cost_usd": round(sum(e.get("cost_usd") or 0 for e in calls), 4),
                "input_tokens": sum((e.get("input_tokens") or 0) + (e.get("cache_creation_input_tokens") or 0) + (e.get("cache_read_input_tokens") or 0) for e in calls),
                "output_tokens": sum(e.get("output_tokens") or 0 for e in calls),
                "per_call": [
                    {"file": e.get("file"), "wall_seconds": e.get("wall_seconds"), "cost_usd": e.get("cost_usd"), "input_tokens": (e.get("input_tokens") or 0) + (e.get("cache_creation_input_tokens") or 0) + (e.get("cache_read_input_tokens") or 0), "output_tokens": e.get("output_tokens"), "cache_read_input_tokens": e.get("cache_read_input_tokens")}
                    for e in accepted
                ],
            }
        )
    return runs


def per_document(runs: list[dict]) -> dict:
    """Tokens, time and cost of one accepted reading call, over every run."""
    calls = [c for run in runs for c in run["per_call"] if c.get("cost_usd") is not None]
    if not calls:
        return {"calls": 0}

    def spread(key):
        values = [c[key] for c in calls if c.get(key) is not None]
        return {"mean": round(statistics.mean(values), 4), "median": round(statistics.median(values), 4), "min": min(values), "max": max(values)} if values else None

    return {"calls": len(calls), "wall_seconds": spread("wall_seconds"), "cost_usd": spread("cost_usd"), "input_tokens": spread("input_tokens"), "output_tokens": spread("output_tokens"), "cache_read_input_tokens": spread("cache_read_input_tokens")}


def plan_calls(settings) -> list[dict]:
    """Every plan call under the current plan prompt version, from the logs."""
    found = []
    for name, lines in _events(settings.logs):
        for e in lines:
            if e.get("event") == "model_call" and e.get("purpose") == "plan" and e.get("plan_prompt_version") == settings.plan_prompt_version:
                found.append({"log": name, "question": e.get("question"), "wall_seconds": e.get("wall_seconds"), "cost_usd": e.get("cost_usd"), "output_tokens": e.get("output_tokens"), "accepted": e.get("accepted")})
    return found


def all_calls(settings) -> dict:
    """Every model call in the logs, whatever the purpose: the cost of the build so far."""
    total = {"calls": 0, "cost_usd": 0.0, "by_purpose": {}}
    for _, lines in _events(settings.logs):
        for e in lines:
            if e.get("event") != "model_call":
                continue
            total["calls"] += 1
            total["cost_usd"] += e.get("cost_usd") or 0
            purpose = total["by_purpose"].setdefault(e.get("purpose"), {"calls": 0, "cost_usd": 0.0})
            purpose["calls"] += 1
            purpose["cost_usd"] += e.get("cost_usd") or 0
    total["cost_usd"] = round(total["cost_usd"], 2)
    for purpose in total["by_purpose"].values():
        purpose["cost_usd"] = round(purpose["cost_usd"], 2)
    return total


# --------------------------------------------------------------------------
# Measured here: the code's time, on saved results
# --------------------------------------------------------------------------


def _no_model(*arguments, **named):
    raise AssertionError("the benchmark called a model where it must not")


def _temporary(settings, folder: Path):
    return dataclasses.replace(settings, store=folder / "abstraction.sqlite", logs=folder / "logs", answers=folder / "answers")


def replay(settings, documents: Path, folder: Path, files=None) -> tuple[float, dict]:
    """Fills an empty store from the saved reading results. Returns the
    seconds it took and the counts."""
    chosen = _temporary(settings, folder)
    original = reader.call_model
    reader.call_model = _no_model
    try:
        started = time.perf_counter()
        connection = store.connect(chosen.store)
        listed = files if files is not None else ingest.files_in(documents)
        original_files_in = ingest.files_in
        ingest.files_in = lambda _folder: listed
        try:
            outcome = ingest.register(connection, documents, NoLog())
            summaries = ingest.read_waiting(connection, chosen, NoLog())
        finally:
            ingest.files_in = original_files_in
        seconds = time.perf_counter() - started
        counts = {"registered": len(outcome["new"]), "read_from_saved_results": sum(1 for s in summaries if s["status"] == "read" and s["reused"]), "not_read": sum(1 for s in summaries if s["status"] != "read")}
        connection.close()
    finally:
        reader.call_model = original
    return seconds, counts


def measure_replay(settings, documents: Path, runs: int) -> dict:
    """Time to fill the store from saved results, and to add the last document
    to a store that holds the rest. The model's time for one document comes
    from the logs and is added beside it, not into it."""
    times, counts = [], None
    for _ in range(runs):
        with tempfile.TemporaryDirectory() as folder:
            seconds, counts = replay(settings, documents, Path(folder))
            times.append(seconds)
    files = ingest.files_in(documents)
    add_times = []
    for _ in range(runs):
        with tempfile.TemporaryDirectory() as folder:
            replay(settings, documents, Path(folder), files[:-1])
            seconds, _ = replay(settings, documents, Path(folder), files)
            add_times.append(seconds)
    return {
        "documents": len(files),
        "fill_from_saved_results_seconds": {"median": round(statistics.median(times), 3), "min": round(min(times), 3), "max": round(max(times), 3), "runs": runs},
        "counts": counts,
        "add_one_document_code_seconds": {"median": round(statistics.median(add_times), 3), "min": round(min(add_times), 3), "max": round(max(add_times), 3), "runs": runs, "file": files[-1].name},
    }


def measure_rerun(settings, documents: Path, runs: int) -> dict:
    """`ingest` on the store on disk, where every file is already known: the
    time of a repeated review that reads nothing."""
    times = []
    for _ in range(runs):
        started = time.perf_counter()
        connection = store.connect(settings.store)
        outcome = ingest.register(connection, documents, NoLog())
        waiting = ingest.waiting(connection, settings)
        connection.close()
        times.append(time.perf_counter() - started)
    return {"seconds": {"median": round(statistics.median(times), 3), "min": round(min(times), 3), "max": round(max(times), 3), "runs": runs}, "skipped_as_known": len(outcome["duplicate"]), "waiting_to_be_read": len(waiting)}


def measure_questions(settings, questions: list[tuple[str, str]], runs: int) -> list[dict]:
    """Code time to answer each question from its saved plan, over several
    runs, with the model switched off. A question whose plan is not saved is
    reported as such and not timed."""
    original = reader.call_model
    reader.call_model = _no_model
    rows = []
    try:
        connection = store.connect(settings.store)
        for question_id, question in questions:
            model = ask.Model(settings, NoLog())
            if not model.saved_path(question).exists():
                rows.append({"id": question_id, "question": question, "saved_plan": False})
                continue
            times = []
            built = None
            for _ in range(runs):
                started = time.perf_counter()
                built = ask.answer(connection, settings, NoLog(), question, question_id)
                times.append(time.perf_counter() - started)
            rows.append(
                {
                    "id": question_id,
                    "question": question,
                    "saved_plan": True,
                    "functions": [r["function"] for r in built["results"]],
                    "collection_wide": any(r["function"] == "patients_below_goal" for r in built["results"]),
                    "code_seconds": {"median": round(statistics.median(times), 4), "min": round(min(times), 4), "max": round(max(times), 4), "runs": runs},
                    "answer_lines": built["text"].count("\n"),
                }
            )
        connection.close()
    finally:
        reader.call_model = original
    return rows


def ask_live(settings, log, questions: list[tuple[str, str]], folder: Path) -> list[dict]:
    """New questions, end to end, plan call included. Their answers are written
    under `folder` and their plans are saved, so asking again calls no model."""
    rows = []
    folder.mkdir(parents=True, exist_ok=True)
    connection = store.connect(settings.store)
    for question_id, question in questions:
        started = time.perf_counter()
        built = ask.answer(connection, settings, log, question, question_id)
        seconds = time.perf_counter() - started
        (folder / f"{question_id}.json").write_text(json.dumps(built, ensure_ascii=False, indent=1), encoding="utf-8")
        (folder / f"{question_id}.md").write_text(built["text"], encoding="utf-8", newline="\n")
        usage = {}
        record = json.loads(ask.Model(settings, log).saved_path(question).read_text(encoding="utf-8")) if built["plan"] is not None else {"attempts": []}
        for attempt in record.get("attempts", []):
            if attempt.get("usage"):
                usage = attempt["usage"]
        # A question asked before has its plan saved and calls no model. Its
        # end-to-end time is then the code time plus the plan call's logged
        # time, and the row says so.
        reused = built["plan_source"] == "saved"
        rows.append(
            {
                "id": question_id,
                "question": question,
                "plan_source": built["plan_source"],
                "plan_attempts": built["plan_attempts"],
                "functions": [r["function"] for r in built["results"]],
                "collection_wide": any(r["function"] == "patients_below_goal" for r in built["results"]),
                "wall_seconds": round(seconds + ((usage.get("wall_seconds") or 0) if reused else 0), 2),
                "code_seconds": round(seconds, 3),
                "plan_call_seconds": usage.get("wall_seconds"),
                "plan_call_cost_usd": usage.get("cost_usd"),
                "plan_call_output_tokens": usage.get("output_tokens"),
                "lead": built["parts"].get("in short", [])[:2],
            }
        )
    connection.close()
    return rows


# --------------------------------------------------------------------------
# Sizes
# --------------------------------------------------------------------------


def _folder_bytes(path: Path) -> int:
    return sum(p.stat().st_size for p in path.rglob("*") if p.is_file()) if path.exists() else 0


def measure_size(settings) -> dict:
    connection = store.connect(settings.store)
    rows = {table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] for table in store.TABLES}
    documents = rows["documents"] or 1
    text_bytes = connection.execute("SELECT COALESCE(SUM(byte_size), 0) FROM documents").fetchone()[0]
    stamp = f"__{settings.model}__{settings.effort}__v{settings.prompt_version}.json"
    saved = [p for p in settings.readings.glob(f"*{stamp}")] if settings.readings.exists() else []
    connection.close()
    store_bytes = settings.store.stat().st_size
    return {
        "store_file": str(settings.store.relative_to(settings.root)),
        "store_bytes": store_bytes,
        "rows": rows,
        "source_text_bytes": text_bytes,
        "store_bytes_per_document": round(store_bytes / documents),
        "saved_results_for_current_settings": {"files": len(saved), "bytes": sum(p.stat().st_size for p in saved)},
        "saved_results_folder_bytes": _folder_bytes(settings.readings),
        "logs_bytes": _folder_bytes(settings.logs),
        "answers_bytes": _folder_bytes(settings.answers),
    }


# --------------------------------------------------------------------------
# Scale, on synthetic copies
# --------------------------------------------------------------------------


def _copy_patient(connection, patient: str, copies: range) -> None:
    """Copies every row of one patient under new patient keys. The copies are
    for timing only: their text and claims are the original's."""
    documents = connection.execute("SELECT * FROM documents WHERE patient_key = ?", (patient,)).fetchall()
    claims = connection.execute("SELECT * FROM claims WHERE patient_key = ?", (patient,)).fetchall()
    conclusions = {table: connection.execute(f"SELECT * FROM {table} WHERE patient_key = ?", (patient,)).fetchall() for table in store.CONCLUDES_TABLES}
    keys = {table: [c[1] for c in connection.execute(f"PRAGMA table_info({table})")] for table in store.TABLES}

    def insert(table, rows):
        marks = ", ".join("?" * len(keys[table]))
        connection.executemany(f"INSERT INTO {table} ({', '.join(keys[table])}) VALUES ({marks})", rows)

    for k in copies:
        tag = f"{k:05d}"
        who = f"{patient}-{tag}"
        insert("documents", [tuple(tag + r["doc_hash"][5:] if c == "doc_hash" else (who if c == "patient_key" else r[c]) for c in keys["documents"]) for r in documents])
        insert("claims", [tuple(tag + r[c][5:] if c in ("claim_id", "doc_hash") else (who if c == "patient_key" else r[c]) for c in keys["claims"]) for r in claims])
        def renamed(column, value):
            if column == "patient_key":
                return who
            if column == "doc_hash":
                return tag + value[5:]
            if column.endswith("_id") and isinstance(value, str):
                return value.replace(patient + "/", who + "/", 1) if value.startswith(patient + "/") else f"{tag}:{value}"
            return value

        for table, rows in conclusions.items():
            insert(table, [tuple(renamed(c, r[c]) for c in keys[table]) for r in rows])
    connection.commit()


def measure_scale(settings, factors: list[int]) -> list[dict]:
    """The same queries on a store holding the patient copied many times over.
    Measured, on synthetic data: each copy is the real patient under another
    record number."""
    rows = []
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "scaled.sqlite"
        shutil.copy(settings.store, path)
        connection = store.connect(path)
        try:
            rows = _scale_rows(connection, path, factors)
        finally:
            connection.close()
    return rows


def _scale_rows(connection, path: Path, factors: list[int]) -> list[dict]:
    rows = []
    if True:
        patient = store.patients(connection)[0]
        question = f"How many therapy sessions did {patient} attend?"
        done = 1
        for factor in sorted(factors):
            if factor > done:
                _copy_patient(connection, patient, range(done, factor))
                done = factor
            timings = {}
            for name, work in (
                ("care_delivered, one patient", lambda: functions.care_delivered(connection, patient)),
                ("resolve_patient, by record number", lambda: functions.resolve_patient(connection, patient)),
                ("patients_in, the list every plan call is given", lambda: functions.patients_in(connection)),
                ("build_message, the plan call's input", lambda: ask.build_message(connection, question)),
                ("patients_below_goal, across the collection", lambda: functions.patients_below_goal(connection)),
                ("known_hashes, the duplicate check at ingest", lambda: store.known_hashes(connection)),
            ):
                samples = []
                for _ in range(3):
                    started = time.perf_counter()
                    result = work()
                    samples.append(time.perf_counter() - started)
                timings[name] = {"median_seconds": round(statistics.median(samples), 4)}
                if name.startswith("build_message"):
                    timings[name]["characters"] = len(result)
            rows.append({"patients": factor, "documents": factor * connection.execute("SELECT COUNT(*) FROM documents WHERE patient_key = ?", (patient,)).fetchone()[0], "store_bytes": os.path.getsize(path), "timings": timings})
    return rows


# --------------------------------------------------------------------------
# The reports
# --------------------------------------------------------------------------


def _spread(entry: dict | None, unit: str = "", digits: int = 2) -> str:
    if not entry:
        return "not measured"
    return f"{entry['median']:.{digits}f}{unit} (min {entry['min']:.{digits}f}, max {entry['max']:.{digits}f}, over {entry.get('runs', 3)} runs)"


def report(result: dict) -> str:
    s = result["settings"]
    lines = [f"# Benchmark, measured on {result['measured_at'][:10]}", ""]
    lines += [f"Everything in this file is measured. Model: {s['model']}, effort {s['effort']}, reading prompt version {s['prompt_version']}, plan prompt version {s['plan_prompt_version']}, {s['parallel_calls']} calls at a time. Estimates are in `estimates.md`.", ""]

    lines += ["## 1. Reading all the documents from empty", ""]
    lines += ["From the logs of the ingest runs that called the model under these settings. The run's wall time is the time from its first event to its last, with the calls running four at a time after the first. The sum of the call times is what one call at a time would take, each call measured on its own.", ""]
    lines += ["| Run | Documents read | Calls | Accepted | Run wall time | Sum of call times | Cost | Tokens in | Tokens out |", "|---|---|---|---|---|---|---|---|---|"]
    for run in result["reading_runs"]:
        lines.append(f"| {run['started'][:16].replace('T', ' ')} | {run['documents_read']} | {run['calls']} | {run['accepted']} | {run['run_wall_seconds']:.0f} s | {run['sum_of_call_seconds']:.0f} s | ${run['cost_usd']:.2f} | {run['input_tokens']:,} | {run['output_tokens']:,} |")
    doc = result["per_document"]
    if doc.get("calls"):
        lines += ["", f"Per document, over {doc['calls']} accepted calls:", ""]
        lines += ["| Measure | Median | Mean | Min | Max |", "|---|---|---|---|---|"]
        for label, key, fmt in (("Seconds a call", "wall_seconds", "{:.1f}"), ("Cost", "cost_usd", "${:.3f}"), ("Tokens in (prompt, document and cache)", "input_tokens", "{:,.0f}"), ("Of which read from the cache", "cache_read_input_tokens", "{:,.0f}"), ("Tokens out", "output_tokens", "{:,.0f}")):
            entry = doc.get(key)
            if entry:
                lines.append(f"| {label} | {fmt.format(entry['median'])} | {fmt.format(entry['mean'])} | {fmt.format(entry['min'])} | {fmt.format(entry['max'])} |")
    total = result["all_calls"]
    lines += ["", f"Every model call in the logs, all purposes and all models: {total['calls']} calls, ${total['cost_usd']:.2f}. By purpose: " + "; ".join(f"{p or 'unknown'} {v['calls']} calls, ${v['cost_usd']:.2f}" for p, v in total["by_purpose"].items()) + ".", ""]

    r = result["replay"]
    lines += ["## 2. Re-running from saved results, and adding one document", ""]
    lines += ["| Measure | Time | What runs |", "|---|---|---|"]
    lines.append(f"| Fill an empty store from the saved results of {r['documents']} documents | {_spread(r['fill_from_saved_results_seconds'], ' s')} | Hash, register, load each saved result, check every quote, rebuild the conclusions. No model |")
    rr = result["rerun"]
    lines.append(f"| `ingest` again on the filled store | {_spread(rr['seconds'], ' s', 3)} | Hash {rr['skipped_as_known']} files, find every one known, read nothing |")
    a = r["add_one_document_code_seconds"]
    lines.append(f"| Add one document to a store holding the other {r['documents'] - 1}, code only | {_spread(a, ' s', 3)} | Hash, register, load its saved result, check its quotes, rebuild the patient's conclusions ({a['file']}) |")
    if doc.get("calls"):
        lines.append(f"| Add one document, with its model call | {a['median'] + doc['wall_seconds']['median']:.1f} s | The code time above plus the median reading call from section 1 ({doc['wall_seconds']['median']:.1f} s) |")
    lines.append("")

    lines += ["## 3. Answering a question", ""]
    lines += ["Code time is measured here, from the saved plan, with the model switched off. The plan call's time and cost are from the logs of the calls that made the plans. A question with a saved plan calls no model; a new question makes one plan call.", ""]
    lines += ["| Question | Functions | Code time (median) | Plan call | Plan cost | Lines |", "|---|---|---|---|---|---|"]
    plans = {" ".join((p["question"] or "").split()): p for p in result["plan_calls"] if p.get("accepted")}
    for q in result["questions"]:
        if not q["saved_plan"]:
            lines.append(f"| {q['id']} | no saved plan | | | | |")
            continue
        p = plans.get(" ".join(q["question"].split()), {})
        scope = " (collection-wide)" if q["collection_wide"] else ""
        lines.append(f"| {q['id']}{scope} | {', '.join(q['functions'])} | {q['code_seconds']['median'] * 1000:.0f} ms | {p.get('wall_seconds', 'n/a') if not p else f'{p['wall_seconds']:.1f} s'} | {'n/a' if not p else f'${p['cost_usd']:.3f}'} | {q['answer_lines']} |")
    if result.get("live"):
        fresh = all(q["plan_source"] == "new" for q in result["live"])
        lines += ["", "New questions asked end to end, plan call included (the related questions in section 8 of the key). Their answers are in `output/answers/related/`." + ("" if fresh else " A row marked \"plan reused\" found its plan saved from an earlier run, so it called no model this time: its end-to-end figure is the code time measured now plus the plan call's time from the log of the run that made the plan."), ""]
        lines += ["| Question | Functions | End to end | Plan call | Plan cost | Tokens out |", "|---|---|---|---|---|---|"]
        for q in result["live"]:
            scope = " (collection-wide)" if q["collection_wide"] else ""
            note = "" if q["plan_source"] == "new" else " (plan reused)"
            lines.append(f"| {q['id']}{scope}: {q['question']} | {', '.join(q['functions']) or 'none'} | {q['wall_seconds']:.1f} s{note} | {q['plan_call_seconds'] or 0:.1f} s | ${q['plan_call_cost_usd'] or 0:.3f} | {q['plan_call_output_tokens'] or 0} |")
    lines.append("")

    z = result["size"]
    lines += ["## 4. Size of the saved abstraction", ""]
    lines += ["| Measure | Value |", "|---|---|"]
    lines.append(f"| `{z['store_file']}` | {z['store_bytes']:,} bytes ({z['store_bytes'] / 1024:.0f} KB) |")
    lines.append(f"| Source text inside it | {z['source_text_bytes']:,} bytes |")
    lines.append(f"| Store bytes per document | {z['store_bytes_per_document']:,} |")
    lines.append("| Rows | " + ", ".join(f"{table} {count}" for table, count in z["rows"].items()) + " |")
    lines.append(f"| Saved reading results, these settings | {z['saved_results_for_current_settings']['files']} files, {z['saved_results_for_current_settings']['bytes']:,} bytes |")
    lines.append(f"| Saved reading results, every model and effort tried | {z['saved_results_folder_bytes']:,} bytes |")
    lines.append(f"| Logs | {z['logs_bytes']:,} bytes |")
    lines.append(f"| Answers | {z['answers_bytes']:,} bytes |")
    lines.append("")

    if result.get("scale"):
        lines += ["## 5. The same queries on a larger store", ""]
        lines += ["Measured on synthetic copies: the patient's rows copied under new record numbers, in a temporary store. Each figure is the median of three runs.", ""]
        names = list(result["scale"][0]["timings"])
        lines += ["| Patients | Documents | Store | " + " | ".join(names) + " |", "|---|---|---|" + "---|" * len(names)]
        for row in result["scale"]:
            cells = []
            for name in names:
                t = row["timings"][name]
                cells.append(f"{t['median_seconds'] * 1000:.0f} ms" + (f", {t['characters']:,} chars" if "characters" in t else ""))
            lines.append(f"| {row['patients']:,} | {row['documents']:,} | {row['store_bytes'] / 1_048_576:.0f} MB | " + " | ".join(cells) + " |")
        lines.append("")
    return "\n".join(lines) + "\n"


def estimates(result: dict) -> tuple[str, dict]:
    """The measured figures multiplied out. Every number here is an estimate."""
    doc = result["per_document"]
    s = result["settings"]
    lines = ["# Estimates at 500,000 documents", "", "Every figure in this file is an estimate: a measured figure from `benchmark.md` multiplied out. Nothing here was run at this size.", ""]
    data = {}
    if not doc.get("calls"):
        return "\n".join(lines + ["No accepted reading call is in the logs, so nothing can be multiplied out."]), data
    cost = doc["cost_usd"]["mean"]
    seconds = doc["wall_seconds"]["mean"]
    z = result["size"]
    data = {
        "basis": {"cost_per_document_usd": cost, "seconds_per_call": seconds, "store_bytes_per_document": z["store_bytes_per_document"], "saved_result_bytes_per_document": round(z["saved_results_for_current_settings"]["bytes"] / max(1, z["saved_results_for_current_settings"]["files"]))},
        "at_500k": {
            "reading_cost_usd": round(cost * PRODUCTION),
            "reading_hours_at_4_parallel": round(seconds * PRODUCTION / 4 / 3600),
            "reading_hours_at_64_parallel": round(seconds * PRODUCTION / 64 / 3600),
            "store_gb": round(z["store_bytes_per_document"] * PRODUCTION / 1e9, 1),
            "saved_results_gb": round(z["saved_results_for_current_settings"]["bytes"] / max(1, z["saved_results_for_current_settings"]["files"]) * PRODUCTION / 1e9, 1),
        },
    }
    e = data["at_500k"]
    lines += ["## Reading every document once", ""]
    lines += ["| Estimate | Figure | From |", "|---|---|---|"]
    lines.append(f"| Cost of reading 500,000 documents with {s['model']} at {s['effort']} | ${e['reading_cost_usd']:,} | ${cost:.3f} a document, the mean over {doc['calls']} calls, times 500,000 |")
    lines.append(f"| Time, at 4 calls at a time as now | {e['reading_hours_at_4_parallel']:,} hours | {seconds:.1f} s a call, times 500,000, over 4 |")
    lines.append(f"| Time, at 64 calls at a time | {e['reading_hours_at_64_parallel']:,} hours | The same, over 64. The service's rate limits, not the code, would set the true figure |")
    lines.append(f"| Daily arrivals of 1,000 documents | ${cost * 1000:,.0f} and {seconds * 1000 / 4 / 60:.0f} minutes a day | The same figures, times 1,000 |")
    lines += ["", "## Storage", ""]
    lines += ["| Estimate | Figure | From |", "|---|---|---|"]
    lines.append(f"| The store | {e['store_gb']} GB | {z['store_bytes_per_document']:,} bytes a document, which includes the document's text |")
    lines.append(f"| The saved reading results | {e['saved_results_gb']} GB | {data['basis']['saved_result_bytes_per_document']:,} bytes a document |")
    if result.get("scale"):
        lines += ["", "## Where the code slows first", ""]
        lines += ["Section 5 of `benchmark.md` measures the queries on a store of the patient copied over. Read along a row: the timing that grows with the number of patients is the one that limits a collection, and the one that stays flat is fine. The reading of these figures is in the README.", ""]
    return "\n".join(lines) + "\n", data


def run(settings, *, documents: Path, runs: int = 5, questions: list[tuple[str, str]], live: list[tuple[str, str]] | None = None, scale: list[int] | None = None, log=None) -> dict:
    result = {
        "measured_at": now(),
        "settings": {"model": settings.model, "effort": settings.effort, "prompt_version": settings.prompt_version, "plan_prompt_version": settings.plan_prompt_version, "parallel_calls": settings.parallel_calls},
        "reading_runs": reading_runs(settings),
    }
    result["per_document"] = per_document(result["reading_runs"])
    result["plan_calls"] = plan_calls(settings)
    result["all_calls"] = all_calls(settings)
    result["replay"] = measure_replay(settings, documents, runs)
    result["rerun"] = measure_rerun(settings, documents, runs)
    result["questions"] = measure_questions(settings, questions, runs)
    if live:
        result["live"] = ask_live(settings, log or NoLog(), live, settings.answers / "related")
    result["size"] = measure_size(settings)
    if scale:
        result["scale"] = measure_scale(settings, scale)
    return result


def write(settings, result: dict) -> tuple[Path, Path]:
    settings.benchmarks.mkdir(parents=True, exist_ok=True)
    text, data = estimates(result)
    (settings.benchmarks / "benchmark.md").write_text(report(result), encoding="utf-8", newline="\n")
    (settings.benchmarks / "benchmark.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    (settings.benchmarks / "estimates.md").write_text(text, encoding="utf-8", newline="\n")
    (settings.benchmarks / "estimates.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return settings.benchmarks / "benchmark.md", settings.benchmarks / "estimates.md"
