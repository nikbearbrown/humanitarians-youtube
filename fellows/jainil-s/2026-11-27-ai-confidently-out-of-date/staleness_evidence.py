"""
Evidence for "Confidently Out Of Date" — what a retrieval index does when the
language moves and the index does not.

Nothing here errors. The stale index returns results, ranks them, and reports
similarity scores just as high as a fresh one. It is simply pointing at the
wrong documents, and no number it produces says so.

numpy only, one seed, no wall clock:

    python staleness_evidence.py
"""

import json
import numpy as np

SEED = 20261127
RNG = np.random.default_rng(SEED)

N_DOCS = 1200          # per era
DOC_LEN = 60           # words per document
DIM = 48               # embedding dimension after SVD
TOP_K = 5

# --------------------------------------------------------------- vocabulary
# Three topics. Era 2 differs from era 1 in two ordinary ways:
#   1. topic C adopts NEW terminology that era 1 has never seen
#   2. the word "pipeline" MIGRATES from topic A to topic C
# Both happen constantly in real corpora: products get renamed, and a word
# quietly changes which conversation it belongs to.
TOPICS = {
    "A_infra": ["server", "cluster", "deploy", "latency", "uptime", "rollback"],
    "B_people": ["hiring", "onboarding", "mentor", "review", "promotion", "team"],
    "C_data": ["schema", "warehouse", "ingest", "backfill", "partition", "query"],
}
SHARED = ["project", "update", "meeting", "status", "plan", "note"]
MIGRANT = "pipeline"                       # topic A in era 1, topic C in era 2
NEW_TERMS = ["lakehouse", "contract", "lineage"]   # exist only in era 2

ERA1 = {
    "A_infra": TOPICS["A_infra"] + [MIGRANT],
    "B_people": TOPICS["B_people"],
    "C_data": TOPICS["C_data"],
}
ERA2 = {
    "A_infra": TOPICS["A_infra"],
    "B_people": TOPICS["B_people"],
    "C_data": TOPICS["C_data"] + [MIGRANT] + NEW_TERMS,
}


def build_corpus(era, n_docs, rng):
    """Each document is one topic's terms plus a little shared boilerplate."""
    names = list(era)
    docs, labels = [], []
    for _ in range(n_docs):
        t = names[rng.integers(len(names))]
        core = era[t]
        words = [core[rng.integers(len(core))] for _ in range(int(DOC_LEN * 0.8))]
        words += [SHARED[rng.integers(len(SHARED))] for _ in range(DOC_LEN - len(words))]
        rng.shuffle(words)
        docs.append(words)
        labels.append(t)
    return docs, np.array(labels)


def embed(docs, dim=DIM):
    """PPMI over within-document co-occurrence, reduced by SVD. Classic, and
    small enough to read — no gensim, no torch, no downloads."""
    vocab = sorted({w for d in docs for w in d})
    idx = {w: i for i, w in enumerate(vocab)}
    V = len(vocab)
    C = np.zeros((V, V))
    for d in docs:
        ids = np.array([idx[w] for w in d])
        counts = np.bincount(ids, minlength=V).astype(float)
        C += np.outer(counts, counts)
    np.fill_diagonal(C, 0.0)

    total = C.sum()
    if total == 0:
        raise ValueError("empty co-occurrence")
    Pxy = C / total
    Px = Pxy.sum(axis=1, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        pmi = np.log(Pxy / (Px @ Px.T))
    ppmi = np.nan_to_num(np.maximum(pmi, 0.0), nan=0.0, posinf=0.0, neginf=0.0)

    U, S, _ = np.linalg.svd(ppmi, full_matrices=False)
    vecs = U[:, :dim] * S[:dim]
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    vecs = vecs / np.where(norms == 0, 1, norms)
    return {w: vecs[idx[w]] for w in vocab}


def doc_vector(words, model):
    """Mean of the word vectors the model actually knows. Out-of-vocabulary
    terms are DROPPED — which is what every real pipeline does, silently."""
    vs = [model[w] for w in words if w in model]
    if not vs:
        return None
    v = np.mean(vs, axis=0)
    n = np.linalg.norm(v)
    return v / n if n else v


print(f"seed={SEED}  docs/era={N_DOCS:,}  doc length={DOC_LEN}  dim={DIM}")
print(f"\nBetween era 1 and era 2, two ordinary things happen:")
print(f"  1. topic C adopts new terms the old corpus never saw: "
      f"{', '.join(NEW_TERMS)}")
print(f"  2. '{MIGRANT}' migrates from topic A to topic C\n")

docs1, lab1 = build_corpus(ERA1, N_DOCS, RNG)
docs2, lab2 = build_corpus(ERA2, N_DOCS, RNG)

stale_model = embed(docs1)      # trained on era 1 — the index nobody rebuilt
fresh_model = embed(docs2)      # trained on era 2 — what you would get today

out = {"seed": SEED, "n_docs": N_DOCS, "dim": DIM, "top_k": TOP_K,
       "new_terms": NEW_TERMS, "migrant": MIGRANT}
out["stale_vocab"] = len(stale_model)
out["fresh_vocab"] = len(fresh_model)
print(f"stale model vocabulary: {len(stale_model)} terms")
print(f"fresh model vocabulary: {len(fresh_model)} terms "
      f"(+{len(fresh_model)-len(stale_model)})\n")


def build_index(model):
    mat, keep = [], []
    for i, d in enumerate(docs2):
        v = doc_vector(d, model)
        if v is not None:
            mat.append(v); keep.append(i)
    return np.array(mat), lab2[np.array(keep)]


def make_query(new_frac, rng, n=6, use_migrant=False):
    """A query as a user would actually type it today. `new_frac` is how much
    of it uses era-2 terminology the old index has never seen."""
    n_new = int(round(n * new_frac))
    pool_new = NEW_TERMS + ([MIGRANT] if use_migrant else [])
    words = [pool_new[rng.integers(len(pool_new))] for _ in range(n_new)]
    old_c = TOPICS["C_data"]
    words += [old_c[rng.integers(len(old_c))] for _ in range(n - n_new)]
    return words


def evaluate(model, mat, labels, new_frac, rng, n_q=400, use_migrant=False):
    hits, sims, unrepresentable = 0, [], 0
    for _ in range(n_q):
        q = make_query(new_frac, rng, use_migrant=use_migrant)
        qv = doc_vector(q, model)
        if qv is None:
            unrepresentable += 1          # the index cannot even form a query
            continue
        s = mat @ qv
        top = np.argsort(-s)[:TOP_K]
        hits += int(np.any(labels[top] == "C_data"))
        sims.append(float(s[top[0]]))
    return {"recall_at_k": hits / n_q,
            "mean_top1_similarity": float(np.mean(sims)) if sims else None,
            "unrepresentable_frac": unrepresentable / n_q}


fresh_mat, fresh_lab = build_index(fresh_model)
stale_mat, stale_lab = build_index(stale_model)

print("HOW MUCH THE QUERY USES LANGUAGE THE INDEX NEVER SAW")
print(f"  {'new terms in query':>20}{'stale recall':>14}{'fresh recall':>14}"
      f"{'stale top-1 sim':>17}{'no query vector':>17}")
print("  " + "-" * 82)
curve = []
for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
    st = evaluate(stale_model, stale_mat, stale_lab, frac, np.random.default_rng(SEED + 11))
    fr = evaluate(fresh_model, fresh_mat, fresh_lab, frac, np.random.default_rng(SEED + 11))
    curve.append({"new_frac": frac, "stale": st, "fresh": fr})
    sim = f"{st['mean_top1_similarity']:.3f}" if st["mean_top1_similarity"] is not None else "—"
    print(f"  {frac:>19.0%}{st['recall_at_k']:>14.1%}{fr['recall_at_k']:>14.1%}"
          f"{sim:>17}{st['unrepresentable_frac']:>17.1%}")
out["curve"] = curve

# ------------------------------------------- the actively-wrong case
# A term that MIGRATED is worse than a term that is missing: the stale index
# has a confident vector for it, pointing at the topic it used to belong to.
print(f"\nTHE MIGRATED TERM — '{MIGRANT}' moved from topic A to topic C")
mig = evaluate(stale_model, stale_mat, stale_lab, 1.0,
               np.random.default_rng(SEED + 23), use_migrant=True)
mig_fresh = evaluate(fresh_model, fresh_mat, fresh_lab, 1.0,
                     np.random.default_rng(SEED + 23), use_migrant=True)
out["migrant_case"] = mig
out["migrant_case_fresh"] = mig_fresh
print(f"  fresh recall@{TOP_K}, same queries  {mig_fresh['recall_at_k']:6.1%}")
print(f"  stale recall@{TOP_K}         {mig['recall_at_k']:6.1%}")
sim = mig["mean_top1_similarity"]
print(f"  stale mean top-1 sim    {sim:6.3f}" if sim is not None else "  (no vector)")
print(f"  no query vector         {mig['unrepresentable_frac']:6.1%}")

# where do topic-C queries actually land in the stale index?
counts = {"A_infra": 0, "B_people": 0, "C_data": 0}
rng = np.random.default_rng(SEED + 31)
scored = 0
for _ in range(400):
    q = make_query(1.0, rng, use_migrant=True)
    qv = doc_vector(q, stale_model)
    if qv is None:
        continue
    scored += 1
    for t in stale_lab[np.argsort(-(stale_mat @ qv))[:TOP_K]]:
        counts[t] += 1
tot = sum(counts.values()) or 1
out["stale_top5_topic_mix"] = {k: v / tot for k, v in counts.items()}
print(f"\nWHERE A TODAY-LANGUAGE TOPIC-C QUERY LANDS IN THE STALE INDEX")
for k, v in counts.items():
    print(f"  {k:<10} {v/tot:6.1%}  {'#' * int(round(v/tot*40))}")

worst = curve[-1]
out["headline"] = {
    "stale_recall_all_new": worst["stale"]["recall_at_k"],
    "fresh_recall_all_new": worst["fresh"]["recall_at_k"],
    "stale_recall_no_new": curve[0]["stale"]["recall_at_k"],
    "sim_at_zero_new": curve[0]["stale"]["mean_top1_similarity"],
    "sim_at_migrant": mig["mean_top1_similarity"],
}
print(f"\n  With no new language in the query the stale index is fine "
      f"({curve[0]['stale']['recall_at_k']:.1%}).")
print(f"  With today's language it collapses "
      f"({worst['stale']['recall_at_k']:.1%} vs {worst['fresh']['recall_at_k']:.1%} fresh).")

with open("staleness_results.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2)
print("\nwrote staleness_results.json")
