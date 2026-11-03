# BUILD-LOG — claude-for-legal--claude-liam-investigation-summary

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-investigation-summary/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
employment-legal skill `investigation-summary`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in four beats (B00, B03, BVDT, BHTF), matching the
identical unfilled-`>` bug already documented on the sibling redos
`claude-for-legal--claude-liam-case-brief` and `-build-guide`. The SKILL.md
investigation-summary was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/investigation-summary/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`employment-legal/` directory). This is NOT a "genuine blocker that halts
the build" per the completion law: unlike the fully-blank case-brief gap,
one real sentence DOES survive here — the source's own B00 states the
skill's job plainly, unhedged: "Draft an audience-specific summary from the
privileged investigation." This redo builds its entire argument from that
one sentence plus the generic, verifiable mechanics of any Claude skill (a
folder read before it acts, one file — SKILL.md — read top to bottom and
executed step by step, specification semantics with a payoff and a hard
limit) and the generic, well-known meaning of legal privilege (not every
reader is entitled to the same amount of privileged material). Nothing
about investigation-summary's specific employment-legal procedure is
asserted anywhere in this reel. Logged in QUESTION.md and SCRIPT.md as
well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
new judgment — its payoff is repeatable results, its limit is anything the
file never covers; and this specific skill's stated job — an
audience-specific summary drawn from one privileged investigation.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes — "an
investigation-summary skill" sounds like one clean write-up handed to
everyone), B02 (wrong guess broken with a falsifying case — sending
counsel's version to the workforce would leak the very analysis privilege
protects), B06 (anchor payoff — restates the design tell against the named
anchor), B07 (both directions — a plain-fact summary proves nothing about
what was stripped; a heavily redacted one proves nothing about whether the
boundary was drawn right). B03/B04/B05 carry the source's anatomy/pipeline/
design-tell facts forward, with B03 now also serving as the anchor plant
(investigation-summary's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 + 7
body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion to satisfy hai-simple's mandatory six-move spine, identical in
shape to the `claude-for-legal--claude-liam-case-brief` and `-build-guide`
sibling redos, which hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes an
"investigation-summary skill" writes one summary the same way for every
reader. Typed text: "Claude writes one investigation summary / for
everyone. / What should change per audience?", trigger "everyone" →
replacement "each audience", ending on the real question. Audio 8.81s
(Remotion extended to 8.8s) — clears the ≥8s WRITER LAW floor; verified on
frames at t=8.0s and t=8.7s that the correction resolves to "for each
audience." before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the `case-brief` sibling
redo, adapted in this reel's own `scenes.py` with investigation-summary-
specific chip labels and narration. Anchor pair: B03 plants
`investigation-summary/` + `SKILL.md` as two plain chips; B06 returns the
identical composition with `SKILL.md` accented. Close: BCRY `WantQuote`
(carry-out), BHTF `ClaudeComposerAsk` (explicit `folderLabel:
"@HumanitariansAI"`), BOUT `OutroCTA` (@HumanitariansAI). All four Remotion
+ WantQuote component prop schemas verified renderable via `./art scenes
--check` before authoring the sheet (GATE L).

**GATE T (type_check.py) — one round-trip:** first run FAILed on B02: its
longest chip ("SEND COUNSEL'S VERSION TO STAFF", 32 chars) fell into the
renderer's smallest font bucket (>22 chars → 17px font), and the resulting
text-run height (15px) landed under the 20px floor. Root-cause fix:
shortened the three B02 chip labels to ≤22 chars each ("SAME SUMMARY TO
STAFF" / "PRIVILEGE HOLDS?" / "LEAKS THE ANALYSIS", same accent/strike
positions and meaning), edited both `beat_sheet.json` and `scenes.py`,
re-rendered only B02, recompiled. Second run: **PASS, 0 FAILs across all 11
beats.**

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0) and 4 Remotion beats via `remotion_scenes.py`
(the call auto-backgrounded past the tool's 120s timeout; blocked on it
explicitly with TaskOutput rather than ending the turn, per the COMPLETION
LAW — exit 0, all 4 beats confirmed rendered before moving on).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media, after the B02 re-render).
`claude-for-legal--claude-liam-investigation-summary.mp4`, 128.6s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md);
noted, not treated as a gate — this reel is legitimately diagram-heavy (a
skill's anatomy/mechanism/spec argument reads naturally as labeled-chip
diagrams), matching the identical, already-accepted warning on the
`case-brief` sibling, and every GRAPHIC beat is original, locally-rendered
Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled ~2fps frames across the full runtime and
read one representative frame per beat by hand — all legible, correct chip
content/accent/strike, safe insets, no overlapping text, the B03→B06 anchor
pair visually identical as intended, B07's vertical-stack layout reads
cleanly, BHTF/BOUT correctly carry the @HumanitariansAI skin. B00's
correction confirmed legible at both t=8.0s ("for each audience.") and
t=8.7s (question still typing, as expected within an 8.8s beat).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −2.9 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime is newer than beat_sheet.json's
last content edit (the B02 chip-label fix, applied before the final
recompile) — beat_sheet.json was NOT touched after the final compile, per
the "never touch beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW — same resolution as the `case-brief` sibling.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about the actual employment-legal
investigation-summary procedure is asserted anywhere in this reel.
