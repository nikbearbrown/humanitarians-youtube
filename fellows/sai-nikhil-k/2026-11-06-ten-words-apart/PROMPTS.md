# PROMPTS — Ten Words Apart

**No open generation slots.** Seven Remotion compositions and three plates of
Commons photos, the author's MIT figures and a model-card screenshot. No image
model, no paid API.

## B00 — the on-screen typed ask

> A researcher trained a 27B model with the Divergent Association Task as its reward. Did it get more creative, or just better at the test? Re-score his raw outputs.

## B08 — the handoff the viewer can paste

> Write ten single-word nouns, as different from each other in meaning as you can. Then tell me which two are closest in meaning, and why.

## Evidence commands

```bash
REEL=weekly_updates/2026-11-06-ten-words-apart
# inputs (not committed): the author's raw responses, Olson's scorer, GloVe 840B, WordNet
git clone https://github.com/crazyleg/dat-grpo-creativity && tar -xzf dat-grpo-creativity/results/raw/dat-full.tar.gz -C <dat_raw>
git clone https://github.com/jayolson/divergent-association-task <dat_official>
curl -L -o glove.840B.300d.zip https://huggingface.co/stanfordnlp/glove/resolve/main/glove.840B.300d.zip && unzip glove.840B.300d.zip
NLTK_DATA=<nltk_data> python -c "import nltk; nltk.download('wordnet', download_dir='<nltk_data>')"
# the re-score (venv with numpy, scipy, nltk)
NLTK_DATA=<nltk_data> <venv>/bin/python $REEL/evidence/dat_rescore.py <dat_raw> glove.840B.300d.txt <dat_official> > $REEL/evidence/dat_rescore.out
# the word photos and tiles
python3 $REEL/evidence/word_photos.py $REEL/images/src && python3 $REEL/make_tiles.py
```
