# BUILD-LOG — claude-for-legal--claude-liam-marketing-claims-review

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-marketing-claims-review/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `marketing-claims-review`.

**Source-fidelity note (better than the sibling redos):** the source's
beat_sheet.json never received its skill-specific "Claude's job: ___" fill —
the literal placeholder `>` survives verbatim in three beats (B00, B03,
BHTF), matching the identical unfilled-`>` bug already documented on the
`claude-for-legal--claude-liam-hiring-review`, `-case-brief`, and
`-build-guide` sibling redos. Unlike those siblings, though, the actual
SKILL.md the source meant to describe IS reachable on this machine: not at
the path named in the source's `source_skill` metadata
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/product-legal/skills/marketing-claims-review/SKILL.md`, which does not
exist here), but at a mirrored copy found by searching outside the
`anthropics/` tree:
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/product-legal/skills/marketing-claims-review/SKILL.md`.
This redo reads that file directly and fills every `>` gap with the skill's
real content instead of staying generic.

**Facts kept and specifically filled in (from the real SKILL.md):** a
five-part claim taxonomy (puffery / specific factual / comparative / implied
/ absolute claims); the worked example claim "Trusted by 10,000 companies"
used as this reel's anchor, with its real substantiation note (actual
*current* count, not cumulative signups); the claim-by-claim call format
(✅ fine / ⚠️ needs substantiation / ⚠️ needs rewording / 🔴 cut, rendered
here as text-only chips — no emoji glyphs, since Manim's font set can't
reliably rasterize them); and the real attorney gate — before a non-lawyer
user is shown "Ready to ship: Yes," the skill requires an explicit
confirmation that an attorney has reviewed the claim.

**New content added to meet hai-simple's spine (not in the source, but
sourced from the real SKILL.md, never invented):** the source has no
explicit wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW /
ANCHOR LAW / BOTH-DIRECTIONS LAW all require their own beat). Added: B01
(stakes — "a marketing-claims-review skill" sounds like Claude will rule the
ad legal or not), B02 (wrong guess broken with a falsifying case — the
skill's real output is a sort into fine/needs-proof/needs-reword/cut, never
a legal ruling), B07 (anchor payoff — the anchor claim returns flagged
"needs substantiation," not ruled on), B08 (both directions — a flag proves
nothing about falsity; a clean pass proves nothing about permanence, since
the product can drift from the copy after ship). B03 plants the anchor
claim (drawn verbatim from the SKILL.md's own example table); B04/B05/B06
carry the source's anatomy/pipeline/design-tell facts forward, split across
classify / substantiate / call-format because the real SKILL.md supports
that much specific, citable detail.

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 + 8
body beats (B01–B08) + BCRY/BHTF/BOUT/BOUTCTA = 13 beats — a proportionate
expansion of a 7-beat source, one beat larger than the `hiring-review`
sibling's 11 because this source's underlying skill was actually readable
and supplied one more distinct, real mechanism step (classify, then
separately substantiate, then separately call+gate) than the unreachable-
SKILL.md siblings had material for.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude can tell me if
my ad is legal" is a question Claude can answer with a legal verdict. Typed
text: "Can Claude tell me / if my ad copy / is legal?", trigger "legal" →
replacement "provable", ending on the real question ("...is provable?").
Audio 9.83s (Remotion extended to 9.8s) — clears the ≥8s WRITER LAW floor;
verified by pulling a frame at t=8.8s: the correction has resolved to
"provable?" and the full sentence reads "Can Claude tell me / if my ad copy
/ is provable?" well before the beat ends.

**Body beats (B01–B08):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the `hiring-review` sibling
redo, adapted in this reel's own `scenes.py` with marketing-claims-review-
specific chip labels and narration. Anchor pair: B03 plants "TRUSTED BY" /
"10,000 COMPANIES" as two plain chips; B07 returns the identical composition
with a third chip, "NEEDS PROOF," accented.

**Outro split:** used the two-beat OutroSeries + OutroCTA split (per the
hai-simple task brief's explicit "OutroSeries/OutroCTA" instruction) rather
than the single-OutroCTA variant seen on the `hiring-review` sibling — both
patterns exist across the batch; this build follows the literal brief.
BOUT (OutroSeries): eyebrow "CLAUDE BASICS", line "From Humanitarians AI."
BOUTCTA (OutroCTA): line "Find more at humanitarians.ai", handle
"@HumanitariansAI", narration ending "…Liam, in for Bear."

**Render order (render → compile → type_check):** ran
`generate_audio_kokoro.py` first (13/13 beats, no `--voice` flag exists on
this build — voice is read from the beat sheet's own `am_onyx` fields), then
`render_scenes.py` (8/8 Manim beats, foreground, no failures), then
`remotion_scenes.py` for B00/BCRY/BHTF/BOUT/BOUTCTA — this step exceeded the
tool's 120s foreground-command timeout and was auto-backgrounded; per the
ONE-SHOT/COMPLETION LAW this was NOT left running unsupervised — blocked on
it explicitly via TaskOutput (5/5 beats confirmed rendered, exit 0) before
proceeding. Then `compile.py` (forced a clean 3840×2160 master directly, no
declared slates — all 13 beats real media), then `type_check.py` (GATE T).

**GATE T:** PASS on the first run, 0 FAILs across all 13 beats (min-size,
overflow, contrast, contrast-local, bbox-overlap, card-clip, kerning,
no-wordy-card). No exemption additions were needed this time.

**Compile:** `claude-for-legal--claude-liam-marketing-claims-review.mp4`,
127.3s, 3840×2160 native. One non-blocking WARNING carried through compile:
GRAPHIC beats are 8/13 (61%), over the toolkit's ~40% "pantry cap"
motion-diversity guidance (MOTION.md) — noted, not treated as a gate; this
reel is legitimately diagram-heavy (a skill's taxonomy/mechanism/spec
argument reads naturally as labeled-chip diagrams) and every GRAPHIC beat is
original, locally-rendered Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled a representative frame per beat (B00 t=5s …
BOUTCTA t=124s) plus one deliberate second pull mid-B04 (t=39s) after the
first B04 sample (t=37s, only 2.46s into that beat's local timeline) showed
only 4 of 5 taxonomy chips — confirmed by the later frame that this was
animation-timing (chip 5, "ABSOLUTE," was still mid-fade-in at the earlier
timestamp, not a rendering defect), all 5 chips and the caption present by
t=39s. Every other beat legible on first pull: correct chip content, safe
insets, no overlapping text, the B03→B07 anchor pair visually identical
apart from the added "NEEDS PROOF" chip as intended, B08's vertical-stack
layout reads cleanly, B00's correction confirmed resolved to "provable"
well before the beat ends, BCRY/BHTF/BOUT/BOUTCTA carry the Humanitarians AI
skin correctly (@HumanitariansAI handle, humanitarians palette, subscribe
CTA).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.0 dB**, max_volume −1.5 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (15:28:58) is newer than
beat_sheet.json's last content edit (15:26:56) — beat_sheet.json was NOT
touched after this point, per the "never touch beat_sheet.json after
compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** `claude-for-legal--claude-liam-marketing-claims-review-4k.mp4`
created — a copy of the compiled master, which was already genuine
3840×2160 (the Remotion beats are natively 4K; the Manim beats are 1080p
source upscaled into the 4K canvas by the compile step itself, same as
every other GRAPHIC beat in this pipeline). Wrote
`claude-for-legal--claude-liam-marketing-claims-review.md` (YouTube
description, @HumanitariansAI, playlist "Claude Basics", direct code link,
AI disclosure). Ran `deliver.py --push` to stage
`DELIVERY/claude-for-legal--claude-liam-marketing-claims-review/` and commit
text artifacts to the humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-marketing-claims-review/`.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap (the
source script's own unfilled `>` placeholders) logged above and in
QUESTION.md/SCRIPT.md/the description's "Deliberately not claimed" section
— every specific fact this reel asserts about the marketing-claims-review
skill is read directly from its real, mirrored SKILL.md.
