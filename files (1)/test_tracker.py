import os
import tempfile

import pytest


@pytest.fixture(autouse=True)
def temp_db(monkeypatch):
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.remove(path)  # let sqlite create it fresh
    import config
    monkeypatch.setattr(config, "DB_PATH", path)
    import database
    database.init_db()
    yield path
    if os.path.exists(path):
        os.remove(path)


def test_no_entries_zero_streak():
    import tracker
    status = tracker.current_streak()
    assert status.days_since_last_relapse == 0
    assert status.had_relapse is False


def test_checkin_without_relapse_counts_from_start():
    import tracker
    tracker.log_checkin("feeling okay")
    status = tracker.current_streak()
    assert status.had_relapse is False
    assert status.days_since_last_relapse >= 0


def test_relapse_resets_streak_flag():
    import tracker
    tracker.log_checkin("day 1")
    tracker.log_relapse("slipped today")
    status = tracker.current_streak()
    assert status.had_relapse is True
    assert status.days_since_last_relapse == 0


def test_urge_logging_stores_intensity_and_note():
    import database
    import tracker
    tracker.log_urge(intensity=7, note="saw an ad", coping_used="called a friend")
    entries = database.recent_entries(limit=5)
    assert len(entries) == 1
    assert entries[0]["entry_type"] == "urge"
    assert entries[0]["intensity"] == 7
    assert entries[0]["note"] == "saw an ad"


def test_counts_by_type():
    import database
    import tracker
    tracker.log_checkin()
    tracker.log_urge()
    tracker.log_urge()
    tracker.log_relapse()
    counts = database.counts_by_type()
    assert counts["checkin"] == 1
    assert counts["urge"] == 2
    assert counts["relapse"] == 1
