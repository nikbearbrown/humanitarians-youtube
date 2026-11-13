#!/usr/bin/env python3
"""dat_rescore.py — re-score the DAT experiment's raw word lists with the official scorer.

Sasha Savsunenko's post (Nov 5, 2026) trained Qwen3.8-27B with the Divergent
Association Task (DAT) as a reward. His repo (github.com/crazyleg/dat-grpo-creativity,
MIT, commit f4715f6) ships the raw responses: results/raw/dat-full.tar.gz, 32
fixed prompts each for nouns, verbs and held-out adjectives, from the base model
("original") and the final full finetune ("step250" = Full250).

This script:
  1. scores every response with Jay Olson's official DAT code
     (github.com/jayolson/divergent-association-task @ 9978dd8, MIT) on GloVe
     840B 300d: the average cosine distance of the first 7 valid unique words,
     times 100. A response that is not a JSON list of words, or has fewer than
     7 valid words, scores 0 (as the repo's means do);
  2. compares each item with the repo's own item-scores.json;
  3. checks every word of the adjective lists against WordNet 3.0 (nltk): does
     it have ANY adjective sense? A list passes only if all ten do;
  4. scores two illustrative lists of our own.

Run (venv with numpy, scipy, nltk):
  python dat_rescore.py <dat_raw dir> <glove.840B.300d.txt> <dat repo dir>
"""
import json
import statistics
import sys
import time
from pathlib import Path


def main():
    raw, glove, dat_repo = map(Path, sys.argv[1:4])
    sys.path.insert(0, str(dat_repo))
    import dat  # Olson's official scorer
    import nltk
    from nltk.corpus import wordnet as wn

    t0 = time.time()
    model = dat.Model(str(glove), str(dat_repo / "words.txt"))
    print(f"official DAT scorer (dat.py, {dat_repo.name}) · GloVe {glove.name}: "
          f"{len(model.vectors):,} dictionary words with vectors · loaded in {time.time() - t0:.0f} s")
    print(f"WordNet {wn.get_version()} via nltk {nltk.__version__}")

    def words_of(text):
        try:
            w = json.loads(text)
        except Exception:
            return None
        return w if isinstance(w, list) and all(isinstance(x, str) for x in w) else None

    def has_adj(word):
        w = word.strip().lower().replace(" ", "_")
        return any(s.pos() in ("a", "s") for s in wn.synsets(w))

    summary = {}
    examples = {}
    for m in ("original", "step250"):
        rows = [json.loads(l) for l in open(raw / "no_think" / m / "responses.jsonl")]
        theirs = json.load(open(raw / "no_think" / m / "item-scores.json"))
        for task in ("dat_nouns", "dat_verbs", "dat_adjectives"):
            sel = [r for r in rows if r["case_id"].startswith(task + "/")]
            scores, worst, all_adj = [], 0.0, 0
            for r in sel:
                w = words_of(r["response"])
                s = model.dat(w) if w else None
                s = 0.0 if s is None else s
                scores.append(s)
                worst = max(worst, abs(s - theirs[r["case_id"]]["reward_score"]))
                if task == "dat_adjectives" and w and len(w) == 10 and all(has_adj(x) for x in w):
                    all_adj += 1
                examples.setdefault((m, task), []).append((round(s, 2), r["case_id"], w))
            mean = statistics.fmean(scores)
            summary[(m, task)] = (mean, len(sel), all_adj)
            extra = f" · lists whose 10 words all have an adjective sense: {all_adj}/{len(sel)}" \
                if task == "dat_adjectives" else ""
            print(f"{m:9s} {task:15s} n={len(sel)}  mean DAT {mean:6.2f}  "
                  f"(worst |ours - repo| per item {worst:.4f}){extra}")

    print("\nchange, base -> Full250 (raw official DAT, unscoreable = 0)")
    for task in ("dat_nouns", "dat_verbs", "dat_adjectives"):
        a, b = summary[("original", task)][0], summary[("step250", task)][0]
        print(f"  {task:15s} {a:6.2f} -> {b:6.2f}   ({b - a:+.2f})")

    print("\nexample lists (score, case, words)")
    for key in (("original", "dat_nouns"), ("step250", "dat_nouns")):
        ex = sorted(examples[key], key=lambda e: e[0])
        med = ex[len(ex) // 2]
        print(f"  {key[0]:9s} nouns median   {med[0]:6.2f} {med[1]:16s} {med[2]}")
    adj3 = [e for e in examples[("step250", "dat_adjectives")] if e[1] == "dat_adjectives/3"][0]
    print(f"  step250   adjectives/3   {adj3[0]:6.2f} {adj3[1]:16s} {adj3[2]}")
    print("    adjective sense per word: " + ", ".join(f"{x}={'yes' if has_adj(x) else 'no'}"
                                                     for x in adj3[2]))

    print("\nour illustrative lists")
    for name, w in (("farm animals", ["cat", "dog", "horse", "cow", "sheep", "pig", "goat"]),
                    ("far apart", ["volcano", "spoon", "justice", "violin", "glacier", "receipt",
                                   "tiger"])):
        print(f"  {name:12s} {model.dat(w):6.2f} {w}")


if __name__ == "__main__":
    main()
