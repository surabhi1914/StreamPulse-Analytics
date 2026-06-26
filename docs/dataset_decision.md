# Dataset Decision

## Final Dataset

Last.fm-1K Listening Dataset

## Decision

Last.fm-1K is selected for the MVP.

## Phase 1 Validation

Phase 1 profiling confirmed that Last.fm-1K is suitable for the MVP.

The dataset contains enough users, listening events, and timestamp coverage to support:

- User-level engagement analysis
- Cohort retention analysis
- Funnel analysis
- User segmentation
- Artist and track replay analysis
- Predictive replay modeling
- Observational experiment-style analysis

Phase 1 confirmed these full-dataset profile values:

| Metric | Value |
|---|---:|
| Parsed listening events | 19,098,853 |
| Unique users | 992 |
| Unique artists | 173,921 |
| Unique tracks | 1,083,470 |
| Date range | 2005-02-14 to 2013-09-29 |

The dataset also requires careful handling of missing IDs:

- `artist_id` has missing values: 600,848 rows, 3.15%
- `track_id` has noticeable missing values: 2,162,719 rows, 11.32%
- `track_name` missingness is negligible relative to total rows: 210 rows, approximately 0.00%

Because of this, Phase 2 will define fallback identifier logic for artist and track analysis.

## Why Selected

It supports:

- Multiple users
- Timestamped listening events
- Repeat listening analysis
- Artist and track engagement
- User retention analysis
- User segmentation
- Predictive replay modeling
- SQL-based analytics
- Dashboard storytelling

## Why Personal Spotify Data Was Not Used

Personal Spotify data is limited to one user and cannot support strong product-level conclusions.

## Why KKBox Was Not Selected

KKBox is excellent for subscription churn, but the project goal is focused on music listening behavior, repeat listening, artist retention, and replay prediction.

## Why Spotify Million Playlist Dataset Was Not Selected

Spotify MPD is excellent for playlist and recommendation analysis, but weaker for user-level retention and time-based engagement analysis.

## Hybrid Decision

Hybrid approach is deferred.
Datasets should not be joined unless they share real user identifiers.

## Valid Analyses

- User engagement
- Repeat listening
- Artist retention
- Track replay
- Cohort retention
- Funnel analysis
- Segmentation
- Predictive replay modeling
- Observational experiment-style analysis

## Invalid / Unsupported Analyses

- Premium conversion
- Revenue analysis
- Saved-track analysis
- Playlist-add analysis
- Skip behavior analysis
- Device/platform analysis
- True causal A/B testing

## Limitations To Carry Forward

- The dataset is historical, so findings should be framed as a product analytics case study.
- The 100K-row sample is useful for schema inspection but not representative for user-level counts because the raw file appears ordered by `user_id`.
- Full-dataset statistics should come from chunked profiling results.
- Chunked parsing uses `on_bad_lines="skip"`, so malformed rows may be excluded from the parsed row count.
