"""Stage 3: the saved results of the full read are replayed into an empty store.

No model is called. These checks fail if a saved result is missing for the
current model, effort and prompt version, which means the documents need
reading again.
"""

from backbone import quotes, reader, settings as settings_file, store
from conftest import replay


def test_every_document_is_read_from_a_saved_result(full_read):
    assert full_read.execute("SELECT COUNT(*) FROM documents WHERE read_status = 'read'").fetchone()[0] == 31


def test_every_quote_is_found_in_its_source(full_read):
    rows = full_read.execute(
        "SELECT c.quote, c.line, c.quote_status, d.text FROM claims c JOIN documents d USING (doc_hash)"
    ).fetchall()
    assert rows
    for row in rows:
        assert row["quote_status"] in (quotes.VERIFIED, quotes.LINE_CORRECTED)
        assert row["quote"] in quotes.split_lines(row["text"])[row["line"] - 1]


def test_every_document_gives_at_least_one_claim(full_read):
    empty = full_read.execute(
        "SELECT file_name FROM documents d WHERE NOT EXISTS"
        " (SELECT 1 FROM claims c WHERE c.doc_hash = d.doc_hash)"
    ).fetchall()
    assert [row["file_name"] for row in empty] == []


def test_every_claim_carries_a_patient_and_a_version(full_read):
    bad = full_read.execute(
        "SELECT COUNT(*) FROM claims WHERE patient_key IS NULL OR patient_key = ?"
        " OR model IS NULL OR prompt_version IS NULL",
        (reader.UNIDENTIFIED,),
    ).fetchone()[0]
    assert bad == 0


def test_every_row_of_a_conclusion_carries_the_patient(full_read):
    for table in store.CONCLUDES_TABLES:
        rows = full_read.execute(f"SELECT patient_key FROM {table}").fetchall()
        assert rows, table
        assert {row["patient_key"] for row in rows} == {"HG-M042"}, table


def test_a_replay_gives_the_same_store_as_the_one_on_disk(full_read):
    on_disk = store.connect(settings_file.load().store)
    try:
        assert store.dump(full_read) == store.dump(on_disk)
    finally:
        on_disk.close()


def test_a_restart_answers_with_no_reading_call(tmp_path):
    """Check 5: a second process finds the store filled and reads nothing."""
    first = replay(tmp_path)
    before = store.dump(first)
    first.close()
    second = replay(tmp_path)
    try:
        assert store.dump(second) == before
    finally:
        second.close()
