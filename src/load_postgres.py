# src/load_postgres.py
"""
Purpose: PostgreSQL loading utilities for modeled analytics tables.
In simple language this file will load cleanedCSV outputs into the PostgreSQL tables


This file will:
- load the tables:
    1. dim_users
    2. dim_artists
    3. dim_tracks
    4. dim_dates
    5. fact_listening_events
- read env variables
- build postresql connection string
-return sqlachemy engine
"""

# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from src.config import CLEANED_CHUNKS_DIR, PROCESSED_DATA_DIR, PROJECT_ROOT
import hashlib

# ---------------------------------------------
# Functions
# ---------------------------------------------


# -------------------Create a SQLAlchemy PostgreSQL connection-------------------
def get_engine():
    load_dotenv()
    DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(DATABASE_URL)
    return engine


# -------------------Create DB structure-------------------
def create_database_structure(engine):
    SQL_PATH = PROJECT_ROOT / "sql" / "schema.sql"
    with open(SQL_PATH, "r", encoding="utf-8-sig") as file:
        schema_sql = file.read()
    with engine.connect() as connection:
        connection.execute(text(schema_sql))
        connection.commit()
    print("✅ Database structure created successfully!")


# -------------------convert into hash-------------------


def compact_key(value, prefix) -> str:
    if pd.isna(value) or value is None:
        return value

    value = str(value).strip()

    # Apply MD5 hashing if it's a dirty natural key or too massive
    if value.startswith("name:") or len(value) > 500:
        hashed = hashlib.md5(value.encode("utf-8")).hexdigest()
        # No matter how massive the input data is, MD5 will condense it down into a unique 128-bit signature.
        # hexdigest() turns the final mathematical hash bytes into a standard, human-readable hexadecimal string.
        return f"{prefix}:{hashed}"

    return value


# -------------------Load all cleaned event chunks into fact_listening_events-------------------
def load_fact_listening_events(engine, chunk_dir=CLEANED_CHUNKS_DIR, max_files=None):
    READ_COLS = ["user_id", "artist_key", "track_key", "timestamp"]
    files_loaded = 0
    rows_loaded = 0

    files = sorted(chunk_dir.glob("*.csv"))
    if max_files is not None:
        files = files[:max_files]
    for f in files:
        chunk_file = pd.read_csv(f, usecols=READ_COLS)

        # convert to datetime
        chunk_file["timestamp"] = pd.to_datetime(chunk_file["timestamp"])

        # create listened_date
        chunk_file["listened_date"] = chunk_file["timestamp"].dt.date

        # Clean the artist_key column
        chunk_file["artist_key"] = chunk_file["artist_key"].apply(
            lambda x: compact_key(x, "artist_hash")
        )

        # Clean the track_key column
        chunk_file["track_key"] = chunk_file["track_key"].apply(
            lambda x: compact_key(x, "track_hash")
        )

        # create source chunk
        chunk_file["source_chunk"] = f.name

        chunk_file = chunk_file.rename(columns={"timestamp": "listened_at"})

        chunk_file.to_sql(
            "fact_listening_events", con=engine, if_exists="append", index=False
        )

        files_loaded += 1
        rows_loaded += len(chunk_file)

    return {"files_loaded": files_loaded, "rows_loaded": rows_loaded}


# -------------------unique track dimension DataFrame from all cleaned listening chunks-------------------
def build_dim_tracks_from_chunks(
    chunk_dir=CLEANED_CHUNKS_DIR, max_files=None
) -> pd.DataFrame:
    master_list = []
    TARGET_COLS = ["track_id", "track_key", "track_name", "artist_key", "artist_name"]

    files = sorted(chunk_dir.glob("*.csv"))
    if max_files is not None:
        files = files[:max_files]
    for f in files:
        chunk_file = pd.read_csv(f, usecols=TARGET_COLS)
        chunk_file = chunk_file.drop_duplicates()
        # Clean the artist_key column
        chunk_file["artist_key"] = chunk_file["artist_key"].apply(
            lambda x: compact_key(x, "artist_hash")
        )

        # Clean the track_key column
        chunk_file["track_key"] = chunk_file["track_key"].apply(
            lambda x: compact_key(x, "track_hash")
        )
        chunk_rows = chunk_file[TARGET_COLS].values.tolist()
        master_list.extend(chunk_rows)

    dim_tracks = pd.DataFrame(master_list, columns=TARGET_COLS)
    dim_tracks = dim_tracks.drop_duplicates(subset=["track_key"], keep="first")

    dim_tracks["has_track_id"] = dim_tracks["track_id"].notna()

    return dim_tracks


# -------------------unique artist dimension DataFrame from all cleaned listening chunks-------------------
def build_dim_artists_from_chunks(
    chunk_dir=CLEANED_CHUNKS_DIR, max_files=None
) -> pd.DataFrame:
    master_list = []
    TARGET_COLS = ["artist_key", "artist_id", "artist_name"]

    files = sorted(chunk_dir.glob("*.csv"))
    if max_files is not None:
        files = files[:max_files]
    for f in files:
        chunk_file = pd.read_csv(f, usecols=TARGET_COLS)
        chunk_file = chunk_file.drop_duplicates()
        # Clean the artist_key column
        chunk_file["artist_key"] = chunk_file["artist_key"].apply(
            lambda x: compact_key(x, "artist_hash")
        )
        chunk_rows = chunk_file[TARGET_COLS].values.tolist()
        master_list.extend(chunk_rows)

    dim_artists = pd.DataFrame(master_list, columns=TARGET_COLS)
    dim_artists = dim_artists.drop_duplicates(subset=["artist_key"], keep="first")

    dim_artists["has_artist_id"] = dim_artists["artist_id"].notna()

    return dim_artists


# -------------------calendar table from listening dates-------------------
def build_dim_dates_from_chunks(
    chunk_dir=CLEANED_CHUNKS_DIR, max_files=None
) -> pd.DataFrame:
    master_list = []
    TARGET_COLS = ["timestamp"]

    files = sorted(chunk_dir.glob("*.csv"))
    if max_files is not None:
        files = files[:max_files]
    for f in files:
        chunk_file = pd.read_csv(f, usecols=TARGET_COLS)
        chunk_file["timestamp"] = pd.to_datetime(
            chunk_file["timestamp"]
        )  # convert to datetime
        chunk_file["date_key"] = chunk_file["timestamp"].dt.date
        chunk_file.drop_duplicates(subset=["date_key"], inplace=True)
        chunk_rows = chunk_file["date_key"].values.tolist()
        master_list.extend(chunk_rows)

    TARGET_COLS = ["date_key"]

    dim_dates = pd.DataFrame(master_list, columns=TARGET_COLS)
    dim_dates["date_key"] = pd.to_datetime(dim_dates["date_key"])

    dim_dates.drop_duplicates(subset=["date_key"], inplace=True)

    dim_dates.sort_values(by="date_key", inplace=True)

    # Deriving required columns
    dim_dates["year"] = dim_dates["date_key"].dt.year
    dim_dates["month"] = dim_dates["date_key"].dt.month
    dim_dates["month_name"] = dim_dates["date_key"].dt.month_name()
    dim_dates["quarter"] = dim_dates["date_key"].dt.quarter
    dim_dates["day_of_week"] = dim_dates["date_key"].dt.day_of_week
    dim_dates["day_name"] = dim_dates["date_key"].dt.day_name()
    dim_dates["day_of_month"] = dim_dates["date_key"].dt.day
    dim_dates["week"] = dim_dates["date_key"].dt.isocalendar().week
    dim_dates["is_weekend"] = dim_dates["date_key"].dt.day_of_week >= 5
    dim_dates["date_key"] = dim_dates["date_key"].dt.date
    return dim_dates


# -------------------Load users_clean.csv into dim_users.-------------------


def load_dim_users(engine):
    user_path = PROCESSED_DATA_DIR / "users_clean.csv"

    SCHEMA_COLUMNS = ["user_id", "gender", "age", "country", "signup_date"]

    users_clean = pd.read_csv(user_path, usecols=SCHEMA_COLUMNS)

    users_clean["signup_date"] = pd.to_datetime(users_clean["signup_date"])

    users_clean = users_clean.drop_duplicates(subset=["user_id"])

    users_clean.to_sql("dim_users", con=engine, if_exists="append", index=False)


# -------------------Reusable loader for dimension tables-------------------
def load_dimension_table(df, table_name, engine):
    df.to_sql(table_name, engine, if_exists="append", index=False)


# -------------------Reusable loader for dimension tables-------------------
def create_indexes(engine):
    IND_PATH = PROJECT_ROOT / "sql" / "indexes.sql"
    with open(IND_PATH, "r", encoding="utf-8-sig") as file:
        indexes_sql = file.read()
    with engine.connect() as connection:
        connection.execute(text(indexes_sql))
        connection.commit()
    print("✅ Indexes created successfully!")
