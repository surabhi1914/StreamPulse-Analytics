# StreamPulse Analytics

Product Analytics Platform for Music Streaming Behavior

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](requirements.txt)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-planned-336791.svg)](sql/schema.sql)
[![Streamlit](https://img.shields.io/badge/Streamlit-planned-FF4B4B.svg)](dashboard/streamlit_app.py)
[![Status](https://img.shields.io/badge/Status-Phase%202%20Complete-brightgreen.svg)](docs/phase_updates.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

StreamPulse Analytics is an end-to-end product analytics and data engineering project built on the Last.fm-1K listening dataset.

The project analyzes timestamped listening behavior across many users to understand repeat listening, retention, engagement patterns, user segments, and replay prediction.

## Business Problem

Music streaming platforms need to understand what behaviors lead to long-term engagement. This project asks:

> What listening behaviors drive repeat listening, long-term engagement, and user retention?

## Selected Dataset

The MVP uses the Last.fm-1K listening dataset because it contains user-level timestamped listening events with artist and track information.

Last.fm-1K supports product analytics questions that require many users and timestamped behavior. It can support cohort analysis, retention-style analysis, segmentation, and replay prediction across listeners.

## Dataset Summary

Phase 1 profiling confirmed:

| Metric | Value |
|---|---:|
| Parsed listening events | 19,098,853 |
| Unique users | 992 |
| Unique artists | 173,921 |
| Unique tracks | 1,083,470 |
| Date range | 2005-02-14 to 2013-09-29 |

## Phase 2: Data Cleaning Summary

Phase 2 converted the raw Last.fm-1K files into analysis-ready processed outputs.

The user profile data was cleaned by standardizing dates, numeric age values, and text fields. Listening events were cleaned by parsing timestamps, removing rows missing required fields, creating fallback artist and track keys, and saving cleaned outputs.

Because the full listening events file is large, full-file cleaning was performed with chunked processing instead of loading all rows into memory at once.

| Metric | Value |
|---|---:|
| Raw parsed listening rows | 19,098,853 |
| Cleaned listening rows saved | 19,098,642 |
| Rows removed | 211 |
| Cleaned chunk files | 39 |
| Cleaned date range | 2005-02-14 to 2013-09-29 |
| Missing required fields after cleaning | 0 |
| Missing artist keys after cleaning | 0 |
| Missing track keys after cleaning | 0 |

Rows with missing `artist_id` or `track_id` were retained because fallback `artist_key` and `track_key` values were created from artist and track names.

## Dataset Limitations

This dataset does not include:

- Saved or liked tracks
- Playlist additions
- Skip behavior
- Device or platform
- Subscription plan
- Premium conversion
- Revenue
- True churn/cancellation labels
- Real A/B test assignment

Because of this, the project focuses on valid analyses such as listening engagement, retention, replay behavior, segmentation, inactivity risk, and observational experimentation.

The dataset is historical, so findings will be framed as a product analytics case study. One ingestion limitation is that chunked parsing uses `on_bad_lines="skip"`, so malformed rows may be excluded from the parsed row count.

## Target Skills Demonstrated

- Product analytics
- Data engineering
- SQL analytics
- Data cleaning and validation
- Data modeling
- KPI design
- Cohort retention analysis
- Funnel analysis
- User segmentation
- Predictive modeling
- Experimentation-style observational analysis
- Streamlit dashboarding
- Business recommendation writing

## MVP Scope

The MVP will include data ingestion and profiling, cleaning, PostgreSQL modeling, KPI views, cohort retention, funnel analysis, user segmentation, replay prediction, observational experiment-style analysis, an executive dashboard, and business recommendations.

## Project Roadmap

1. Phase -1: Dataset decision documentation
2. Phase 0: Project setup
3. Phase 1: Data ingestion and profiling
4. Phase 2: Data cleaning and transformation
5. Phase 3: Analytics data modeling
6. Phase 4: Product metrics layer
7. Phase 5: Cohort retention analysis
8. Phase 6: Funnel analysis
9. Phase 7: User segmentation
10. Phase 8: Predictive replay modeling
11. Phase 9: Experimentation-style observational analysis
12. Phase 10: Executive dashboard
13. Phase 11: Business recommendations

## Repository Structure

```text
streampulse-analytics/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- docs/
|   |-- project_plan.md
|   |-- source_assessment.md
|   |-- dataset_decision.md
|   |-- data_dictionary.md
|   |-- phase_updates.md
|   `-- business_recommendations.md
|-- data/
|   |-- raw/
|   |   `-- lastfm_1k/
|   |-- processed/
|   |-- warehouse/
|   `-- outputs/
|-- notebooks/
|-- sql/
|-- src/
`-- dashboard/
```

## Tech Stack

| Category | Tools |
| --- | --- |
| Programming | Python |
| Data processing | pandas, NumPy |
| Database | PostgreSQL, SQLAlchemy |
| Analytics | SQL |
| Statistics | scipy, statsmodels |
| Machine learning | scikit-learn, XGBoost |
| Visualization | Streamlit, Plotly, Matplotlib |
| Workflow | Jupyter, ipykernel |

## Data Privacy And Raw Data Note

Raw Last.fm files should be placed in `data/raw/lastfm_1k/` locally only. Raw, processed, warehouse, and output data files are ignored by Git so the repository stays lightweight and does not commit datasets or generated artifacts.

## Project Status

Complete: Phase -1: Dataset selected  
Complete: Phase 0: Project setup complete  
Complete: Phase 1: Data ingestion and profiling complete  
Complete: Phase 2: Data cleaning and transformation complete  
Next: Phase 3: Analytics data modeling
