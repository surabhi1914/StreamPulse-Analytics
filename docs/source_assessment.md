# Source Assessment

## Goal

Evaluate candidate datasets and select the best one for a senior-level product analytics project.

## Candidate 1: Last.fm-1K Listening Dataset

Status: Selected for MVP

Strengths:
- User-level listening behavior
- Timestamped activity
- Artist and track information
- Supports retention analysis
- Supports repeat listening analysis
- Supports segmentation
- Supports predictive replay modeling

Limitations:
- No subscription data
- No revenue data
- No saved-track data
- No playlist-add data
- No skip behavior
- No device/platform
- No real churn label

## Candidate 2: KKBox Churn Dataset

Status: Not selected for MVP

Strengths:
- Strong for churn prediction
- Strong for subscription analytics
- Useful for renewal behavior

Limitations:
- Less focused on detailed music listening behavior
- Less ideal for artist/track replay modeling

Possible future project:
Music Subscription Churn Intelligence

## Candidate 3: Spotify Million Playlist Dataset

Status: Not selected for MVP

Strengths:
- Strong for playlist analytics
- Strong for recommendation analysis
- Large-scale Spotify-related dataset

Limitations:
- Not ideal for time-based user retention
- Not ideal for churn or replay prediction
- Playlist-focused rather than listener-lifecycle-focused

Possible future project:
Playlist Recommendation Intelligence

## Candidate 4: Hybrid Approach

Status: Deferred

Reason:
Hybrid datasets should not be joined at the user level unless they share real user identifiers.
For this MVP, one dataset gives a cleaner and more honest analytical story.
