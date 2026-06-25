# StreamPulse Analytics

Product Analytics Platform for Music Streaming Behavior

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](requirements.txt)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-planned-336791.svg)](sql/schema.sql)
[![Streamlit](https://img.shields.io/badge/Streamlit-planned-FF4B4B.svg)](dashboard/streamlit_app.py)
[![Status](https://img.shields.io/badge/Status-Phase%200-lightgrey.svg)](docs/phase_updates.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

StreamPulse Analytics is an end-to-end product analytics and data engineering project built on the Last.fm-1K listening dataset.

The project analyzes timestamped listening behavior across many users to understand repeat listening, retention, engagement patterns, user segments, and replay prediction.

## Business Problem

Music streaming platforms need to understand what behaviors lead to long-term engagement. This project asks:

> What listening behaviors drive repeat listening, long-term engagement, and user retention?

## Selected Dataset

The MVP uses the Last.fm-1K listening dataset because it contains user-level timestamped listening events with artist and track information.

## Why Last.fm-1K Was Selected

Last.fm-1K supports product analytics questions that require many users and timestamped behavior. It is better suited for this MVP than single-user personal Spotify exports because it can support cohort analysis, retention-style analysis, segmentation, and replay prediction across listeners.

## What The Dataset Supports

- User engagement analysis
- Repeat listening analysis
- Artist and track replay behavior
- Cohort retention analysis
- Listening funnel analysis
- User segmentation
- Predictive replay modeling
- SQL-based analytics and dashboard storytelling

## Important Limitation

The dataset does not include saved tracks, playlist additions, skip behavior, device/platform, subscription plan, premium conversion, revenue, or real A/B test assignment.

Because of this, the project avoids unsupported claims and focuses on valid analyses such as retention, replay behavior, listening funnels, segmentation, and predictive replay modeling.

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
|   |-- 01_data_profile.ipynb
|   |-- 02_data_cleaning.ipynb
|   |-- 03_data_modeling.ipynb
|   |-- 04_kpi_analysis.ipynb
|   |-- 05_cohort_retention.ipynb
|   |-- 06_funnel_analysis.ipynb
|   |-- 07_segmentation.ipynb
|   |-- 08_replay_prediction.ipynb
|   |-- 09_experiment_analysis.ipynb
|   `-- 10_dashboard_prep.ipynb
|-- sql/
|   |-- schema.sql
|   |-- views_kpis.sql
|   |-- cohort_queries.sql
|   |-- funnel_queries.sql
|   |-- segmentation_queries.sql
|   |-- replay_prediction_queries.sql
|   `-- experiment_queries.sql
|-- src/
|   |-- __init__.py
|   |-- config.py
|   |-- ingest.py
|   |-- clean.py
|   |-- transform.py
|   |-- load_postgres.py
|   |-- sessionize.py
|   |-- features.py
|   |-- modeling.py
|   |-- evaluation.py
|   `-- utils.py
`-- dashboard/
    `-- streamlit_app.py
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
In progress: Phase 0: Project setup in progress  
Not started: Phase 1: Data ingestion and profiling
