"""Week 12 evidence run for 'The Check That Passed'.

Mirrors github.com/Kenny0bi/pulse-recsys benchmarks/train_all.py exactly
(EPOCHS_TT=6, BATCH=4096, dim 64, batch rng seed 1, model seed 0, same
deduping batcher, same evaluation) for three rungs: the popularity counter,
the two-tower WITHOUT the logQ correction (item_freq=None, the original
failure) and WITH it (item_freq=popularity). Writes results here, not into
the repo's tracked assets/.
"""
import json, os, sys, time
from pathlib import Path
import numpy as np

REPO = Path(os.environ.get("PULSE_REPO", "pulse-recsys")).expanduser()
sys.path.insert(0, str(REPO))
from pulse.evaluate import build_seen, build_user_pos, evaluate_scores
from pulse.models import TwoTower

DATA = REPO / "data"; EPOCHS_TT, BATCH = 6, 4096
OUT = Path(__file__).with_name("evidence.json")

def batches(tr_u, tr_i, rng, batch):
    order = rng.permutation(len(tr_u))
    for s in range(0, len(order) - batch, batch):
        idx = order[s : s + batch]; u, i = tr_u[idx], tr_i[idx]
        _, first = np.unique(i, return_index=True)
        yield u[first], i[first]

d = np.load(DATA / "prepared.npz")
tr_u, tr_i, te_u, te_i = d["train_user"], d["train_item"], d["test_user"], d["test_item"]
n_users, n_items = int(d["n_users"]), int(d["n_items"])
pop = np.load(DATA / "popularity.npy").astype(np.float32)
user_pos = build_user_pos(te_u, te_i); seen = build_seen(tr_u, tr_i)
eval_users = np.array(sorted(user_pos.keys()))
res = {"train": int(len(tr_u)), "test": int(len(te_u)), "users": n_users, "items": n_items,
       "eval_users": int(len(eval_users)), "epochs": EPOCHS_TT, "batch": BATCH}

r, n = evaluate_scores(lambda b: np.tile(pop, (len(b), 1)).copy(), eval_users, user_pos, seen, n_items)
res["popularity"] = {"recall": r, "ndcg": n}; print("popularity", res["popularity"], flush=True)
OUT.write_text(json.dumps(res, indent=1))

for name, freq in (("two_tower_no_logq", None), ("two_tower_logq", pop)):
    tt = TwoTower(n_users, n_items, dim=64, item_freq=freq)
    rng = np.random.default_rng(1); t0 = time.time(); losses = []
    for ep in range(EPOCHS_TT):
        for step, (u, i) in enumerate(batches(tr_u, tr_i, rng, BATCH)):
            loss = tt.train_step(u, i)
            if step % 500 == 0:
                losses.append(round(loss, 4)); print(f"{name} ep{ep} step{step} loss {loss:.4f} ({time.time()-t0:,.0f}s)", flush=True)
    V = tt.item_vectors()
    r, n = evaluate_scores(lambda b: tt.user_vectors(b) @ V.T, eval_users, user_pos, seen, n_items)
    # how popularity-heavy are each model's recommendations? share of top-10 slots
    # that go to the 100 most popular items, over the first 2,000 eval users
    top100 = set(np.argsort(-pop)[:100].tolist()); hits = tot = 0
    for s0 in range(0, 2000, 500):
        b = eval_users[s0:s0 + 500]; sc = tt.user_vectors(b) @ V.T
        top = np.argpartition(-sc, 10, axis=1)[:, :10]
        hits += sum(1 for row in top for j in row if j in top100); tot += top.size
    res[name] = {"recall": r, "ndcg": n, "train_s": round(time.time() - t0, 1),
                 "top10_share_from_100_most_popular": round(hits / tot, 4), "loss_every_500_steps": losses}
    print(name, {k: v for k, v in res[name].items() if k != "loss_every_500_steps"}, flush=True)
    OUT.write_text(json.dumps(res, indent=1))
print("done", flush=True)
