# Spotify Listening Intelligence Platform

## 1. Project Goal

Build a real-data analytics project that analyzes Spotify listening behavior using Spotify Web API data and Spotify account export data.

The project answers:

> What listening behaviors predict engagement, repeat listening, playlist usage, and possible drop-off risk?

This project is designed to demonstrate senior-level data analyst, product analyst, and analytics engineering skills.

---

## 2. Target Skills / Keywords

* SQL at scale
* Product analytics
* KPI design
* User behavior analysis
* Funnel analysis
* Cohort retention
* Segmentation
* Data modeling
* Star schema design
* Stakeholder reporting
* Business recommendations
* Data pipelines
* Predictive analytics
* Experimentation-style analysis
* Storytelling with data

---

## 3. Important Data Reality Check

This project will use real data, not fake data.

However, Spotify does not provide full internal business data such as:

* Premium upgrades for all users
* Spotify revenue
* True user churn across many users
* Full search behavior for all users
* Real randomized A/B test assignment
* Listening history for other users

So this project will focus on realistic personal listening intelligence.

Available data sources:

### Spotify Web API

Can provide:

* User profile
* Current user playlists
* Playlist tracks
* Saved tracks
* Recently played tracks
* Top artists
* Top tracks
* Artist and track metadata where available

### Spotify Account Data Export

Can provide:

* Extended streaming history
* Timestamp
* Track name
* Artist name
* Album name
* Milliseconds played
* Platform/device information if included
* Country if included
* Shuffle/skipped/reason fields if included

---

## 4. Final Project Idea

## Spotify Listening Intelligence Platform

A product analytics and data engineering project that analyzes personal Spotify listening history to understand:

* Listening trends
* Engagement patterns
* Repeat listening behavior
* Playlist influence
* Saved-track influence
* Device/platform behavior
* Genre and artist retention
* Drop-off risk
* Music discovery patterns

---

## 5. Main Business Questions

1. Which listening behaviors are associated with repeat listening?
2. Are saved tracks more likely to be replayed?
3. Are playlist-added tracks more likely to have long-term engagement?
4. Which artists or genres have the strongest retention?
5. Does device/platform affect skip behavior or session duration?
6. What types of listening sessions show high engagement?
7. Can we predict whether a track or artist will be listened to again within 30 days?
8. What product recommendations could improve retention and engagement?

---

## 6. MVP Scope

The MVP will include:

1. Spotify API data collection
2. Spotify export data parsing
3. Clean data model
4. PostgreSQL database
5. SQL-based KPI layer
6. Cohort retention analysis
7. Funnel analysis
8. Segmentation
9. Predictive replay model
10. Experimentation-style observational analysis
11. Streamlit dashboard
12. Business recommendation report
13. README updates after every phase

---

# Phase 0: Project Setup

## Goal

Set up a clean, professional project structure before writing major code.

## Deliverables

* GitHub repository
* Project folder structure
* README v0
* `.env.example`
* `requirements.txt`
* `docs/project_plan.md`
* `docs/data_sources.md`
* `docs/data_dictionary.md`
* `docs/phase_updates.md`

## Skills Demonstrated

* Project planning
* Documentation
* Clean engineering setup
* Portfolio organization

---

# Phase 1: Data Collection

## Goal

Collect real Spotify data from available sources.

## Source 1: Spotify Web API

Collect:

* User profile
* Playlists
* Playlist tracks
* Saved tracks
* Recently played tracks
* Top artists
* Top tracks

## Source 2: Spotify Extended Streaming History Export

Parse:

* Full listening history
* Track name
* Artist name
* Album name
* Timestamp
* Milliseconds played
* Platform/device fields if available
* Skip/reason fields if available

## Important Note

Some desired data may not be available depending on what Spotify includes in the export. The pipeline should handle missing fields safely.

## Deliverables

* `src/spotify_api.py`
* `src/parse_exports.py`
* Raw API outputs saved to `data/raw/spotify_api/`
* Raw export files placed in `data/raw/spotify_export/`
* Clean parsed files saved to `data/processed/`

## README Update

Add:

[] Data sources used
[] What each source provides
[] What data is unavailable
[] Privacy note

---

# Phase 2: Data Engineering and Data Modeling

## Goal

Transform raw Spotify data into analytics-ready tables.

## Clean Tables

Dimension tables:

```text
dim_tracks
dim_artists
dim_albums
dim_playlists
dim_devices
dim_dates
```

Fact tables:

```text
fact_listening_events
fact_saved_tracks
fact_playlist_tracks
fact_sessions
```

## Session Definition

A listening session will be created by grouping listening events where the time gap between plays is less than 30 minutes.

Example:

```text
If two plays happen within 30 minutes, they belong to the same session.
If the gap is more than 30 minutes, a new session starts.
```

## Deliverables

* `sql/schema.sql`
* `src/transform.py`
* `src/load_postgres.py`
* PostgreSQL tables
* Data dictionary

## Skills Demonstrated

* SQL
* ETL
* Data cleaning
* Data modeling
* Star schema
* Analytics engineering

## README Update

Add:

[] Data model diagram
[] Table descriptions
[] Sessionization logic

---

# Phase 3: Product Metrics Layer

## Goal

Create reusable SQL views for Spotify-style product metrics.

## SQL Views

```text
daily_listening_kpis
weekly_engagement_kpis
monthly_engagement_kpis
track_engagement_kpis
artist_engagement_kpis
genre_engagement_kpis
device_engagement_kpis
session_kpis
```

## Metrics

Engagement:

* Listening hours
* Total plays
* Active listening days
* Sessions per day
* Average session duration
* Songs per session
* Average milliseconds played per track

Retention:

* Repeat listen rate
* Track replay rate
* Artist replay rate
* Genre revisit rate

Content:

* Skip rate, if available
* Save rate
* Playlist coverage rate
* Top genres
* Top artists
* Top tracks

Device/platform:

* Listening by device/platform
* Skip rate by device/platform
* Session duration by device/platform


## Deliverables

* `sql/views_kpis.sql`
* KPI output tables
* KPI explanation in docs

## README Update

Add:

[] KPI framework
[] Metric definitions
[] Example KPI results

---

# Phase 4: Cohort Retention Analysis

## Goal

Analyze whether early engagement actions are associated with future listening retention.

## Main Question

> Do saved or playlist-added tracks continue to receive more future listening?

## Cohorts

Track-level cohorts:

* Saved tracks
* Non-saved tracks
* Playlist-added tracks
* Non-playlist-added tracks
* Tracks listened to for more than 80% of duration
* Tracks skipped early, if skip data is available

Artist-level cohorts:

* New artists
* Repeat artists
* High-frequency artists
* Low-frequency artists

Genre-level cohorts:

* Frequently revisited genres
* One-time discovery genres

## Retention Windows

Measure replay within:

* 1 day
* 7 days
* 14 days
* 30 days

## Deliverables

* `sql/retention_queries.sql`
* Cohort retention table
* Retention chart data
* Written interpretation

## README Update

Add:

[] Cohort definitions
[] Retention results
[] Key insights

---

# Phase 5: Funnel Analysis

## Goal

Understand where listening engagement drops off.

## Funnel 1: Track Engagement Funnel

```text
First listen
→ meaningful listen
→ repeat listen
→ saved track
→ playlist added
→ 30-day replay
```

## Funnel 2: Artist Engagement Funnel

```text
First artist listen
→ second artist listen
→ 5+ artist plays
→ saved/playlist track by artist
→ 30-day artist revisit
```

## Funnel 3: Discovery Funnel

```text
New track discovered
→ listened more than 60 seconds
→ listened again
→ saved or playlisted
→ became repeat favorite
```

## Deliverables

* `sql/funnel_queries.sql`
* Funnel conversion table
* Drop-off analysis
* Business recommendations

## README Update

Add:

[] Funnel design
[] Conversion rates
[] Biggest drop-off point
[] Product recommendation

---

# Phase 6: Segmentation

## Goal

Group listening behavior into meaningful segments.

## Segmentation Units

Segment:

* Tracks
* Artists
* Sessions
* Listening days

## Example Segments

Track segments:

* Repeat favorites
* Discovery tracks
* Skip-heavy tracks
* Background tracks
* High-save tracks

Artist segments:

* Core artists
* Occasional artists
* Discovery artists
* High-retention artists

Session segments:

* Long focused sessions
* Short casual sessions
* Late-night sessions
* Mobile sessions
* Skip-heavy sessions

## Methods

Use:

* Feature engineering
* StandardScaler
* KMeans
* PCA for visualization

## Deliverables

* `src/features.py`
* `notebooks/06_segmentation.ipynb`
* Segment labels
* Segment summary table
* Segment visualization

## README Update

Add:
[] Features used
[] Segment descriptions
[] Business meaning of each segment

---

# Phase 7: Predictive Analytics

## Goal

Predict whether a track or artist will be listened to again within 30 days.

## Prediction Target

```text
Will this track be replayed within 30 days of first listen?
```

Optional second target:

```text
Will this artist be revisited within 30 days of first listen?
```

## Features

* First listen duration
* Percent of track played
* Skip flag, if available
* Hour of day
* Day of week
* Device/platform
* Saved status
* Playlist status
* Previous artist familiarity
* Genre
* Session length
* Listening context

## Models

Start simple:

* Logistic Regression

Then compare with:

* Random Forest
* XGBoost

## Evaluation

Use:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion matrix
* Feature importance

## Deliverables

* `src/modeling.py`
* `notebooks/07_prediction_model.ipynb`
* Model comparison table
* Feature importance chart
* Honest failure analysis

## README Update

Add:

[] Prediction task
[] Model results
[] Best features
[] Limitations

---

# Phase 8: Experimentation-Style Analysis

## Goal

Demonstrate experimentation thinking using observational data.

## Important Note

This is not a real randomized A/B test because we do not control Spotify product assignment.

This phase will be written as:

> Observational experiment-style analysis.

## Hypothesis 1

> Playlist-added tracks have higher future replay rates than non-playlist-added tracks.

## Hypothesis 2

> Saved tracks have higher 30-day replay rates than non-saved tracks.

## Hypothesis 3

> Longer first listens are associated with higher repeat listening.

## Analysis

Calculate:

* Control group
* Treatment-like group
* Conversion rate
* Lift %
* Confidence interval
* p-value
* Effect size

## Deliverables

* `sql/experiment_queries.sql`
* `notebooks/08_experiment_analysis.ipynb`
* Statistical test results
* Clear interpretation

## README Update

Add:

[] Hypothesis
[] Method
[] Result
[] Limitation: observational, not causal

---

# Phase 9: Executive Dashboard

## Goal

Create a dashboard that tells the story clearly.

## Build First

Use Streamlit first.

Power BI can be added later if useful.

## Dashboard Pages

1. Executive Overview
2. Listening Trends
3. Engagement KPIs
4. Retention and Cohorts
5. Funnel Analysis
6. Segmentation
7. Predictive Model
8. Recommendations

## Executive View

Show:

* Total listening hours
* Total tracks played
* Active listening days
* Average session duration
* Top artists
* Top genres
* Repeat listen rate
* Save rate
* Playlist coverage rate

## Product View

Show:

* Funnels
* Cohorts
* Engagement trends
* Skip behavior if available

## Growth / Retention View

Show:

* Replay prediction
* Retention drivers
* Track/artist revisit behavior

## Experiment View

Show:

* Hypotheses
* Lift
* Confidence intervals
* p-values
* Interpretation

## Deliverables

* `dashboard/streamlit_app.py`
* Dashboard screenshots
* Dashboard GIF or short demo video

## README Update

Add:

* Dashboard screenshots
* How to run dashboard
* Summary of findings

---

# Phase 10: Business Recommendations

## Goal

Translate analysis into product recommendations.

## Questions to Answer

1. Are highest-retention artists concentrated in certain genres?
2. Are tracks saved within 24 hours more likely to be replayed?
3. Does mobile listening have higher skip behavior than desktop?
4. Do playlist-added tracks show higher repeat-listen probability?
5. Which listening behaviors predict future engagement?
6. Which moments in the funnel have the biggest drop-off?

## Recommendation Format

Each recommendation should include:

```text
Finding:
Evidence:
Business interpretation:
Recommendation:
Expected impact:
Limitation:
```

## Example

```text
Finding:
Tracks saved within 24 hours of first listen had a higher 30-day replay rate.

Evidence:
Saved tracks showed a 30-day replay rate of X%, compared with Y% for non-saved tracks.

Business interpretation:
Saving appears to be a strong signal of future engagement.

Recommendation:
Spotify could make the save action more visible during early discovery sessions.

Expected impact:
This may increase repeat listening and long-term engagement.

Limitation:
This is observational and does not prove causality.
```

## Deliverables

* `docs/business_recommendations.md`
* Final README insights section
* LinkedIn-ready project summary
* Resume bullets

---

# Final Tech Stack

## Data Processing

* Python
* Pandas
* NumPy

## API/Data Collection

* Spotify Web API
* Spotipy
* Python dotenv

## Database

* PostgreSQL
* SQLAlchemy

## Analytics

* SQL
* scipy
* statsmodels

## Machine Learning

* scikit-learn
* XGBoost optional

## Visualization

* Streamlit first
* Power BI optional later
* Matplotlib or Plotly

## Workflow

* Notebooks for exploration
* Modular Python scripts for reusable pipeline
* Airflow optional later only if the core project is complete

## Cloud

Optional later:

* AWS S3 for storage
* AWS RDS PostgreSQL
* Streamlit Community Cloud or Render for demo

---

# Suggested Repository Structure

```text
spotify-listening-intelligence/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── docs/
│   ├── project_plan.md
│   ├── data_sources.md
│   ├── data_dictionary.md
│   ├── phase_updates.md
│   └── business_recommendations.md
│
├── data/
│   ├── raw/
│   │   ├── spotify_api/
│   │   └── spotify_export/
│   ├── processed/
│   └── outputs/
│
├── notebooks/
│   ├── 01_collect_spotify_api_data.ipynb
│   ├── 02_parse_streaming_history.ipynb
│   ├── 03_data_modeling.ipynb
│   ├── 04_kpi_analysis.ipynb
│   ├── 05_retention_funnel_analysis.ipynb
│   ├── 06_segmentation.ipynb
│   ├── 07_prediction_model.ipynb
│   ├── 08_experiment_analysis.ipynb
│   └── 09_dashboard_prep.ipynb
│
├── sql/
│   ├── schema.sql
│   ├── views_kpis.sql
│   ├── retention_queries.sql
│   ├── funnel_queries.sql
│   └── experiment_queries.sql
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── spotify_api.py
│   ├── parse_exports.py
│   ├── transform.py
│   ├── load_postgres.py
│   ├── features.py
│   ├── modeling.py
│   └── utils.py
│
└── dashboard/
    └── streamlit_app.py
```

---

# Build Order

[] Step 1: Create repository and folder structure.
[] Step 2: Write README v0 and project plan.
[] Step 3: Set up Spotify Developer app and OAuth scopes.
[] Step 4: Collect Spotify API data.
[] Step 5: Request/download Spotify Extended Streaming History.
[] Step 6: Parse export JSON files.
[] Step 7: Design PostgreSQL schema.
[] Step 8: Load cleaned data into PostgreSQL.
[] Step 9: Create KPI SQL views.
[] Step 10: Build cohort and funnel analysis.
[] Step 11: Build segmentation.
[] Step 12: Build replay prediction model.
[] Step 13: Build experiment-style analysis.
[] Step 14: Build Streamlit dashboard.
[] Step 15: Write final business recommendations.
[] Step 16: Polish README, screenshots

---

# Project Success Criteria

This project is successful if it shows:

1. Real data collection from Spotify sources
2. Clean data pipeline from raw data to analytics-ready tables
3. Strong SQL analytics layer
4. Clear KPI definitions
5. Cohort and funnel analysis
6. Segmentation using meaningful features
7. Predictive analytics with honest evaluation
8. Experimentation-style thinking
9. Dashboard storytelling
10. Business recommendations supported by data
11. Clear README and documentation
