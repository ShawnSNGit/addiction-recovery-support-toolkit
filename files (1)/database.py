"""
Local, private SQLite journal. Nothing here is shared or synced anywhere -
it's a single file on your own machine.
"""
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import List, Optional

import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_type TEXT NOT NULL CHECK(entry_type IN ('checkin', 'urge', 'relapse')),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    intensity INTEGER,       -- 1-10, optional, mainly for 'urge' entries
    note TEXT,               -- free-text: trigger, feelings, context
    coping_used TEXT         -- what they did about it, if anything
);
CREATE INDEX IF NOT EXISTS idx_entries_type ON entries(entry_type);
CREATE INDEX IF NOT EXISTS idx_entries_timestamp ON entries(timestamp);
"""


@contextmanager
def get_connection():
    conn = sqlite3.connect(config.DB_PATH, timeout=30)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    with get_connection() as conn:
        conn.executescript(SCHEMA)


def add_entry(entry_type: str, note: str = "", intensity: Optional[int] = None,
              coping_used: str = "") -> int:
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO entries (entry_type, intensity, note, coping_used) VALUES (?, ?, ?, ?)",
            (entry_type, intensity, note, coping_used),
        )
        return cur.lastrowid


def last_relapse_timestamp() -> Optional[str]:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT timestamp FROM entries WHERE entry_type = 'relapse' "
            "ORDER BY timestamp DESC LIMIT 1"
        ).fetchone()
        return row["timestamp"] if row else None


def first_entry_timestamp() -> Optional[str]:
    with get_connection() as conn:
        row = conn.execute("SELECT MIN(timestamp) AS ts FROM entries").fetchone()
        return row["ts"] if row and row["ts"] else None


def recent_entries(limit: int = 20) -> List[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM entries ORDER BY timestamp DESC LIMIT ?", (limit,)
        ).fetchall()
        return [dict(r) for r in rows]


def counts_by_type() -> dict:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT entry_type, COUNT(*) AS n FROM entries GROUP BY entry_type"
        ).fetchall()
        return {r["entry_type"]: r["n"] for r in rows}
