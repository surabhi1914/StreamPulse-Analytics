# Data Dictionary

Status: Updated after Phase 3 analytics data modeling.

## Raw Listening Events

| Column | Description | Phase 1 Notes |
|---|---|---|
| user_id | Listener identifier | Required for user-level analytics |
| timestamp | Time of listening event | Required for retention, sessions, and replay windows |
| artist_id | Artist identifier | Contains missing values: 600,848 rows, 3.15% |
| artist_name | Artist name | Important fallback identifier |
| track_id | Track identifier | Contains noticeable missing values: 2,162,719 rows, 11.32% |
| track_name | Track/song name | Very low missingness: 210 rows, approximately 0.00% |

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

## PostgreSQL Warehouse Tables

### `dim_users`

| Column | Description | Notes |
|---|---|---|
| `user_id` | User identifier | Primary key |
| `gender` | User profile gender field | Nullable |
| `age` | User age | Nullable |
| `country` | User country | Nullable |
| `signup_date` | User registration date | Stored as date |

### `dim_artists`

| Column | Description | Notes |
|---|---|---|
| `artist_key` | Analysis-ready artist identifier | Primary key |
| `artist_id` | Raw artist identifier | Nullable |
| `artist_name` | Artist name | Required |
| `has_artist_id` | Boolean flag for raw artist ID availability | Required |

### `dim_tracks`

| Column | Description | Notes |
|---|---|---|
| `track_key` | Analysis-ready track identifier | Primary key |
| `track_id` | Raw track identifier | Nullable |
| `track_name` | Track name | Required |
| `artist_key` | Artist key associated with track | Foreign key to `dim_artists` |
| `artist_name` | Artist name | Required |
| `has_track_id` | Boolean flag for raw track ID availability | Required |

### `dim_dates`

| Column | Description | Notes |
|---|---|---|
| `date_key` | Calendar date | Primary key |
| `year` | Calendar year | Integer |
| `quarter` | Calendar quarter | Integer |
| `month` | Calendar month number | Integer |
| `month_name` | Calendar month name | Text |
| `week` | ISO week | Integer |
| `day_of_month` | Day of month | Integer |
| `day_of_week` | Day of week number | Integer |
| `day_name` | Day name | Text |
| `is_weekend` | Weekend flag | Boolean |

### `fact_listening_events`

| Column | Description | Notes |
|---|---|---|
| `event_id` | Surrogate event identifier | Primary key |
| `user_id` | User identifier | Foreign key to `dim_users` |
| `artist_key` | Artist identifier | Foreign key to `dim_artists` |
| `track_key` | Track identifier | Foreign key to `dim_tracks` |
| `listened_at` | Full listening timestamp | Stored as `TIMESTAMPTZ` |
| `listened_date` | Listening event date | Foreign key to `dim_dates` |
| `source_chunk` | Source cleaned chunk filename | Load traceability metadata |

## Warehouse Counts

| Table | Rows |
|---|---:|
| `dim_users` | 992 |
| `dim_artists` | 176,697 |
| `dim_tracks` | 1,503,135 |
| `dim_dates` | 1,589 |
| `fact_listening_events` | 19,098,642 |

## Phase 3 Modeling Notes

- `artist_key` and `track_key` are used as analysis-ready identifiers.
- Missing raw IDs were retained using fallback keys.
- Long fallback keys were compacted using deterministic hashing before PostgreSQL loading.
- Hashing was applied consistently across artist dimensions, track dimensions, and fact rows to preserve referential integrity.
- The fact table passed null and foreign-key validation checks.
- PostgreSQL stores `listened_at` as `TIMESTAMPTZ`, so displayed timestamps may appear in local timezone while corresponding to the UTC-equivalent cleaned data range.

## Future Derived Tables

### fact_sessions
Sessionized listening activity.

### fact_user_daily_activity
Daily user engagement table.

### fact_user_artist_activity
User-artist interaction table.

### fact_user_track_activity
User-track interaction table.
