# Spotify Listening Intelligence Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-planned-336791.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-planned-FF4B4B.svg)
![Status](https://img.shields.io/badge/Status-Planning%20%26%20Setup-lightgrey.svg)

Product analytics, data engineering, predictive analytics, and business intelligence project using real Spotify listening data.

## Overview

Spotify listening history contains rich behavioral signals: repeat plays, saves, playlist additions, session length, device usage, artist loyalty, and discovery patterns. This project turns personal Spotify data into an analytics-ready platform for understanding engagement and retention-style behavior.

The project combines data from the Spotify Web API and Spotify account exports, models it in PostgreSQL, builds reusable SQL KPI views, and presents insights through analysis notebooks and a Streamlit dashboard.

## Business Problem

Music platforms depend on sustained engagement. This project investigates which listening behaviors are associated with:

- Repeat listening
- Strong track, artist, and genre engagement
- Playlist and saved-track retention signals
- Music discovery success
- Possible drop-off risk

The central question is:

> What listening behaviors predict engagement, repeat listening, playlist usage, and possible drop-off risk?

## Planned Analysis Questions

1. Which listening behaviors are associated with repeat listening?
2. Are saved tracks more likely to be replayed?
3. Are playlist-added tracks more likely to have long-term engagement?
4. Which artists or genres show the strongest retention?
5. Does device or platform affect skip behavior or session duration?
6. What types of sessions show high engagement?
7. Can a model predict whether a track or artist will be replayed within 30 days?
8. What product recommendations could improve retention and engagement?

## Data Sources

### Spotify Web API

Planned collection includes:

- User profile
- Playlists
- Playlist tracks
- Saved tracks
- Recently played tracks
- Top artists
- Top tracks
- Artist and track metadata where available

### Spotify Account Data Export

Planned parsing includes:

- Extended streaming history
- Track, artist, and album names
- Playback timestamp
- Milliseconds played
- Platform or device fields when available
- Country, shuffle, skip, and reason fields when available

Spotify does not provide full internal business data such as revenue, true churn, premium upgrades, randomized experiment assignment, or other users' listening history. This project is therefore framed as personal listening intelligence and observational product analysis.

## Analytics Scope

The MVP is designed to include:

- Spotify API data collection
- Spotify export parsing
- Raw and processed data storage
- PostgreSQL star schema
- SQL KPI layer
- Cohort retention analysis
- Funnel analysis
- Behavioral segmentation
- Predictive replay model
- Observational experiment-style analysis
- Streamlit dashboard
- Business recommendation report

## Data Model

The planned warehouse model uses a star schema.

Dimension tables:

- `dim_tracks`
- `dim_artists`
- `dim_albums`
- `dim_playlists`
- `dim_devices`
- `dim_dates`

Fact tables:

- `fact_listening_events`
- `fact_saved_tracks`
- `fact_playlist_tracks`
- `fact_sessions`

Listening sessions will be created by grouping events where the gap between plays is less than 30 minutes.

## KPI Framework

Engagement metrics:

- Listening hours
- Total plays
- Active listening days
- Sessions per day
- Average session duration
- Songs per session
- Average milliseconds played per track

Retention metrics:

- Repeat listen rate
- Track replay rate
- Artist replay rate
- Genre revisit rate

Content and behavior metrics:

- Save rate
- Playlist coverage rate
- Skip rate, if available
- Top genres, artists, and tracks

Device and platform metrics:

- Listening by device or platform
- Skip rate by device or platform, if available
- Session duration by device or platform

## Project Workflow

1. Set up repository structure and documentation.
2. Collect Spotify API data.
3. Download and parse Spotify account export data.
4. Clean, standardize, and sessionize listening events.
5. Load analytics-ready tables into PostgreSQL.
6. Build SQL views for reusable product metrics.
7. Analyze cohorts, funnels, and behavioral segments.
8. Train replay prediction models.
9. Run observational experiment-style comparisons.
10. Build a Streamlit dashboard.
11. Translate findings into business recommendations.

## Repository Structure

```text
spotify-listening-intelligence/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- .env.example
|-- docs/
|   |-- project_plan.md
|   |-- data_sources.md
|   |-- data_dictionary.md
|   `-- phase_updates.md
|-- data/
|   |-- raw/
|   |   |-- spotify_api/
|   |   `-- spotify_export/
|   |-- processed/
|   `-- outputs/
|-- notebooks/
|-- sql/
|-- src/
|   |-- __init__.py
|   |-- config.py
|   `-- utils.py
`-- dashboard/
```

## Tech Stack

| Category | Tools |
| --- | --- |
| Programming | Python |
| Data processing | pandas, NumPy |
| API collection | Spotify Web API, Spotipy, python-dotenv |
| Database | PostgreSQL, SQLAlchemy |
| Analytics | SQL |
| Statistics | scipy, statsmodels |
| Machine learning | scikit-learn, XGBoost optional |
| Visualization | Streamlit, Plotly, Matplotlib |

## Current Status

This repository is in the planning and setup phase. Existing documentation defines the project goal, data sources, build phases, planned data model, KPI framework, and final deliverables.

## Privacy Note

Raw Spotify exports and API outputs may contain personal listening history and account metadata. These files should remain local and are intentionally excluded from version control.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
