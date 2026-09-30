"""The commands. Run as `python -m backbone <command>`."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import json

from . import ask, benchmark, checks, compare, export, functions, ingest, settings as settings_file, store, trace
from .logs import RunLog


def _settings(arguments):
    return settings_file.load(Path(arguments.settings) if arguments.settings else None)


def run_ingest(arguments) -> int:
    settings = _settings(arguments)
    folder = Path(arguments.folder)
    if not folder.exists():
        print(f"No such file or folder: {folder}")
        return 2
    log = RunLog(settings.logs, "ingest")
    connection = store.connect(settings.store)
    outcome = ingest.register(connection, folder, log)
    print(
        f"Files: {len(outcome['new'])} new, {len(outcome['duplicate'])} already in the store,"
        f" {len(outcome['unreadable'])} not readable as UTF-8."
    )
    if len(outcome["duplicate"]) <= 5:
        for name in outcome["duplicate"]:
            print(f"  skipped, same content already stored: {name}")
    for name in outcome["unreadable"]:
        print(f"  not readable: {name}")

    if arguments.register_only:
        rows = ingest.waiting(connection, settings, arguments.only)
        print(f"Registered only. {len(rows)} documents wait to be read.")
    else:
        summaries = ingest.read_waiting(connection, settings, log, arguments.only)
        calls = cost = 0
        for summary in summaries:
            if summary["status"] != "read":
                print(f"  NOT READ {summary['file']}: {'; '.join(summary['errors'][:3])}")
                continue
            source = "saved result" if summary["reused"] else f"{summary['attempts']} call(s)"
            print(
                f"  read {summary['declared_id'] or '?':8} {summary['file']}: {summary['claims']} claims,"
                f" {summary['unverified_quotes']} quotes not found, {summary['invalid_claims']} invalid,"
                f" {summary['coverage']['not_captured']} values not captured ({source})"
            )
            if not summary["reused"]:
                for usage in summary["usage"]:
                    if usage:
                        calls += 1
                        cost += usage.get("cost_usd") or 0
        print(f"Documents read this run: {len(summaries)}. Model calls: {calls}. Reported cost: ${cost:.4f}.")

    total = connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    read = connection.execute("SELECT COUNT(*) FROM documents WHERE read_status = 'read'").fetchone()[0]
    print(f"Store: {total} documents, {read} read. Log: {log.path.name}")
    log.event("run_finished", documents=total, read=read)
    connection.close()
    return 0


def run_rebuild(arguments) -> int:
    settings = _settings(arguments)
    log = RunLog(settings.logs, "rebuild")
    connection = store.connect(settings.store)
    for patient_key in store.patients(connection):
        sizes = ingest.conclude(connection, patient_key, log)
        print(f"{patient_key}: " + ", ".join(f"{count} {table.replace('_', ' ')}" for table, count in sizes.items()))
    connection.commit()
    connection.close()
    return 0


def run_ask(arguments) -> int:
    settings = _settings(arguments)
    log = RunLog(settings.logs, "ask")
    connection = store.connect(settings.store)
    questions = []
    if arguments.file:
        for entry in json.loads(Path(arguments.file).read_text(encoding="utf-8")):
            questions.append((entry.get("id"), entry["question"]))
    if arguments.question:
        questions.append((arguments.id, arguments.question))
    if not questions:
        print("Give a question, or --file with a list of questions.")
        return 2
    settings.answers.mkdir(parents=True, exist_ok=True)
    for number, (question_id, question) in enumerate(questions, start=1):
        built = ask.answer(connection, settings, log, question, question_id)
        name = question_id or f"question-{ask.Model(settings, log).saved_path(question).name[:16]}"
        (settings.answers / f"{name}.json").write_text(json.dumps(built, ensure_ascii=False, indent=1), encoding="utf-8")
        (settings.answers / f"{name}.md").write_text(built["text"], encoding="utf-8", newline="\n")
        if not arguments.quiet:
            print(built["text"])
        print(f"[{name}: plan {built['plan_source']}, {len(built['results'])} function calls; written to {settings.answers / (name + '.md')}]")
    connection.close()
    return 0


def run_call(arguments) -> int:
    settings = _settings(arguments)
    connection = store.connect(settings.store)
    given = {name: getattr(arguments, name) for name in ("patient", "start", "end", "date", "on", "group_by", "instrument", "topic", "speaker", "weeks", "first_start", "first_end", "second_start", "second_end") if getattr(arguments, name, None) is not None}
    if given.get("patient"):
        who = functions.resolve_patient(connection, given["patient"])
        if who["status"] != "found":
            print(json.dumps(who, ensure_ascii=False, indent=1))
            return 1
        given["patient"] = who["patient"]
    try:
        result = functions.call(connection, arguments.function, given)
    except (KeyError, TypeError) as error:
        print(f"Cannot run: {error}")
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=1))
    connection.close()
    return 0


def run_trace(arguments) -> int:
    settings = _settings(arguments)
    connection = store.connect(settings.store)
    print(trace.follow(connection, arguments.what, arguments.value))
    connection.close()
    return 0


def run_compare(arguments) -> int:
    result = compare.compare(arguments.settings_files)
    text = compare.report(result)
    if arguments.out:
        Path(arguments.out).write_text(text, encoding="utf-8", newline="\n")
        Path(arguments.out).with_suffix(".json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"Written: {arguments.out}")
    else:
        print(text)
    return 0


def run_export(arguments) -> int:
    settings = _settings(arguments)
    connection = store.connect(settings.store)
    export.write(connection, settings.export)
    connection.close()
    print(f"Written: {settings.export}")
    return 0


def run_check(arguments) -> int:
    """The checks on the store and the answers on disk, then the test suite."""
    settings = _settings(arguments)
    failed = 0
    connection = store.connect(settings.store)
    print(f"Store: {settings.store}")
    for name, check in checks.STORE_CHECKS.items():
        problems = check(connection)
        failed += bool(problems)
        print(f"  {'pass' if not problems else 'FAIL'}  {name}" + (f": {len(problems)} problem(s)" if problems else ""))
        for problem in problems[: arguments.show]:
            print(f"        {problem}")
    connection.close()
    answers = sorted(p for p in settings.answers.rglob("*.json") if "plans" not in p.parts) if settings.answers.exists() else []
    print(f"Answers: {len(answers)} in {settings.answers}")
    for name, check in checks.ANSWER_CHECKS.items():
        problems = []
        for path in answers:
            built = json.loads(path.read_text(encoding="utf-8"))
            if "parts" in built:
                problems += check(built)
        failed += bool(problems)
        print(f"  {'pass' if not problems else 'FAIL'}  {name}" + (f": {len(problems)} problem(s)" if problems else ""))
        for problem in problems[: arguments.show]:
            print(f"        {problem}")
    if arguments.no_tests:
        return 1 if failed else 0
    print("Tests: python -m pytest tests -q")
    try:
        import pytest  # noqa: F401
    except ImportError:
        print("  pytest is not installed. Install it with: python -m pip install pytest")
        return 1
    import subprocess

    done = subprocess.run([sys.executable, "-m", "pytest", str(settings.root / "tests"), "-q"], cwd=settings.root)
    return 1 if failed or done.returncode else 0


def _questions_from(path: Path) -> list[tuple[str, str]]:
    return [(entry.get("id"), entry["question"]) for entry in json.loads(path.read_text(encoding="utf-8"))]


def run_benchmark(arguments) -> int:
    settings = _settings(arguments)
    documents = Path(arguments.documents)
    questions = _questions_from(settings.root / "questions.json")
    problems = settings.root / "tests" / "problem_questions.json"
    if problems.exists():
        questions += _questions_from(problems)
    live = _questions_from(Path(arguments.live)) if arguments.live else None
    scale = None if arguments.no_scale else [int(n) for n in arguments.scale.split(",")]
    log = RunLog(settings.logs, "benchmark") if live else None
    result = benchmark.run(settings, documents=documents, runs=arguments.runs, questions=questions, live=live, scale=scale, log=log)
    measured, estimated = benchmark.write(settings, result)
    print(benchmark.report(result))
    print(f"Written: {measured} and {estimated}, with a .json beside each.")
    return 0


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(prog="backbone", description=__doc__)
    parser.add_argument("--settings", help="path to a settings file; default is settings.toml")
    commands = parser.add_subparsers(dest="command", required=True)

    command = commands.add_parser("ingest", help="read new documents and update the abstraction")
    command.add_argument("folder", help="a folder of documents, or one file")
    command.add_argument("--register-only", action="store_true", help="hash and store the files; call no model")
    command.add_argument("--only", nargs="+", metavar="TEXT", help="read only files whose name contains one of these")
    command.set_defaults(run=run_ingest)

    command = commands.add_parser("rebuild", help="work out the conclusions again from the stored claims; calls no model")
    command.set_defaults(run=run_rebuild)

    command = commands.add_parser("export", help="write the abstraction in readable form")
    command.set_defaults(run=run_export)

    command = commands.add_parser("ask", help="answer a question in the nine-part format")
    command.add_argument("question", nargs="?", help="the question")
    command.add_argument("--id", help="a name for the answer files")
    command.add_argument("--file", help="a JSON list of {id, question}, such as questions.json")
    command.add_argument("--quiet", action="store_true", help="write the answers without printing them")
    command.set_defaults(run=run_ask)

    command = commands.add_parser("call", help="run one function and print its result; calls no model")
    command.add_argument("function", choices=sorted(functions.CATALOGUE))
    for name in ("patient", "start", "end", "date", "on", "group_by", "instrument", "topic", "speaker", "first_start", "first_end", "second_start", "second_end"):
        command.add_argument(f"--{name.replace('_', '-')}", dest=name)
    command.add_argument("--weeks", type=int)
    command.set_defaults(run=run_call)

    command = commands.add_parser("trace", help="follow a figure back to contacts, claims and source lines; calls no model")
    command.add_argument("what", choices=["contact", "week", "conflict", "claim", "assessment", "finding"])
    command.add_argument("value", help="an encounter number, a week start date, a conflict or claim id, an assessment date")
    command.set_defaults(run=run_trace)

    command = commands.add_parser("compare", help="compare reads by different models or efforts; the first settings file is the baseline; calls no model")
    command.add_argument("settings_files", nargs="+", help="settings files whose stores were filled by ingest")
    command.add_argument("--out", help="write the report here, with a .json beside it")
    command.set_defaults(run=run_compare)

    command = commands.add_parser("check", help="run the checks on the store and the answers, then the test suite; calls no model")
    command.add_argument("--no-tests", action="store_true", help="skip the test suite")
    command.add_argument("--show", type=int, default=5, help="how many problems to print per check")
    command.set_defaults(run=run_check)

    command = commands.add_parser("benchmark", help="measure times, sizes, tokens and cost; calls a model only with --live")
    command.add_argument("--documents", default="documents", help="the folder of documents; default documents/")
    command.add_argument("--runs", type=int, default=5, help="how many times each code timing is repeated")
    command.add_argument("--live", help="a JSON list of {id, question} to ask end to end, plan call included")
    command.add_argument("--scale", default="1,10,100,1000", help="patient counts for the synthetic scale run")
    command.add_argument("--no-scale", action="store_true", help="skip the synthetic scale run")
    command.set_defaults(run=run_benchmark)

    arguments = parser.parse_args(argv)
    return arguments.run(arguments)
