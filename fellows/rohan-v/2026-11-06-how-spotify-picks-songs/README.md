# How Spotify Picks Songs — Rohan V.

Tech explainer, week of 2026-11-02 to 2026-11-06 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** How does a music app guess what you'll want to hear next, and what does that approach get wrong?

**Prediction.** Going in, the working assumption was that a textbook recommender would beat "just play the hits"
by a wide margin, and that feeding its picks back to listeners would narrow their tastes (a filter bubble).

**What I built/tried.** `recs.py`: a made-up music service (1,600 songs in 8 Western genres with overlapping
neighbours, 3,000 listeners, play counts with a strong popularity pull) and implicit-feedback matrix factorisation
(ALS, 24 taste numbers per listener and song). Tested by hiding a fifth of each listener's songs; then popularity
bias, an 8-round feedback loop with and without 2 exploration slots in 10, and cold start.

**Observed result.** 74.1% of listeners got a hidden song back in 10 picks, against 65.3% for the hits and 6.4%
for random. With no genre labels, a song's 5 nearest songs shared its genre 83.7% of the time. Only 5.9% of picks
came from the less popular half of the catalogue (25.8% of listening). A new song with no plays was never picked.
The loop did not narrow tastes in my test; exploration put 99.5% of the catalogue in play.

**Next experiment.** Add a content model (audio or text features) so new songs can be recommended before anyone
plays them, and measure how much it fixes cold start.

## Human and AI work

**My decisions, implementation and verification:** chose this topic from the suggestions and gave this week's hours; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) researched Spotify's published descriptions and the papers, wrote the simulation and recommender, the six scenes and the narration, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** a first synthetic service that was too easy (98% hit rate); a filter-bubble claim the run did not support (genres per list rose); any claim about Spotify's current internal algorithm (unpublished).

**What remains unverified or failed:** a simulation, not Spotify's data; one recommender; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `04afd9ff`, checked 2026-11-09: origin/main `3a6d397`
merged locally that day (Remotion 4.0.535), plus local commits adding this week's scenes and fixes
(not pushed upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `RecsSignals`, `RecsGrid`, `RecsNeighbours`, `RecsAccuracy`, `RecsPopularity`, `RecsExplore` (+ `916` siblings, each with its own phone layout) and `scenes/recs/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`recs.py`](./recs.py) → [`evidence/`](./evidence/) (run.log, results.json, scene.json); [`export_recs_data.py`](./export_recs_data.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python recs.py && python export_recs_data.py
python runtime/scripts/generate_audio_kokoro.py <reel> && python runtime/scripts/align.py <reel>
python runtime/scripts/sync_cues.py <reel>
./art vertical <reel> && python vertical_strings.py
./art final <reel> --height 2160 --out <reel>
./art final <reel>/vertical --height 3840 --out <reel>/vertical
```

**Approvals and checks:** GATE F (FACTCHECK, SHOTLIST, PROMPTS), GATE T and Gate V on both cuts;
results in [`BUILD-LOG.md`](./BUILD-LOG.md) and [`TYPECHECK.md`](./TYPECHECK.md). No human approval
record is required for this reel type; none is claimed.

## Watch and review

Landscape — [`landscape/SpotifyRecs_RohanV.mp4`](https://drive.google.com/drive/folders/165VvmWLT98x6VstvtF8vprmmCjWLSYfO) — 3840×2160 — 2:06 (126.17 s) — SHA-256 `3d40a17b000001d84b9a98beb72a661bedde53e908a9a85a5b4fec8a0f5433ed`

Vertical — [`vertical/SpotifyRecs_RohanV.mp4`](https://drive.google.com/drive/folders/1SDCwDXTTT4Aonr8agKstjHSdyTnxhK2h) — 2160×3840 — 2:06 (126.17 s) — SHA-256 `4864b795391b73959992aacf39248006e8262a8fe50e19af2f1ad4d83eddbcd1`

Week folder on Drive: [`2026-11-06/`](https://drive.google.com/drive/folders/1B6U2I7MnL4-X35Q-RXDuGdnMHd0Is2f4)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
