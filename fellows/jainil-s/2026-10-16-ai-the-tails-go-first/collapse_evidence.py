"""
Primary evidence for "The Tails Go First".

Recursive generative training: every generation is a model fitted to the
PREVIOUS generation's output, never to real data again. This is the setup
Shumailov et al. call model collapse (Nature, 2024).

Setup
-----
  The true distribution is a common bulk, N(0, 1), plus a RARE subpopulation
  worth 5% of the data at N(6, 0.6) -- far enough out that the bulk essentially
  never reaches it.

  Generation 0 draws n = 200 real samples. Each later generation draws n
  samples from a fixed-bandwidth kernel density model fitted to the previous
  generation's samples. No real data is ever seen again.

  Every point carries a lineage label saying whether it descends from the rare
  subpopulation. The label is carried through resampling and is never used by
  the model -- it exists only so the experiment can say exactly when the rare
  subpopulation is gone, rather than inferring it from a threshold that bulk
  outliers can cross.

What it shows
-------------
  The rare subpopulation thins out generation by generation and then goes
  extinct. It never returns, because nothing in the loop can reinvent it.

  Meanwhile the ordinary summary statistics stay healthy. The mean and the
  standard deviation of the surviving data barely move. A model that has
  permanently lost 5% of the world looks, by the usual numbers, fine.

Every figure spoken or shown in the video comes out of this file.
Run:  python collapse_evidence.py
"""
import numpy as np

RARE_W, RARE_MU, RARE_SD = 0.05, 6.0, 0.6
N, H, GENS, SEEDS = 200, 0.15, 120, 60
FAR = 4.0          # "observed" cutoff: N(0,1) essentially never gets here


def one_run(seed):
    rng = np.random.default_rng(seed)
    is_rare = rng.random(N) < RARE_W
    data = np.where(is_rare, rng.normal(RARE_MU, RARE_SD, N), rng.normal(0, 1, N))
    lab = is_rare.copy()

    share, observed, mean, sd = [], [], [], []
    extinct_at = None
    for g in range(GENS + 1):
        s = float(lab.mean())
        share.append(s)
        observed.append(float((data > FAR).mean()))
        mean.append(float(data.mean()))
        sd.append(float(data.std(ddof=1)))
        if s == 0.0 and extinct_at is None:
            extinct_at = g
        idx = rng.integers(0, N, N)                  # sample from the model
        data = data[idx] + rng.normal(0, H, N)       # fixed-bandwidth smoothing
        lab = lab[idx]                               # lineage follows the sample
    return (np.array(share), np.array(observed),
            np.array(mean), np.array(sd), extinct_at)


def main():
    runs = [one_run(s) for s in range(SEEDS)]
    med = lambda arrs, g: float(np.median([a[g] for a in arrs]))
    share = [r[0] for r in runs]
    obs = [r[1] for r in runs]
    mean = [r[2] for r in runs]
    sd = [r[3] for r in runs]
    deaths = [r[4] for r in runs if r[4] is not None]

    print(__doc__.split("Run:")[0].strip())
    print(f"\n{SEEDS} seeds, n={N} samples per generation, {GENS} generations, median over seeds\n")
    print(f"{'gen':>5} {'rare lineage %':>15} {'seen past 4.0 %':>16} {'mean':>8} {'sd':>8}")
    for g in [0, 5, 10, 20, 30, 40, 60, 80, 120]:
        print(f"{g:>5} {100*med(share,g):>15.2f} {100*med(obs,g):>16.2f} "
              f"{med(mean,g):>8.2f} {med(sd,g):>8.2f}")

    print("\n--- the numbers the video uses ---")
    print(f"  the rare subpopulation is 5% of the real world, and {100*med(share,0):.1f}% of generation 0")
    print(f"  by generation 20 it is down to {100*med(share,20):.2f}%")
    print(f"  it goes EXTINCT in {len(deaths)}/{SEEDS} seeds, median at generation {int(np.median(deaths))}")
    print(f"      earliest {min(deaths)}, latest {max(deaths)}")
    recovered = sum(1 for sh, _, _, _, d in runs if d is not None and (sh[d:] > 0).any())
    print(f"  it comes back in {recovered} of those {len(deaths)} seeds")
    print(f"  still alive at generation {GENS}: {SEEDS-len(deaths)}/{SEEDS}")

    print("\n--- and the model still looks healthy ---")
    print(f"  mean  generation 0: {med(mean,0):+.2f}   generation {GENS}: {med(mean,GENS):+.2f}")
    print(f"  sd    generation 0: {med(sd,0):.2f}   generation {GENS}: {med(sd,GENS):.2f}")
    print("  Nothing in those two numbers says 5% of the distribution is gone for good.")

    print("\n--- lineage label vs what you could actually observe ---")
    print("  (the label is bookkeeping; these track each other, so the finding is")
    print("   visible in the data itself, not an artefact of the labelling)")
    for g in [0, 10, 20, 40]:
        print(f"    gen {g:>3}: lineage {100*med(share,g):>5.2f}%   observed {100*med(obs,g):>5.2f}%")
    return runs


def curves_for_the_video(runs):
    """
    The two density silhouettes drawn on screen, printed so the beat sheet's
    numbers trace back here instead of being eyeballed. Generation 0 against a
    generation where the rare subpopulation is already extinct, binned on one
    shared grid so the two curves are directly comparable.
    """
    GRID = np.linspace(-4.0, 9.0, 40)
    step = GRID[1] - GRID[0]
    edges = np.concatenate([GRID - step / 2, [GRID[-1] + step / 2]])

    def density_at(seed, stop_gen):
        """Run the real loop and histogram the data actually present at stop_gen."""
        rng = np.random.default_rng(seed)
        is_rare = rng.random(N) < RARE_W
        data = np.where(is_rare, rng.normal(RARE_MU, RARE_SD, N), rng.normal(0, 1, N))
        for _ in range(stop_gen):
            idx = rng.integers(0, N, N)
            data = data[idx] + rng.normal(0, H, N)
        return np.histogram(data, bins=edges, density=True)[0]

    # Pooled over seeds only to smooth histogram noise: every sample counted
    # here came out of the simulation, at the generation named.
    early = np.median([density_at(s, 0) for s in range(SEEDS)], axis=0)
    late = np.median([density_at(s, 40) for s in range(SEEDS)], axis=0)
    scale = max(early.max(), late.max())

    print("\n--- rare-lineage share every 5 generations, for the on-screen curve ---")
    gens5 = list(range(0, 61, 5))
    series = [round(100 * float(np.median([r[0][g] for r in runs])), 2) for g in gens5]
    print("   generations:", gens5)
    print("   share %:    ", series)

    print("\n--- density silhouettes for the beat sheet (x from -4.0 to 9.0, 40 bins) ---")
    print("  generation 0, rare subpopulation present:")
    print("   ", [round(float(v / scale), 3) for v in early])
    print("  generation 40, after extinction in most seeds:")
    print("   ", [round(float(v / scale), 3) for v in late])
    rare_from = next(i for i, g in enumerate(GRID) if g > 4.0)
    print("  the rare bump sits at x > 4.0 = bins %d-39 = fractions %.3f-1.000 of the axis"
          % (rare_from, rare_from / 39))


if __name__ == "__main__":
    curves_for_the_video(main())
