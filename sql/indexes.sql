
-- -------------------Indexes - Listening events-------------------
-- An index is a separate, highly organized lookup table (usually structured as a B-Tree) that points directly to where the data lives. 
-- It allows the database to instantly find matching rows in milliseconds.
-- Cons - While indexes make reading data lightning fast, they slow down writing data (INSERT / LOAD DATA INFILE). This is because every time you add a row, the database has to update all 6 of these indexes.
-- CREATE INDEX index_name ON table_name(column_names)


CREATE INDEX idx_listening_user ON fact_listening_events(user_id);
CREATE INDEX idx_listened_at ON fact_listening_events(listened_at);
CREATE INDEX idx_listened_date ON fact_listening_events(listened_date);
CREATE INDEX idx_artist_key ON fact_listening_events(artist_key);
CREATE INDEX idx_track_key ON fact_listening_events(track_key);

CREATE INDEX idx_listening_user_time ON fact_listening_events(user_id, listened_at);