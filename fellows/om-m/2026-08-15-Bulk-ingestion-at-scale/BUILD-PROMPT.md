# BUILD-PROMPT — bulk-ingestion-at-scale

The single paste-ready Claude Code prompt that rebuilds this reel end to end.
Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/humanitarians-youtube/fellows/om-mali/2026-08-15-Bulk-ingestion-at-scale

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata_week2.json is queried from the built Parquet in the Mycroft repo. Every on-screen
   number is a prop read from it. If you change a figure, change the data file and re-inject —
   never type a number into a scene or a beat sheet by hand. Re-inject the staircase with:

     python3 - <<'PY'
     import json, pathlib
     R = pathlib.Path(".")   # the reel dir
     fig = json.loads((R/"figdata_week2.json").read_text(encoding="utf-8"))
     bs  = json.loads((R/"beat_sheet.json").read_text(encoding="utf-8"))
     for b in bs["beats"]:
         if b["beat_id"] == "B03":
             b["shot"]["remotion"]["props"]["series"] = [
                 {"date": r["date"], "med": r["med"]} for r in fig["anthropic"]]
     (R/"beat_sheet.json").write_text(json.dumps(bs, indent=1, ensure_ascii=False), encoding="utf-8")
     PY

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Row 16 ("counted one manager as five") is DERIVED from the
     worklog's "four independent managers" plus Fidelity's own mapped registrations — confirm
     it rather than assuming it.
   - PEDAGOGY.md must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human what
     they are being asked to sign — do not sign it yourself, do not pass --no-gate for a final.
   - CHECKS-REPORT.md must exist before the first compile.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the whole report series. Never change
   it silently. Then write each beat's measured actual_duration_s into its
   shot.remotion.props.durationInSeconds so every scene re-times to its real narration.

3. RENDER
   python3 runtime/scripts/remotion_scenes.py <reel> --only <BID>
   Eleven beats, all Remotion, zero slates. The seven reel-local scenes live in
   runtime/remotion/src/BulkIngestionAtScale.tsx (registered in Root.tsx under the
   BulkIngestionAtScale folder). Never hand-roll `npx remotion render`.
   Render in small foreground batches — a full-reel background run gets killed part-way.

4. COMPILE
   ./art run <reel> --height 1080      # review cut + GATE L + GATE V
   ./art final <reel>                  # clean 4K master, only once GATE P reads PASS

5. VISUAL QC — LOOK at frames, never trust the mp4 probe
   Sample each beat at ~55% and ~90% of its span, actually Read the PNGs, and audit the 9-point
   rubric. GATE V passing is NOT the end of QC: on this reel the gate caught B05's contrast but
   missed B06 emptying its lower two-thirds and B04's tick collapse. Log everything in
   _qc/REPORT.md and fix root causes in the scene source.

6. REPORT — never publish. The master stays in the reel folder.

Laws that bind hardest on this reel:
- REBUILD LAW — pantry/w2-*.png and .svg are REFERENCE ONLY. Never slot them as media.
- DOUBLE-CHECK LAW — no figure on screen that is not traceable to a FACTCHECK.md row.
- ILLUSTRATE LAW — the Claude UI appears at B00, B08, B09, B10 only. Seven body beats, seven
  different visual schemes.
- SHOW-DON'T-TELL — every body beat must MOVE. In particular B03's step path DRAWS, B02's third
  bar COLLAPSES, and B04's 24 ticks GROUP into 7. Those three motions are the reel's arguments.
```

---

## Series context

This is week 2. Week 1 is `../2026-08-08-Verifying-Private-AI-Valuations` and its
`_previous-build/` holds the pre-brutalist cut. The two reels share a channel, a voice, a
palette and a spine; their scene files are deliberately independent so either can be
re-rendered without touching the other.
