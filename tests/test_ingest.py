"""Stage 1: files are registered once, copies are skipped, and a restart finds the same store."""

import shutil

from backbone import ingest, store
from conftest import DOCUMENTS


def test_all_supplied_documents_are_registered(connection, log):
    outcome = ingest.register(connection, DOCUMENTS, log)
    assert len(outcome["new"]) == 31
    assert outcome["duplicate"] == []
    assert outcome["unreadable"] == []
    assert connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0] == 31


def test_the_store_has_the_eight_tables(connection):
    names = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    assert set(store.TABLES) <= names
    assert len(store.TABLES) == 8


def test_a_copy_of_a_file_changes_nothing(connection, log, tmp_path):
    folder = tmp_path / "documents"
    shutil.copytree(DOCUMENTS, folder)
    ingest.register(connection, folder, log)
    before = store.dump(connection)

    first = sorted(folder.iterdir())[0]
    shutil.copy(first, folder / "a_copy_under_another_name.txt")
    outcome = ingest.register(connection, folder, log)

    assert outcome["new"] == []
    assert len(outcome["duplicate"]) == 32
    assert store.dump(connection) == before


def test_a_restart_finds_the_same_store(settings, log):
    first = store.connect(settings.store)
    ingest.register(first, DOCUMENTS, log)
    before = store.dump(first)
    first.close()

    second = store.connect(settings.store)
    outcome = ingest.register(second, DOCUMENTS, log)
    assert outcome["new"] == []
    assert store.dump(second) == before
    second.close()


def test_text_is_stored_as_utf8(connection, log):
    ingest.register(connection, DOCUMENTS, log)
    texts = [row["text"] for row in connection.execute("SELECT text FROM documents")]
    assert any("–" in text for text in texts), "an en dash between two times should survive"
    assert not any("�" in text for text in texts)
    assert not any("â€" in text for text in texts), "UTF-8 read as another encoding"


def test_a_file_that_is_not_utf8_is_recorded_as_not_read(connection, log, settings, tmp_path):
    folder = tmp_path / "documents"
    folder.mkdir()
    (folder / "latin1.txt").write_bytes("Café visit 10:00".encode("latin-1"))
    outcome = ingest.register(connection, folder, log)
    assert outcome["unreadable"] == ["latin1.txt"]
    row = connection.execute("SELECT read_status, read_error FROM documents").fetchone()
    assert row["read_status"] == "failed"
    assert "not UTF-8" in row["read_error"]
    assert ingest.waiting(connection, settings) == []


def test_documents_wait_until_read_and_can_be_picked_by_name(connection, log, settings):
    ingest.register(connection, DOCUMENTS, log)
    assert len(ingest.waiting(connection, settings)) == 31
    assert len(ingest.waiting(connection, settings, only=["D103", "D108"])) == 2
