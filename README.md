# StreamPulse Analytics

Product Analytics Platform for Music Streaming Behavior

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](requirements.txt)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-planned-336791.svg)](sql/schema.sql)
[![Streamlit](https://img.shields.io/badge/Streamlit-planned-FF4B4B.svg)](dashboard/streamlit_app.py)
[![Status](https://img.shields.io/badge/Status-Phase%201%20Complete-brightgreen.svg)](docs/phase_updates.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

StreamPulse Analytics is an end-to-end product analytics and data engineering project built on the Last.fm-1K listening dataset.

The project analyzes timestamped listening behavior across many users to understand repeat listening, retention, engagement patterns, user segments, and replay prediction.

## Business Problem

Music streaming platforms need to understand what behaviors lead to long-term engagement. This project asks:

> What listening behaviors drive repeat listening, long-term engagement, and user retention?

## Selected Dataset

The MVP uses the Last.fm-1K listening dataset because it contains user-level timestamped listening events with artist and track information.

Last.fm-1K supports product analytics questions that require many users and timestamped behavior. It is better suited for this MVP than single-user personal Spotify exports because it can support cohort analysis, retention-style analysis, segmentation, and replay prediction across listeners.

## Dataset Summary

Phase 1 profiling confirmed:

| Metric | Value |
|---|---:|
| Parsed listening events | 19,098,853 |
| Unique users | 992 |
| Unique artists | 173,921 |
| Unique tracks | 1,083,470 |
| Date range | 2005-02-14 to 2013-09-29 |

## Phase 1: Data Profiling Summary

Phase 1 focused on understanding the raw Last.fm-1K files before cleaning or modeling.

A 100K-row sample was used for schema inspection, while full-dataset profiling was performed with chunked processing to avoid loading the full listening file into memory.

Key findings:

- The dataset supports user-level product analytics because it includes user IDs and timestamped listening events.
- The dataset supports retention analysis because listening activity spans multiple years.
- Artist-level and track-level replay analysis are feasible.
- `artist_id` is missing in 600,848 rows, or 3.15% of parsed listening events.
- `track_id` is missing in 2,162,719 rows, or 11.32% of parsed listening events.
- `track_name` is missing in 210 rows, which is negligible relative to the full dataset size.
- Phase 2 will define fallback identifier logic for artist-level and track-level analysis.
- The dataset is historical, so final insights will be framed as a product analytics case study.

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

One ingestion limitation is that chunked parsing uses `on_bad_lines="skip"`, so malformed rows may be excluded from the parsed row count.

## Target Skills Demonstrated

- Product analytics
- Data engineering
- SQL analytics
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
Next: Phase 2: Data cleaning and transformation
