# Data Dictionary

Status: Updated after Phase 1 profiling.

## Raw Listening Events

| Column | Description | Phase 1 Notes |
|---|---|---|
| user_id | Listener identifier | Required for user-level analytics |
| timestamp | Time of listening event | Required for retention, sessions, and replay windows |
| artist_id | Artist identifier | Contains missing values: 600,848 rows, 3.15% |
| artist_name | Artist name | Important fallback identifier |
| track_id | Track identifier | Contains noticeable missing values: 2,162,719 rows, 11.32% |
| track_name | Track/song name | Very low missingness: 210 rows, approximately 0.00% |

## Raw User Profile

| Column | Description | Phase 1 Notes |
|---|---|---|
| user_id | Listener identifier | Renamed from raw `#id` column |
| gender | User profile field | Available if present in raw profile file |
| age | User profile field | Needs validation in Phase 2 |
| country | User location field | Useful for exploratory analysis if complete enough |
| signup_date | Registration date | Renamed from raw `registered` column |

## Phase 1 Dataset Profile

| Metric | Value |
|---|---:|
| Parsed listening events | 19,098,853 |
| Unique users | 992 |
| Unique artists | 173,921 |
| Unique tracks | 1,083,470 |
| Date range | 2005-02-14 to 2013-09-29 |

## Planned Derived Tables

### dim_users
User-level dimension table.

### dim_artists
Artist-level dimension table.

### dim_tracks
Track-level dimension table.

### dim_dates
Date dimension for time-based analysis.

### fact_listening_events
Main event-level fact table.

### fact_sessions
Sessionized listening activity.

### fact_user_daily_activity
Daily user engagement table.

### fact_user_artist_activity
User-artist interaction table.

### fact_user_track_activity
User-track interaction table.

## Phase 2 Cleaning Decisions To Make

- Whether to use `artist_id`, `artist_name`, or a fallback key for artist-level analysis
- Whether to use `track_id`, `track_name`, or a fallback key for track-level analysis
- How to handle missing track names
- Whether exact duplicate listening events should be removed
- How to validate and standardize timestamps
- How to handle malformed rows skipped during ingestion
