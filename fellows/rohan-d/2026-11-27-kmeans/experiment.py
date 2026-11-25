"""Every number the k-means film shows (numpy; deterministic)."""
import numpy as np
P = np.array([[1, 1], [1.5, 2], [3, 4], [5, 7], [3.5, 5], [4.5, 5], [3.5, 4.5]], dtype=float)
def inertia(P, C, lab): return float(sum(np.sum((P[lab == k] - C[k]) ** 2) for k in range(len(C))))
def run(P, C0, verbose=True):
    C = np.array(C0, dtype=float)
    hist = []
    for rnd in range(1, 20):
        d = np.linalg.norm(P[:, None, :] - C[None, :, :], axis=2)
        lab = d.argmin(axis=1)
        J = inertia(P, C, lab)
        newC = np.array([P[lab == k].mean(axis=0) if np.any(lab == k) else C[k] for k in range(len(C))])
        if verbose:
            print(f"round {rnd}: labels {lab.tolist()}  inertia (before move) {J:.3f}  new centers {np.round(newC, 3).tolist()}")
        hist.append((lab.copy(), J, newC.copy()))
        if np.allclose(newC, C):
            return hist, C, lab, J
        C = newC
    return hist, C, lab, J
print("points", P.tolist())
hist, C, lab, J = run(P, [[1, 1], [5, 6]])
print("final centers", np.round(C, 3).tolist(), "labels", lab.tolist(), "inertia", round(J, 3))
d0 = np.linalg.norm(P[2] - np.array([[1, 1], [5, 6]]), axis=1)
print("point (3,4) distances to initial centers (1,1),(5,6):", np.round(d0, 3).tolist())
print("-- the bad start: four corners of a rectangle")
R = np.array([[0, 0], [0, 2], [4, 0], [4, 2]], dtype=float)
for name, C0 in (("start A: (0,1),(4,1)", [[0, 1], [4, 1]]), ("start B: (2,0),(2,2)", [[2, 0], [2, 2]])):
    h, Cf, lf, Jf = run(R, C0, verbose=False)
    print(name, "-> centers", Cf.tolist(), "labels", lf.tolist(), "inertia", round(Jf, 3), "rounds", len(h))
