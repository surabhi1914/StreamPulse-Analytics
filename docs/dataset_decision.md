# Dataset Decision

## Final Dataset

Last.fm-1K Listening Dataset

## Decision

Last.fm-1K is selected for the MVP.

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
