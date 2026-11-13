"""EXECUTABLE EVIDENCE for "How Spotify Picks Songs."

A made-up music service, small enough to inspect: 1,600 songs in 8 Western genres (neighbouring genres overlap:
indie and rock, pop and electronic, jazz and classical, country and rock), 3,000 listeners whose tastes mix one
to three genres and who have each played only a small part of the catalogue, and play counts drawn from those tastes plus a strong popularity pull (a few
songs get most of the plays, as on real services). Nothing here is Spotify's data or Spotify's code.

The recommender is the textbook one for play counts: implicit-feedback matrix factorization (ALS, Hu, Koren &
Volinsky 2008). Every listener and every song becomes a short list of numbers (a taste vector); a song's score
for a listener is the dot product of the two. It never sees a genre label: genres are used only to build the
data and to grade the results.

Measured:
  1. accuracy: hide 20% of each listener's songs, recommend 10, count how many hidden songs come back
     (hit rate / recall@10), against "most popular" and "random" baselines;
  2. what the taste vectors learned: nearest songs to an example song by cosine similarity, and how often
     a song's nearest neighbours share its genre (genre labels never shown to the model);
  3. popularity bias: how popular the recommended songs are compared with what listeners actually play,
     and how much of the catalogue ever gets recommended;
  4. the feedback loop: listeners play mostly what is recommended, the model retrains, repeat 8 rounds;
     track catalogue coverage and genre spread, with and without 2 exploration slots in every 10;
  5. cold start: a brand-new song with no plays, and a brand-new listener.

    python recs.py        # writes evidence/run.log, results.json, scene.json
"""
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
EV.mkdir(exist_ok=True)
LOG = []


def P(s=""):
    print(s)
    LOG.append(s)


GENRES = ["pop", "rock", "indie", "hip-hop", "jazz", "country", "electronic", "classical"]
N_SONGS, N_USERS, K, SEED = 1600, 3000, 24, 2026
rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------- the made-up service
song_genre = np.repeat(np.arange(len(GENRES)), N_SONGS // len(GENRES))
# popularity: a Zipf-like pull, shuffled across genres so every genre has hits and deep cuts
pop_rank = rng.permutation(N_SONGS)
popularity = 1.0 / (1 + pop_rank) ** 1.0
popularity /= popularity.sum()
# each song also has a small "sound" twist inside its genre, so songs in one genre are not identical
song_twist = rng.normal(0, 1, (N_SONGS, 3))

# how much a fan of one genre also plays each other genre (rows sum to 1)
GENRE_NEAR = np.eye(len(GENRES))
for a, b in (("indie", "rock"), ("pop", "electronic"), ("jazz", "classical"), ("country", "rock"), ("pop", "hip-hop")):
    i, j = GENRES.index(a), GENRES.index(b)
    GENRE_NEAR[i, j] = GENRE_NEAR[j, i] = 0.35
GENRE_NEAR /= GENRE_NEAR.sum(1, keepdims=True)
user_mix = np.zeros((N_USERS, len(GENRES)))
for u in range(N_USERS):
    n = rng.choice([1, 2, 3], p=[0.25, 0.5, 0.25])
    g = rng.choice(len(GENRES), n, replace=False)
    user_mix[u, g] = rng.dirichlet(np.ones(n) * 2)
user_twist = rng.normal(0, 1, (N_USERS, 3))
user_pop = rng.uniform(0.3, 0.9, N_USERS)       # how much each listener follows the charts


def taste(u):
    """Probability that listener u picks each song on a given play."""
    g = (user_mix[u] @ GENRE_NEAR)[song_genre] + 0.04     # neighbouring genres, and a little of everything
    t = np.exp(0.5 * song_twist @ user_twist[u])           # within-genre preference
    p = g * t
    p = p / p.sum()
    return (1 - user_pop[u]) * p + user_pop[u] * (p * popularity * N_SONGS) / (p * popularity * N_SONGS).sum()


plays = np.zeros((N_USERS, N_SONGS))
for u in range(N_USERS):
    n_plays = int(rng.lognormal(np.log(60), 0.7))          # most listeners light, a few heavy
    plays[u] = rng.multinomial(n_plays, taste(u))

# ---------------------------------------------------------------- hold out 20% of each listener's songs
train, test = plays.copy(), [[] for _ in range(N_USERS)]
for u in range(N_USERS):
    heard = np.flatnonzero(plays[u])
    k = max(1, int(round(0.2 * len(heard))))
    hide = rng.choice(heard, k, replace=False)
    train[u, hide] = 0
    test[u] = list(hide)


def als(R, k=K, alpha=20.0, reg=0.1, iters=12, seed=0):
    """Implicit ALS (Hu, Koren & Volinsky 2008): preference p = plays > 0, confidence c = 1 + alpha*log(1+plays)."""
    r = np.random.default_rng(seed)
    nu, ni = R.shape
    X, Y = r.normal(0, 0.1, (nu, k)), r.normal(0, 0.1, (ni, k))
    C = alpha * np.log1p(R)                       # confidence minus 1; zero where nothing was played
    I = reg * np.eye(k)
    rows = [np.flatnonzero(R[u]) for u in range(nu)]
    cols = [np.flatnonzero(R[:, i]) for i in range(ni)]
    for _ in range(iters):
        YtY = Y.T @ Y
        for u in range(nu):
            j, c = rows[u], C[u, rows[u]]
            X[u] = np.linalg.solve(YtY + (Y[j].T * c) @ Y[j] + I, Y[j].T @ (1 + c))
        XtX = X.T @ X
        for i in range(ni):
            j, c = cols[i], C[cols[i], i]
            Y[i] = np.linalg.solve(XtX + (X[j].T * c) @ X[j] + I, X[j].T @ (1 + c))
    return X, Y


def recommend(scores, seen, n=10):
    s = scores.copy()
    s[seen] = -np.inf
    return np.argsort(-s)[:n]


def evaluate(recs_fn):
    hits, recall, recd = 0, [], set()
    for u in range(N_USERS):
        r = recs_fn(u)
        recd.update(r.tolist())
        h = len(set(r.tolist()) & set(test[u]))
        hits += h > 0
        recall.append(h / min(10, len(test[u])))
    return hits / N_USERS, float(np.mean(recall)), len(recd) / N_SONGS


P(f"MADE-UP SERVICE: {N_SONGS} songs in {len(GENRES)} Western genres, {N_USERS} listeners, "
  f"{int(plays.sum()):,} plays (seed {SEED}). Not Spotify data.")
top10_share = np.sort(plays.sum(0))[::-1][: N_SONGS // 10].sum() / plays.sum()
P(f"  the top 10% of songs get {top10_share * 100:.0f}% of all plays")

X, Y = als(train)
seen = [np.flatnonzero(train[u]) for u in range(N_USERS)]
pop_scores = train.sum(0)
hr_als, rc_als, cov_als = evaluate(lambda u: recommend(X[u] @ Y.T, seen[u]))
hr_pop, rc_pop, cov_pop = evaluate(lambda u: recommend(pop_scores, seen[u]))
rr = np.random.default_rng(1)
hr_rnd, rc_rnd, cov_rnd = evaluate(lambda u: recommend(rr.random(N_SONGS), seen[u]))
P("")
P("1. ACCURACY (20% of each listener's songs hidden; 10 recommendations each)")
P(f"  taste vectors (ALS, {K} numbers each): {hr_als * 100:.1f}% of listeners get at least one hidden song back; recall@10 {rc_als:.3f}")
P(f"  most popular:                         {hr_pop * 100:.1f}%; recall@10 {rc_pop:.3f}")
P(f"  random:                               {hr_rnd * 100:.1f}%; recall@10 {rc_rnd:.3f}")

# ---------------------------------------------------------------- 2. what the vectors learned
Yn = Y / np.linalg.norm(Y, axis=1, keepdims=True)
cos = Yn @ Yn.T
np.fill_diagonal(cos, -1)
nn = np.argsort(-cos, axis=1)[:, :5]
same = (song_genre[nn] == song_genre[:, None]).mean()
P("")
P("2. WHAT THE TASTE VECTORS LEARNED (genre labels never shown to the model)")
P(f"  a song's 5 nearest songs (cosine) share its genre {same * 100:.1f}% of the time (chance: {100 / len(GENRES):.1f}%)")
by_genre = {GENRES[g]: float((song_genre[nn[song_genre == g]] == g).mean()) for g in range(len(GENRES))}
P("  by genre: " + ", ".join(f"{g} {v * 100:.0f}%" for g, v in by_genre.items()))
# example: a mid-popularity jazz song (not a chart hit, not a dud)
jazz = np.flatnonzero(song_genre == GENRES.index("jazz"))
ex_song = int(jazz[np.argsort(pop_rank[jazz])][len(jazz) // 3])
ex_nn = [(int(j), GENRES[song_genre[j]], round(float(cos[ex_song, j]), 3)) for j in nn[ex_song]]
P(f"  example: song {ex_song} (jazz, popularity rank {pop_rank[ex_song] + 1} of {N_SONGS}) -> nearest: "
  + ", ".join(f"#{j} {g} {c}" for j, g, c in ex_nn))

# ---------------------------------------------------------------- 3. popularity bias
recs_all = np.array([recommend(X[u] @ Y.T, seen[u]) for u in range(N_USERS)])
med_rank_rec = float(np.median(pop_rank[recs_all.ravel()] + 1))
med_rank_play = float(np.median(np.repeat(pop_rank, plays.sum(0).astype(int)) + 1))
tail = pop_rank >= N_SONGS // 2
P("")
P("3. POPULARITY BIAS")
P(f"  median popularity rank of a recommended song: {med_rank_rec:.0f}; of a song actually played: {med_rank_play:.0f} (1 = biggest hit)")
P(f"  share of recommendations from the less popular half of the catalogue: {tail[recs_all.ravel()].mean() * 100:.1f}%"
  f" (share of plays: {plays[:, tail].sum() / plays.sum() * 100:.1f}%)")
P(f"  catalogue ever recommended: taste vectors {cov_als * 100:.0f}%, most popular {cov_pop * 100:.0f}%")

# ---------------------------------------------------------------- 4. feedback loop
def genre_spread(recs):
    """Mean number of distinct genres in a listener's 10 recommendations."""
    return float(np.mean([len(set(song_genre[r].tolist())) for r in recs]))


def loop(explore, rounds=8, seed=7):
    r = np.random.default_rng(seed)
    R = train.copy()
    out = []
    for t in range(rounds + 1):
        Xl, Yl = als(R, iters=6, seed=t)
        recs = []
        for u in range(N_USERS):
            s = Xl[u] @ Yl.T
            heard = np.flatnonzero(R[u])
            if explore:
                top = recommend(s, heard, 8)
                pool = np.setdiff1d(np.arange(N_SONGS), np.concatenate([heard, top]))
                # exploration: 2 songs the listener has never heard, chosen from songs few people have heard
                w = 1.0 / (1 + R[:, pool].sum(0))
                pick = r.choice(pool, 2, replace=False, p=w / w.sum())
                rec = np.concatenate([top, pick])
            else:
                rec = recommend(s, heard, 10)
            recs.append(rec)
        recs = np.array(recs)
        cov = len(set(recs.ravel().tolist())) / N_SONGS
        counts = np.bincount(recs.ravel(), minlength=N_SONGS)
        top_share = np.sort(counts)[::-1][: N_SONGS // 10].sum() / counts.sum()
        out.append({"round": t, "coverage": round(cov, 4), "genres": round(genre_spread(recs), 3),
                    "top10_share": round(float(top_share), 4)})
        if t == rounds:
            break
        # listeners play 3 of their 10 recommendations each round (whichever they like most), 1-3 plays each
        for u in range(N_USERS):
            like = taste(u)[recs[u]]
            chosen = recs[u][np.argsort(-like * r.uniform(0.7, 1.3, len(like)))[:3]]
            R[u, chosen] += r.integers(1, 4, 3)
    return out


P("")
P("4. THE FEEDBACK LOOP (listeners play what they're shown; the model retrains; 8 rounds)")
loop_plain = loop(False)
loop_explore = loop(True)
for a, b in zip(loop_plain, loop_explore):
    P(f"  round {a['round']}: catalogue recommended {a['coverage'] * 100:5.1f}% (with exploration {b['coverage'] * 100:5.1f}%), "
      f"top 10% of songs get {a['top10_share'] * 100:4.1f}% of slots ({b['top10_share'] * 100:4.1f}%), "
      f"genres per list {a['genres']:.2f} ({b['genres']:.2f})")

# ---------------------------------------------------------------- 5. cold start
P("")
P("5. COLD START")
new_vec = np.zeros(K)          # a new song with no plays: ALS has nothing to learn from
rank_new = int((X @ Y.T > (X @ new_vec)[:, None]).sum(1).mean()) + 1
P(f"  a brand-new song with zero plays: its taste vector is all zeros, score 0 for everyone; "
  f"it ranks on average {rank_new} of {N_SONGS + 1} and appears in {0} of {N_USERS} top-10 lists")
cold_recs = recommend(pop_scores, np.array([], int))
P(f"  a brand-new listener with no plays: only popularity to go on -> top 10 = the 10 most-played songs "
  f"(genres: {', '.join(sorted(set(GENRES[g] for g in song_genre[cold_recs])))})")

# ---------------------------------------------------------------- example listener
cand = [u for u in range(N_USERS) if np.count_nonzero(user_mix[u]) == 2 and len(test[u]) >= 8]
ex_u = cand[len(cand) // 2]
ex_rec = recommend(X[ex_u] @ Y.T, seen[ex_u])
ex_hits = sorted(set(ex_rec.tolist()) & set(test[ex_u]))
P("")
P(f"EXAMPLE LISTENER {ex_u}: tastes " + ", ".join(f"{GENRES[g]} {user_mix[ex_u, g] * 100:.0f}%" for g in np.flatnonzero(user_mix[ex_u]))
  + f"; {len(seen[ex_u])} songs heard, {len(test[ex_u])} hidden")
P("  recommended: " + ", ".join(f"#{s} {GENRES[song_genre[s]]}{' (hidden hit)' if s in ex_hits else ''}" for s in ex_rec))

# ---------------------------------------------------------------- write
res = dict(n_songs=N_SONGS, n_users=N_USERS, n_plays=int(plays.sum()), k=K, seed=SEED, top10_share=round(float(top10_share), 4),
           accuracy=dict(als=dict(hit=round(hr_als, 4), recall=round(rc_als, 4), coverage=round(cov_als, 4)),
                         popular=dict(hit=round(hr_pop, 4), recall=round(rc_pop, 4), coverage=round(cov_pop, 4)),
                         random=dict(hit=round(hr_rnd, 4), recall=round(rc_rnd, 4), coverage=round(cov_rnd, 4))),
           same_genre_nn=round(float(same), 4), same_genre_by=by_genre,
           pop_bias=dict(med_rank_rec=med_rank_rec, med_rank_play=med_rank_play,
                         tail_share_recs=round(float(tail[recs_all.ravel()].mean()), 4),
                         tail_share_plays=round(float(plays[:, tail].sum() / plays.sum()), 4)),
           loop_plain=loop_plain, loop_explore=loop_explore, cold_new_song_rank=rank_new,
           cold_new_user=[int(s) for s in cold_recs])
scene = dict(genres=GENRES,
             example_song=dict(id=ex_song, genre="jazz", rank=int(pop_rank[ex_song] + 1), nearest=ex_nn),
             example_user=dict(id=ex_u, mix={GENRES[g]: round(float(user_mix[ex_u, g]), 3) for g in np.flatnonzero(user_mix[ex_u])},
                               recs=[dict(id=int(s), genre=GENRES[song_genre[s]], hit=bool(s in ex_hits)) for s in ex_rec],
                               heard=int(len(seen[ex_u])), hidden=int(len(test[ex_u]))),
             # a 2-D picture of the song vectors (first two principal components), coloured by genre at draw time
             pca=None)
Yc = Y - Y.mean(0)
U, S, Vt = np.linalg.svd(Yc, full_matrices=False)
pc = Yc @ Vt[:2].T
pc = pc / np.abs(pc).max(0)
scene["pca"] = [[round(float(a), 3), round(float(b), 3), int(g)] for (a, b), g in zip(pc, song_genre)]
scene["pca_var"] = [round(float(v), 4) for v in (S[:2] ** 2 / (S ** 2).sum())]
(EV / "results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
(EV / "scene.json").write_text(json.dumps(scene), encoding="utf-8")
(EV / "run.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")
P("")
P("wrote evidence/run.log, results.json, scene.json")
