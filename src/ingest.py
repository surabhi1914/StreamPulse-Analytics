# src/ingest.py
"""
Purpose: only loads and inspect the data files.

This file will:
- list the raw files
- load the user profile file
- loads the listening events sample
- loads the listening events in chunk later
- print basic file information
"""

# ----------------------------------------
# Importing Libraries
# ----------------------------------------
from typing import List
from pathlib import Path
import pandas as pd
from src.config import LASTFM_RAW_DIR, PROFILE_PATH, LISTENING_PATH

# ----------------------------------------
# Functions
# ----------------------------------------


def get_raw_files() -> List[Path]:
    """
    Get all the files which are inside the folder data/raw/lastfm_1k
    """
    if not LASTFM_RAW_DIR.exists():
        raise FileNotFoundError("The raw data folder does not exist")
    files = LASTFM_RAW_DIR.iterdir()
    files = [f for f in files if f.suffix == ".tsv"]

    if len(files) == 0:
        raise ValueError("The folder is empty or does not contain .tsv data files")

    return files


def check_columns(df: pd.DataFrame, required_columns) -> bool:
    if df.empty:
        raise ValueError("Dataframe is empty")
    for i in required_columns:
        if i not in df.columns:
            return False
    return True


def load_user_profile() -> pd.DataFrame:
    """
    Loads the smaller user profile file
    Delimiter: \\t
    Does it have heading?: Yes
    """
    profile_df = pd.read_csv(PROFILE_PATH, delimiter="\t")
    required_columns = ["#id", "gender", "age", "country", "registered"]

    if not check_columns(profile_df, required_columns):
        raise ValueError("Required columns does not exist in the profile data")

    profile_df = profile_df.rename(
        columns={"#id": "user_id", "registered": "signup_date"}
    )  # We are only standardizing obvious column names for usability

    return profile_df


def load_listening_events_sample(nrows: int = 100_000) -> pd.DataFrame:
    """
    Load a sample of listening events
    Lets consider rows count = 100_000
    Delimiter: \\t
    Does it have heading?: No
    """
    required_columns = [
        "user_id",
        "timestamp",
        "artist_id",
        "artist_name",
        "track_id",
        "track_name",
    ]
    listening_df = pd.read_csv(
        LISTENING_PATH, delimiter="\t", nrows=nrows, header=None, names=required_columns
    )

    if not check_columns(listening_df, required_columns):
        raise ValueError("Required columns does not exist in the listening events data")

    return listening_df


def profile_listening_events_in_chunks(chunksize=500_000) -> dict:

    required_columns = [
        "user_id",
        "timestamp",
        "artist_id",
        "artist_name",
        "track_id",
        "track_name",
    ]
    chunk_iterator = pd.read_csv(
        LISTENING_PATH,
        delimiter="\t",
        chunksize=chunksize,
        header=None,
        names=required_columns,
        on_bad_lines="skip",  # Tells pandas to silently drop the broken lines and keep going
    )
    total_rows = 0
    missing_counts = pd.Series(0, index=required_columns)
    unique_users = set()
    unique_artists = set()
    unique_tracks = set()
    min_timestamp = None
    max_timestamp = None
    for i, chunk in enumerate(chunk_iterator):
        chunk["timestamp"] = pd.to_datetime(chunk["timestamp"], errors="coerce")
        total_rows += len(chunk)
        unique_users.update(chunk["user_id"].dropna().unique())
        unique_artists.update(chunk["artist_name"].dropna().unique())
        unique_tracks.update(chunk["track_name"].dropna().unique())
        missing_counts += chunk.isna().sum()
        chunk_min = chunk["timestamp"].min()
        chunk_max = chunk["timestamp"].max()
        if pd.notna(chunk_min):
            min_timestamp = (
                chunk_min
                if (min_timestamp is None or chunk_min < min_timestamp)
                else min_timestamp
            )
        if pd.notna(chunk_max):
            max_timestamp = (
                chunk_max
                if (max_timestamp is None or chunk_max > max_timestamp)
                else max_timestamp
            )

    summary = {
        "total_rows": total_rows,
        "unique_users": len(unique_users),
        "unique_artists": len(unique_artists),
        "unique_tracks": len(unique_tracks),
        "min_timestamp": min_timestamp,
        "max_timestamp": max_timestamp,
        "missing_counts": missing_counts,
        "missing_percentage": ((missing_counts / total_rows) * 100).round(2),
    }

    return summary


def get_file_size_mb(path) -> float:
    file_bytes = Path(path).stat().st_size
    file_mb = file_bytes / (1024 * 1024)
    return round(file_mb, 2)


def preview_tsv(path, n_rows=5) -> pd.DataFrame:
    """
    load first few rows from any TSV file
    return DataFrame

    """
    path = Path(path)
    file_name = path.name
    if "profile" in file_name:
        df = load_user_profile()
    elif "timestamp" in file_name:
        df = load_listening_events_sample()
    else:
        raise ValueError("Unknown file path")

    return df.head(n_rows)
