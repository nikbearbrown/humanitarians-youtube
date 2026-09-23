# FRICTIONAL — 2026-09-22-minirag-explainer

Dated record of the process behind this reel. Appended as work happened; earlier
entries are not rewritten.

---

## 2026-09-08 — Getting the toolkit to run at all

**Expected:** clone `brutalist.art`, run `./setup --install`, start building.

**What resisted:** three separate failures before a single frame rendered.

**1. No working Python.** The machine had Anaconda 3.13.9, Homebrew 3.14.3 and
Apple 3.9.6. All three fail `requirements.txt` — `manim>=0.18,<0.19` declares
`requires-python <3.13`, so on 3.13/3.14 pip silently omits the whole 0.18 line
from its candidate list. 3.9.6 is below the repo's documented floor.

**2. The 3.12 I installed was broken.** `brew install python@3.12` succeeded, then
`python3.12 -m venv` failed with an `ensurepip` error that printed no cause —
`venv` discards the subprocess output. Running `ensurepip` as its own foreground
command surfaced the real chain:

```
pyexpat.so → Symbol not found: _XML_SetAllocTrackerActivationThreshold
  → plistlib can't import
    → platform.mac_ver() returns ''
      → pip's vendored truststore does int('') → ValueError
```

`otool -L` showed `pyexpat` linking the **system** expat, and `brew deps
python@3.12` lists no expat dependency, so there is no bundled fallback. The
bottle was built against a different libexpat than macOS 26.2 ships. Confirmed
isolated by asking each interpreter for the OS version: Homebrew 3.12 returned
`''`; 3.14, Anaconda 3.13.9 and Apple 3.9.6 all returned `26.2`.

**What was done:** used `uv venv --python 3.12 --seed`, which supplies a
python-build-standalone interpreter bundling its own expat. One-line regression
test: `python3 -c "import platform; print(platform.mac_ver()[0])"` must print the
OS version, not `''`.

**3. `pycairo` wouldn't compile** — no wheel for this platform, and the source
build needs `pkg-config`, which wasn't installed. `brew install pkg-config cairo
pango` fixed it. Manim went from uninstallable to fine.

**Claude's contribution:** diagnosed all three. I accepted the uv route over
rebuilding Homebrew's Python from source — faster and doesn't touch Homebrew's
state. I ran every install command myself rather than delegating, which was the
right call: I now understand what's on this machine and why.

**Still open:** the Homebrew `python@3.12` bottle is still broken. Left installed
but unused rather than uninstalled, since other formulae may depend on it.

---

## 2026-09-08 — A bug in the toolkit's own smoke test

**Expected:** `./art smoke` passes, proving the pipeline works end to end.

**What resisted:** it failed at the first gate —
`[kokoro] REFUSED: metadata.slug must be a filename, not a path`.

The message is misleading. The fixture's slug is `_smoke`, which contains no
path. The real rule is in `build_safety.py:186`: the slug regex required the
first character to be alphanumeric. But `smoke_test.sh:60` hardcodes the output
as `_smoke-slate.mp4`, so the fixture's slug *must* start with an underscore.
**The shipped smoke test could never pass.** `git log` put the tightened regex in
the then-current HEAD commit.

**What was done:** widened the leading character class from `[A-Za-z0-9]` to
`[A-Za-z0-9_]`. Verified the change still rejects `../evil`, `a/b`, `.hidden` and
`-flag`, so no path-safety or argv-injection protection is lost. One character.

**Accepted / rejected:** Claude offered three routes — patch the validator, prove
the pipeline in a scratch copy without touching the repo, or skip verification. I
chose the patch because leaving `./art smoke` broken for the next person is worse
than a one-character diff. **This is an upstream bug worth reporting to Bear.**

---

## 2026-09-08 — Library-first turned up unregistered components

**Expected:** GATE L says ask the library before authoring. I expected the
documented structural templates to be usable.

**What resisted:** `./art scenes --check` reported `FlowDiagram`, `LayerStack`,
`SourceFlow`, `ChipGrid` and `PredictCard` as **NOT RENDERABLE** — they exist in
`src/illustrations/structural.tsx` and are documented in `ILLUSTRATIONS.md`, but
have no `<Composition>` in `Root.tsx`. The search returns them as leads that
cannot actually render.

Separately, `BarChart` *is* renderable but uses the Vox palette (teal/slate).
Using it would have broken the Claude fidelity brand law, which says terracotta
is the one accent and the palette may not be retinted. Rejected it and searched
again, which surfaced `ReqBars` — Claude palette, two-series, reusable. That one
component ended up carrying three beats.

**What was done:** authored six reel-local components in `MiniRag.tsx`, registered
them in `Root.tsx`, re-ran `./art scene-index` (610 → 616). Every number is a
prop from the beat sheet; nothing hardcodes a statistic.

**Now understood:** a library hit is genuinely a lead, not a verdict — the
doctrine says so and this proved why. Two of my searches returned things that
looked perfect and were unusable for different reasons.

---

## 2026-09-08 — Reading the paper before writing anything

**Expected:** summarise the paper and script from the summary.

**What was done instead:** read all 16 pages as rendered images, so the figures
and tables were visible rather than extracted as text. Every number in the reel
was read off Table 1, Table 2 or Table 3 directly, then written into
`FACTCHECK.md` with its source location — 25 rows.

Three claims from the paper's own abstract were **dropped as unsupported by its
own data**: "comparable performance to LLM-based methods" and "state-of-the-art
across all evaluation settings" don't survive Table 1's gpt-4o-mini row on
LiHuaWorld, where MiniRAG scores 54.08 against LightRAG's 56.90. The reel makes
the narrower claim that does hold — MiniRAG wins *on small models*.

One finding the paper underplays was **promoted to a full beat**: MiniRAG's
error rate on MultiHop-RAG is 28.44% against LightRAG's 11.78%. §3.2 discusses
the accuracy gains and the storage savings and never mentions this. B11 exists
because of it.

**Accepted / rejected:** Claude proposed centring the whole film on one claim
("RAG needed a better index, not a bigger model"). I rejected that framing — the
brief was to explain the research, not argue a thesis — and asked for the full
structure: problem, question, method, architecture, evidence, meaning,
conclusion. The one-claim version became beat B01's executive summary instead,
which is where it belongs.

---

## 2026-09-22 — Six rounds against one quality gate

**Expected:** the reel renders, `./art final` produces a clean master.

**What resisted:** `./art final` **refused**. Its pre-flight,
`final_frame_check.py`, treats MAJOR defects as fatal and has no lenient
passthrough — so four cosmetic "underfill" warnings I had written off as
out-of-scope were actually blocking the master.

B01 took five attempts: 10% → 23% → 43% → 51% → clean. The first three were me
assuming the text was too small and enlarging it. Wrong diagnosis. Extracting the
frame at the 85% sample point showed the writer was **still typing** — the
hesitant-writer's pauses were consuming the entire 12.8-second beat, so the
correction landed exactly on the cut. Repacing it (`charMs` 50 → 14, hesitation
reduced but not removed) fixed the gate *and* the pedagogy: the corrected
sentence now lands at ~25% and holds.

**Now understood:** the gate was right and I was wrong about why. Looking at the
actual frame took two minutes and would have saved three rounds. "Verify by
looking at frames, never by the probe alone" is in the repo rules for a reason.

**Accepted / rejected:** Claude offered a shortcut — stitch the finished beats
with ffmpeg directly and bypass the gate, two minutes, visually identical. I
rejected it. The gate is the repo's standard and working around it would have
left a defect in the film that nobody would have caught until someone watched it.

---

## 2026-09-22 — Revision after review

Two changes came back: remove the `B0x GRAPHIC VIDEO` footer, and change the
channel handle to `@NeelabhBhardwaj`.

The footer was not an edit — it is the `--review` burn-in, and the fix was to
render with `./art final` rather than `./art run`. Worth knowing the difference.

The handle appeared in four places. Three were `folderLabel` props in the beat
sheet. The fourth was hardcoded in `ClaudeTitleOutro.tsx`, deliberately —
`OUTRO-LOCK.md` says the handle must never be *derived* from a channel variable,
because a previous bug shipped `@Musinique` on a Bear reel. Changing the constant
would have silently re-branded every other claude-liam reel on its next render.
Made it an **optional prop defaulting to the existing constant** instead, so the
lock's intent survives and only a sheet that explicitly asks gets a different
handle. Verified both the cold open and the outro card by extracting frames and
reading them.

v1 was copied to `revisions/` before any re-render, since the toolkit always
writes the same filename.

---

## Open

- The `build_safety.py` slug fix is an uncommitted local patch. Needs reporting
  upstream, or it disappears on the next clone and `./art smoke` breaks again.
- `FlowDiagram` / `LayerStack` / `SourceFlow` / `ChipGrid` / `PredictCard` are
  still documented-but-unregistered. Registering them would save the next fellow
  the same detour.
- The YouTube description document in Drive predates the handle change. Needs
  checking for stale `@NikBearBrown` references before upload.
- No 9:16 vertical cut. A Short is a different beat sheet, not a crop, and the
  six `MiniRag*` components are 16:9 only — portrait variants would need
  authoring.
