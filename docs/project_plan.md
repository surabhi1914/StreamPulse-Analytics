# StreamPulse Analytics

## Product Analytics Platform for Music Streaming Behavior

---

## 1. Project Goal

Build an end-to-end product analytics and data engineering project for a music streaming platform using a large real-world public listening dataset.

The project will analyze user behavior, engagement, repeat listening, retention patterns, user segmentation, predictive replay behavior, and product recommendations.

The main question is:

> What listening behaviors drive repeat listening, long-term engagement, and user retention in a music streaming platform?

---

## 2. Selected Dataset

## Last.fm-1K Listening Dataset

The MVP will use the Last.fm-1K listening dataset as the main dataset.

This dataset is selected because it supports user-level behavioral analytics with:

- Multiple users
- Timestamped listening events
- Artist information
- Track/song information
- User listening histories over time

This makes it suitable for:

- SQL-based KPI analysis
- Cohort retention analysis
- Funnel analysis
- User segmentation
- Predictive replay modeling
- Observational experiment-style analysis
- Streamlit dashboard storytelling
- Business recommendation reporting

---

## 3. Why This Dataset Was Selected

The updated project uses Last.fm-1K because it contains listening behavior across many users.

This allows the project to ask stronger product analytics questions such as:

- Which users retain over time?
- Which early behaviors predict long-term engagement?
- Which artists or tracks drive repeat listening?
- Which listener segments are at risk of inactivity?
- Can we predict whether a user will replay an artist or track?

---

## 4. Target Skills / Keywords

This project is designed to demonstrate:

- SQL at scale
- Product analytics
- KPI design
- User behavior analysis
- Cohort analysis
- Retention analysis
- Funnel analysis
- Segmentation
- Inactivity prediction
- Predictive replay modeling
- Data modeling
- Star schema design
- Data pipelines
- Predictive analytics
- Experimentation-style observational analysis
- Stakeholder reporting
- Business recommendations
- Dashboard storytelling
- Data storytelling

---

## 5. Project Direction

## StreamPulse Analytics

A product analytics and data engineering platform for music streaming behavior.

The project will analyze Last.fm listening behavior to understand:

- User engagement
- Listening frequency
- Repeat listening behavior
- Artist loyalty
- Track replay behavior
- User retention
- User inactivity risk
- Listening funnels
- Behavioral segments
- Product opportunities to improve engagement

---

## 6. Main Business Questions

The project will focus on business questions that are valid for the Last.fm-1K dataset.

1. Which listener behaviors are associated with long-term retention?
2. Do high first-week activity users retain better than low first-week activity users?
3. Which users are most likely to become inactive?
4. Which tracks and artists are most likely to be replayed within 30 days?
5. Which artists create the strongest repeat engagement?
6. Do users with higher artist diversity remain active longer?
7. What listener segments exist based on behavior?
8. Where do users drop off between first activity and long-term engagement?
9. Can a model predict whether a user will replay an artist or track within 30 days?
10. What product actions could improve repeat listening and user retention?

---

## 7. MVP Scope

The MVP will include:

1. Data ingestion and profiling
2. Data cleaning and validation
3. PostgreSQL data modeling
4. SQL-based KPI layer
5. Cohort retention analysis
6. Funnel analysis
7. User segmentation
8. Predictive replay model
9. Observational experiment-style analysis
10. Streamlit dashboard
11. Business recommendation report
12. README updates after every major phase

---

## 8. Non-Goals

The MVP will not include:

- Real-time streaming pipelines
- Production-scale orchestration
- Deep learning models
- Complex recommendation systems
- Fake joins between unrelated datasets
- Claims about saved tracks, playlist adds, skips, devices, or premium conversion
- Claims of causality from observational analysis
- Overly complex infrastructure before the core analytics is strong

Optional future modules may use other datasets, but the MVP will stay focused on Last.fm-1K.

---

# Phase -1: Dataset Evaluation and Decision

## Goal

Evaluate candidate datasets and select the dataset that best supports the project.

---

## Candidate Datasets Considered

### Candidate 1: Last.fm-1K Listening Dataset

Best for:

- User listening behavior
- Repeat listening
- Artist retention
- Track replay behavior
- Sessionization
- User segmentation
- Predictive replay modeling
- Retention-style analysis

Decision:

> Selected for MVP.

Reason:

Last.fm-1K supports the strongest version of this project because it has user-level timestamped listening events.

---

### Candidate 2: KKBox Churn Dataset

Best for:

- Subscription churn prediction
- Renewal behavior
- Paid-user lifecycle analysis
- Transaction-based product analytics

Decision:

> Not selected for MVP.

Reason:

KKBox is strong for subscription churn, but weaker for detailed music listening behavior, repeat listening, artist retention, and track replay modeling.

Possible future project:

> Music Subscription Churn Intelligence

---

### Candidate 3: Spotify Million Playlist Dataset

Best for:

- Playlist analytics
- Track co-occurrence
- Recommendation analysis
- Playlist continuation

Decision:

> Not selected for MVP.

Reason:

Spotify Million Playlist Dataset is strong for playlist/recommendation work, but weaker for user-level retention, churn, funnels, and time-based replay prediction.

Possible future project:

> Playlist Recommendation Intelligence

---

### Candidate 4: Hybrid Approach

A hybrid approach could use:

- Last.fm for listening behavior and retention
- KKBox for churn/subscription analytics
- Spotify Million Playlist Dataset for playlist/recommendation analytics

Decision:

> Not used for MVP.

Reason:

Hybrid datasets should not be joined at the user level unless they share real user identifiers.

For this MVP, using one dataset makes the project cleaner, more honest, and easier to explain in interviews.

Hybrid can be added later as separate modules, not as fake merged data.

---

## Phase -1 Deliverables

Create:

```text
docs/source_assessment.md
docs/dataset_decision.md
```

### `docs/source_assessment.md`

Should include:

- Dataset name
- Source link
- Dataset owner/source
- File format
- File size
- Number of users
- Number of listening events
- Available fields
- Missing fields
- Pros
- Cons
- Possible analyses
- Risks

### `docs/dataset_decision.md`

Should include:

- Final dataset selected
- Why Last.fm-1K was selected
- Why KKBox was not selected for MVP
- Why Spotify Million Playlist Dataset was not selected for MVP
- Why hybrid is deferred
- What analyses are valid
- What analyses are not valid
- Final MVP project scope

---

## README Update After Phase -1

Add:

```markdown
## Dataset Selection

Before implementation, multiple music datasets were evaluated to ensure the project supported realistic product analytics workflows.

Datasets considered:

- Last.fm-1K listening dataset
- KKBox churn dataset
- Spotify Million Playlist Dataset
- Hybrid approach

Last.fm-1K was selected for the MVP because it supports user-level listening behavior, timestamped activity, retention analysis, replay prediction, segmentation, and funnel analysis.

The project does not claim to analyze saved tracks, playlist additions, skip behavior, devices, premium conversion, or revenue because those fields are not available in the selected dataset.
```

---

# Phase 0: Project Setup

## Goal

Set up a clean project structure for the Last.fm-based analytics project.

---

## Deliverables

- GitHub repository
- README v0
- `.gitignore`
- `requirements.txt`
- `docs/project_plan.md`
- `docs/source_assessment.md`
- `docs/dataset_decision.md`
- `docs/data_dictionary.md`
- `docs/phase_updates.md`

---

## Repository Name

Recommended:

```text
streampulse-analytics
```

Alternative names:

```text
music-streaming-analytics
streaming-retention-intelligence
music-product-analytics
listener-retention-analytics
```

---

## Suggested Repository Structure

```text
streampulse-analytics/
â”‚
â”œâ”€â”€ README.md
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ .gitignore
â”‚
â”œâ”€â”€ docs/
â”‚   â”œâ”€â”€ project_plan.md
â”‚   â”œâ”€â”€ source_assessment.md
â”‚   â”œâ”€â”€ dataset_decision.md
â”‚   â”œâ”€â”€ data_dictionary.md
â”‚   â”œâ”€â”€ phase_updates.md
â”‚   â””â”€â”€ business_recommendations.md
â”‚
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ raw/
â”‚   â”œâ”€â”€ processed/
â”‚   â”œâ”€â”€ warehouse/
â”‚   â””â”€â”€ outputs/
â”‚
â”œâ”€â”€ notebooks/
â”‚   â”œâ”€â”€ 01_data_profile.ipynb
â”‚   â”œâ”€â”€ 02_data_cleaning.ipynb
â”‚   â”œâ”€â”€ 03_data_modeling.ipynb
â”‚   â”œâ”€â”€ 04_kpi_analysis.ipynb
â”‚   â”œâ”€â”€ 05_cohort_retention.ipynb
â”‚   â”œâ”€â”€ 06_funnel_analysis.ipynb
â”‚   â”œâ”€â”€ 07_segmentation.ipynb
â”‚   â”œâ”€â”€ 08_replay_prediction.ipynb
â”‚   â”œâ”€â”€ 09_experiment_analysis.ipynb
â”‚   â””â”€â”€ 10_dashboard_prep.ipynb
â”‚
â”œâ”€â”€ sql/
â”‚   â”œâ”€â”€ schema.sql
â”‚   â”œâ”€â”€ views_kpis.sql
â”‚   â”œâ”€â”€ cohort_queries.sql
â”‚   â”œâ”€â”€ funnel_queries.sql
â”‚   â”œâ”€â”€ segmentation_queries.sql
â”‚   â”œâ”€â”€ replay_prediction_queries.sql
â”‚   â””â”€â”€ experiment_queries.sql
â”‚
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ config.py
â”‚   â”œâ”€â”€ ingest.py
â”‚   â”œâ”€â”€ clean.py
â”‚   â”œâ”€â”€ transform.py
â”‚   â”œâ”€â”€ load_postgres.py
â”‚   â”œâ”€â”€ sessionize.py
â”‚   â”œâ”€â”€ features.py
â”‚   â”œâ”€â”€ modeling.py
â”‚   â”œâ”€â”€ evaluation.py
â”‚   â””â”€â”€ utils.py
â”‚
â””â”€â”€ dashboard/
    â””â”€â”€ streamlit_app.py
```

---

# Phase 1: Data Ingestion and Data Profiling

## Goal

Load the Last.fm-1K dataset, inspect its structure, and create an initial data profile.

---

## Expected Raw Files

Depending on the dataset version, expected files may include:

```text
userid-timestamp-artid-artname-traid-traname.tsv
userid-profile.tsv
```

---

## Tasks

- Download Last.fm-1K dataset
- Place raw files in `data/raw/lastfm_1k/`
- Inspect file structure
- Check row counts
- Check column names
- Check missing values
- Check duplicate records
- Check date ranges
- Check number of users
- Check number of artists
- Check number of tracks
- Check user profile fields, if available
- Identify columns that can be used for modeling

---

## Deliverables

- `notebooks/01_data_profile.ipynb`
- `src/ingest.py`
- Initial data profile summary
- Raw data inventory
- Updated data dictionary

---

## README Update

Add:

- Dataset selected
- Why selected
- Dataset size
- Available fields
- Initial observations
- Dataset limitations

---


## Phase 1 Profiling Update

Status: Complete

Phase 1 confirmed that the Last.fm-1K dataset is large enough and structured enough for the MVP. Full-dataset profiling found 19,098,853 parsed listening events, 992 users, 173,921 artists, 1,083,470 tracks, and activity from 2005-02-14 to 2013-09-29.

Phase 2 is complete. It cleaned the full listening dataset into 39 chunk files and created fallback `artist_key` and `track_key` values for rows with missing IDs.
---

# Phase 2: Data Cleaning and Transformation

## Goal

Clean raw Last.fm data and create reliable processed datasets.

---

## Tasks

- Standardize column names
- Convert listening timestamps
- Remove invalid records
- Handle missing artists/tracks
- Deduplicate exact duplicate events if needed
- Normalize artist and track text fields
- Create derived date fields
- Create user-level activity fields
- Save cleaned data to `data/processed/`

---

## Important Cleaning Decisions

The project should document:

- How missing track IDs are handled
- Whether missing track names are retained or removed
- Whether duplicate listening events are removed
- How timestamps are converted
- How date ranges are filtered
- How users with extremely low activity are handled

---

## Deliverables

- `notebooks/02_data_cleaning.ipynb`
- `src/clean.py`
- `src/transform.py`
- Cleaned datasets
- Data quality report

---

## README Update

Add:

- Cleaning decisions
- Important data issues found
- How missing values were handled
- Data quality checks

---


## Phase 2 Cleaning Update

Status: Complete

Phase 2 cleaned the Last.fm-1K profile data, a 100K-row listening sample, and the full listening dataset. Full-file cleaning retained 19,098,642 valid listening events across 39 cleaned chunk files and removed 211 rows missing required fields.

Rows with missing `artist_id` or `track_id` were retained by creating fallback `artist_key` and `track_key` values. Global duplicate detection across chunks will be handled later during warehouse loading or SQL modeling if needed.

Phase 3 is the next active phase and will focus on analytics data modeling.
---

# Phase 3: Analytics Data Modeling

## Goal

Transform cleaned Last.fm data into analytics-ready tables.

---

## Dimension Tables

```text
dim_users
dim_artists
dim_tracks
dim_dates
```

Optional:

```text
dim_user_profiles
```

---

## Fact Tables

```text
fact_listening_events
fact_sessions
fact_user_daily_activity
fact_user_artist_activity
fact_user_track_activity
```

---

## Session Definition

A listening session will be created by grouping events for the same user where the time gap between consecutive listening events is less than 30 minutes.

Example:

```text
If a user listens to multiple tracks within 30 minutes, those events belong to the same session.
If the gap is more than 30 minutes, a new session begins.
```

This threshold can be adjusted during analysis.

---

## Core Modeling Principles

- Keep raw data immutable.
- Separate facts and dimensions.
- Create reproducible transformations.
- Use clear primary keys and foreign keys.
- Document every table.
- Avoid over-modeling before analysis needs are clear.
- Build the model around business questions, not just data availability.

---

## Deliverables

- `sql/schema.sql`
- `src/load_postgres.py`
- PostgreSQL database
- Star schema
- `docs/data_dictionary.md`

---

## README Update

Add:

- Data model overview
- Table descriptions
- Sessionization logic
- Schema diagram, if available

---

# Phase 4: Product Metrics Layer

## Goal

Create reusable SQL views for product analytics.

---

## KPI Views

```text
daily_platform_kpis
weekly_platform_kpis
monthly_platform_kpis
user_engagement_kpis
artist_engagement_kpis
track_replay_kpis
session_kpis
retention_kpis
```

---

## Metrics

Platform engagement:

- Total users
- Active users
- Daily active users
- Weekly active users
- Monthly active users
- Total listening events
- Total active days
- Average events per active user
- Average active days per user

User engagement:

- Total listens per user
- Active days per user
- Unique artists per user
- Unique tracks per user
- Repeat artist rate
- Repeat track rate
- Average listens per active day
- Days since last activity

Session metrics:

- Total sessions
- Sessions per user
- Average session length
- Events per session
- Long-session rate

Content metrics:

- Top artists
- Top tracks
- Artist replay rate
- Track replay rate
- Artist retention rate
- Track retention rate

Retention metrics:

- D1 retention
- D7 retention
- D30 retention
- Weekly retention
- Monthly retention
- Returning listener rate

---

## Deliverables

- `sql/views_kpis.sql`
- KPI tables/views
- KPI definitions document
- Example metric outputs

---

## README Update

Add:

- KPI framework
- Metric definitions
- Example business interpretation

---

# Phase 5: Cohort Retention Analysis

## Goal

Analyze how listening behavior changes over time and identify which user groups retain better.

---

## Cohorts

User-level cohorts:

- First listening month cohort
- First listening week cohort
- High first-week activity users
- Medium first-week activity users
- Low first-week activity users
- High artist-diversity users
- Low artist-diversity users
- Repeat-heavy listeners
- Discovery-heavy listeners

Artist-level cohorts:

- Artists first discovered by users
- High early-repeat artists
- Low early-repeat artists
- Popular artists
- Niche artists

---

## Retention Windows

Measure retention over:

- Day 1
- Day 7
- Day 14
- Day 30
- Week 1
- Week 4
- Month 1
- Month 3

---

## Main Questions

- Which user cohorts retain better?
- Does high first-week activity predict long-term retention?
- Do users with high artist diversity remain active longer?
- Do repeat-heavy listeners retain better than discovery-heavy listeners?
- Which artists drive longer-term repeat engagement?

---

## Deliverables

- `sql/cohort_queries.sql`
- Retention cohort tables
- Retention heatmap data
- Interpretation of cohort trends

---

## README Update

Add:

- Cohort definitions
- Retention heatmap
- Key findings
- Limitations

---

# Phase 6: Funnel Analysis

## Goal

Analyze user progression through key engagement steps.

---

## Funnel 1: User Engagement Funnel

```text
First listening event
â†’ second active day
â†’ 7 active days
â†’ 30 active days
â†’ active after 90 days
```

---

## Funnel 2: Artist Engagement Funnel

```text
First artist listen
â†’ second artist listen
â†’ 5+ artist listens
â†’ listens across multiple weeks
â†’ artist replay within 30 days
```

---

## Funnel 3: Repeat Listening Funnel

```text
First track listen
â†’ second track listen
â†’ 3+ track listens
â†’ replay within 7 days
â†’ replay within 30 days
```

---

## Main Questions

- Where do users drop off?
- Which funnel step has the largest conversion loss?
- Which behaviors are associated with long-term retention?
- Which stage should the product improve first?

---

## Deliverables

- `sql/funnel_queries.sql`
- Funnel conversion table
- Drop-off analysis
- Product recommendation

---

## README Update

Add:

- Funnel design
- Conversion rates
- Biggest drop-off
- Business recommendation

---

# Phase 7: User Segmentation

## Goal

Cluster users into meaningful listener segments.

---

## Feature Ideas

- Total listening events
- Active days
- Listening span in days
- Average events per active day
- Session count
- Average session length
- Unique artists
- Unique tracks
- Artist diversity ratio
- Track diversity ratio
- Repeat artist rate
- Repeat track rate
- Weekend listening share
- Night listening share
- Days since last activity
- 30-day inactivity flag

---

## Possible Segments

Final segment names should come from the data.

Possible examples:

- Power listeners
- Casual listeners
- At-risk users
- Artist loyalists
- Track repeaters
- Music explorers
- Weekend listeners
- Short-session users
- Dormant users

---

## Methods

- Feature engineering
- StandardScaler
- KMeans
- PCA
- Segment profiling

---

## Deliverables

- `notebooks/07_segmentation.ipynb`
- `src/features.py`
- User feature table
- Segment labels
- Segment summary table
- Segment visualization

---

## README Update

Add:

- Features used
- Segment descriptions
- Business meaning of each segment
- How segments could guide product strategy

---

# Phase 8: Predictive Replay Modeling

## Goal

Predict whether a user will replay an artist or track within 30 days.

---

## Primary Prediction Target

```text
artist_replayed_30d
```

Definition:

```text
For a user-artist first-listen event, predict whether the same user listens to the same artist again within 30 days.
```

---

## Optional Prediction Target

```text
track_replayed_30d
```

Definition:

```text
For a user-track first-listen event, predict whether the same user listens to the same track again within 30 days.
```

---

## Feature Ideas

User features:

- User total prior listens
- User active days before event
- User unique artists before event
- User unique tracks before event
- User repeat artist rate before event
- User repeat track rate before event
- User average events per active day

Artist/track features:

- Artist popularity in dataset
- Track popularity in dataset
- Artist prior familiarity for user
- Track prior familiarity for user
- Number of first-day listens
- Number of first-week listens

Time/session features:

- Day of week
- Hour of day
- Weekend flag
- Session length
- Event position in session
- Time since previous listening event

---

## Models

Start simple:

- Logistic Regression

Then compare with:

- Random Forest
- XGBoost

---

## Evaluation

Use:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix
- Feature importance

Important:

> The model should be evaluated honestly. A simple interpretable model with strong explanation is better than a complex model with unclear business value.

---

## Deliverables

- `notebooks/08_replay_prediction.ipynb`
- `src/modeling.py`
- Model comparison table
- Feature importance chart
- Error analysis
- Business interpretation

---

## README Update

Add:

- Prediction task
- Target definition
- Model results
- Important features
- Limitations

---

# Phase 9: Experimentation-Style Observational Analysis

## Goal

Demonstrate experimentation thinking using observational data.

---

## Important Limitation

The dataset does not include real randomized A/B test assignment.

This phase should be described as:

> Observational experiment-style analysis, not a causal A/B test.

---

## Hypothesis 1

> High first-week activity users have higher 90-day retention than low first-week activity users.

Groups:

```text
Treatment-like group: users in top activity tier during first week
Control-like group: users in low activity tier during first week
```

---

## Hypothesis 2

> Users with high artist diversity are more likely to remain active than users with low artist diversity.

Groups:

```text
Treatment-like group: high artist-diversity users
Control-like group: low artist-diversity users
```

---

## Hypothesis 3

> Users who replay an artist within 24 hours are more likely to stay active after 30 days.

Groups:

```text
Treatment-like group: users with 24-hour artist replay
Control-like group: users without 24-hour artist replay
```

---

## Analysis Methods

- Treatment-like group vs control-like group
- Retention rate comparison
- Replay rate comparison
- Lift calculation
- Confidence intervals
- p-values
- Effect size
- Clear non-causal interpretation

---

## Deliverables

- `notebooks/09_experiment_analysis.ipynb`
- `sql/experiment_queries.sql`
- Hypothesis test results
- Interpretation and limitation statement

---

## README Update

Add:

- Hypothesis
- Method
- Result
- Limitation: observational, not causal

---

# Phase 10: Executive Dashboard

## Goal

Create a dashboard that tells a clear product analytics story.

---

## Tool

Build first with:

```text
Streamlit
```

Optional later:

```text
Power BI
Tableau
```

---

## Dashboard Pages

1. Executive Overview
2. User Engagement
3. Retention Cohorts
4. Funnel Analysis
5. User Segments
6. Replay Prediction
7. Experimentation Analysis
8. Business Recommendations

---

## Dashboard Metrics

Executive overview:

- Total users
- Total listening events
- Total artists
- Total tracks
- Active users
- Returning listener rate
- Average events per user
- Average active days per user

Engagement:

- Listening events over time
- Active users over time
- Sessions over time
- Top artists
- Top tracks
- Repeat artist rate
- Repeat track rate

Retention:

- Cohort retention heatmap
- D7 retention
- D30 retention
- 90-day active rate

Segmentation:

- Segment sizes
- Segment profiles
- Segment retention comparison

Prediction:

- Replay model performance
- Feature importance
- High-probability replay examples

Experimentation:

- Hypothesis results
- Lift
- Confidence intervals
- Interpretation

---

## Deliverables

- `dashboard/streamlit_app.py`
- Dashboard screenshots
- Dashboard GIF or demo video
- Dashboard run instructions

---

## README Update

Add:

- Dashboard screenshots
- How to run dashboard
- Summary of what the dashboard shows

---

# Phase 11: Business Recommendations

## Goal

Translate analysis into product recommendations.

---

## Questions to Answer

1. Which listener behaviors are strongest indicators of long-term retention?
2. Do high first-week activity users retain better?
3. Do users with higher artist diversity remain active longer?
4. Which artists or tracks create the strongest replay behavior?
5. Where do users drop off in the engagement funnel?
6. Which listener segments are most at risk of inactivity?
7. What product actions could improve repeat listening and retention?

---

## Recommendation Format

Each recommendation should follow this structure:

```text
Finding:
Evidence:
Business interpretation:
Recommendation:
Expected impact:
Limitation:
```

---

## Example

```text
Finding:
Users with high first-week listening activity had stronger 90-day retention.

Evidence:
High first-week activity users retained at X%, compared with Y% for low first-week activity users.

Business interpretation:
Early engagement appears to be a strong signal of long-term listening behavior.

Recommendation:
The product team could design onboarding experiences that encourage users to complete multiple listening sessions in their first week.

Expected impact:
Improving first-week engagement may increase long-term retention.

Limitation:
This is observational analysis and does not prove causality.
```

---

## Deliverables

- `docs/business_recommendations.md`
- Final README insights section
- LinkedIn-ready project summary
- Resume bullets

---

## README Update

Add:

- Final findings
- Business recommendations
- Project limitations
- Future improvements

---

# Final Tech Stack

## Data Processing

- Python
- Pandas
- NumPy

## Database

- PostgreSQL
- SQLAlchemy

## Analytics

- SQL
- scipy
- statsmodels

## Machine Learning

- scikit-learn
- XGBoost optional

## Visualization

- Streamlit
- Plotly
- Matplotlib

## Documentation

- Markdown
- README
- Data dictionary
- Phase updates

## Optional Later

- Airflow for orchestration
- AWS S3 for storage
- AWS RDS for PostgreSQL
- Streamlit Cloud or Render for deployment

---

# MVP Scope

The MVP should include:

1. Dataset decision documentation
2. Data ingestion
3. Data profiling
4. Data cleaning
5. PostgreSQL data model
6. SQL KPI views
7. Cohort retention analysis
8. Funnel analysis
9. User segmentation
10. Predictive replay model
11. Experimentation-style observational analysis
12. Streamlit dashboard
13. Business recommendations
14. Strong README documentation

---

# Optional Future Extensions

After the MVP is complete, possible extensions include:

## Spotify Music Streaming Sessions Dataset Module

Use for:

- Skip behavior
- Session interaction analysis
- Recommendation interaction analysis

## Spotify Million Playlist Dataset Module

Use for:

- Playlist continuation
- Track co-occurrence
- Playlist recommendation analytics

## KKBox Churn Dataset Project

Use as a separate project for:

- Subscription churn prediction
- Renewal behavior
- Monetization analytics

These extensions should be separate modules or separate projects unless the datasets share real user identifiers.

---

# Updated Build Order

```text
[x] Phase -1: Dataset decision documentation
[x] Phase 0: Project setup
[x] Phase 1: Data ingestion and profiling
[x] Phase 2: Data cleaning and transformation
[ ] Phase 3: Analytics data modeling (next)
[ ] Phase 4: Product metrics layer
[ ] Phase 5: Cohort retention analysis
[ ] Phase 6: Funnel analysis
[ ] Phase 7: User segmentation
[ ] Phase 8: Predictive replay modeling
[ ] Phase 9: Experimentation-style observational analysis
[ ] Phase 10: Executive dashboard
[ ] Phase 11: Business recommendations
[ ] Final: README polish, screenshots, resume bullets, LinkedIn post
```

---

# Project Success Criteria

This project is successful if it demonstrates:

1. A thoughtful dataset selection process
2. Clear reasoning about what analyses are valid
3. Clean data pipeline from raw data to analytics-ready tables
4. Strong SQL analytics layer
5. Clear KPI definitions
6. User-level cohort retention analysis
7. Funnel analysis with business interpretation
8. Meaningful user segmentation
9. Predictive replay modeling with honest evaluation
10. Experimentation-style thinking without false causal claims
11. Executive dashboard storytelling
12. Business recommendations supported by data
13. Clean GitHub repository structure
14. Strong README documentation
15. Resume-ready and interview-discussable project narrative

---


