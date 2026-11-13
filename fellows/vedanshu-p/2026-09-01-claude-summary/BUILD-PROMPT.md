# BUILD-PROMPT — claude-rag-the-right-text

Paste-ready prompt that rebuilds this reel end to end. Run from the repo that
holds the toolkit (`brutalist.art-main`). Free path only — Kokoro is local,
nothing here calls a paid API, and nothing here publishes.

---

## Prompt

```
Rebuild the reel at D:/ai1-cli-main/youtube/2026-09-07-claude-rag-the-right-text
end to end, following skills/make/ai-explainer/SKILL.md.

Windows preflight (both are required on this machine, and both are silent
failures if skipped):
  export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
  # several runtime/scripts read and write with the cp1252 default codec and
  # crash on the em-dashes in their own output
  # runtime/models/kokoro/{kokoro-v1.0.onnx,voices-v1.0.bin} must exist —
  # they are not in the git repo; fetch per ./setup --install if absent
  python runtime/scripts/setup_smoke_kokoro.py   # must print mean_volume > -40 dB

1. GATE L — confirm every pattern the sheet asks for is renderable:
     for n in ClaudeComposerAsk BrutalistHesitantWriter EmbedWordToPassage \
              CliRunOutput EmbedRevealPairs EmbedCosineSimilarity \
              ClaudeVerdictArtifact TitleOutroChannel; do
       python runtime/scripts/scene_search.py --check "$n"
     done

2. Audio (the master clock — durations are ground truth, do not hand-time):
     python runtime/scripts/generate_audio_kokoro.py <REEL>
   Verify B01 measures >= 9s, or the hesitant-writer correction gets cut off.

3. Beats:
     python runtime/scripts/remotion_scenes.py <REEL> --now <iso8601>
   Renders 1920x1080 comps at --scale=2, i.e. true 3840x2160.

4. Review cut (slates visible, timecode burned):
     python runtime/scripts/compile.py <REEL> --review --height 1080

5. VISUAL QC LAW — mandatory, and the mp4 probe does NOT count:
     ffmpeg -i <review.mp4> -vf fps=2 _qc/frames/%05d.png
   Actually READ the PNGs and audit the 9-point rubric (edge bleed, title-safe,
   overflow, collision, offscreen anchors, legibility, brand bug, aspect,
   canvas fill). Log findings in _qc/REPORT.md. Fix root causes in the scene
   source, never by nudging pixels, and re-render until zero BLOCKER/MAJOR.

6. Clean 4K master (no beat markers, no timecode):
     python runtime/scripts/compile.py <REEL> --height 2160 --out <REEL>

Never publish. The master stays in the reel folder for human review.
```

---

## Known traps on this reel

- **`ClaudeComposerAsk.output` is `z.array(z.string())`.** Passing a
  newline-delimited string renders nothing and fails the beat with
  `output.map is not a function`. B00 carries four lines as an array.
- **`BrutalistHesitantWriter` triggers are matched per whitespace token**, so a
  multi-word `triggerWords` entry can never fire (the SKILL.md's advice to put
  a whole phrase there does not work against the current component).
  B01 therefore swaps the single word `more` → `the right`, which still
  corrects the whole sentence.
- **`lead_silence_s` on B01 is inert** — no script reads it. The 9s window is
  met by narration length instead.
- **`compile.py --review` needed a Windows fix** to escape the font path before
  it enters the ffmpeg filtergraph; without it the drawtext timecode aborts the
  compile. Fixed in-tree.

## Provenance

Nothing in this reel is a new claim — it summarises three finished reels, and
every on-screen number traces to one of their beat sheets. See `SOURCES.md`
for the claim-by-claim table, and `CHECKS-REPORT.md` for the PROOF GATE audit.
