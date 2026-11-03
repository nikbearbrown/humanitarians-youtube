# VISUAL QC LOG — The Bottleneck Moved.

Frame-level QC per VISUAL QC LAW. Frames were sampled at ~15/50/85% of every beat's
measured span and **read as images**, not probed. `_qc/REPORT.md` is machine-generated
by Gate V (`runtime/qc/final_frame_check.py`) and is overwritten on each `./art run`;
this file is the durable record of what was found, fixed, and deliberately accepted.

The mp4 probe (duration + frame count) was never treated as QC.

---

## Defects found and FIXED

### 1. B01 — rising line labelled "unchanged" · BLOCKER · fixed
The terracotta track was authored `path: 'up'` with `outcome: 'unchanged'`. On the frame
the line visibly *climbs* while its own label says it didn't change — the picture
contradicting the caption. Relabelled to **"did not fall"**, which is true of a rising
line and matches the narration ("It did not collapse the cost of being worth someone's
attention"). The `show` block was corrected to describe a climb, not a flat hold.

### 2. B01 — doubled arrow `→ →` · MAJOR · fixed
`DivergentFates` prepends its own "→" to `outcome`. The prop value also began with "→",
rendering "→ → near zero". Removed the leading arrow from the prop.

### 3. B01 / B06 — label boxes crossed the title-safe inset · BLOCKER · fixed
Both reused deckPatterns scenes place end-of-track label boxes hard against the canvas
edge; at 1920×1080 that put them at x≈3792 of 3840 in the 4K render, past `SAFE.r` (3648).
The patterns are shared with other reels, so their internal margins were left alone.
Instead the whole composition is mapped onto the safe box in the reel-local `Stage`
wrapper: the inset is a uniform 5%, so `SAFE.w/CANVAS.w === SAFE.h/CANVAS.h === 0.9`
exactly — isotropic, no distortion, and ink coverage as a fraction of SAFE is unchanged.

### 4. B02 — `ScaleComparison` crashed the render · BLOCKER · fixed by replacement
`RangeError: Invalid array length`. Root cause read from source, not guessed: the
component builds decade ticks with `for (e = ceil(log10(ax.min)) … )`, and this beat's
axis starts at 0, so `log10(0) = -Infinity` and the loop never terminates.
Raising `min` to 1 would have stopped the crash but not the real problem — it is a
LOG-SCALE component that stamps "(log scale, \<unit\>)" onto its own axis. `scenes/BarChart`
was evaluated next and rejected too: vox palette (TEAL accent, not terracotta) and it
prints each bar's raw numeric value. Replaced with a purpose-built ordinal bar scene.
**Post-fix measurement: canvas coverage 0.98 of SAFE** (Gate V floor is 0.55).

### 5. B04 — `AttritionChain` printed invented-looking numbers · BLOCKER · fixed by replacement
The component multiplies per-stage survivals cumulatively, so 0.35·0.30·0.25·0.20
rendered as **"1 / 100"** and **"1% remain"** on screen, inside five otherwise-empty
boxes. Numbers that look measured are the one thing this reel must not show
(`FACTCHECK.md`). Replaced with a purpose-built ordinal funnel: monotone widths, no
counts, and the top visibly doubling against a terracotta ghost line while the tail
holds — which is what the narration actually claims.

### 6. B04 — two collisions · MAJOR · fixed
The terracotta bracket ran *through* the right-aligned row labels ("Publish|ed",
"See|n"), and the two bottom captions overlapped each other. Row labels narrowed to
240px and the bracket moved into the resulting gutter; the bracket caption dropped
clear of the tail note.

### 7. B05 — `Threshold` printed a numeric axis and clipped its own label · BLOCKER · fixed by replacement
Rendered a 0–100 numeric y-axis plus "60 rel." over data explicitly labelled
*not measured*, clipped its axis label off the left edge ("UBLISHING"), and left ~80% of
the frame empty. Replaced with a purpose-built two-zone cutoff: verdict per zone, the
falsifier as the closing line, and an unticked direction-only axis.

### 8. B09 — wrong channel's subline · BLOCKER · fixed
The outro rendered **"bot vs bot, season one"** — the Musinique default. `ClaudeTitleOutro`
accepts only `{title, handle, subline}`; the beat sheet passed a `slug` prop that the
component ignores, so `subline` fell through to its default. OUTRO-LOCK requires **no
subline** on the @NikBearBrown card. Now passes `subline: ""` explicitly.

### 9. B03 — empty spark line · MAJOR · fixed
The toolkit's own SKIN LINT caught this: an inner composer beat with a bare asterisk
violates SPARK-LINE LAW. Given the cue **"After publish."**

### 10. Motion histogram over the per-language cap · WARNING · fixed
All five body beats were labelled `motion: illustrate`, tripping MOTION.md's ~40%
per-language cap at 50%. The label was simply inaccurate — these are five different
motion languages. Relabelled `diverge / grow / stagger / reveal / branch`, which both
describes what happens and clears the cap honestly.

---

## Gate V's 20 BLOCKERs are a FALSE POSITIVE — toolkit bug, not a reel defect

`./art run` reported `frames=20 BLOCKER=20 MAJOR=2`, one identical `edge-bleed` on every
sampled frame — including B09, which is centered text on empty cream. That uniformity was
the tell. Measured with Gate V's own functions:

| file | ink bbox | verdict |
|---|---|---|
| `<slug>-slate.mp4` (**review** cut) | x → **3831** / 3840, y → **8** | BLOCKER edge-bleed |
| `<slug>.mp4` (**clean** master) | x[1286, 2552] y[908, 1272] | **clean — inside SAFE** |

Gate V runs against the `--review` cut and flags **the review burn-in that
`compile.py --review` deliberately draws**. `final_frame_check.py` does try to exclude it —
`BURN_IN_EXCLUDE = (0.0, 0.94, 0.60, 1.0)` — but that rectangle masks only the *bottom*
strip, while the offending label sits *top-right*. So the exclusion never applies and
every frame of every review cut fails.

**Consequence:** on this toolkit, Gate V cannot pass any reel. The reel's real
edge-bleed count on the delivered master is **zero**. Suggested upstream fix: either run
Gate V against the clean cut, or widen `BURN_IN_EXCLUDE` to cover the top-right label.

---

## Accepted, not fixed (with reasons)

- **`underfill` on B07 and B09 · MAJOR · accepted.** Gate V's `FILL_MIN = 0.55`; measured
  coverage is 0.46 (B07 verdict artifact) and 0.07 (B09 title outro). Both are *shipped
  fidelity components* — a Claude artifact page and a poster-style title card, whose
  generous whitespace is the Claude app's own design. FILL-THE-CANVAS LAW and the
  FIDELITY-brand rule ("do not retint it, theme it, or improve it") point opposite ways
  here, and the fidelity rule is the more specific one. Redesigning shipped bookends to
  satisfy a fill metric would be the wrong call on a reel, so this is logged rather than
  "fixed". All five *body* beats — the ones this reel authored — clear the floor.
- **Mono labels in the two reused deckPatterns scenes (B01, B06).** The claude brand
  reserves mono for terminal/output lines. Fixing it means either editing a file shared
  with other reels or forking the patterns. The three purpose-built scenes use
  `CLAUDE_FONT.serif`/`.ui` correctly; the two reused ones stay mono for now.
- **Two terracotta elements on B06.** The `warn` branch and the resolver are both accented,
  softening "one terracotta moment per beat". Both come from the shared component's own
  tone mapping.

## Blocked by the toolkit, not by this reel

- **GATE T (type-lock) never ran.** The skill calls `scripts/type_check.py` "ALWAYS RUN",
  but that script does not exist anywhere in this tree. Type sizes were checked by eye
  against the ~24px floor instead.
- **The outro mascot clause cannot be satisfied.** OUTRO-LOCK asks for one of 18
  slug-seeded crisp-safe mascots; `ClaudeMascotScene`/`ClaudeMascotGrid` are not in this
  tree, and `ClaudeTitleOutro` renders no mascot. PIXEL-ART LAW is therefore moot here —
  there are no pixel-art rects to rotate. Not faked; the beat's `show` block says so.
- **`OUTRO-LOCK.md`, `AUDIT-MODE.md`, `DESIGN-PRINCIPLES.md` are all referenced by the
  skill and none ship** in this toolkit (`skills/make/ai-explainer/` contains only
  `SKILL.md`). Their rules were followed as quoted inside SKILL.md.
- **Manim is uninstallable here.** `manimpango` needs cairo's C headers, which come from
  Homebrew, and Homebrew needs sudo. Irrelevant to this reel — 0 Manim beats — but it
  blocks any reel with an equation or plotted-curve beat.

## Audio

Independently verified before compositing: 10/10 narration files present, mean volume
−22.9 to −24.7 dB against a −40 dB floor, durations matching the beat sheet exactly.
Each composition's `durationInFrames` equals its beat's measured length × 30fps, so
`compile.py` conformed every slot without a retime or freeze-pad.
