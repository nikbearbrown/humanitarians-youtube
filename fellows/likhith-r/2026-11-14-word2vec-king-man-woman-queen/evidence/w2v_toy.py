"""w2v_toy.py — a tiny skip-gram Word2Vec (negative sampling) in plain numpy, for claude-hai-word2vec.

Every number the reel shows comes from this run (evidence/w2v_toy.json, summarised in w2v_toy.out.txt):
vocabulary ids and one-hot cosines (B03), shared-neighbour shares (B04), the vector length and a real
vector (B05), cosine similarities, offset ("direction") cosines and a 2-D PCA map (B06), and the
analogy ranking with and without the input words excluded (B07).

The corpus is BUILT IN: sentences generated from fixed templates with a fixed seed, written for this
video. It is NOT natural text, so the toy shows the mechanism, not Google's results. The templates give
every word only its company (neighbouring words); no labels such as "royal" or "female" exist anywhere
in the model's input — "he"/"crown" are just more words.

Training hyperparameters were fixed before the first run and never changed. The corpus templates were
revised ONCE after the first run (log kept as run_v1.log / w2v_toy_v1.out.txt): king and prince had
identical company (cosine 0.997), so prince/princess were dropped and words got lives outside gender and
rank (chess, bees, lions), and each city/country pair got its own local words (sushi, the seine):
dim 300 (the size of Google's released vectors), window 2, 5 negatives, unigram^0.75 noise,
SGD lr 0.025 → 0.0001 linear decay, 5 epochs, seed 2026.

Usage:  .venv/bin/python youtube/brutalist/claude-hai-word2vec/evidence/w2v_toy.py
"""
import json
import os
import pathlib
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SEED, DIM, WINDOW, NEG, EPOCHS, LR0, LR_MIN, BATCH = 2026, 300, 2, 5, 5, 0.025, 0.0001, 256
N_SENT = 30000
OTHER_SHARE = float(os.environ.get("W2V_OTHER_SHARE", "0.6"))  # share of king/queen/man/woman sentences from their other lives
OUT = os.environ.get("W2V_OUT", "w2v_toy")

rng = np.random.default_rng(SEED)
pick = lambda xs: xs[rng.integers(len(xs))]

# ---------------------------------------------------------------- the built-in corpus
PEOPLE = {  # word: (pronouns, status)
    "king": ("m", "royal"), "queen": ("f", "royal"),
    "man": ("m", "common"), "woman": ("f", "common"), "boy": ("m", "common"), "girl": ("f", "common"),
}
# words have other lives too (polysemy, as in real text): company that has nothing to do with gender or rank
OTHER = {
    "king": ["the lion is the king of the jungle", "the king piece moves one square in chess", "elvis was called the king of rock"],
    "queen": ["the queen bee lays eggs in the hive", "the queen piece moves across the chess board", "the queen of hearts is a playing card"],
    "man": ["the man in the moon is a story", "a man overboard call stops the boat"],
    "woman": ["the woman of the year award was given", "a woman's march filled the square"],
}
PRON = {"m": ["he", "his", "him"], "f": ["she", "her", "her"]}
STATUS = {
    "royal": dict(verb=["rules", "rules over", "guards", "visits"], obj=["the kingdom", "the palace", "the throne", "the crown", "the royal court"]),
    "common": dict(verb=["works on", "walks to", "cleans", "visits"], obj=["the farm", "the shop", "the street", "the market", "the village"]),
}
PLACES = [("paris", "france", "french", ["croissants", "wine", "cheese"]), ("tokyo", "japan", "japanese", ["sushi", "ramen", "sake"]),
          ("rome", "italy", "italian", ["pasta", "pizza", "espresso"]), ("berlin", "germany", "german", ["sausages", "beer", "pretzels"]),
          ("madrid", "spain", "spanish", ["tapas", "paella", "churros"]), ("cairo", "egypt", "egyptian", ["falafel", "dates", "koshari"])]
THINGS = {
    "cat": ["purrs", "sleeps", "chases mice", "drinks milk", "licks its fur", "sits on the sofa"],
    "kitten": ["purrs", "sleeps", "chases mice", "drinks milk", "licks its fur", "sits on the sofa"],
    "dog": ["barks", "sleeps", "chases the ball", "wags its tail", "fetches sticks", "sits on the sofa"],
    "puppy": ["barks", "sleeps", "chases the ball", "wags its tail", "fetches sticks", "sits on the sofa"],
    "carburetor": ["mixes fuel and air", "feeds the engine", "needs a new gasket", "leaks fuel", "is under the hood", "was cleaned by the mechanic"],
    "piston": ["moves in the engine", "drives the engine", "needs a new ring", "leaks oil", "is under the hood", "was cleaned by the mechanic"],
}
YOUNG = {"kitten": "little", "puppy": "little", "cat": "old", "dog": "old"}


def person_sentence():
    w = pick(list(PEOPLE))
    if w in OTHER and rng.random() < OTHER_SHARE:
        return pick(OTHER[w])
    g, s = PEOPLE[w]; p = PRON[g]; st = STATUS[s]
    t = rng.integers(4)
    if t == 0:
        return f"the {w} said {p[0]} {pick(st['verb'])} {pick(st['obj'])}"
    if t == 1:
        return f"{p[0]} is the {w} and {p[0]} {pick(st['verb'])} {pick(st['obj'])}"
    if t == 2:
        return f"the {w} {pick(st['verb'])} {pick(st['obj'])} with {p[1]} family"
    return f"everyone met the {w} and thanked {p[2]} at {pick(st['obj'])}"


def place_sentence():
    # every place-specific word sits within the window (2) of the place name
    city, country, lang, local = PLACES[rng.integers(len(PLACES))]
    place = pick([city, country])
    t = rng.integers(8)
    if t == 0:
        return f"{city} is the capital of {country}"
    if t == 1:
        return f"we visited the {lang} capital {city} last year"
    if t == 2:
        return f"the mayor of {city} rides the city bus"
    if t == 3:
        return f"{country} speaks {lang} as a nation"
    if t == 4:
        return f"the government of {country} guards the border"
    if t == 5:
        return f"people in {place} love {pick(local)}"
    if t == 6:
        return f"{pick(local)} from {place} is famous"
    return f"{place} {pick(local)} tastes great"


def thing_sentence():
    w = pick(list(THINGS))
    t = rng.integers(3)
    if t == 2 and w in YOUNG:
        return f"the {YOUNG[w]} {w} {pick(THINGS[w])}"
    return f"the {w} {pick(THINGS[w])}"


makers = [person_sentence, place_sentence, thing_sentence]
corpus = [makers[rng.integers(3)]().split() for _ in range(N_SENT)]
tokens = [w for s in corpus for w in s]

# ---------------------------------------------------------------- vocabulary (ids by frequency)
uniq, counts = np.unique(np.array(tokens), return_counts=True)
order = np.lexsort((uniq, -counts))
vocab = [str(uniq[i]) for i in order]
freq = counts[order]
idx = {w: i for i, w in enumerate(vocab)}
V = len(vocab)

# ---------------------------------------------------------------- (centre, context) pairs
cen, ctx = [], []
for s in corpus:
    ids = [idx[w] for w in s]
    for i, c in enumerate(ids):
        for j in range(max(0, i - WINDOW), min(len(ids), i + WINDOW + 1)):
            if j != i:
                cen.append(c); ctx.append(ids[j])
cen, ctx = np.array(cen), np.array(ctx)
noise = freq ** 0.75; noise = noise / noise.sum()

# neighbour statistics for B04 (the company each word keeps)
def neighbours(w):
    return set(ctx[cen == idx[w]].tolist())
def share(a, b):  # share of b's distinct neighbours that are also a's
    na, nb = neighbours(a), neighbours(b)
    return len(na & nb) / len(nb)

# ---------------------------------------------------------------- skip-gram, negative sampling
W_in = (rng.random((V, DIM)) - 0.5) / DIM
W_out = np.zeros((V, DIM))
sig = lambda x: 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))
n_pairs = len(cen); total = EPOCHS * n_pairs; seen = 0
loss_log = []
t0 = time.time()
for ep in range(EPOCHS):
    perm = rng.permutation(n_pairs)
    run_loss, run_n = 0.0, 0
    for k in range(0, n_pairs, BATCH):
        bi = perm[k:k + BATCH]
        lr = max(LR_MIN, LR0 * (1 - seen / total))
        c, o = cen[bi], ctx[bi]
        negs = rng.choice(V, size=(len(bi), NEG), p=noise)
        tgt = np.concatenate([o[:, None], negs], 1)                  # (B, 1+NEG)
        lab = np.zeros(tgt.shape); lab[:, 0] = 1
        vc = W_in[c]                                                 # (B, D)
        vo = W_out[tgt]                                              # (B, 1+NEG, D)
        sc = sig(np.einsum("bd,bkd->bk", vc, vo))
        g = sc - lab                                                 # dL/dscore
        run_loss += float(-(np.log(sc[:, 0] + 1e-9) + np.log(1 - sc[:, 1:] + 1e-9).sum(1)).sum()); run_n += len(bi)
        grad_c = np.einsum("bk,bkd->bd", g, vo)
        grad_o = g[:, :, None] * vc[:, None, :]
        np.add.at(W_in, c, -lr * grad_c)
        np.add.at(W_out, tgt.reshape(-1), -lr * grad_o.reshape(-1, DIM))
        seen += len(bi)
    loss_log.append(round(run_loss / run_n, 4))
    print(f"epoch {ep + 1}/{EPOCHS} loss {loss_log[-1]:.4f} ({time.time() - t0:.0f}s)")

E = W_in / np.linalg.norm(W_in, axis=1, keepdims=True)
vec = lambda w: E[idx[w]]
cos = lambda a, b: float(vec(a) @ vec(b))


def analogy(a, b, c, exclude, k=6):
    """3CosAdd: nearest words to b − a + c (e.g. king − man + woman), cosine on unit vectors."""
    q = vec(b) - vec(a) + vec(c); q = q / np.linalg.norm(q)
    sims = E @ q
    ranked = [(vocab[i], round(float(sims[i]), 3)) for i in np.argsort(-sims)]
    if exclude:
        ranked = [r for r in ranked if r[0] not in (a, b, c)]
    return ranked[:k]


def offset_cos(a1, b1, a2, b2):
    d1 = vec(b1) - vec(a1); d2 = vec(b2) - vec(a2)
    return float(d1 @ d2 / np.linalg.norm(d1) / np.linalg.norm(d2))


# one-hot cosines (B03): ids are positions; every pair of different one-hots is orthogonal
onehot = np.eye(V)
oh = lambda a, b: float(onehot[idx[a]] @ onehot[idx[b]])

# 2-D PCA over the words on the map (B06)
MAP = ["king", "queen", "man", "woman", "paris", "france", "tokyo", "japan", "cat", "kitten", "carburetor"]
M = np.stack([vec(w) for w in MAP]); Mc = M - M.mean(0)
_, sv, Vt = np.linalg.svd(Mc, full_matrices=False)
xy = Mc @ Vt[:2].T
var2 = float((sv[:2] ** 2).sum() / (sv ** 2).sum())

# per-group 2-D PCA (B06 directions panels): each panel is fitted to its own four words only
def group_pca(ws):
    G = np.stack([vec(w) for w in ws]); Gc = G - G.mean(0)
    _, gs, gV = np.linalg.svd(Gc, full_matrices=False)
    return {"words": ws, "xy": [[round(float(a), 4), round(float(b), 4)] for a, b in Gc @ gV[:2].T],
            "var2": round(float((gs[:2] ** 2).sum() / (gs ** 2).sum()), 3)}


def examples(w, n=3):
    out = []
    for s_ in corpus:
        j = " ".join(s_)
        if w in s_ and j not in out:
            out.append(j)
        if len(out) == n:
            break
    return out


res = {
    "seed": SEED, "other_share": OTHER_SHARE, "numpy": np.__version__, "dim": DIM, "window": WINDOW, "negatives": NEG, "epochs": EPOCHS,
    "sentences": N_SENT, "tokens": len(tokens), "vocab_size": V, "pairs": int(n_pairs), "loss_by_epoch": loss_log,
    "ids": {w: idx[w] for w in ["cat", "kitten", "carburetor", "king", "queen", "man", "woman"]},
    "onehot_cos": {"cat_kitten": oh("cat", "kitten"), "cat_carburetor": oh("cat", "carburetor")},
    "neighbour_share": {"kitten_in_cat": round(share("cat", "kitten"), 3), "carburetor_in_cat": round(share("cat", "carburetor"), 3)},
    "neighbours": {w: sorted(vocab[i] for i in neighbours(w)) for w in ["cat", "kitten", "carburetor"]},
    "cos": {"cat_kitten": round(cos("cat", "kitten"), 3), "cat_carburetor": round(cos("cat", "carburetor"), 3),
            "king_queen": round(cos("king", "queen"), 3), "paris_tokyo": round(cos("paris", "tokyo"), 3)},
    "nearest": {w: [(vocab[i], round(float(E[idx[w]] @ E[i]), 3)) for i in np.argsort(-(E @ vec(w)))[1:6]] for w in ["cat", "king", "paris"]},
    "offset_cos": {"man_woman__king_queen": round(offset_cos("man", "woman", "king", "queen"), 3),
                   "france_paris__japan_tokyo": round(offset_cos("france", "paris", "japan", "tokyo"), 3),
                   "man_woman__paris_france": round(offset_cos("man", "woman", "paris", "france"), 3)},
    "analogy_king_included": analogy("man", "king", "woman", exclude=False),
    "analogy_king_excluded": analogy("man", "king", "woman", exclude=True),
    "analogy_tokyo_included": analogy("france", "paris", "japan", exclude=False),
    "analogy_tokyo_excluded": analogy("france", "paris", "japan", exclude=True),
    "pca_words": MAP, "pca_xy": [[round(float(a), 4), round(float(b), 4)] for a, b in xy], "pca_var2": round(var2, 3),
    "group_places": group_pca(["paris", "france", "tokyo", "japan"]),
    "group_people": group_pca(["man", "woman", "king", "queen"]),
    "examples": {w: examples(w) for w in ["cat", "kitten", "carburetor"]},
    "window_sentence": next(" ".join(s_) for s_ in corpus if " ".join(s_) == "the king said he rules the kingdom"),
    "window_sentence_count": sum(1 for s_ in corpus if " ".join(s_) == "the king said he rules the kingdom"),
    "token_vectors": {w: [round(float(x), 4) for x in vec(w)[:48]] for w in ["the", "cat", "purrs"]},
    "king_vector": [round(float(x), 4) for x in vec("king")],
    "sample_sentences": [" ".join(s) for s in corpus[:12]],
}
(HERE / f"{OUT}.json").write_text(json.dumps(res, indent=1) + "\n")

lines = [
    f"w2v_toy.py · numpy {np.__version__} · seed {SEED} · other-life share {OTHER_SHARE}",
    f"corpus: {N_SENT:,} built-in template sentences, {len(tokens):,} tokens, vocab {V}",
    f"skip-gram + negative sampling: dim {DIM}, window {WINDOW}, {NEG} negatives, {EPOCHS} epochs, {n_pairs:,} pairs",
    f"loss by epoch: {loss_log}",
    f"ids: {res['ids']}",
    f"one-hot cosine: cat·kitten {res['onehot_cos']['cat_kitten']}, cat·carburetor {res['onehot_cos']['cat_carburetor']}",
    f"neighbour share: kitten's neighbours also cat's {res['neighbour_share']['kitten_in_cat']}, carburetor's {res['neighbour_share']['carburetor_in_cat']}",
    f"cosine after training: {res['cos']}",
    f"nearest: {res['nearest']}",
    f"offset cosines: {res['offset_cos']}",
    f"king - man + woman, inputs included: {res['analogy_king_included']}",
    f"king - man + woman, inputs excluded: {res['analogy_king_excluded']}",
    f"paris - france + japan, inputs included: {res['analogy_tokyo_included']}",
    f"paris - france + japan, inputs excluded: {res['analogy_tokyo_excluded']}",
    f"PCA 2-D share of variance over the map words: {var2:.3f}",
    f"train time {time.time() - t0:.0f}s",
]
(HERE / f"{OUT}.out.txt").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
