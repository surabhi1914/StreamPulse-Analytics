# Data Dictionary

Status: Updated after Phase 2 cleaning.

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
| age | User profile field | Validated and converted during Phase 2 cleaning |
| country | User location field | Useful for exploratory analysis if complete enough |
| signup_date | Registration date | Renamed from raw `registered` column |

## Cleaned User Profile

| Column | Description | Cleaning Notes |
|---|---|---|
| user_id | Listener identifier | Required user-level key |
| gender | User profile field | Whitespace stripped; empty strings converted to missing values |
| age | User age | Converted to numeric |
| country | User country field | Whitespace stripped; empty strings converted to missing values |
| signup_date | User registration date | Converted to datetime |

## Cleaned Listening Events

| Column | Description | Cleaning Notes |
|---|---|---|
| user_id | Listener identifier | Required; rows missing this field are removed |
| timestamp | Listening event timestamp | Converted to datetime; rows missing this field are removed |
| artist_id | Raw artist identifier | Allowed to be missing |
| artist_name | Artist name | Required; used for fallback artist key |
| track_id | Raw track identifier | Allowed to be missing |
| track_name | Track name | Required; used for fallback track key |
| artist_key | Analysis-ready artist identifier | Uses `artist_id` when available; otherwise normalized `artist_name` |
| track_key | Analysis-ready track identifier | Uses `track_id` when available; otherwise normalized `artist_name + track_name` |

## Cleaned Outputs

| Output | Description |
|---|---|
| `data/processed/users_clean.csv` | Cleaned user profile file |
| `data/processed/listening_events_clean_sample.csv` | Cleaned 100K-row listening sample |
| `data/processed/listening_events_cleaned_chunks/` | Folder containing full cleaned listening events split into 39 chunk files |

## Phase 2 Cleaning Results

| Metric | Value |
|---|---:|
| Full raw parsed listening rows | 19,098,853 |
| Full cleaned listening rows saved | 19,098,642 |
| Rows removed during cleaning | 211 |
| Number of cleaned chunk files | 39 |
| Cleaned date range | 2005-02-14 00:00:07+00:00 to 2013-09-29 18:32:04+00:00 |
| Missing user_id after cleaning | 0 |
| Missing timestamp after cleaning | 0 |
| Missing artist_name after cleaning | 0 |
| Missing track_name after cleaning | 0 |
| Missing artist_key after cleaning | 0 |
| Missing track_key after cleaning | 0 |

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

## Phase 3 Modeling Decisions To Make

- How to define primary keys for user, artist, track, date, and listening event tables
- Whether global duplicate detection across chunks should be handled during warehouse loading or SQL modeling
- How to preserve fallback `artist_key` and `track_key` values in dimension and fact tables
- How to structure sessionization and daily user activity tables
