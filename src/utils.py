# src/utils.py
"""
Purpose: Provide small shared utilities for notebooks and scripts.

This file will:
- Create directories when needed.
- Print readable section headers during exploratory work.
"""

from pathlib import Path


def ensure_directory(path: str | Path) -> None:
    """Create a directory if it does not already exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def print_section(title: str) -> None:
    """Print a simple section header for notebooks and scripts."""
    line = "=" * 80
    print(f"\n{line}\n{title}\n{line}")
