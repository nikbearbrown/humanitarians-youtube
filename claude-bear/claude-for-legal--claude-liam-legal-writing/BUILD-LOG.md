# BUILD-LOG — claude-for-legal--claude-liam-legal-writing

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-legal-writing/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
law-student skill `legal-writing`.

**Source-fidelity note — a real gap, closed by finding the actual file.** The
source beat_sheet.json's narration and Remotion props carried literal `>`
placeholders (`"Claude's job: >"`, `"I want to >"`, etc.) that were never
filled in with the skill's real specifics — a broken/incomplete source
script, not a redacted fact. Rather than inventing content for those slots,
I located and read the real `legal-writing` SKILL.md in full:
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/law-student/skills/legal-writing/SKILL.md`.
Every specific claim in this reel (the "Hard rule: no rewriting. Ever." /
"Rewrite. Period. The hard guardrail." wording, the graceful-refusal script,
the four structural types memo/brief/paper/exam-essay, the top-down feedback
order structure→analysis→clarity/citation→top-three-fixes, the confidence
split — confident on structure, `[VERIFY]`-flagged on substantive law and
citation edge cases, the "write yours — don't copy" labeled-example rule,
the negligence/car-crash worked example, and the "what this skill does not
do" edge list) is a direct read of that file, logged in QUESTION.md/SCRIPT.md.

**Facts kept unchanged from source:** the skill's stated purpose (structural
feedback on a legal writing draft); a skill is a folder Claude reads before
it acts; SKILL.md is one file read top to bottom, executed step by step.

**Beat-count note (redo):** source is 7 beats (B00, B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF your-turn, BOUT outro) — no
explicit wrong-guess, anchor, or both-directions beat. hai-simple's spine
requires all three as their own beats, so this redo expands identically in
shape to the `legal-hold` sibling redo: B01 (stakes) + B02 (wrong guess,
broken) new; B03/B04/B05 carry the source's anatomy/pipeline/design-tell
facts (now grounded in the real SKILL.md) to the anchor; B06 new
anchor-payoff; B07 (both directions) new. Result: B00 + 7 body beats +
BCRY/BHTF/BOUT = 11 beats.

**B00 WRITER LAW:** wrong guess — a newcomer assumes asking Claude for
"feedback on my memo" is a polite way of asking it to fix/rewrite the memo.
Typed text: "Claude, fix my / legal memo. / Wait — what does the / legal-writing
skill do?", trigger "fix" → replacement "critique", landing on "Claude,
critique my legal memo." before the real question. Audio 10.24s, clearing
the ≥8s WRITER LAW floor; verified on a mid-beat frame that the correction
to "critique" is visible.

**Body beats (B01–B07):** Manim GRAPHIC scenes reusing the chip-row/
chip-stack renderer pattern from the `legal-hold` sibling redo, adapted in
this reel's own `scenes.py` with legal-writing-specific chip labels. Anchor
pair: B03 plants "NEGLIGENCE MEMO" + "READ TOP TO BOTTOM" as two plain
chips (the SKILL.md's own negligence/car-crash example); B06 returns the
identical composition with the second chip accented. Close: BCRY `WantQuote`
(carry-out), BHTF `ClaudeComposerAsk` (`folderLabel: "@HumanitariansAI"`),
BOUT `OutroCTA` (`@HumanitariansAI`). All Remotion + WantQuote component
prop schemas verified renderable via `./art scenes --check` before authoring
the sheet (GATE L).

**GATE T (type_check.py) — real defects, root-caused and fixed, not worked
around (four iterations to green):**

1. **Contrast, root cause.** The `_chip()` helper's "accented" style
   inverted fill to solid terracotta with cream text. WCAG math confirms
   this can never clear 4.5:1 against terracotta's mid-range luminance —
   neither near-white nor near-black text reaches the floor against it as a
   full-fill background. Fixed by redesigning the accent as INK-on-cream
   text (guaranteed contrast) with a terracotta border + a thin terracotta
   backing-plate bar under the label, per type_check.py's own suggested
   remediation. Applied to all four accented chips (B01, B02, B05, B06),
   which needed re-rendering.
2. **Min-size, root cause.** Two chip labels (B02, B05) exceeded the
   `_chip()` helper's 22-character tier, dropping to its smallest font size
   (17pt) — below the min-size floor. Shortened both labels.
3. **Kerning, false positive → real fragmentation → real fix.** B02 (3
   chips on one horizontal row) failed §8.4 kerning repeatedly even after
   the above fixes. Diagnosed by writing a standalone script against
   type_check.py's own `row_ink`/`col_dark`/run-detection logic (not by
   guessing from rendered frames) and dumping the exact flagged runs/gaps.
   Root cause: multiple separate chip labels sharing type_check.py's single
   "densest row" scan lets ordinary blank space between two different chips
   register as an anomalous "kerning gap" — the same defect class already
   documented and fixed for B07 in this file via a vertical stack. Added a
   new generic `render_chip_column()` layout and moved B02 to it; the
   defect class (multiple labels on one scanned row) is now eliminated
   structurally rather than patched per-symptom. A same-issue MUTE-color
   sub-diagnosis (struck text at luma ~87 sat just above the checker's
   `gray<80` ink-detection floor, erasing it from the scan entirely) was
   found and fixed in passing (`MUTE` darkened to `#524D44`) even though the
   column-layout fix superseded it as the primary cause.
4. GATE T: **PASS**, 0 FAILs across all 11 beats, confirmed on the final
   recompile.

**Compile bug found and fixed (not a content defect — a render-pipeline
race):** the first several `compile.py` runs in this session were launched
via a detached `(...) > logfile &` shell pattern with a polling loop reading
the logfile for "GATE T" — logically sequential inside the subshell, but the
resulting master.mp4 was silently **truncated to 104.7s**, cutting off BOUT
(and the tail of BHTF) entirely, even though `clips/master.m4a` (110.32s),
the raw video concat (110.33s), and a faithful manual reproduction of
compile.py's exact final mux command (110.2s) all proved correct in
isolation — proof the truncation was a transient artifact of the detached
background invocation, not a logic bug in compile.py or a bad clip. Re-running
`compile.py` as a normal **foreground, blocking** call (per this skill's own
"never background a render step" law) produced the correct 110.208s master
on the first try. Logged here as a concrete instance of exactly the failure
mode the task brief warned about, caught by verifying the master's measured
duration against the beat-duration sum rather than trusting the compile
step's own log output.

**Compile:** `compile.py` (foreground) — clean 3840×2160 master, no declared
slates (all 11 beats real media). `claude-for-legal--claude-liam-legal-writing.mp4`,
110.208s.

**Gate V (visual QC):** pulled ~2fps frames across the full runtime plus
targeted frames per beat and read them by hand — all legible, correct chip
content, safe insets, no overlapping text, the B03→B06 anchor pair visually
identical as intended, B07's vertical-stack layout reads cleanly, B00's
"fix"→"critique" correction confirmed on a mid-beat frame, and — after the
foreground recompile — the true final frame (t≈108s, verified via a
non-seeking sequential decode, not just `-ss`) confirmed the outro carries
the @HumanitariansAI / SUBSCRIBE HAI skin correctly.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−23.9 dB**, max_volume −2.9 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime is newer than beat_sheet.json's
last content edit; beat_sheet.json was not touched after the final
foreground compile, per the "never touch beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Status: review cut DONE.** Passes content-check, frame-check, lane-check,
GATE T (0 FAILs), Gate V (by eye), and audio presence. Proceeding to Phase 4
(4K delivery).
