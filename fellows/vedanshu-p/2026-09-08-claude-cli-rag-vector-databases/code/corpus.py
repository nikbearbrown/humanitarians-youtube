"""corpus.py — the synthetic embedding collection both benchmarks search over.

WHY SYNTHETIC, AND WHY LIKE THIS. The chapter's claim is about how search COST
behaves as a collection grows, which depends on the number of vectors and their
geometry — not on what the text said. So the corpus is generated, not embedded,
and both scripts build it from the same seed so cycle 1 and cycle 2 search an
identical collection.

The generator is not uniform noise, and that matters. Draw 384-dimensional
vectors from an isotropic Gaussian and every point sits at roughly the same
distance from every other; there is no neighbourhood structure for an index to
exploit, and ANN recall collapses to near zero. That would misrepresent ANN
badly — it would be measuring the curse of dimensionality, not the method.

Real sentence embeddings do not look like that. They have a high AMBIENT
dimension (384 here) but a much lower INTRINSIC one: the vectors lie close to a
low-dimensional manifold, because the texts they encode vary along far fewer
degrees of freedom than the model has output units. That local structure is
exactly what a nearest-neighbour index exploits.

So: sample a LATENT vector in `LATENT` dimensions, map it into the ambient 384
with a fixed random linear map, add a little ambient noise, normalise. The
result has 384 columns and genuine local neighbourhood structure, which is the
property under test.
"""
import numpy as np

DIM = 384          # ambient dimension — a common sentence-embedding width
LATENT = 16        # intrinsic dimension — the manifold the vectors lie near
NOISE = 0.02       # ambient jitter off that manifold
SEED = 5


def unit(v: np.ndarray) -> np.ndarray:
    """Normalise rows, so a dot product IS cosine similarity."""
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def make_corpus(n: int, rng: np.random.Generator, projection: np.ndarray) -> np.ndarray:
    z = rng.normal(size=(n, LATENT)).astype(np.float32)
    ambient = z @ projection
    return unit(ambient + NOISE * rng.normal(size=(n, DIM)).astype(np.float32))


def new_run():
    """A fresh generator + the fixed latent->ambient map. Same seed everywhere."""
    rng = np.random.default_rng(SEED)
    projection = rng.normal(size=(LATENT, DIM)).astype(np.float32) / np.sqrt(LATENT)
    return rng, projection
