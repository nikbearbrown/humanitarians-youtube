# BUILD-LOG — claude-for-legal--claude-liam-draft

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-draft/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `draft`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in three beats (B00, B03, BVDT) plus the handoff clause in
BHTF ("I want to >"), matching the identical unfilled-`>` bug already
documented on the `claude-for-legal--claude-liam-case-brief` and
`claude-for-legal--claude-liam-build-guide` sibling redos. The SKILL.md
draft was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/draft/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`legal-clinic/` directory). This is NOT a "genuine blocker that halts the
build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about what draft's particular legal-clinic
procedure does or what document type it targets. This redo treats "draft"
literally and generically — the named example of a skill-shaped folder
aimed at producing a formatted document — and never asserts an invented
procedure from the unread SKILL.md. Logged in QUESTION.md and SCRIPT.md
as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes —
"a draft skill" sounds like a writing upgrade), B02 (wrong guess broken
with a falsifying case — delete the skill's folder, no drafting ability is
forgotten, because there was nothing to learn), B06 (anchor payoff —
restates the design tell against the named anchor), B07 (both directions —
a clean draft proves nothing about understanding; a rough one proves
nothing about breakage). B03/B04/B05 carry the source's anatomy/pipeline/
design-tell facts forward, with B03 now also serving as the anchor plant
(draft's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion, identical in shape to the `claude-for-legal--claude-liam-case-
brief` and `claude-for-legal--claude-liam-build-guide` sibling redos, which
hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a draft
skill" means the model itself learned legal writing. Typed text: "Claude
learned legal writing / from the draft skill. / What is a skill?", trigger
"learned" → replacement "was given", ending on the real question. Audio
10.03s (Remotion extended to 10.0s) — clears the ≥8s WRITER LAW floor with
margin; verified on a frame at t=8.5s that the correction resolves to "was
given" and the full question types out to "What is a skill?" before the
beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern from the `claude-for-legal--
claude-liam-case-brief` sibling redo verbatim, adapted in this reel's own
`scenes.py` with draft-specific chip labels and narration. Anchor pair: B03
plants `draft/` + `SKILL.md` as two plain chips; B06 returns the identical
composition with `SKILL.md` accented. Close: BCRY `WantQuote` (carry-out),
BHTF `ClaudeComposerAsk` (explicit `folderLabel: "@HumanitariansAI"` — the
known ClaudeComposerAsk-defaults-to-@NikBearBrown bug, worked around per
precedent — confirmed correct on the rendered frame), BOUT `OutroCTA`
(@HumanitariansAI). All four Remotion + WantQuote component prop schemas
verified renderable via `./art scenes --check` before authoring the sheet
(GATE L).

**GATE T (type_check.py) — one round-trip fix.** First run: FAIL — B02's
middle chip label "CLAUDE FORGETS HOW TO DRAFT?" (29 chars) triggered
min-size §8.1 (15px < 20px floor), bbox-overlap §8.6b (100% overlap), and
kerning §8.4 (max gap 537px) — the auto-shrink-to-fit-width logic in
`_chip()` scaled the long label down past the legibility floor. Fix:
shortened the label to "FORGETS HOW TO DRAFT?" (21 chars, same meaning,
fits the ≤22-char font-size tier) in both `scenes.py` and `beat_sheet.json`,
re-rendered only B02's Manim scene, recompiled (fast path — only 1/11 beats
re-encoded). Second run: **GATE T PASS**, 0 FAILs across all 11 beats.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-draft.mp4`, 108.9s. One non-blocking WARNING
carried through compile: GRAPHIC beats are 7/11 (63%), over the toolkit's
~40% "pantry cap" motion-diversity guidance (MOTION.md) — noted, not
treated as a gate; this reel is legitimately diagram-heavy (a skill's
anatomy/mechanism/spec argument reads naturally as labeled-chip diagrams)
and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled 2fps frames across the full runtime and read
one representative frame per beat by hand — all legible, correct chip
content, safe insets, no overlapping text, the B03→B06 anchor pair visually
identical as intended, B07's vertical-stack layout reads cleanly, BHTF and
BOUT both carry the correct @HumanitariansAI skin.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −2.9 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (00:04) is newer than
beat_sheet.json's last content edit (00:02, the B02 label fix +
recompile-stamp) — no further beat_sheet.json edits followed the final
compile, per the "never touch beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Status: review cut DONE.** Review cut passes every gate (content-check,
frame-check, lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity
gap logged above and in QUESTION.md/SCRIPT.md/the description's
"Deliberately not claimed" section — nothing about the actual legal-clinic
draft procedure is asserted anywhere in this reel. Proceeding to Phase 4
(4K render + delivery).
