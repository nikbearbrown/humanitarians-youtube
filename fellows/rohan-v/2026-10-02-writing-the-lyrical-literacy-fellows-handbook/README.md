# Writing the Lyrical Literacy Fellows Handbook — Rohan V.

Progress video, week of 2026-10-02 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

> **Submitted late:** built and submitted on Monday 2026-10-05; I forgot to submit on Friday 2 Oct.

## This week's contribution

**Question.** Can everything a new Lyrical Literacy fellow needs, from access to renewals, live in one
document that the team can keep current?

**Prediction.** That one handbook would replace asking around, if it was written for people
with no technical background and could be rebuilt quickly when a rule changes.

**What I built/tried.** The Lyrical Literacy Fellows Handbook v1.0 (46 pages, 12 sections,
editable Word file with version history), drafted with Claude from the program's pages and our
nine tutorials, then reviewed and corrected: rebuilt in the website's look, three Word comments
applied, two rule changes folded in, the Wednesday meeting and optional playlist added.

**Observed result.** v1.0 delivered 30 Sep, a month ahead of the 30 Oct target on my renewal
plan; shared privately with the team because it holds shared account details.

**Next experiment.** Watch a new fellow follow it from page one without help, and note every
place they get stuck. Then: test OpenReel and DaVinci Resolve on the same footage (2–20 Nov).

## Human and AI work

**My decisions, implementation and verification:** the handbook's scope and audience, the rejection of the first palette, three review comments, the routing and access answers, keeping it off the public repository; reviewed both cuts on 2026-10-06, no changes requested.

**AI tools/voices used and what they generated:** Claude (Claude Code) researched the sources, drafted and built the handbook, and this week built this video (one new scene, six reused), rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** the brand-PDF navy and cream design; a line saying the guide was for Northeastern students; a checklist step to email a GitHub username; logs as a fellow's chore.

**What remains unverified or failed:** not yet used by a new fellow; master copy location undecided; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `098fbc8`, checked 2026-10-05: origin/main `22264a3`
merged locally that day, plus two local commits adding this week's scenes (not pushed upstream; the
scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `HaiDocPages` (+ `HaiDocPages916`), new; `HaiProgressSignupChain`, `HaiProgressOverturned`, `HaiVerdictSplit` (gained opt-in `baseline`), `HaiProgressRoadmap` (gained opt-in `phoneType`), `HaiApplyCard`, `ClaudeComposerAsk`, `HaiTitleOutro`, reused in the Brutalist toolkit.

**Inputs:** [`pantry/handbook/`](./pantry/handbook/): six crops of the v1.0 PDF, with page numbers, clip boxes and SHA-256 in `crops.json` (the handbook itself is not committed: it holds shared account details).

**Commands:**

```bash
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

Landscape — [`landscape/FellowsHandbookUpdate_RohanV.mp4`](https://drive.google.com/drive/folders/1UwqjjrSjNVImmV4h0O-BlK2zqaZT8W_6) — 3840×2160 — 2:16 (136.00 s) — SHA-256 `b7ed3eb39bcce276aca18f47e25622898d95a264c54e6aeef33f830d4bfc933c`

Vertical — [`vertical/FellowsHandbookUpdate_RohanV.mp4`](https://drive.google.com/drive/folders/1zTLwRuGQklj3NC5lyshPXgLxEBfGV06_) — 2160×3840 — 2:16 (136.00 s) — SHA-256 `23be8916b05f4967e05342537abc1e9f23734ac61b40ebab7c66376da7f35e7f`

Week folder on Drive: [`2026-10-02/`](https://drive.google.com/drive/folders/1P5rUqd8BM9Y9-MWwsTVTNtMLx_0FmiEe)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
