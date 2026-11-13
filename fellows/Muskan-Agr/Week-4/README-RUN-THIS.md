# README-RUN-THIS — Week 4

Everything runs from `~/Desktop/brutalist.art-main`.

## 0. Every new terminal session starts here

```bash
cd ~/Desktop/brutalist.art-main
source .venv/bin/activate
```

## 1. Narration (the master clock)

```bash
python3 runtime/scripts/generate_audio_kokoro.py reels/humanitarians-ai-week4-navigation-cleanup-handoff
```

## 2. Render + QC + review cut

```bash
./art run reels/humanitarians-ai-week4-navigation-cleanup-handoff
```

20 scenes at 3840×2160.

What to expect:
- **No `gate A warning` lines and no `gate W warning` lines.** Both gates were
  reproduced in a sandbox against this exact scenes.py and came back completely
  clean. Anything printed here is new.
- `GATE A FAILED` or a `GATE B` failure would both be new — send the **full**
  output, and for GATE B the **contents of `layout_audit.md`**. That file is
  what made Week 3's failure fixable precisely rather than by guesswork.

## 3. Check nothing is unfilled

```bash
./art todo reels/humanitarians-ai-week4-navigation-cleanup-handoff
```

## 4. Clean 4K master

```bash
./art final reels/humanitarians-ai-week4-navigation-cleanup-handoff
```

Writes to `renders/humanitarians-ai-week4-navigation-cleanup-handoff.mp4` **at
the toolkit root**.

The file inside the reel folder ending `-slate.mp4` is the review cut with the
QC burn-in bottom-left. That overlay is meant to be there. The file in
`renders/` is the clean one.

## 5. The 9:16 vertical cut

```bash
./art shorts reels/humanitarians-ai-week4-navigation-cleanup-handoff
ls -la reels/humanitarians-ai-week4-navigation-cleanup-handoff/short/manim/
```

If `short/manim/` comes back empty, that is the Week 1 failure reproducing —
send the full output.

## 6. Runtime check

```bash
python3 - <<'PY'
import json
d=json.load(open('reels/humanitarians-ai-week4-navigation-cleanup-handoff/beat_sheet.json'))
t=sum(b.get('actual_duration_s') or 0 for b in d['beats'])
w=sum(len(b['narration_text'].split()) for b in d['beats'])
print(f"total {int(t//60)}:{t%60:05.2f}   ({w} words / {t:.2f}s = {w/t:.2f} wps)" if t else "no audio yet")
PY
```
