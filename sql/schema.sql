-- SQL schema for StreamPulse Analytics.


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
-- Design Note: Contains NO text attributes (like user names or song names). 
--              Instead, it acts as the bridge connecting all dim_ tables 
--              together via optimized relational Foreign Keys.
-- ============================================================================

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



-- -------------------Create Tables - Artist-------------------
CREATE TABLE dim_artists (
    artist_key VARCHAR(512) NOT NULL PRIMARY KEY,
    artist_id VARCHAR(512),
    artist_name TEXT,
    has_artist_id BOOLEAN
);


-- -------------------Create Tables - Tracks-------------------
CREATE TABLE dim_tracks (
    track_key  VARCHAR(512) NOT NULL PRIMARY KEY,
    track_id VARCHAR(512),
    track_name TEXT,
    artist_key VARCHAR(512),
    artist_name TEXT,
    has_track_id BOOLEAN,

    CONSTRAINT fk_artist_key
        FOREIGN KEY (artist_key) REFERENCES dim_artists(artist_key)
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
    day_of_month TEXT,
    day_of_week TEXT,
    day_name TEXT,
    is_weekend BOOLEAN
);

-- -------------------Create Tables - Listening evnts-------------------
CREATE TABLE facts_listening_events (
    event_id INT GENERATED ALWAYS AS IDENTITY NOT NULL PRIMARY KEY,
    user_id VARCHAR(512),
    artist_key VARCHAR(512),
    track_key VARCHAR(512),
    listened_at TIMESTAMP,
    listened_date DATE,
    source_chunk TEXT,

    CONSTRAINT fkn_user_id
        FOREIGN KEY (user_id) REFERENCES dim_users(user_id)

    CONSTRAINT fk_artist_key
        FOREIGN KEY (artist_key) REFERENCES dim_artists(artist_key)

    CONSTRAINT fk_track_key
        FOREIGN KEY (track_key) REFERENCES dim_tracks(track_key)

    CONSTRAINT fkn_listened_date
        FOREIGN KEY (listened_date) REFERENCES dim_dates(date_key)
)


-- -------------------Indexes - Listening events-------------------
-- An index is a separate, highly organized lookup table (usually structured as a B-Tree) that points directly to where the data lives. 
-- It allows the database to instantly find matching rows in milliseconds.
-- Cons - While indexes make reading data lightning fast, they slow down writing data (INSERT / LOAD DATA INFILE). This is because every time you add a row, the database has to update all 6 of these indexes.
-- CREATE INDEX index_name ON table_name(column_names)


CREATE INDEX idx_listening_user ON fact_listening_events(user_id);
CREATE INDEX idx_listened_at ON facts_listening_events(listened_at);
CREATE INDEX idx_listened_date ON facts_listening_events(listened_date);
CREATE INDEX idx_artist_key ON facts_listening_events(artist_key);
CREATE INDEX idx_track_key ON facts_listening_events(track_key);

CREATE INDEX idx_listening_user_time ON facts_listening_events(user_id, listened_at);