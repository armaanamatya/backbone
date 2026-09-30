"""Stage 2, the parts that need no model: the schema, the quote check, the
coverage check, and turning a result into claims. The result used here was
written by hand for a made-up document."""

import copy

from backbone import coverage, ingest, quotes, reader, store
from backbone.reading_schema import CLAIM_LISTS, validate
from conftest import MADE_UP

LINES = quotes.split_lines(MADE_UP)


def cited(section=1, contact="c1", **fields):
    return {"section": section, "contact": contact, **fields}


def made_up_reading():
    reading = {
        "document": {
            "declared_id": "ZZ-D900",
            "organization": "Northfield Clinic",
            "patient_name": "Jamie Hale",
            "patient_dob": "1980-02-03",
            "patient_record_number": "NF-P001",
        },
        "sections": [
            {
                "id": 1,
                "heading": None,
                "kind": "clinical_note",
                "kind_as_written": "Counselling note",
                "first_line": 1,
                "last_line": 10,
                "author_name": "Dana Ortiz",
                "author_role": "LPC",
                "signature": "signed",
                "signed_by": "Dana Ortiz, LPC",
                "signed_date": "2025-03-04",
                "signed_time": "16:40",
                "signature_line": 10,
                "is_copy": False,
                "dates": [
                    {"kind": "service", "date": "2025-03-04", "quote": "Service date 2025-03-04", "line": 4}
                ],
            }
        ],
        **{name: [] for name in CLAIM_LISTS},
    }
    reading["contacts"] = [
        {
            "section": 1,
            "ref": "c1",
            "encounter_id": "NF-E500",
            "appointment_id": None,
            "service_date": "2025-03-04",
            "service_as_written": "Counselling",
            "service_class": "individual_therapy",
            "quote": "Encounter NF-E500",
            "line": 4,
        }
    ]
    reading["times"] = [
        cited(what="contact_interval", start="15:00", end="15:50", label="scheduled",
              position="header", quote="Booked slot 15:00–15:50.", line=5),
        cited(what="patient_arrival", start="15:12", end=None, label="actual",
              position="header", quote="Mr Hale came in at 15:12.", line=5),
        cited(what="no_therapy_interval", start="15:30", end="15:35", label="actual",
              position="body", detail="fire drill",
              quote="The session paused from 15:30 to 15:35 for a fire drill", line=8),
    ]
    reading["observations"] = [
        cited(date="2025-03-04", speaker="patient", topic="other", summary="Ate little",
              quote="Mr Hale said he had eaten little all week.", line=7),
        cited(date="2025-03-04", speaker="clinician", topic="other", summary="Poor appetite",
              quote="Appetite remains poor.", line=7),
    ]
    return reading


def test_the_made_up_result_fits_the_schema():
    assert validate(made_up_reading()) == []
    assert reader.problems_in(made_up_reading(), len(LINES)) == []


def test_the_schema_rejects_a_malformed_result():
    reading = made_up_reading()
    reading["times"][0]["start"] = "3pm"
    reading["times"][1]["label"] = "probably"
    del reading["observations"][0]["quote"]
    reading["surprise"] = 1
    errors = validate(reading)
    assert len(errors) == 4


def test_references_that_point_nowhere_are_rejected():
    reading = made_up_reading()
    reading["times"][0]["contact"] = "c9"
    reading["times"][1]["section"] = 4
    reading["observations"][0]["line"] = 99
    assert len(reader.problems_in(reading, len(LINES))) == 3


def test_a_quote_is_found_only_when_copied_exactly():
    assert quotes.locate(LINES, "Appetite remains poor.", 7) == (7, quotes.VERIFIED)
    assert quotes.locate(LINES, "Appetite remains poor.", 2) == (7, quotes.LINE_CORRECTED)
    assert quotes.locate(LINES, "7| Appetite remains poor.", 7) == (7, quotes.VERIFIED)
    assert quotes.locate(LINES, "Appetite remained poor.", 7) == (7, quotes.UNVERIFIED)
    assert quotes.locate(LINES, "Booked slot 15:00-15:50.", 5)[1] == quotes.UNVERIFIED, "a hyphen is not an en dash"
    assert quotes.locate(LINES, "", 5)[1] == quotes.UNVERIFIED


def test_claims_carry_the_contact_and_the_patient():
    header, claims = reader.to_claims(made_up_reading(), "a" * 64, LINES)
    assert header["patient_key"] == "NF-P001"
    assert header["kinds"] == ["clinical_note"]
    assert len(claims) == 6
    assert len({claim["claim_id"] for claim in claims}) == 6
    for claim in claims:
        assert claim["encounter_id"] == "NF-E500"
        assert claim["service_date"] == "2025-03-04"
        assert claim["quote_status"] == quotes.VERIFIED
        assert claim["valid"]
    arrival = next(claim for claim in claims if claim["value"].get("what") == "patient_arrival")
    assert arrival["time_label"] == "actual"


def test_an_end_before_a_start_makes_a_claim_invalid():
    reading = made_up_reading()
    reading["times"][0]["start"], reading["times"][0]["end"] = "15:50", "15:00"
    _, claims = reader.to_claims(reading, "a" * 64, LINES)
    invalid = [claim for claim in claims if not claim["valid"]]
    assert len(invalid) == 1
    assert invalid[0]["invalid_reason"] == "the end is before the start"


def test_a_patient_with_no_record_number_is_known_by_name_and_birth_date():
    document = {"patient_name": "Jamie  Hale", "patient_dob": "1980-02-03", "patient_record_number": None}
    assert reader.patient_key(document) == "jamie hale|1980-02-03"
    assert reader.patient_key({}) == reader.UNIDENTIFIED


def test_coverage_passes_when_every_value_is_in_a_claim():
    reading = made_up_reading()
    reading["sections"][0]["dates"].append(
        {"kind": "signed", "date": "2025-03-04", "time": "16:40", "quote": "March 4, 2025, 16:40", "line": 10}
    )
    result = coverage.check(LINES, reading)
    assert result["counts"][coverage.NOT_CAPTURED] == 0
    assert result["counts"][coverage.QUOTED_ONLY] == 0


def test_coverage_lists_a_value_that_is_in_no_claim():
    reading = copy.deepcopy(made_up_reading())
    reading["times"] = [item for item in reading["times"] if item["what"] != "no_therapy_interval"]
    result = coverage.check(LINES, reading)
    missed = {(row["line"], row["value"]) for row in result["listed"] if row["status"] == coverage.NOT_CAPTURED}
    assert missed == {(8, "15:30"), (8, "15:35")}


def test_coverage_tells_a_quoted_value_from_a_captured_one():
    reading = made_up_reading()
    reading["times"][1]["start"] = None
    reading["times"][1]["end"] = "15:50"
    result = coverage.check(LINES, reading)
    quoted = [row for row in result["listed"] if row["status"] == coverage.QUOTED_ONLY]
    assert [(row["line"], row["value"]) for row in quoted] == [(5, "15:12")]


def test_the_document_reaches_the_model_as_numbered_data():
    message = reader.build_message(["first", "second"])
    assert "<document>\n1| first\n2| second\n</document>" in message
    again = reader.build_message(["first"], ["result.times[0].start: bad"])
    assert "rejected" in again and "result.times[0].start: bad" in again


def saved_result(settings, doc_hash, reading):
    """Puts a result where a model call would have saved it."""
    path = reader.saved_path(settings, doc_hash)
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "doc_hash": doc_hash,
        "file_name": "made_up.txt",
        "model": settings.model,
        "effort": settings.effort,
        "prompt_version": settings.prompt_version,
        "read_at": "2025-03-05T00:00:00+00:00",
        "status": "read",
        "attempts": [],
        "reading": reading,
    }
    path.write_text(store.to_json(record), encoding="utf-8")


def test_a_saved_result_is_used_and_no_model_is_called(settings, connection, log, tmp_path, monkeypatch):
    folder = tmp_path / "documents"
    folder.mkdir()
    (folder / "made_up.txt").write_bytes(MADE_UP.encode("utf-8"))
    ingest.register(connection, folder, log)
    doc_hash = ingest.hash_bytes(MADE_UP.encode("utf-8"))
    saved_result(settings, doc_hash, made_up_reading())

    def no_call(*arguments, **named):
        raise AssertionError("a model was called")

    monkeypatch.setattr(reader, "call_model", no_call)
    summaries = ingest.read_waiting(connection, settings, log)

    assert [summary["status"] for summary in summaries] == ["read"]
    assert summaries[0]["reused"] is True
    assert connection.execute("SELECT COUNT(*) FROM claims").fetchone()[0] == 6
    patients = {row[0] for row in connection.execute("SELECT patient_key FROM claims")}
    assert patients == {"NF-P001"}
    assert ingest.waiting(connection, settings) == []


def test_a_document_that_fails_twice_is_recorded_as_not_read(settings, connection, log, tmp_path, monkeypatch):
    folder = tmp_path / "documents"
    folder.mkdir()
    (folder / "made_up.txt").write_bytes(MADE_UP.encode("utf-8"))
    ingest.register(connection, folder, log)
    messages = []

    def broken(settings, message):
        messages.append(message)
        return {"structured_output": {"document": {}}, "usage": {}, "total_cost_usd": 0.0}

    monkeypatch.setattr(reader, "call_model", broken)
    summaries = ingest.read_waiting(connection, settings, log)

    assert len(messages) == 2, "one retry, and no more"
    assert "rejected" in messages[1], "the error is shown to the model on the retry"
    assert summaries[0]["status"] == "failed"
    row = connection.execute("SELECT read_status, read_error FROM documents").fetchone()
    assert row["read_status"] == "failed" and row["read_error"]
    assert not list(settings.readings.glob("*.json")), "a failed read is not saved"
