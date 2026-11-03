# BUILD-LOG — financial-services--claude-liam-kyc-doc-parse

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-kyc-doc-parse/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `kyc-doc-parse` skill (not an unfilled
placeholder shell) — see QUESTION.md. Facts preserved: the skill parses an
investor/client onboarding packet into five structured KYC fields
(identity, ownership, control, source of funds, document inventory); used
as the first step of KYC screening, with output feeding a downstream
rules engine; same input → same output every run; limited to only what
the SKILL.md specifies. The `source_skill` path it names does not exist
on this machine (different machine's home directory, same situation as
the `initiating-coverage` / `clean-data-xls` sibling redos), but no
reconstruction was needed.

**The call:** register re-registered Teardown → Plain. Source's B03
framed "what it gets right: repeatable results / what it bites: anything
outside the spec" as a design-tell verdict — Teardown language — removed;
Plain states only the mechanism (extraction into five structured fields)
and its two failure directions as properties of the practice, never a
verdict on the skill's design. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` per WRITER LAW: "approve" →
"parse it into fields" — the naive assumption that the skill approves or
clears a client, corrected to: it only parses the packet into structured
fields. Added a wrong-guess beat (B01: "clear or flag?" decision box vs.
five-field extraction, falsified by "feed it a packet where the
beneficial-owner section is left blank, and it doesn't raise an alarm —
it records that field as missing") and an anchor (B02 → B03: one
onboarding packet's data landing in all five field buckets, then
returning fully filled and splitting into the two both-directions
cautions) per this factory's PHASE 1 structure requirement — the source's
Teardown shape (anatomy / pipeline / design-tell / verdict) carried
neither. Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Kept the source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF,
BOUT). No source beat was AI-VIDEO, pantry, or a human-drop slot — every
source beat was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no beat replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.88s (clear of the ≥9s TIMING LAW
   floor) on the first narration draft (33 words + `lead_silence_s: 0.8`).
   Durations: B00 10.88s, B01 22.76s, B02 19.09s, B03 18.13s, BCRY 14.10s,
   BHTF 19.58s, BOUT 4.84s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `KDB01Scene` /
   `KDB02Scene` / `KDB03Scene`, reusing the `initiating-coverage` sibling's
   worked-around card-border pattern — TEAL borders, not INK, the
   traveling token fading beside each card, off-card overflow lines, and
   the B03 mini-summary row pre-emptively set to font_size 34 rather than
   the smaller value that failed GATE T on that sibling) and
   `render_scenes.py`; rendered B01, B02, B03 clean on the first pass.
3. Rendered the Remotion beats via `remotion_scenes.py`. The first
   invocation (all 4 beats) was killed by the shell tool's own 2-minute
   default timeout while still running — **not** by the process itself,
   which kept rendering as an orphan (`chrome-headless-shell` +
   `compositor ffmpeg` still alive). Per the COMPLETION LAW / ONE-SHOT
   warning, did **not** end the turn or launch a duplicate render; instead
   waited in the foreground on the still-running PID until it exited
   (~8 more minutes), confirmed BCRY/BHTF/BOUT had landed, found B00
   missing (its own sub-step apparently hadn't been reached before the
   parent was cut off from stdout), and re-ran `remotion_scenes.py --only
   B00` in the foreground — completed in well under a minute. All four
   beats confirmed present afterward. B00 verified ≥8s (10.9s) and the
   "approve" → "parse it into fields" correction confirmed legible on
   frames pulled at t=9.5s (mid-typing "approv") and t=10.6s (replacement
   visible: "...parse it into|").
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K LAW),
   mean_volume -24.2 dB, motion histogram remotion:4 graphic:3.
5. GATE T (`type_check.py`) → **PASS, first pass**, 0 FAILs — the
   pre-emptive font_size-34 fix on the B03 mini-summary row (learned from
   the `initiating-coverage` sibling's GATE T failure) avoided that defect
   class entirely this time.
6. Gate V (visual, manual): pulled 14 frames every 8s across the full
   110.4s runtime, plus two frames at t=9.5s/10.6s for the B00 correction,
   and read every one directly. B00's correction ("approve" → "parse it
   into fields") lands legibly; B01's struck "clear or flag?" decision box
   and lit five-field list read cleanly, including the off-card
   "beneficial owner blank — recorded as missing, not flagged" line; B02's
   five-field anchor (with the fading "ONBOARDING PACKET" token beside
   each card) is legible at every step; B03's anchor-return and
   both-directions split ("captured is not cleared" / "missing is not
   fraud") read cleanly, including the strike-through on "CLEARED?" and
   the legible mini summary row; BCRY's carry-out quote, BHTF's Your Turn
   composer card, and BOUT's title outro all render legibly with no
   overlap, no clipping, no contrast issues. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.2 dB**, max -2.8 dB. Master mtime (00:03:23)
   is newer than beat_sheet.json mtime (00:00:45).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`financial-services--claude-liam-initiating-coverage`,
`financial-services--claude-liam-clean-data-xls`,
`financial-services--claude-liam-accrual-schedule`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), first pass
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 110.4s; mp4 mtime newer than beat_sheet.json mtime

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as every other `financial-services--*` sibling reel in this log.

Metadata file written: `financial-services--claude-liam-kyc-doc-parse.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
