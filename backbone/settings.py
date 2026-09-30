"""Loads settings.toml. Every path in it is taken relative to the project root."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Settings:
    root: Path
    model: str
    effort: str
    prompt_version: int
    plan_prompt_version: int
    spending_cap_usd: float
    parallel_calls: int
    timeout_seconds: int
    claude_path: str
    store: Path
    readings: Path
    logs: Path
    answers: Path
    benchmarks: Path
    export: Path
    prompts: Path


def load(path: Path | None = None, root: Path | None = None) -> Settings:
    root = (root or PROJECT_ROOT).resolve()
    path = path or root / "settings.toml"
    with open(path, "rb") as handle:
        data = tomllib.load(handle)
    model = data["model"]
    paths = data["paths"]
    return Settings(
        root=root,
        model=model["name"],
        effort=model["effort"],
        prompt_version=int(model["prompt_version"]),
        plan_prompt_version=int(model.get("plan_prompt_version", 1)),
        spending_cap_usd=float(model["spending_cap_usd"]),
        parallel_calls=int(model["parallel_calls"]),
        timeout_seconds=int(model["timeout_seconds"]),
        claude_path=model.get("claude_path", ""),
        store=root / paths["store"],
        readings=root / paths["readings"],
        logs=root / paths["logs"],
        answers=root / paths["answers"],
        benchmarks=root / paths["benchmarks"],
        export=root / paths["export"],
        prompts=root / paths["prompts"],
    )
