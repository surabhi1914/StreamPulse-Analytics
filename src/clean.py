# src/clean.py
"""
Purpose: Data cleaning utilities for the Last.fm-1K dataset.

This module standardizes profile and listening-event DataFrames,
creates fallback artist/track keys, and removes invalid event rows.

This file will:
- strip whitespace from user_id, gender, country
- strip whitespace from text columns
- converts age to numeric
- convert timestamp to datetime
- remove rows with missing user_id
- remove rows with missing timestamp
- remove rows with missing artist_name
- remove rows with missing track_name
- create artist_key fallback
- create track_key fallback
- remove exact duplicate rows

"""

# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
import pandas as pd
from src.config import PROFILE_PATH, LISTENING_PATH, PROCESSED_DATA_DIR
from src.utils import ensure_directory
from pathlib import Path

# ---------------------------------------------
# Main Functions
# ---------------------------------------------


# -------------------Clean Profile data-------------------
def clean_user_profile(profile_df: pd.DataFrame) -> pd.DataFrame:
    profile = profile_df.copy()
    # Convert signup into datetime
    profile["signup_date"] = pd.to_datetime(profile["signup_date"], errors="coerce")
    # age to numeric
    profile["age"] = pd.to_numeric(profile["age"], errors="coerce")

    # Strip white space from user_id, gender, country
    strip_columns = ["user_id", "gender", "country"]
    existing_cols = [col for col in strip_columns if col in profile.columns]

    if existing_cols:
        profile[existing_cols] = (
            profile[existing_cols].astype("string").apply(lambda x: x.str.strip())
        )
        profile[existing_cols] = profile[existing_cols].replace("", pd.NA)
    return profile


# -------------------Clean listening events data-------------------
def clean_listening_events(listening_df: pd.DataFrame) -> pd.DataFrame:
    listening = listening_df.copy()
    # convert timestamp to datetime
    listening["timestamp"] = pd.to_datetime(listening["timestamp"], errors="coerce")

    # Strip text columns
    strip_columns = ["artist_name", "user_id", "track_name", "artist_id", "track_id"]
    existing_cols = [col for col in strip_columns if col in listening.columns]

    if existing_cols:
        listening[existing_cols] = (
            listening[existing_cols].astype("string").apply(lambda x: x.str.strip())
        )
        listening[existing_cols] = listening[existing_cols].replace("", pd.NA)

    # remove rows with missing track_name, artist_name, timestamp, user_id
    listening.dropna(
        subset=["track_name", "artist_name", "timestamp", "user_id"], inplace=True
    )

    # remove duplicate rows
    listening = listening.drop_duplicates()

    # Create artist key
    listening = create_artist_key(listening)

    # Create track key
    listening = create_track_key(listening)

    return listening


# -------------------Clean listening events data( full data - in chunks)-------------------
def clean_listening_events_in_chunks(
    input_path=LISTENING_PATH,
    chunk_size=500_000,
    output_dir=PROCESSED_DATA_DIR / "listening_events_cleaned_chunks",
    max_chunks=None,
) -> dict:
    # Check if the output directory exists
    output_dir = Path(output_dir)
    ensure_directory(output_dir)

    required_columns = [
        "user_id",
        "timestamp",
        "artist_id",
        "artist_name",
        "track_id",
        "track_name",
    ]

    # defining the chunk interator
    chunk_iterator = pd.read_csv(
        input_path,
        delimiter="\t",
        chunksize=chunk_size,
        header=None,
        names=required_columns,
        on_bad_lines="skip",  # Tells pandas to silently drop the broken lines and keep going
    )

    # defining the detailed needed
    total_raw_rows_processed = 0
    total_cleaned_rows_saved = 0
    total_rows_removed = 0
    number_of_chunks_written = 0
    output_files = []

    # loop through the chunk to get the details
    for i, chunk in enumerate(chunk_iterator):
        if max_chunks is not None and i >= max_chunks:
            break
        raw_count = len(chunk)
        cleaned_chunk = clean_listening_events(chunk)

        # Calculate summary of the chunk
        clean_count = len(cleaned_chunk)
        total_raw_rows_processed += raw_count
        total_cleaned_rows_saved += clean_count
        total_rows_removed += raw_count - clean_count
        chunk_id = str(i).zfill(3)
        number_of_chunks_written += 1
        events_data_file_name = (
            output_dir / f"listening_events_cleaned_part_{chunk_id}.csv"
        )
        output_files.append(str(events_data_file_name))

        cleaned_chunk.to_csv(events_data_file_name, index=False)

    # summary dictionary with all the relevant details for the whole file
    summary_events = {
        "total_raw_rows_processed": total_raw_rows_processed,
        "total_cleaned_rows_saved": total_cleaned_rows_saved,
        "total_rows_removed": total_rows_removed,
        "number_of_chunks_written": number_of_chunks_written,
        "output_files": output_files,
    }
    return summary_events


# ---------------------------------------------
# Helper Functions
# ---------------------------------------------


# -------------------Create primary key for artists-----------------
def create_artist_key(listening_df: pd.DataFrame) -> pd.DataFrame:
    listening_df["artist_key"] = listening_df["artist_id"].fillna(
        "name:"
        + listening_df["artist_name"].str.replace(" ", "_", regex=False).str.lower()
    )
    return listening_df


# -------------------Create primary key for tracks-----------------
def create_track_key(listening_df: pd.DataFrame) -> pd.DataFrame:
    listening_df["track_key"] = listening_df["track_id"].fillna(
        "name:"
        + listening_df["artist_name"].str.replace(" ", "_", regex=False).str.lower()
        + "::"
        + listening_df["track_name"].str.replace(" ", "_", regex=False).str.lower()
    )
    return listening_df
