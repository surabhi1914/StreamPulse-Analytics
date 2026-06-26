# src/config.py
"""
Purpose: Define shared project paths for StreamPulse Analytics.

This file will:
- Provide reusable path constants for data, docs, SQL, notebooks, and dashboard folders.
- Keep configuration lightweight until Phase 1 implementation begins.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
WAREHOUSE_DATA_DIR = DATA_DIR / "warehouse"
OUTPUT_DATA_DIR = DATA_DIR / "outputs"

DOCS_DIR = PROJECT_ROOT / "docs"
SQL_DIR = PROJECT_ROOT / "sql"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DASHBOARD_DIR = PROJECT_ROOT / "dashboard"

LASTFM_RAW_DIR = RAW_DATA_DIR / "lastfm_1k"
PROFILE_PATH = LASTFM_RAW_DIR / "userid-profile.tsv"
LISTENING_PATH = LASTFM_RAW_DIR / "userid-timestamp-artid-artname-traid-traname.tsv"
