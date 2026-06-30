# Phase Updates

## Phase -1: Dataset Decision

Status: Complete

Completed:

- Evaluated multiple dataset options
- Selected Last.fm-1K as the MVP dataset
- Rejected personal Spotify data for product-level analysis
- Deferred KKBox, Spotify MPD, and hybrid approach for future work
- Defined valid and invalid analyses based on available fields

Key Decision:
Use one strong dataset for the MVP instead of forcing unrelated datasets together.

---

## Phase 0: Project Setup

Status: Complete

Completed:

- Created repository structure
- Added README v0
- Added requirements.txt
- Added .gitignore
- Added starter documentation
- Added placeholder source files
- Added placeholder notebooks and SQL files

Notes:
No analytics or modeling implementation was added in Phase 0.

---

## Phase 1: Data Ingestion and Profiling

Status: Complete

Completed:

- Loaded and inspected raw Last.fm-1K files
- Created reusable ingestion helpers in `src/ingest.py`
- Loaded user profile data
- Loaded a 100K-row listening events sample for schema inspection
- Performed full listening dataset profiling using chunked processing
- Confirmed dataset supports user-level analytics, retention analysis, replay modeling, segmentation, and funnel analysis
- Identified missingness in `artist_id` and `track_id`
- Documented limitations around historical data and unavailable Spotify-style product fields

Key Results:

| Metric | Value |
|---|---:|
| Parsed listening events | 19,098,853 |
| Unique users | 992 |
| Unique artists | 173,921 |
| Unique tracks | 1,083,470 |
| Date range | 2005-02-14 to 2013-09-29 |

---

## Phase 2: Data Cleaning and Transformation

Status: Complete

Completed:

- Created reusable cleaning utilities in `src/clean.py`
- Cleaned user profile data
- Cleaned a 100K-row listening events sample
- Saved cleaned sample outputs to `data/processed/`
- Built chunked full-file cleaning for the large listening events file
- Cleaned the full listening dataset into 39 chunk files
- Validated cleaned chunk outputs without loading all rows into memory
- Confirmed required fields are complete after cleaning
- Confirmed `artist_key` and `track_key` are fully populated

Key Results:

| Metric | Value |
|---|---:|
| Raw parsed listening rows | 19,098,853 |
| Cleaned listening rows saved | 19,098,642 |
| Rows removed during cleaning | 211 |
| Cleaned chunk files | 39 |
| Missing user_id after cleaning | 0 |
| Missing timestamp after cleaning | 0 |
| Missing artist_name after cleaning | 0 |
| Missing track_name after cleaning | 0 |
| Missing artist_key after cleaning | 0 |
| Missing track_key after cleaning | 0 |
| Cleaned date range | 2005-02-14 to 2013-09-29 |

Important Notes:

- Rows missing `user_id`, `timestamp`, `artist_name`, or `track_name` were removed.
- Rows with missing `artist_id` or `track_id` were retained.
- Fallback keys were created to support reliable artist-level and track-level grouping.
- Cleaning was performed in chunks to avoid loading the full 2.4GB listening file into memory.
- Duplicate removal currently happens within each chunk. Global duplicate detection across chunks will be handled later during warehouse loading or SQL modeling if needed.

---

## Phase 3: Analytics Data Modeling

Status: Complete

Completed:

- Designed PostgreSQL star schema
- Created dimension tables for users, artists, tracks, and dates
- Created central fact table for listening events
- Loaded cleaned user profile data
- Built artist and track dimensions from cleaned event chunks
- Built date dimension from listening timestamps
- Loaded 19,098,642 cleaned listening events into PostgreSQL
- Separated index creation into `sql/indexes.sql`
- Created indexes after loading
- Validated null checks and referential integrity
- Created `notebooks/03_data_modeling.ipynb` to document warehouse validation

Final Warehouse Counts:

| Table | Rows |
|---|---:|
| `dim_users` | 992 |
| `dim_artists` | 176,697 |
| `dim_tracks` | 1,503,135 |
| `dim_dates` | 1,589 |
| `fact_listening_events` | 19,098,642 |

Validation Results:

| Check | Result |
|---|---:|
| Fact rows with required null fields | 0 |
| Fact rows missing user dimension match | 0 |
| Fact rows missing artist dimension match | 0 |
| Fact rows missing track dimension match | 0 |
| Fact rows missing date dimension match | 0 |

Important Notes:

- The warehouse uses a star schema optimized for analytics.
- The fact table stores one row per cleaned listening event.
- Long fallback keys were compacted with deterministic hashing before loading to PostgreSQL.
- Indexes were created after loading to improve full-load performance.
- PostgreSQL displays `TIMESTAMPTZ` values in local timezone, while the cleaned data was validated against UTC-equivalent timestamps.

Next Phase:

Phase 4 will focus on the product metrics layer.
