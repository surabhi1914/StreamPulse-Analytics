-- KPI views for StreamPulse Analytics. 
-- -------------Daily platform engagement metrics--------------
CREATE
OR REPLACE VIEW vw_daily_activity AS
SELECT
    listened_date as activity_date,
    COUNT(*) AS daily_listens,
    COUNT(DISTINCT user_id) AS daily_active_users,
    COUNT(DISTINCT track_key) AS unique_tracks_played,
    COUNT(DISTINCT artist_key) AS unique_artists_played,
    ROUND(
        COUNT (*) :: NUMERIC / NULLIF(COUNT(DISTINCT user_id), 0),
        2
    ) AS avg_listens_per_active_user
FROM
    fact_listening_events
GROUP BY
    listened_date;

-- -------------Monthly platform engagement metrics--------------
CREATE
OR REPLACE VIEW vw_monthly_activity AS
SELECT
    DATE_TRUNC('month', listened_date :: timestamp) :: DATE AS activity_month,
    COUNT(*) AS monthly_listens,
    COUNT(DISTINCT user_id) AS monthly_active_users,
    COUNT(DISTINCT track_key) AS unique_tracks_played,
    COUNT(DISTINCT artist_key) AS unique_artists_played,
    ROUND(
        COUNT (*) :: NUMERIC / NULLIF(COUNT(DISTINCT user_id), 0),
        2
    ) AS avg_listens_per_active_user
FROM
    fact_listening_events
GROUP BY
    DATE_TRUNC('month', listened_date :: timestamp) :: DATE;

-- -------------One row per user showing lifetime listening behavior--------------
CREATE
OR REPLACE VIEW vw_user_lifetime_summary AS
SELECT
    user_id,
    MIN(listened_at) AS first_listened_at,
    MAX(listened_at) AS last_listened_at,
    COUNT(*) AS lifetime_listens,
    COUNT(DISTINCT listened_date) AS active_days,
    COUNT(DISTINCT artist_key) AS unique_artists,
    COUNT(DISTINCT track_key) AS unique_tracks,
    (
        MAX(listened_date) :: DATE - MIN(listened_date) :: DATE
    ) AS listening_span_days,
    ROUND(
        COUNT(*) :: NUMERIC / NULLIF(COUNT(DISTINCT listened_date), 0),
        2
    ) AS avg_listens_per_active_day
FROM
    fact_listening_events
GROUP BY
    user_id;

-- -------------Artist-level engagement ranking--------------
CREATE
OR REPLACE VIEW vw_artist_popularity AS
SELECT
    f.artist_key,
    a.artist_name,
    COUNT(*) AS total_listens,
    COUNT(DISTINCT f.user_id) AS unique_listeners,
    COUNT(DISTINCT f.track_key) AS unique_tracks_played,
    MIN(f.listened_at) AS first_played_at,
    MAX(f.listened_at) AS last_played_at
FROM
    fact_listening_events f
    LEFT JOIN dim_artists a ON f.artist_key = a.artist_key
GROUP BY
    f.artist_key,
    a.artist_name;

-- -------------Track-level engagement ranking.--------------
CREATE
OR REPLACE VIEW vw_track_popularity AS
SELECT
    f.track_key,
    t.track_name,
    t.artist_key,
    t.artist_name,
    COUNT(*) AS total_listens,
    COUNT(DISTINCT f.user_id) AS unique_listeners,
    MIN(f.listened_at) AS first_played_at,
    MAX(f.listened_at) AS last_played_at
FROM
    fact_listening_events f
    LEFT JOIN dim_tracks t ON f.track_key = t.track_key
GROUP BY
    f.track_key,
    t.track_name,
    t.artist_key,
    t.artist_name;

-- -------------Identify tracks that users replay--------------
CREATE
OR REPLACE VIEW vw_repeat_track_listens AS
SELECT
    f.user_id,
    f.track_key,
    t.track_name,
    t.artist_key,
    t.artist_name,
    COUNT(*) AS listen_count,
    MIN(f.listened_at) AS first_listened_at,
    MAX(f.listened_at) AS last_listened_at,
    CASE
        WHEN COUNT(*) > 1 THEN TRUE
        ELSE FALSE
    END AS replayed_flag
FROM
    fact_listening_events f
    LEFT JOIN dim_tracks t ON f.track_key = t.track_key
GROUP BY
    f.user_id,
    f.track_key,
    t.track_name,
    t.artist_key,
    t.artist_name;