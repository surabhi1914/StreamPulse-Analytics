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

Data Quality Notes:

| Field | Missing Rows | Missing % |
|---|---:|---:|
| `artist_id` | 600,848 | 3.15% |
| `track_id` | 2,162,719 | 11.32% |
| `track_name` | 210 | ~0.00% |

Important Notes:

- The 100K-row sample is not representative for user-level counts because the raw file appears ordered by `user_id`.
- Full-dataset profiling should be used for dataset-level statistics.
- `artist_id` and `track_id` missingness will be handled in Phase 2.
- Chunked parsing uses `on_bad_lines="skip"`, so malformed rows may be excluded from the parsed row count.
- The dataset is historical and should be framed as a product analytics case study.

Next Phase:

Phase 2 will focus on data cleaning and transformation.
