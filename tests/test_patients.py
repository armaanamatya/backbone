"""Two made-up patients in one store. Neither may reach the other's rows, and
a claim whose quote was not found may not reach a count."""

from backbone import ingest, store
from made_up import DAY, Record


def put(connection, record, name):
    """Stores the claims of a made-up record as one read document."""
    doc_hashes = sorted({claim["doc_hash"] for claim in record.claims})
    for doc_hash in doc_hashes:
        store.register_document(
            connection, doc_hash=doc_hash, file_name=f"{name}-{doc_hash[:6]}.txt", byte_size=1, line_count=1,
            text="made up", registered_at="2025-03-04T00:00:00+00:00",
        )
        header = {
            "declared_id": f"{name}-{doc_hash[:6]}",
            "kinds": [record.sections[(doc_hash, 1)]["kind"]],
            "patient_key": record.patient,
            "patient_name": name,
            "patient_dob": None,
            "patient_record_number": record.patient,
            "sections": [record.sections[(doc_hash, 1)]],
            "not_captured": {"values": 0, "counts": {}, "listed": []},
        }
        claims = [
            {**claim, "invalid_reason": None, "valid": bool(claim["valid"])}
            for claim in record.claims
            if claim["doc_hash"] == doc_hash
        ]
        store.save_reading(
            connection, doc_hash, header, claims, model="none", effort="none", prompt_version=0,
            read_at="2025-03-04T00:00:00+00:00",
        )


def one_session(patient, number, start, end):
    record = Record(patient)
    record.document("plan", kind="plan", signed="2025-03-03T13:00").plan(days=1, minutes=45)
    record.document("note").contact(number, service="individual_therapy").present(start, end)
    return record


def test_one_patient_never_reaches_another_patients_rows(connection, log):
    put(connection, one_session("NF-P001", "NF-E1", "10:00", "10:50"), "first")
    put(connection, one_session("NF-P002", "NF-E1", "14:00", "14:30"), "second")
    for patient in store.patients(connection):
        ingest.conclude(connection, patient, log)

    first = store.rows_of(connection, "contacts", "NF-P001")
    second = store.rows_of(connection, "contacts", "NF-P002")
    assert [row["minutes"][0]["minutes"] for row in first] == [50]
    assert [row["minutes"][0]["minutes"] for row in second] == [30]
    assert first[0]["contact_id"] != second[0]["contact_id"], "the same encounter number, two patients"

    weeks = {
        patient: [row["verdict"] for row in store.rows_of(connection, "weekly_status", patient) if row["week_start"] == "2025-03-03"]
        for patient in ("NF-P001", "NF-P002")
    }
    assert weeks == {"NF-P001": ["met"], "NF-P002": ["not_met"]}
    for table in store.CONCLUDES_TABLES:
        for row in connection.execute(f"SELECT * FROM {table}"):
            other = "NF-P002" if row["patient_key"] == "NF-P001" else "NF-P001"
            assert other not in " ".join(str(value) for value in tuple(row))


def test_rebuilding_one_patient_leaves_the_other_untouched(connection, log):
    put(connection, one_session("NF-P001", "NF-E1", "10:00", "10:50"), "first")
    put(connection, one_session("NF-P002", "NF-E1", "14:00", "14:30"), "second")
    for patient in store.patients(connection):
        ingest.conclude(connection, patient, log)
    before = store.rows_of(connection, "contacts", "NF-P002")
    ingest.conclude(connection, "NF-P001", log)
    assert store.rows_of(connection, "contacts", "NF-P002") == before


def test_a_claim_whose_quote_was_not_found_is_not_used_in_a_count(connection, log):
    record = one_session("NF-P001", "NF-E1", "10:00", "10:50")
    record.document("second note").contact("NF-E2", date="2025-03-05", service="individual_therapy").present("09:00", "09:40")
    for claim in record.claims:
        if claim["document"] == "second note" and claim["type"] == "time":
            claim["quote_status"] = "unverified"
    put(connection, record, "first")
    ingest.conclude(connection, "NF-P001", log)
    contacts = {row["encounter_id"]: row for row in store.rows_of(connection, "contacts", "NF-P001")}
    assert contacts["NF-E2"]["status"] == "not_established", "nothing that was verified says the patient attended"
    assert contacts["NF-E2"]["minutes"] == []
    week = store.rows_of(connection, "weekly_status", "NF-P001", "week_start")[0]
    assert week["minutes"][0]["minutes"] == 50
    assert week["days"][0]["days"] == 1
    kept = connection.execute("SELECT COUNT(*) FROM claims WHERE quote_status = 'unverified'").fetchone()[0]
    assert kept == 1
    assert DAY
