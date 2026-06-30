-- ============================================================================
-- STREAMPULSE ANALYTICS - DATA WAREHOUSE SCHEMA DOCUMENTATION
-- ============================================================================
-- This project utilizes a Star Schema design optimized for analytics.
-- Tables are explicitly named with prefixes to define their structural role:
--
-- 1. DIMENSION TABLES (dim_):
--    - Answer the "Who, What, Where, and When" of the data.
--    - Contain descriptive text, categories, and analytical attributes.
--    - Relatively small tables linked to the central fact table.
--
-- 2. FACT TABLES (fact_):
--    - Answer "What quantitative events actually happened."
--    - Acts as the massive central logbook (containing ~19M rows).
--    - Composed primarily of numerical keys and numeric metrics.
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. dim_users
-- ----------------------------------------------------------------------------
-- Role: Holds demographic data about "Who" listened.
-- Granularity: One row per unique user.
-- Use Case: Filtering listening behaviors by country, age group, or gender.

-- ----------------------------------------------------------------------------
-- 2. dim_artists
-- ----------------------------------------------------------------------------
-- Role: Holds master profile records for the creators of the music.
-- Granularity: One row per unique artist_key.
-- Use Case: Aggregating streaming metrics by artist name or checking verified IDs.

-- ----------------------------------------------------------------------------
-- 3. dim_tracks
-- ----------------------------------------------------------------------------
-- Role: Holds catalog details for "What" specific song was streamed.
-- Granularity: One row per unique track_key.
-- Use Case: Identifying individual song titles and metadata without text duplication.

-- ----------------------------------------------------------------------------
-- 4. dim_dates
-- ----------------------------------------------------------------------------
-- Role: Time-intelligence lookup table answering "When" an event occurred.
-- Granularity: One row per calendar date.
-- Use Case: Powers fast analytical groupings by Day of Week, Month, Quarter, or Year.

-- ----------------------------------------------------------------------------
-- 5. fact_listening_events
-- ----------------------------------------------------------------------------
-- Role: The core transactional data table capturing the stream events (~19M rows).
-- Granularity: One row per unique stream/play instance.
-- Contains no descriptive music/user text attributes; only keys, timestamps, and load metadata.
-- ============================================================================

-- ---------------------------------------------
-- Database Drop
-- ---------------------------------------------
DROP TABLE IF EXISTS fact_listening_events;
DROP TABLE IF EXISTS dim_tracks;
DROP TABLE IF EXISTS dim_artists;
DROP TABLE IF EXISTS dim_dates;
DROP TABLE IF EXISTS dim_users;
-- ---------------------------------------------
-- Database Definitions
-- ---------------------------------------------
-- -------------------Create Tables - Users-------------------
CREATE TABLE dim_users (
    user_id VARCHAR(512) NOT NULL PRIMARY KEY,
    gender TEXT,
    age INT,
    country TEXT,
    signup_date DATE
);



-- -------------------Create Tables - dates-------------------
-- Calendar helper table for time-based analysis
CREATE TABLE dim_dates (
    date_key DATE NOT NULL PRIMARY KEY,
    year INT,
    quarter INT,
    month INT,
    month_name TEXT,
    week INT,
    day_of_month INT,
    day_of_week INT,
    day_name TEXT,
    is_weekend BOOLEAN
);


-- -------------------Create Tables - Artist-------------------
CREATE TABLE dim_artists (
    artist_key VARCHAR(512) NOT NULL PRIMARY KEY,
    artist_id VARCHAR(512),
    artist_name TEXT NOT NULL,
    has_artist_id BOOLEAN NOT NULL
);

-- -------------------Create Tables - Tracks-------------------
CREATE TABLE dim_tracks (
    track_key TEXT NOT NULL PRIMARY KEY,
    track_id TEXT,
    track_name TEXT NOT NULL, 
    artist_key VARCHAR(512) NOT NULL,
    artist_name TEXT NOT NULL,
    has_track_id BOOLEAN NOT NULL,

    CONSTRAINT fk_dim_tracks_artist
        FOREIGN KEY (artist_key) REFERENCES dim_artists(artist_key)
);


-- -------------------Create Tables - Listening events-------------------
CREATE TABLE fact_listening_events (
    event_id BIGINT GENERATED ALWAYS AS IDENTITY NOT NULL PRIMARY KEY,
    user_id VARCHAR(512) NOT NULL,
    artist_key VARCHAR(512) NOT NULL,
    track_key VARCHAR(512) NOT NULL,
    listened_at TIMESTAMPTZ NOT NULL,
    listened_date DATE NOT NULL,
    source_chunk TEXT,

    CONSTRAINT fk_fact_events_user
        FOREIGN KEY (user_id) REFERENCES dim_users(user_id),

    CONSTRAINT fk_fact_events_artist
        FOREIGN KEY (artist_key) REFERENCES dim_artists(artist_key),

    CONSTRAINT fk_fact_events_track
        FOREIGN KEY (track_key) REFERENCES dim_tracks(track_key),

    CONSTRAINT fk_fact_events_date
        FOREIGN KEY (listened_date) REFERENCES dim_dates(date_key)
);





