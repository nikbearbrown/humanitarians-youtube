# README-RUN-THIS — Week 2

Everything below runs from the toolkit root: `~/Desktop/brutalist.art-main`.

## 0. Every new terminal session starts here

```bash
cd ~/Desktop/brutalist.art-main
source .venv/bin/activate
```

If you skip this, Manim and Kokoro are not on the path and step 2 fails in a
confusing way.

## 1. Generate the narration (this is the master clock)

```bash
python3 runtime/scripts/generate_audio_kokoro.py reels/humanitarians-ai-week2-typography-hero-concepting
```

Every beat's final length is however long its own mp3 runs. The `self.wait()`
values in scenes.py are approximate and auto-retime to match.

## 2. Render + QC + review cut

```bash
./art run reels/humanitarians-ai-week2-typography-hero-concepting
```

17 scenes at 3840×2160, 24fps. Expect this to take a while.

What to expect in the log, and what is fine:
- `gate A warning on B01_ScopeCard (continuing)` and the same for B02, B03,
  B07, B12, B15, B16 — **expected, 7 of them, non-blocking.** Week 1 shipped
  with 4 of the same class.
- `gate W warning ... continuing` — should NOT appear this time. All 17 scenes
  were made checkable; if one does appear, that is new and worth a look.
- `GATE A FAILED` — this would be new. Stop and send me the full output.
- `GATE B` failure — send me the **contents of `layout_audit.md`**, not a
  summary. That file has the exact box coordinates needed to fix it precisely.

The review cut has a burned-in QC overlay bottom-left (beat id, shot type,
running clock). That is intentional and only on this cut.

## 3. Check nothing is unfilled

```bash
./art todo reels/humanitarians-ai-week2-typography-hero-concepting
```

## 4. Clean 4K master

```bash
./art final reels/humanitarians-ai-week2-typography-hero-concepting
```

Writes to `renders/humanitarians-ai-week2-typography-hero-concepting.mp4` at
the toolkit root — no `-cut` suffix, not inside the reel folder. Check the log
line the command prints rather than guessing the path.

## 5. The 9:16 vertical cut — and actually verify it this time

```bash
./art shorts reels/humanitarians-ai-week2-typography-hero-concepting
ls -la reels/humanitarians-ai-week2-typography-hero-concepting/short/manim/
ls -la renders/
```

On Week 1 this command created `short/` with a derived beat_sheet.json and
rendered **nothing** — `short/manim/` is still empty and no vertical master
exists. The review checklist requires both 16:9 and 9:16, so if `short/manim/`
comes back empty again, paste me the full output of the `./art shorts` command.

## 6. Runtime check

Target is 3:00–4:00. The script is written for 3:50 at Week 1's measured pace
of 2.89 words/sec. After step 1, this prints the real total:

```bash
python3 - <<'PY'
import json
d=json.load(open('reels/humanitarians-ai-week2-typography-hero-concepting/beat_sheet.json'))
t=sum(b.get('actual_duration_s') or 0 for b in d['beats'])
print(f"total {int(t//60)}:{t%60:05.2f}  ({t:.1f}s)")
PY
```

If it lands under 3:00, SHOPPING.md names the cheapest beat to add.
