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

## Phase 2 Cleaning Validation

Phase 2 further validated the decision to use Last.fm-1K for the MVP.

The full listening dataset was cleaned successfully using chunked processing. The cleaning process retained 19,098,642 valid listening events across 39 chunk files and removed only 211 rows with missing required fields.

The cleaned dataset contains complete values for the fields needed for core product analytics:

- `user_id`
- `timestamp`
- `artist_name`
- `track_name`
- `artist_key`
- `track_key`

Rows with missing `artist_id` or `track_id` were retained because fallback identifiers were created. This allows the project to preserve useful listening behavior while still supporting reliable artist-level and track-level analysis.

This confirms that Last.fm-1K is suitable for retention analysis, funnel analysis, behavioral segmentation, replay modeling, and analytics data modeling.

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
- Duplicate removal currently happens within each chunk. Global duplicate detection across chunks will be handled later during warehouse loading or SQL modeling if needed.
