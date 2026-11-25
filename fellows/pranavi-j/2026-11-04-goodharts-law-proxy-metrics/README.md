# Weekly STEM Video: Goodhart's Law — When the Proxy Stops Being the Target

**Fellow:** Sai Pranavi J.
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering work. Describes a well-established, generic phenomenon — Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure") and the closely related Campbell's Law — qualitatively. No real company, vendor, product, or dataset is named or benchmarked, no fabricated statistic is shown. The worked example (B04, a textbook-level call-center average-handle-time scenario) and its falsifiability/counterbalance case (B05, the identical scenario with a tracked counterbalancing check added) are both fully generic/hypothetical illustrations. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): `deliverables/landscape/GoodhartsLaw_SaiPranaviJ.mp4`
- Vertical (4K 9:16): `deliverables/vertical/GoodhartsLaw_SaiPranaviJ.mp4`

This video teaches a reusable 3-question test — **Name the Target / Find the Lever / Watch the
Coupling** — for telling when and why a proxy metric (a measurable stand-in, chosen because it once
correlated with a real target) diverges from that real target. The framework is taught in full
before any example, walked through a worked example (a call center's average handle time, gamed,
while the real target — problems actually resolved — quietly worsens unwatched), stress-tested
against a falsifiability case where the identical scenario and gaming pressure do NOT produce
divergence because a counterbalancing check is tracked alongside the proxy, and closed with a
concrete audit task the viewer can run today against any metric they already track.

## What this covers (and what it deliberately leaves out)

Covered: a hook showing a generic dashboard metric climbing while the real target goes unchecked
(B02); all 3 tests shown together, before any example (B03); a worked example (B04) where a call
center's average handle time improves on schedule while the real target — never tracked — quietly
worsens, tagged "DIVERGED"; a falsifiability/counterbalance case (B05) where the identical scenario,
numbers, and gaming pressure are paired with a tracked counterbalancing check, catching the same
worsening immediately instead of hiding it, tagged "CAUGHT — STAYS HONEST"; a concrete audit task
distinct from the framework card (B06); and a closing takeaway.

Deliberately left out: this is not a report of any real system's actual metrics, and does not name
or evaluate any specific real company, vendor, or product (Goodhart's Law and proxy-metric
divergence are well-documented, generic phenomena, not a single paper or vendor-specific claim).
This is also a distinct topic from six adjacent, already-covered videos in this series: **not
hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`, fabrication), **not
tokenization** (how text is chunked before any reasoning happens), **not lost-in-the-middle**
(`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`, position within a long context),
**not chain-of-thought faithfulness**
(`2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`, whether a stated reasoning
trace caused the answer), **not calibration**
(`2026-10-21-calibration-why-confidence-isnt-accuracy`, whether a stated confidence number tracks
accuracy for a single prediction), and **not in-context learning**
(`2026-10-28-in-context-learning-limits`, what a prompt alone can teach a model with no weight
updates). This video asks a different question: when a system tracks a number as a stand-in for
what it actually cares about, under what conditions does that number stop meaning what everyone
assumes it means? No specific percentage or statistic is fabricated or claimed as a real
measurement anywhere — the call-center numbers are illustrative.

This week's companion project-update video separately covers a real bug involving two related
metrics drifting apart once one started being corrected independently of the other — a live
instance of exactly the general phenomenon this STEM video explains. Per the house rule, that
specific incident is not named or described anywhere in this video; B06 carries one brief, fully
generic sentence acknowledging the pattern is not unique to any one system.

## Illustrative content chosen for B02 / B04 / B05

**B02 (hook):** a generic "DASHBOARD METRIC (PROXY)" panel climbing week over week (100 → 118 →
139), tagged "TREND: UP" / "LOOKS GOOD," then an overlay asking the real question the rest of the
video answers: proxy up — target up too? No domain, company, or system is named.

**B04 (worked example):** a call center's average handle time (a well-established, textbook-level
illustration of a gameable efficiency metric) improves from 6.5 MIN to 4.0 MIN under pressure to
reward shorter calls, while the real target — problems actually resolved — drops from 82% to 61%,
unwatched. Tagged "DIVERGED — NOBODY SAW IT." Chosen because it's a standard illustration in
operations-management literature, mechanically checkable on screen, with no real company named.

**B05 (falsifiability/counterbalance case):** the identical scenario, the identical before/after
numbers, and the identical gaming pressure as B04 — the ONLY change is that the real target is now
framed as a tracked counterbalancing check ("first-call resolution... ON THE SCOREBOARD"). The same
worsening happens, but it's caught immediately instead of hiding, tagged "CAUGHT — STAYS HONEST."
Chosen to give B04's divergence a real, visibly distinct counterpart — stress-testing the framework
against a naive "every optimized proxy always diverges" over-trigger, per `FACTCHECK.md`.

## Production state

- Plan: **approved (Gate P)** — signed 2026-11-04
- Fact-check gate: **resolved** — see `FACTCHECK.md`; kept fully generic, no real company/vendor named, no fabricated statistic
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-11-04
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `GoodhartsLaw_SaiPranaviJ.mp4`, **3840x2160, 24fps, h264/aac, 169.25s**. GATE V on the true clean master (verified directly, not the review slate): **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `GoodhartsLaw_SaiPranaviJ.mp4`, **2160x3840, 24fps, h264/aac, 169.25s** — identical runtime to the landscape master, all 9 beats kept, no drops, no duration cap. GATE V on the true clean master (verified directly, not the review slate): **0 BLOCKER, 0 MAJOR**.
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires fellow/PM sign-off per `brutalist/docs/FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review confirming the mechanism, worked example, and falsifiability/counterbalance case are generic/qualitative
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous build log of what resisted and what Claude contributed
