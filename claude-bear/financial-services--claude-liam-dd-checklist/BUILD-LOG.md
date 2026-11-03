# BUILD-LOG — financial-services--claude-liam-dd-checklist

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-dd-checklist/beat_sheet.json`
(7-beat Teardown "skill-teardown" sheet for the Anthropic `dd-checklist`
skill, private-equity vertical plugin, brand `claude-liam`, @NikBearBrown).

**Source note:** the source sheet's narration already carries real,
specific facts about the skill — generate and track comprehensive due
diligence checklists tailored to the target company's sector, deal type,
and complexity; covers all major workstreams with request lists, status
tracking, and red-flag escalation; used when kicking off diligence,
organizing a data room review, or tracking outstanding items — see
QUESTION.md. The `source_skill` path it names (private-equity vertical
plugin `SKILL.md`) does not exist on this machine, but no reconstruction
was needed.

**The call:** register re-registered Teardown → Plain. Source's B03 framed
"what it gets right / where it bites" as a design-tell verdict — Teardown
language — removed; Plain states only the mechanism (read sector/type/
complexity, build workstreams from the file, escalate red flags) and its
two failure directions as properties of the practice, never a verdict on
the skill's design. B00 replaced the source's `ClaudeComposerAsk` cold open
with `BrutalistHesitantWriter` per WRITER LAW: "judgment" → "the file" —
the naive assumption that building the checklist takes Claude's own
judgment about this deal's risks, corrected to: it tailors from what the
file already defines. Added a wrong-guess beat (B01: deal judgment vs.
sector/type/complexity-to-workstreams, falsified by "hand it a sector the
file never lists and it has no independent research to reach for") and an
anchor (B02 → B03: a software acquisition's "customer contracts" request
traveling requested → received → reviewed → flagged, then paid off into
"run twice, same checklist" / "a mineral rights transfer has nothing
tailored to reach for") per this factory's PHASE 1 structure requirement —
the source's Teardown shape (anatomy / pipeline / design-tell / verdict)
carried neither. Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Kept the source's 7-beat count (B00, B01, B02, B03, BCRY,
BHTF, BOUT). No source beat was AI-VIDEO, pantry, or a human-drop slot —
every source beat was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no beat replacement beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.79s (clear of the ≥9s TIMING LAW floor)
   on the first narration draft (34 words + `lead_silence_s: 0.8`).
   Durations: B00 10.79s, B01 21.42s, B02 20.63s, B03 22.93s, BCRY 11.50s,
   BHTF 20.29s, BOUT 4.35s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `DDCB01Scene` /
   `DDCB02Scene` / `DDCB03Scene`) and `render_scenes.py`; rendered B01/B02/B03
   clean on the first pass, foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` — the shell moved it
   to a background task past the 120s inline timeout; blocked on it with
   `TaskOutput` rather than ending the turn, per the one-shot COMPLETION
   LAW. All four rendered clean on the first pass, each extended to its
   measured audio duration (B00 10.8s, BCRY 11.5s, BHTF 20.3s, BOUT 4.3s).
   Confirmed BHTF's explicit `folderLabel: "@HumanitariansAI"` override
   rendered correctly (a known sibling-reel defect is `ClaudeComposerAsk`'s
   Root.tsx `defaultProps` hardcoding `@NikBearBrown` when the beat sheet
   omits the override).
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K LAW),
   mean_volume -24.0 dB (GATE AUDIO pass on the first compile).
5. GATE T (`type_check.py`) FAILED on B03 across two fix attempts before
   landing clean:
   - **Attempt 1**: contrast §8.3 FAIL — terracotta accent text
     ("SAME CHECKLIST") on cream, 2.74:1 < 4.5:1 WCAG. Recolored that text
     run to INK. Re-rendered, re-ran GATE T — **still FAILED**, identical
     finding.
   - **Attempt 2, root cause**: a second TERRA-colored `Text()` element (a
     "✓" checkmark glyph) was also present and read the same way. Recolored
     it to INK too. **Still FAILED**, identical finding — the real source
     was the top mini-row's three small cards using `border=TERRA`, the
     exact documented false-positive class from the
     `financial-services--claude-liam-accrual-schedule` sibling reel's own
     GATE T failure (a small card's thin accent-colored stroke has enough
     perimeter-to-area fill to get read as an accent "text" region and
     contrast-checked against cream). Recolored those three card borders
     (and their connector lines) from TERRA to TEAL — matching the already-
     working convention in B01/B02 — and updated `scenes.py`'s module
     docstring and the `_card()` helper's default border to TEAL so future
     beats in this reel don't reintroduce the same class of defect. GATE T →
     PASS, clean, no other changes needed.
6. Gate V (visual, manual): pulled 13 frames across the full 112.9s
   runtime at settled (not mid-animation) points and read every one
   directly. B00's correction ("judgment" → "the file") is fully typed and
   settled by t=9.5s of a 10.8s beat; B01's struck deal-judgment box and lit
   procedure card read cleanly, including the "sector not listed — no
   template" caption outside the card border; B02's four-stop anchor (with
   the traveling "CUSTOMER CONTRACTS" token beside each TEAL-bordered card)
   is legible at every step, landing on "revenue concentration — one
   customer"; B03's anchor-return and both-directions split ("same input,
   same checklist" with a checkmark / "stops where the file does" with the
   struck "TAILORED?") read cleanly; BCRY's carry-out quote, BHTF's Your
   Turn composer card (confirmed `@HumanitariansAI`, not the hardcoded
   default), and BOUT's title outro (confirmed `@HumanitariansAI`, no
   Claude mascot) all render legibly with no overlap, no clipping, no
   contrast issues. No defects found.
7. Audio presence: independently verified with `ffprobe` (h264 3840×2160 +
   aac streams present) and `ffmpeg -af volumedetect` on the final master →
   mean_volume **-24.0 dB**, max -2.8 dB. Master mtime (1788283987) is
   newer than beat_sheet.json mtime (1788283412).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), third pass (B03 TERRA→TEAL card-border root-cause
  fix above)
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 112.9s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as the `accrual-schedule` and `3-statement-model` sibling reels in this
same family.

Metadata file written:
`financial-services--claude-liam-dd-checklist.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
