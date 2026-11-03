# ECIS Episode 11 — Reading Between the Questions

## Series
ECIS Weekly Update (Episode 11)


## Summary
Episode 11 covers Phase 16 (Week 16): advanced analytics and ML models. Three major additions: (1) Q&A dodge detection — parsing analyst questions from management answers, scoring evasion with a cross-encoder reranker and question-type weighting, (2) market share language analysis — an ensemble of lexicon-based, zero-shot (BART-MNLI), and fine-tuned stance detection classifiers scoring offensive vs defensive competitive positioning, and (3) a guidance revision predictor — six ML models (logistic regression, XGBoost, Random Forest, LightGBM, MLP, CatBoost) predicting whether a company will revise guidance next quarter. Also covers financial Q&A fine-tuned Sentence-BERT and a FinBERT ensemble for stable sentiment.

## Beat structure
| Beat | Title                        |
|------|------------------------------|
| B01  | Recap                        |
| B02  | Dodge Detection              |
| B03  | Competitive Positioning      |
| B04  | Guidance Revision Predictor  |
| B05  | Embedding Upgrades           |
| B06  | Your Turn                    |


## Delivery

Both orientations at 4K:

| Cut | Composition | Master | Runtime |
|-----|-------------|--------|---------|
| 16:9 | 3840×2160 | `ecis-ep11.mp4` | 286.2s (4:46) |
| 9:16 | 2160×3840 | `short/ecis-ep11-short.mp4` | 149.2s (2:29) |


## Rebuild


```sh
python3 runtime/scripts/generate_audio_kokoro.py /ecis-ep11
python3 runtime/scripts/remotion_scenes.py      /ecis-ep11 
./art final /ecis-ep11
```
