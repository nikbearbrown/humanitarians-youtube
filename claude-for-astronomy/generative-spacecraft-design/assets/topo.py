"""Topology optimisation (SIMP) for the Ep. 11 bracket experiment.

This is the mechanism the episode is about, written out rather than imported:
a 2-D plane-stress cantilever bracket, discretised into bilinear quads,
with the Solid Isotropic Material with Penalisation scheme and the
optimality-criteria update. It is a port of Sigmund's 99-line reference code
to numpy/scipy, kept deliberately plain so the loop is readable.

Nothing here is a surrogate or a neural network. The point of the episode is
what the OPTIMISER does with the problem you hand it, so the optimiser has to
be the real thing.

Node numbering is column-major, row 0 at the top, which is what fixes the
element dof order below. Get that ordering wrong and the stiffness matrix is
still symmetric and still solves -- it just solves a different structure.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

NU = 0.3
E0 = 1.0
EMIN = 1e-9
PENAL = 3.0


def element_stiffness(nu=NU, E=E0):
    """The 8x8 plane-stress stiffness of a unit square.

    dof order: [n1x n1y n2x n2y n3x n3y n4x n4y] with the nodes taken
    top-left, top-right, bottom-right, bottom-left.
    """
    k = np.array([0.5 - nu / 6.0,
                  0.125 + nu / 8.0,
                  -0.25 - nu / 12.0,
                  -0.125 + 3.0 * nu / 8.0,
                  -0.25 + nu / 12.0,
                  -0.125 - nu / 8.0,
                  nu / 6.0,
                  0.125 - 3.0 * nu / 8.0])
    idx = np.array([
        [0, 1, 2, 3, 4, 5, 6, 7],
        [1, 0, 7, 6, 5, 4, 3, 2],
        [2, 7, 0, 5, 6, 3, 4, 1],
        [3, 6, 5, 0, 7, 2, 1, 4],
        [4, 5, 6, 7, 0, 1, 2, 3],
        [5, 4, 3, 2, 1, 0, 7, 6],
        [6, 3, 4, 1, 2, 7, 0, 5],
        [7, 2, 1, 4, 3, 6, 5, 0],
    ])
    return E / (1.0 - nu ** 2) * k[idx]


class Bracket:
    """The design problem: a domain, a support, and a set of load cases."""

    def __init__(self, nelx=120, nely=60):
        self.nelx, self.nely = nelx, nely
        self.ndof = 2 * (nelx + 1) * (nely + 1)
        self.KE = element_stiffness()

        # element -> its 8 global dofs
        ex, ey = np.meshgrid(np.arange(nelx), np.arange(nely), indexing="ij")
        ex, ey = ex.ravel(), ey.ravel()
        n1 = ex * (nely + 1) + ey          # top-left node
        n2 = (ex + 1) * (nely + 1) + ey    # top-right node
        self.edof = np.column_stack([2 * n1, 2 * n1 + 1,
                                     2 * n2, 2 * n2 + 1,
                                     2 * n2 + 2, 2 * n2 + 3,
                                     2 * n1 + 2, 2 * n1 + 3])
        self.iK = np.kron(self.edof, np.ones((8, 1), dtype=int)).ravel()
        self.jK = np.kron(self.edof, np.ones((1, 8), dtype=int)).ravel()

        # the root of the bracket is bolted down: the whole left edge
        fixed = np.concatenate([2 * np.arange(nely + 1),
                                2 * np.arange(nely + 1) + 1])
        self.free = np.setdiff1d(np.arange(self.ndof), fixed)

    def node(self, col, row):
        return col * (self.nely + 1) + row

    def load(self, *dof_value):
        f = np.zeros(self.ndof)
        for dof, val in dof_value:
            f[dof] += val
        return f

    # ---- the lug and the three load directions -------------------------
    # PAD_W x PAD_H solid elements at the free end, mid-height: the bolt
    # interface. It is held at full density and withheld from the design
    # variables, because on real hardware the interface is a requirement.
    # Without it a load lands on elements sitting at the density floor and
    # the solve returns ~1e9 -- a restatement of EMIN, not a load path.
    PAD_W, PAD_H = 6, 6

    def pad_mask(self):
        """True for the elements the optimiser is not allowed to touch."""
        m = np.zeros((self.nelx, self.nely), dtype=bool)
        r0 = self.nely // 2 - self.PAD_H // 2
        m[self.nelx - self.PAD_W:, r0:r0 + self.PAD_H] = True
        return m.ravel()

    def _lug(self):
        return self.node(self.nelx, self.nely // 2)

    # A unit load on ONE lug, in three directions. This is how a launch load
    # is specified -- a quasi-static envelope along each axis -- not as one
    # vector. y is positive DOWNWARD here, matching the node numbering.
    def case_down(self):
        """Straight down. The case everybody writes down."""
        n = self._lug()
        return self.load((2 * n + 1, -1.0))

    def case_down_out(self):
        """Down and outboard at 45 degrees. Bending plus tension."""
        n, c = self._lug(), 2.0 ** -0.5
        return self.load((2 * n, c), (2 * n + 1, -c))

    def case_up_out(self):
        """Up and outboard at 45 degrees. Never shown to any optimiser here.

        The mirror of case_down_out about mid-height. A design that only saw
        case_down is symmetric and scores these two identically; a design
        hardened for case_down_out cannot.
        """
        n, c = self._lug(), 2.0 ** -0.5
        return self.load((2 * n, c), (2 * n + 1, c))

    # ---- physics --------------------------------------------------------
    def solve(self, x, f):
        """Return (compliance, per-element strain energy density)."""
        xp = EMIN + x.ravel() ** PENAL * (E0 - EMIN)
        sK = (self.KE.ravel()[np.newaxis, :] * xp[:, np.newaxis]).ravel()
        K = coo_matrix((sK, (self.iK, self.jK)),
                       shape=(self.ndof, self.ndof)).tocsc()
        u = np.zeros(self.ndof)
        u[self.free] = spsolve(K[self.free, :][:, self.free], f[self.free])
        ue = u[self.edof]
        ce = np.einsum("ij,jk,ik->i", ue, self.KE, ue)
        return float(f @ u), ce

    def compliance(self, x, f):
        return self.solve(x, f)[0]


def filter_matrix(nelx, nely, rmin):
    """Sensitivity filter weights. Without this the optimiser produces a
    checkerboard -- alternating solid and void elements that are stiff in the
    discretisation and meaningless as a structure."""
    ex, ey = np.meshgrid(np.arange(nelx), np.arange(nely), indexing="ij")
    ex, ey = ex.ravel(), ey.ravel()
    rows, cols, vals = [], [], []
    r = int(np.ceil(rmin)) - 1
    for e in range(nelx * nely):
        i, j = ex[e], ey[e]
        for ii in range(max(i - r, 0), min(i + r + 1, nelx)):
            for jj in range(max(j - r, 0), min(j + r + 1, nely)):
                w = rmin - np.hypot(i - ii, j - jj)
                if w > 0:
                    rows.append(e)
                    cols.append(ii * nely + jj)
                    vals.append(w)
    H = coo_matrix((vals, (rows, cols)),
                   shape=(nelx * nely, nelx * nely)).tocsr()
    return H, np.asarray(H.sum(axis=1)).ravel()


def oc_update(x, dc, volfrac, passive=None, move=0.2):
    """Optimality-criteria step: push material where it buys the most
    stiffness, then bisect the Lagrange multiplier until the volume
    constraint is met exactly.

    `passive` elements are pinned solid and spend their volume up front, so
    the multiplier is bisected over the remaining budget only. Charging the
    pad to the mass budget is the honest accounting -- the lug is part of the
    part.
    """
    l1, l2 = 1e-9, 1e9
    n = x.size
    target = volfrac * n
    while (l2 - l1) / (l1 + l2) > 1e-6:
        lmid = 0.5 * (l1 + l2)
        xn = np.clip(x * np.sqrt(np.maximum(-dc, 1e-30) / lmid),
                     np.maximum(x - move, 0.0),
                     np.minimum(x + move, 1.0))
        if passive is not None:
            xn[passive] = 1.0
        if xn.sum() - target > 0:
            l1 = lmid
        else:
            l2 = lmid
    return xn


def optimise(br, loads, volfrac=0.40, rmin=2.4, iters=90, snapshots=(),
             label=""):
    """Minimise the SUM of compliance over `loads` at fixed volume.

    `loads` is the list of load cases the optimiser is allowed to know about.
    That list -- not the algorithm -- is what this episode is about.
    """
    n = br.nelx * br.nely
    passive = br.pad_mask()
    x = np.full(n, volfrac)
    x[passive] = 1.0
    H, Hs = filter_matrix(br.nelx, br.nely, rmin)
    shots, hist = {}, []
    for it in range(iters):
        c_total = 0.0
        ce_total = np.zeros(n)
        for f in loads:
            c, ce = br.solve(x, f)
            c_total += c
            ce_total += ce
        dc = -PENAL * x ** (PENAL - 1.0) * ce_total
        dc = H.dot(x * dc) / Hs / np.maximum(x, 1e-3)   # sensitivity filter
        hist.append(c_total)
        if (it + 1) in snapshots:
            shots[it + 1] = x.copy()
        x = oc_update(x, dc, volfrac, passive=passive)
    if label:
        print("  %-28s iters=%d  c: %.4f -> %.4f   vol=%.4f"
              % (label, iters, hist[0], hist[-1], x.mean()))
    return x, hist, shots
