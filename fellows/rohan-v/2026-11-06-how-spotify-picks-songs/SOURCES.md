# SOURCES — How Spotify Picks Songs

Full notes, URLs, confidence levels and the "do not say" list: `week-11/_research/facts-recs.md`. Checked 2026-11-09.

## The method

- "Collaborative Filtering for Implicit Feedback Datasets," IEEE ICDM 2008. Play counts as preference plus
  confidence, fitted by alternating least squares; the cold-start problem. The recommender `recs.py` runs (the
  paper's own data was TV viewing, not music). B02, B04, B05.
- "Matrix Factorization Techniques for Recommender Systems," IEEE Computer 42(8), 2009. Hidden taste factors; a
  score is the dot product of two lists. B02.
- scikit-learn user guide, cosine similarity. B03.

## What Spotify says

- Spotify Safety & Privacy Center, "Understanding recommendations on Spotify" (updated 23 Oct 2026): the taste
  profile is the most important input, built from what you search, listen to, skip and save. B01, B07.
- Spotify Newsroom, "Amplifying Artist Input in Your Personalized Recommendations" (2020): the habits of people
  with similar taste. B01.
- Spotify Help, "Exclude playlists or tracks from your taste profile"; Spotify Newsroom on the kids & family
  toggle (2026). B07.
- Exploration: Spotify Engineering, "For Your Ears Only" (2020); "Explore, Exploit, and Explain: Personalizing
  Explainable Recommendations with Bandits," RecSys '18; Spotify Research on centralised exploration (2024) and
  calibrated recommendations (2025). B06.

## Background

- "Algorithmic Effects on the Diversity of Consumption on Spotify," WWW '20: algorithm-driven listening was less
  varied. An association, not a cause; not stated.

## Evidence

- `recs.py`, `export_recs_data.py` and `evidence/` in this folder.
