"""Writes one line per event, as JSON, to one log file per run."""

from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


class RunLog:
    def __init__(self, directory: Path, command: str):
        directory.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        self.path = directory / f"{stamp}_{command}.jsonl"
        self._lock = threading.Lock()
        self.event("run_started", command=command)

    def event(self, name: str, **fields) -> None:
        line = json.dumps({"at": now(), "event": name, **fields}, ensure_ascii=False)
        with self._lock:
            with open(self.path, "a", encoding="utf-8") as handle:
                handle.write(line + "\n")


class NoLog:
    """Used by checks that must not write log files."""

    path = None

    def event(self, name: str, **fields) -> None:
        pass
