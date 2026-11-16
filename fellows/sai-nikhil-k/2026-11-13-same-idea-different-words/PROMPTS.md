# PROMPTS — Same Idea, Different Words

**No open generation slots.** Six Remotion compositions and one plate of three
Portals worlds rendered locally from Mollick's code. No image model, no paid API.

## B00 — the on-screen typed ask

> Ethan Mollick says Fable 5.2 is “jagged AGI”. Test one of his examples against the code he published, not against the essay.

## B05 — the handoff the viewer can paste

> Give me twenty ideas for short videos about AI. Then group any that are the same idea in different words, and say why.

## Evidence commands

```bash
REEL=weekly_updates/2026-11-13-same-idea-different-words
SP=<scratch dir>   # downloads in their own folder; scripts elsewhere
git clone --depth 1 https://github.com/emollick/ai-portals.git $SP/dl-portals/repo
# 1. the overlap measurement (system python3: scikit-learn 1.8.0)
python3 -I $REEL/evidence/overlap.py $SP/dl-portals/repo > $REEL/evidence/overlap.out
# 2. the stills: serve the repo as static files, then the repo's own freeze/grab harness
python3 -I -m http.server 8010 --bind 127.0.0.1 --directory $SP/dl-portals/repo &
TOOLS=$SP/tools node $REEL/evidence/portal_shots.mjs $SP/portal_shots http://127.0.0.1:8010 \
    reindeer-cyclone:0.55:25 manta-cyclone:0.55:25 stork-kettle-riso:0.05:2
```

Pose = (path fraction u, world time t). Each world picks its own seed (logged
in the sidecars); `&seed=` hung the page, so it isn't used. zsh: pass poses as
separate arguments (an unquoted string variable is not word-split).
