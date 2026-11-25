# PROMPTS — Same App, New Look

**No open generation slots.** Six Remotion compositions and one plate of real
Gavia screenshots. No image model, no paid API.

## B00 — the on-screen typed ask

> Audit Gavia's interface against WCAG 2.2 AA and the Humanitarians AI brand. Propose the changes, build them on a branch, and measure before and after.

## B05 — the handoff the viewer can paste

> Here are my app's CSS colour tokens. List every text and background pair under 4.5:1 contrast (WCAG 2.2), and show the luminance arithmetic for the worst one.

## Evidence commands

```bash
REEL=weekly_updates/2026-11-13-same-app-new-look
SP=<scratch dir>
# 1. contrast from the tokens (before = 5dd8471 via git show; after = branch working tree)
python3 $REEL/evidence/contrast.py ~/Documents/gavia > $REEL/evidence/contrast.out
# 2. both versions side by side (real node_modules copies — a symlink 403s the fonts)
cd ~/Documents/gavia && git archive 5dd8471 desktop | tar -x -C $SP/app/asis
rsync -a --exclude node_modules desktop/ $SP/app/tobe/desktop/
cp -R desktop/node_modules $SP/app/asis/desktop/ && cp -R desktop/node_modules $SP/app/tobe/desktop/
(cd $SP/app/asis/desktop && ./node_modules/.bin/vite --port 5181 --strictPort &)
(cd $SP/app/tobe/desktop && ./node_modules/.bin/vite --port 5182 --strictPort &)
# 3. capture at 2x + axe-core 4.10.2 (TOOLS holds node_modules/{playwright-core,axe-core})
TOOLS=$SP/tools node $REEL/evidence/recapture.mjs $SP/cap \
    before=http://localhost:5181/ after=http://localhost:5182/ > $REEL/evidence/recapture.out
cp $SP/cap/recapture.json $REEL/evidence/
```
