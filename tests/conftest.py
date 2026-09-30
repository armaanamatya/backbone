"""Shared set-up for the checks. No check here calls a model."""

from __future__ import annotations

import dataclasses
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from backbone import settings as settings_file  # noqa: E402
from backbone import store  # noqa: E402
from backbone.logs import NoLog  # noqa: E402

DOCUMENTS = ROOT / "documents"

# A made-up document. Nothing in it comes from the supplied documents.
MADE_UP = """Document ID: ZZ-D900
Northfield Clinic | Counselling note
Patient: Jamie Hale | DOB: 1980-02-03 | MRN: NF-P001
Encounter NF-E500 | Service date 2025-03-04
Booked slot 15:00–15:50. Mr Hale came in at 15:12.

Mr Hale said he had eaten little all week. Appetite remains poor.
The session paused from 15:30 to 15:35 for a fire drill; no counselling took place.

Signed: Dana Ortiz, LPC | March 4, 2025, 16:40
"""


@pytest.fixture
def settings(tmp_path):
    """The settings of the project, with everything written under a temporary folder."""
    loaded = settings_file.load()
    return dataclasses.replace(
        loaded,
        store=tmp_path / "abstraction.sqlite",
        readings=tmp_path / "readings",
        logs=tmp_path / "logs",
        answers=tmp_path / "answers",
        benchmarks=tmp_path / "benchmarks",
        export=tmp_path / "abstraction.md",
    )


@pytest.fixture
def connection(settings):
    opened = store.connect(settings.store)
    yield opened
    opened.close()


@pytest.fixture
def log():
    return NoLog()


def no_model(*arguments, **named):
    raise AssertionError("a model was called")


def replay(folder, *, prompt_version=None, effort=None, order=None, batches=None):
    """Fills an empty store from the saved results of the full read, with no
    model. `order` sorts the files. `batches` splits them into several runs."""
    import dataclasses as _dataclasses

    from backbone import ingest, reader

    loaded = settings_file.load()
    chosen = _dataclasses.replace(
        loaded,
        store=folder / "abstraction.sqlite",
        logs=folder / "logs",
        prompt_version=prompt_version or loaded.prompt_version,
        effort=effort or loaded.effort,
    )
    connection = store.connect(chosen.store)
    files = sorted(DOCUMENTS.iterdir(), key=order) if order else sorted(DOCUMENTS.iterdir())
    runs = batches(files) if batches else [files]
    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(reader, "call_model", no_model)
        for run in runs:
            patch.setattr(ingest, "files_in", lambda _folder, run=run: run)
            ingest.register(connection, DOCUMENTS, NoLog())
            ingest.read_waiting(connection, chosen, NoLog())
    return connection


@pytest.fixture(scope="session")
def full_read(tmp_path_factory):
    """The store as the saved results of the full read give it."""
    connection = replay(tmp_path_factory.mktemp("full_read"))
    yield connection
    connection.close()


QUESTIONS = {entry["id"]: entry["question"] for entry in json.loads((ROOT / "questions.json").read_text(encoding="utf-8"))}
PROBLEMS = {entry["id"]: entry["question"] for entry in json.loads((ROOT / "tests" / "problem_questions.json").read_text(encoding="utf-8"))}


@pytest.fixture(scope="session")
def answers(full_read):
    """Every answer, from the saved plans, against the replayed store. The
    plans the model returned are read from `output/answers/plans`, the same
    way saved reading results are. No model is called."""
    from backbone import ask

    loaded = settings_file.load()
    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(ask.reader, "call_model", no_model)
        built = {}
        for question_id, question in {**QUESTIONS, **PROBLEMS}.items():
            built[question_id] = ask.answer(full_read, loaded, NoLog(), question, question_id)
    return built
