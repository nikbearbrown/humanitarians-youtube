"""Toy remote build cache (content-addressed) for claude-hai-monorepos-polyrepos.
A target's cache key = hash(its own sources + its dependencies' keys).
Build 1 on an empty cache; build 2 on a fresh machine sharing the cache; build 3 after
editing one library. Deterministic: no randomness, fixed inputs."""
import hashlib
GRAPH = {  # target -> deps
    "libs/auth": [], "libs/ui": [],
    "apps/web": ["libs/auth", "libs/ui"], "apps/mobile": ["libs/auth", "libs/ui"],
    "services/billing": ["libs/auth"], "services/search": [], "services/ads": [], "tools/ci": [],
}
SRC = {t: f"source of {t} v1" for t in GRAPH}
def key(t, memo):
    if t not in memo:
        h = hashlib.sha256(SRC[t].encode())
        for d in GRAPH[t]: h.update(key(d, memo).encode())
        memo[t] = h.hexdigest()[:12]
    return memo[t]
CACHE = {}  # the shared "remote" cache: key -> artifact
def build(label):
    memo, built, reused = {}, [], []
    for t in GRAPH:
        k = key(t, memo)
        if k in CACHE: reused.append(t)
        else: CACHE[k] = f"artifact({t})"; built.append(t)
    print(f"{label:<34} built {len(built)}  reused {len(reused)}   built: {', '.join(built) or '-'}")
build("build 1 (empty cache)")
build("build 2 (new laptop, same commit)")
SRC["libs/auth"] = "source of libs/auth v2"
build("build 3 (edit libs/auth)")
