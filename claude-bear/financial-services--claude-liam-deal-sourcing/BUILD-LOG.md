# BUILD-LOG — financial-services--claude-liam-deal-sourcing

## 2026-09-01 — review cut, DELIVERED

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-deal-sourcing/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
private-equity plugin skill `deal-sourcing`.

**Source-fidelity note (better than some `claude-for-legal` siblings — read
before assuming a blocker):** the underlying SKILL.md the source describes
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-
services/plugins/vertical-plugins/private-equity/skills/deal-sourcing/
SKILL.md`) is not reachable on this machine (confirmed via `find` across
`anthropics/financial-services/` — only `youtube/` exists locally). Unlike
the `claude-for-legal--claude-liam-hiring-review` / `case-brief` siblings,
though, this source's own beat_sheet.json narration was NOT an unfilled
`>` placeholder — it carries the skill's actual job description verbatim:
"PE deal sourcing workflow — discover target companies, check CRM for
existing relationships, and draft personalized founder outreach emails,"
with triggers "find companies", "source deals", "draft founder email",
"check if we've seen this company", "outreach to founder." This redo
carries those three concrete steps (search a sector, check the CRM, draft
the outreach email) forward unchanged, and invents nothing about the PE
process beyond what the source's own narration already asserted.

**Facts kept unchanged (from the source):** a skill is a folder Claude
reads before it acts; the whole routine lives in one file (SKILL.md);
Claude reads it and executes the file's steps in order, with no branching
unless the file itself branches; deal-sourcing's three steps are search a
sector for target companies, check the CRM for existing relationships, and
draft a personalized founder outreach email; a skill is a specification,
not a capability — its payoff is repeatable results, its limit is anything
the file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented PE fact either):** the source has no explicit wrong-guess, anchor,
or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW / BOTH-DIRECTIONS LAW
all require their own beat). Added: B01 (stakes — "a deal-sourcing skill"
sounds like Claude got investment judgment), B02 (wrong guess broken with a
falsifying case — delete the skill's folder, Claude loses no investment
judgment, because there was none to begin with), B06 (anchor payoff —
restates the anchor file against the three-step checklist), B07 (both
directions — surfacing candidates proves nothing about deal quality;
drafting a clean email proves nothing about the founder replying). B03/B04/
B05 carry the source's anatomy/pipeline/design-tell facts forward, with B03
also serving as the anchor plant (deal-sourcing's single SKILL.md, its
three steps).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — the same proportionate
expansion used on the `claude-for-legal--claude-liam-hiring-review` sibling
redo, which hit an analogous six-move-spine gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
deal-sourcing skill" means Claude itself judges which companies are good
investments. Typed text: "Claude decides which / companies to invest in /
with the deal-sourcing / skill. What is a skill?", trigger "decides" →
replacement "finds", ending on the real question. Audio 9.3s — clears the
≥8s WRITER LAW floor; verified on a late frame (t=8.5s) that the correction
resolves to "finds" and the sentence reads "Claude finds which companies to
invest in with the deal-sourcing skil..." before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern verbatim from the
`claude-for-legal--claude-liam-hiring-review` sibling redo, adapted in this
reel's own `scenes.py` with deal-sourcing-specific chip labels and
narration. Anchor pair: B03 plants `deal-sourcing/` + `SKILL.md` as two
plain chips; B06 returns the identical composition with `SKILL.md`
accented.

**GATE T iteration:** first `type_check.py` run (after render → compile,
matching `simple`'s documented Step 5 order) came back GATE T FAIL on B01 —
§8.1 min-size: smallest text run 15px < floor 20px. Root cause: the chip
label "CLAUDE HAS A DEAL-SOURCING SKILL" (33 chars) fell into the >22-char
autoscale bucket in `scenes.py`'s `_chip()` helper and, combined with the
fixed 2-chip row's `chip_w` cap (3.4 Manim units), scaled down below the
pixel floor — longer than the hiring-review sibling's equivalent label
("CLAUDE HAS A HIRING SKILL", 26 chars), which passed. Fixed by shortening
both B01 chip labels to "CLAUDE HAS A SOURCING SKILL" (26 chars) and
"JUDGES DEAL QUALITY?" (20 chars, down from "JUDGES WHICH DEALS ARE
GOOD?"), matching the sibling's label-length budget, in both `scenes.py`
and `beat_sheet.json`'s `production_viz.chips` (documentation field, not
render-path, but kept in sync). Re-rendered B01 only, recompiled — GATE T
PASS, 0 FAILs, 11/11 beats checked.

**Compile warning (non-blocking):** `compile.py` flagged the motion
histogram — graphic:7/remotion:4 (63%), over the ~40% pantry cap advisory
in MOTION.md. This is structurally identical to the `hiring-review` sibling
(same 7 GRAPHIC body beats / 4 REMOTION frame beats ratio, inherent to the
hai-simple spine on a 7-beat skill-teardown source) and was accepted as-is,
consistent with that precedent — not a GATE failure, no exit effect.

**Gate V (frame QC):** pulled `fps=2` frames across all 11 beats and read a
representative sample (B00 open + late-frame correction check, B01-B07 body,
BCRY carry-out, BHTF handoff, BOUT outro). All legible, safe inset, no text
overlap, one terracotta accent per beat.

**Audio presence:** `ffprobe`/compile GATE AUDIO — mean_volume -24.1 dB,
well above the -40 dB floor.

**Master:** `financial-services--claude-liam-deal-sourcing.mp4`, 3840×2160,
118.3s, all 11 beats real (no slates). Newer than `beat_sheet.json`'s last
edit (the B01 chip-label fix was applied, then recompiled — beat_sheet.json
was not touched again after that final compile, per the COMPLETION LAW).

**Playlist:** `financial-services` is not itself in playlists.json's map;
per the redo instructions, matched the `hai-simple` prefix instead → "Claude
Basics" (same resolution as every other hai-simple redo to date).

**Phase 4 — delivery:** compile.py's 4K LAW already produced the master
natively at 3840×2160, so `<slug>-4k.mp4` was made as a direct copy (no
separate upscale render needed). Ran
`python3 skills/make/hai-simple/loop/deliver.py <reel_dir> --push`: staged
`DELIVERY/financial-services--claude-liam-deal-sourcing/` (4K master +
description) for the Drive sync, and committed/pushed the text artifacts
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md) to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-deal-
sourcing/` (commit `33fa5354`). Logged to HAILOOP-LOG.md.
