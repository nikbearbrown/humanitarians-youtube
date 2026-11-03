# Homes of Hope Songs: Proof of Concept Progress — Rohan V.

Weekly progress update, week of 2026-10-16 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** Can one small set of songs show Homes of Hope how Lyrical Literacy would work:
the teaching method, two levels, the sound, and the safeguards?

**Prediction.** That two themes at two tiers, in English and Hindi, would be enough to let them hear
the idea instead of reading about it.

**What I built/tried.** Four songs ("Sisters Side by Side", "I Will Be"; Tier 1 about 50/50, Tier 2
mostly English), drafted with Claude and generated in Suno; a sound revision of "I Will Be" around
dhol, tabla and sitar at 108/110 BPM; versions shared with the team; this 84-second update.

**Observed result.** All four songs drafted with lyrics, styles prompts and meta tags; versions
generated and shared for the team to pick. The Hindi still needs native review, and the home-life
lines need staff review.

**Next experiment.** The team's picks, then a native Hindi review, then the proof of concept video
for the pitch.

## Human and AI work

**My decisions, implementation and verification:** the proof of concept itself (scope, themes, sound revision, safeguards, favourite versions), the 90-second limit and visuals-only choice for this video, and this week's hours.

**AI tools/voices used and what they generated:** Claude drafted the songs' lyrics, styles prompts and meta tags with me; Suno generated the songs; Claude (Claude Code) wrote this video's script from my summary and two new scenes, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** the first violin-heavy sound; the reference style's soft vocal tone (call and response needs a strong lead); naming any girl, home, staff or team member; song audio in this video.

**What remains unverified or failed:** Hindi pronunciation, meaning and tone (native review pending); staff review of the home-life lines; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `e758e22`, checked 2026-10-17: origin/main `4115560`
merged locally that day (Remotion 4.0.535), plus local commits adding this week's scenes and fixes
(not pushed upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `HohCallResponse`, `HohTiers` (+ `916` siblings, each with its own phone layout); library `HaiProgressOverturned`, `HaiVerdictSplit`, `HaiProgressRoadmap` in the Brutalist toolkit.

**Inputs:** my project summary (PDF, not committed: it names team members), summarised in [`SOURCE-brief.md`](./SOURCE-brief.md).

**Commands:**

```bash
python author_sheet.py
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

Landscape — [`landscape/HomesOfHopePoC_RohanV.mp4`](https://drive.google.com/drive/folders/1vQFZdDag6dH7hFnyrmtsHsdTYe8Q6Rhi) — 3840×2160 — 1:24 (83.88 s) — SHA-256 `5c818794b32615b2ff6bf2ce7b6953f3df538f40af9aec748ffbb91d2b6aa449`

Vertical — [`vertical/HomesOfHopePoC_RohanV.mp4`](https://drive.google.com/drive/folders/12Sjys-7FJ2klZNPhihIldT9TLa3Mc_W5) — 2160×3840 — 1:24 (83.88 s) — SHA-256 `00196f15d0fa87b89a88b0fb9577eca6702e87287f04f3ab83a0ae3145578a47`

Week folder on Drive: [`2026-10-16/`](https://drive.google.com/drive/folders/17pJ6dCN9-GP_vnSmeY3U5a4KKg59V85g)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
