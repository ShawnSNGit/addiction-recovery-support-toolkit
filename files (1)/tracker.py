"""
Streak tracking. A "slip"/relapse doesn't erase your history - it's logged,
the streak resets, and you keep going. Recovery isn't graded on being
perfect; it's graded on continuing.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

import database


@dataclass
class StreakStatus:
    days_since_start: int          # days since the very first journal entry
    days_since_last_relapse: int   # current streak
    had_relapse: bool


def _parse_ts(ts_str: str) -> datetime:
    # SQLite CURRENT_TIMESTAMP is "YYYY-MM-DD HH:MM:SS" in UTC.
    dt = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    return dt.replace(tzinfo=timezone.utc)


def current_streak() -> StreakStatus:
    now = datetime.now(timezone.utc)

    first_ts = database.first_entry_timestamp()
    days_since_start = (now - _parse_ts(first_ts)).days if first_ts else 0

    last_relapse = database.last_relapse_timestamp()
    if last_relapse:
        days_since_last_relapse = (now - _parse_ts(last_relapse)).days
        had_relapse = True
    else:
        days_since_last_relapse = days_since_start
        had_relapse = False

    return StreakStatus(
        days_since_start=days_since_start,
        days_since_last_relapse=days_since_last_relapse,
        had_relapse=had_relapse,
    )


def log_checkin(note: str = "") -> int:
    return database.add_entry("checkin", note=note)


def log_urge(intensity: Optional[int] = None, note: str = "", coping_used: str = "") -> int:
    return database.add_entry("urge", note=note, intensity=intensity, coping_used=coping_used)


def log_relapse(note: str = "") -> int:
    """Logging a relapse is not a judgment - it's data. Showing up to log it
    honestly is itself a recovery behavior worth recognizing."""
    return database.add_entry("relapse", note=note)
