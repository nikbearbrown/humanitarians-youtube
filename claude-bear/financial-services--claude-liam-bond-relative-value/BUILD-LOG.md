# BUILD-LOG — financial-services--claude-liam-bond-relative-value

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-bond-relative-value/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `bond-relative-value` skill (not an
unfilled placeholder shell) — see QUESTION.md. Facts preserved: the skill
performs relative value analysis on bonds by combining pricing, yield
curve context, credit spreads, and scenario stress testing; used for
richness/cheapness, spread decomposition, bond comparison, and rate-shock
scenarios. The `source_skill` path it names does not exist on this
machine (different machine's home directory), but no reconstruction was
needed.

**The call:** register re-registered Teardown → Plain. Source's B03
framed "what it gets right / where it bites" as a design-tell verdict —
Teardown language — removed; Plain states only the mechanism (price,
curve, spread, stress test) and its two failure directions as properties
of the practice, never a verdict on the skill's design. B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per
WRITER LAW: "feel" → "a curve" — the naive assumption that telling a
bond's richness or cheapness takes a trader's feel, corrected to: a read
computed against a yield curve. Added a wrong-guess beat (B01: trader's
feel vs. price/curve/spread/stress, falsified by "a bond with no yield
curve to compare against has nothing to spread it against, so nothing to
read") and an anchor (B02 → B03: a ten-year corporate bond, +40bp over
curve, traveling priced → curve read → spread decomposed → stress run →
a computed read, waiting) per this factory's PHASE 1 structure
requirement — the source's Teardown shape (anatomy / pipeline /
design-tell / verdict) carried neither. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Kept the source's 7-beat count
(B00, B01, B02, B03, BCRY, BHTF, BOUT). No source beat was AI-VIDEO,
pantry, or a human-drop slot — every source beat was already REMOTION,
so NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00
itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. **First B00
   draft failed the WRITER LAW timing check**: narration of 30 words
   (9.30s) never let the writer finish typing the replacement before the
   clip ended — frame-verified still mid-typing "by the s" (of "a
   curve") at t=9.25s of a 9.3s clip, one word short of landing the
   correction on screen at all. Fixed by lengthening the narration to 35
   words ("...the way a trader might...") for 10.41s, and shortening the
   replacement word from "the spread" to "a curve"; re-rendered,
   frame-verified the correction ("feel" → "a curve") fully lands by
   t=9.8s with real margin before the 10.43s clip ends. Other beat
   durations: B01 21.29s, B02 21.33s (later 21.30s after a scene edit
   below), B03 22.55s, BCRY 9.19s, BHTF 16.98s, BOUT 4.61s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `BRVB01Scene` /
   `BRVB02Scene` / `BRVB03Scene`) and `render_scenes.py`; all three
   rendered clean on the first pass.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the
   foreground (one run hit no background/timeout issue this time — all
   four completed within the single foreground call). All four rendered
   clean on the first pass (B00 re-rendered once after the timing fix
   above).
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K
   LAW). Manim clips B01/B02/B03 were each time-stretched 1.8–2.4x to
   fill their (longer) narration-driven beat durations — noted, not a
   defect: the scenes' own animation+hold timeline was authored shorter
   than the audio, and compile.py's slot-fill slows video to match
   audio, same mechanism used throughout this toolkit.
5. GATE T (`type_check.py`) FAILED on first pass — B02 flagged
   min-size §8.1 (an 8px text run under the 20px floor). Traced this to
   the documented em-dash false-positive class already logged
   extensively elsewhere in `type_check.py` (a dash glyph renders as a
   much narrower/shorter ink run than surrounding letters, occasionally
   fragmenting under the checker's connected-component detector).
   Per SKILL.md ("fix content, never the validator") did not touch
   `type_check.py`. First fix attempt: removed the em dash from B02's
   caption ("read: cheap 8bp — waiting" → "read: cheap 8bp, waiting") —
   GATE T still FAILED at 8px, same location, so the em dash was not
   the actual cause. Re-examined the scene: the checker samples a fixed
   frame at `dur*0.5` of the RAW manim clip, which landed mid
   fade-out/fade-in of the traveling anchor token between two of the
   four cards — a low-opacity cross-fade whose partial-alpha glyph
   edges can fragment into a tiny disconnected ink run (same general
   class of transitional-frame false positive documented for other
   scenes in this checker, though not this exact trigger). Fixed by
   replacing the token's per-stop `FadeOut`/`FadeIn` cycle with a single
   continuous `.animate.move_to()` — safe here because the token lives
   in its own column well clear of every card label (never crosses
   another element) — so there is no fade state left for the sampler to
   land inside. Re-rendered B02, recompiled, GATE T → PASS, clean, no
   other beats affected.
6. Gate V (visual, manual): pulled 27 frames every 4s across the full
   107.36s runtime and read every one directly. B00's correction
   ("feel" → "a curve") lands legibly with margin; B01's struck
   trader's-feel box and lit price/curve/spread/stress card read
   cleanly; B02's four-stop anchor (with the "10Y CORP +40BP" token
   beside each card) is legible at every step, including the payoff
   line "read: cheap 8bp, waiting"; B03's anchor-return and
   both-directions split ("cheap is not worth buying" / "rich is not
   avoid it") read cleanly, including the strike-through on "WORTH
   BUYING?"; BCRY's carry-out quote, BHTF's Your Turn composer card, and
   BOUT's title outro all render legibly with no overlap, no clipping,
   no contrast issues. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.0 dB**, max -2.9 dB. Master mtime is newer
   than beat_sheet.json mtime.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat
white rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family
(e.g. `financial-services--claude-liam-accrual-schedule`,
`financial-services--claude-liam-bond-futures-basis`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (B02 fade→continuous-move fix
  above; the em-dash-removal attempt in between did not fix it and is
  logged for the next agent's benefit)
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 107.36s; mp4 mtime newer than beat_sheet.json mtime

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the
map's documented fallback ("match SUBJECT.json's family, or the
hai-simple prefix"), fell through to the `hai-simple` skill-key literal
match, resolving to **Claude Basics** — same resolution as every other
`financial-services--*` sibling in this family.

Metadata file written:
`financial-services--claude-liam-bond-relative-value.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-bond-relative-value.mp4 \
   financial-services--claude-liam-bond-relative-value-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-bond-relative-value/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-bond-relative-value/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `13374fe8`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
