# Data Dictionary

Status: Draft. To be updated after Phase 1 data profiling.

## Expected Raw Listening Events

| Column | Description | Notes |
|---|---|---|
| user_id | Listener identifier | Required for user-level analytics |
| timestamp | Time of listening event | Required for retention and sessions |
| artist_id | Artist identifier | May contain missing values |
| artist_name | Artist name | Used for artist-level analysis |
| track_id | Track identifier | May contain missing values |
| track_name | Track/song name | Used for track-level replay analysis |

## Planned Derived Tables

### dim_users
User-level table.

### dim_artists
Artist-level table.

### dim_tracks
Track-level table.

### dim_dates
Date dimension.

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
