# Renewal supplement — two video scripts

**Fellow:** Charitha Sree Veluru  
**Project:** Physics Vol. 1, Chapter 4 — OpenStax interactive textbook  
**Branch:** https://github.com/Medhavy/physics-vol-1/tree/VelCharitha77/chat-anims  
**Period:** June 29 – August 23, 2026  

**Format:** Two separate screen recordings (or voice-over + screen).  
**Suggested length:** 3–5 minutes each.  
**Upload:** YouTube (unlisted) or Google Drive link in renewal email — do **not** attach large MP4s to email.

> **Book-wide / parallel-agents update (new):** see [`VIDEO_SCRIPTS_BOOKWIDE.md`](./VIDEO_SCRIPTS_BOOKWIDE.md) · regenerate with `python build_videos_bookwide.py`.

---

## How the two videos differ

| | **Video 1** | **Video 2** |
|---|-------------|-------------|
| **Topic** | Building the simulation *engine* | Placing the sim where the *textbook teaches* |
| **Question it answers** | *How* did we make figures interactive and usable? | *Where* should interactivity live in a textbook page? |
| **Main arc** | D3 → iframe canvas → direct manipulation | Gallery → side-by-side → scope + layout polish |
| **Demo focus** | Drag handles, Play, presets, one sim deep-dive | Figure + sim pairs, theme toggle, clean layout |

---

# Video 1 — Building the Chapter 4 Simulation Engine

**Title suggestion:** *From Static Figures to Canvas Sims — Physics Vol. 1 Ch. 4*

### 0:00–0:45 — Context (set the scene before any demo)

**Say something like:**

> This is **Physics Vol. 1, Chapter 4** — motion in two and three dimensions: vectors, projectile paths, circular motion, relative velocity. It's an OpenStax-based textbook running as a web app.  
>  
> The prose constantly points at figures: "as in Figure 4.7," "consider the trajectory." Those figures started as static images. A reader could read about a parabola but couldn't scrub one, drag a launch angle, or watch horizontal and vertical motion split apart.  
>  
> The job was to make those moments **live** — not to sprinkle charts everywhere, but to make the *mechanism* explorable where the text is already pointing.  
>  
> This video is about **how we built that**: architecture, tools, what broke, and what shipped.

**On screen (optional):** Ch. 4 section in the textbook, or one static figure next to where the sim will go.

---

### 0:45–1:30 — What we did

**Say:**

> We started by wiring interactive diagrams **inside** the Next.js app — React components in MDX, tied to the textbook design system. Production builds passed.  
>  
> Then we pivoted to **13 standalone HTML canvas pages** in `public/embeds/ch04/`, each loaded through a thin React wrapper (`DemoEmbed`). Shared utilities in `utils.js` and scenario configs in `presets.js` keep behavior consistent across sims.

**On screen:**

- Brief flash of repo: `public/embeds/ch04/`, `components/physics/DemoEmbed.tsx`
- Open **one** embed directly, e.g. `vector-2d.html` or `projectile.html`

---

### 1:30–2:30 — Problems we faced

**Say:**

> **Problem 1 — Wrong kind of "done."** Integrated D3 looked like generic charting, not a physics demo. Builds were green; the *feel* was wrong.  
>  
> **Problem 2 — Interactivity that didn't interact.** Clicking reset the animation. Sliders changed numbers but not intuition. Play ran too fast to see motion. Newton's cannon clipped the orbit or hid the Earth. Labels overlapped on the canvas.  
>  
> **Problem 3 — Broken third-party sims.** PhET Java embeds failed in the iframe stack — a dead sim erodes trust more than no sim.  
>  
> **Problem 4 — No Play on every sim.** Review feedback: every simulation needs an explicit Play control, not only scrubbing.

**On screen:** You don't need to show broken states — name them while showing the *current* fixed sim if easier.

---

### 2:30–3:30 — What we used & how we solved it

**Say:**

> **Tools & stack:** HTML5 Canvas, vanilla JS modules, shared `utils.js` (`fitCanvas`, `bindPlay`, `bindCanvasInteraction`, `bindCanvasLockToggle`, `drawHandle`, `clipToScene`), preset chips per scenario, React `DemoEmbed` / `ThemedDemoFrame` for iframe loading and theme messages.  
>  
> **How we solved it:**  
> - **Iframe boundary** — each sim is self-contained; tune physics without redeploying the whole site.  
> - **Direct manipulation** — drag vector tips, launch pads, and path points; pause Play when the user interacts.  
> - **Play loops** with capped `animationDt` so motion is visible, not a blur.  
> - **Scene fitting & clipping** so trajectories and orbits stay in frame.  
> - **Removed PhET** where embeds didn't work; replaced with our canvas sims.  
> - **`bindPlay` on every embed** so Play/Pause is consistent.

**On screen (live demo — pick 2–3):**

1. **Projectile** — drag launch pad, press Play, scrub path  
2. **Vector 2D** — drag a tip; switch preset chip (e.g. plane & wind)  
3. **Newton's cannon** — change speed, Play trace, show ghost regimes  

---

### 3:30–4:15 — Result & takeaway

**Say:**

> **Result:** 13 working canvas embeds covering vectors, orbits, independence of motion, projectile range and components, circular motion, relative velocity, parametric graphs, and more — all with shared UX patterns and Play controls.  
>  
> **Takeaway:** "Integrated" and "right for the reader" are not the same gate. A deliberate **boundary** (iframe + shared utils) let us iterate on teaching UX faster than deep coupling into the app. And **build passes are not user passes** — if exploring resets the sim, you're training the reader not to explore.

**On screen:** Quick montage — 3–4 embed thumbnails or rapid tab through `ch04/*.html`.

**End card:** GitHub branch URL.

---

# Video 2 — Layout, Scope, and Where the Simulation Belongs

**Title suggestion:** *Don't Put the Simulation at the Bottom — Textbook Layout & Scope*

### 0:00–0:45 — Context (different entry point from Video 1)

**Say something like:**

> Video 1 was about **building** the simulations. This one is about **where they belong on the page**.  
>  
> Once the canvas sims worked, we had a different problem: a student reads "see Figure 4.7" in the middle of a section, but the interactive version lived in a **gallery at the bottom** — one iframe, many scenario chips, three scroll lengths away.  
>  
> We also tried rolling the same embed pattern across the **whole book** before pulling back to finish **Chapter 4 properly**.  
>  
> This video covers those layout and scope decisions: keeping OpenStax figures trustworthy, putting each sim beside the figure it illustrates, and fixing the UI so the canvas isn't crushed by chrome around it.

**On screen:** Textbook page with figure + sim side by side, or the Substack title *Don't Put the Simulation at the Bottom*.

---

### 0:45–1:30 — What we did

**Say:**

> We **reverted** chapters 1–3 and 5–17, keeping the embed *stack* but not every MDX swap.  
>  
> We **restored inline OpenStax figures** — readers expect a licensed textbook to look like one.  
>  
> We built **`FigureWithSim`**: textbook image on one side, live sim on the other; stacks on narrow screens.  
>  
> We mapped **28+ figure-to-sim pairs** across §4.1–§4.5 so each sim sits beside the figure the prose references.  
>  
> We synced **light/dark theme** via `postMessage` so toggling appearance doesn't remount the iframe and wipe scrub state.  
>  
> Finally we separated **HUD, legend, readout, and controls** from the canvas band and added **content-aware fitting** so plots don't draw outside the frame.

**On screen:**

- Textbook page with `FigureWithSim` (figure + sim side by side)
- Toggle light/dark — sim should **not** reset

---

### 1:30–2:30 — Problems we faced

**Say:**

> **Problem 1 — Pedagogical misplacement.** The sim for Figure 4.7 was three scroll lengths below the paragraph that cites it. Students hit the reference before the tool.  
>  
> **Problem 2 — Scope outran quality.** Multi-chapter rollout looked like progress by file count; some pages had errors, wrong figures interactive, objects off-frame.  
>  
> **Problem 3 — Theme toggle erased state.** Early iframe remount on dark mode lost scrub position and presets.  
>  
> **Problem 4 — Chrome ate the canvas.** Title, legend, readout, and control chips stacked on or over the sim; on narrow iframes the drawable area shrank to a thin strip.  
>  
> **Problem 5 — Geometry still overflowed.** After layout separation, some orbits and vectors still clipped past the canvas edge.

**On screen:** If you have an old screenshot of bottom gallery, show it briefly; otherwise describe while showing current good layout.

---

### 2:30–3:30 — What we used & how we solved it

**Say:**

> **Tools:** `FigureWithSim`, `DemoEmbed` / `ThemedDemoFrame`, Fumadocs `useFdTheme`, CSS flex layout in `style.css`, shared helpers `plotBox`, `fitCircle`, `fitWorldPoints`, `clipFrame` in `utils.js`, git revert to `e1abb1f` for scope correction.  
>  
> **How we solved it:**  
> - **Side-by-side layout** — sim co-located with the figure citation.  
> - **Ch. 4-only scope** — one chapter done well beats a whole book halfway.  
> - **Stable iframe src + postMessage theme** — appearance changes without remount.  
> - **Strict vertical stack:** HUD → canvas stage → readout → controls; capped chrome height; horizontal scroll on preset chips.  
> - **Fit-to-frame scaling** — scale geometry to the plot box; clip only as safety net.  
> - Raised default iframe height so the sim band has room.

**On screen (live demo):**

1. Scroll through a section — pause at a figure **next to** its sim  
2. Toggle theme — confirm state preserved  
3. Show **narrow width** — legend above, canvas unobstructed, plot inside frame  
4. Orbit or circular-motion — vectors stay inside gray canvas band  

---

### 3:30–4:15 — Result & takeaway

**Say:**

> **Result:** Chapter 4 keeps OpenStax figures **and** live sims at the point of reference. Branch `VelCharitha77/chat-anims` includes layout separation, theme sync, Play on every sim, and fit-to-frame geometry. Substack article published: *Don't Put the Simulation at the Bottom of the Page*.  
>  
> **Takeaway:** Layout is part of the physics lesson. The sentence creates a pointer; the UI must resolve it **there**. Agents can execute rollouts; **humans** must call stop when volume outruns quality. Reverting a large diff isn't failure if the reader experience improves.

**On screen:** Substack URL, GitHub branch (optional).

**End card:** Links — branch, Substack article.

---

## Recording checklist (both videos)

- [ ] `npm start` running; hard-refresh (`Ctrl+Shift+R`) before recording  
- [ ] Browser zoom 100%; window ~1280×800 or full screen  
- [ ] Mic test; quiet room  
- [ ] Close unrelated tabs/notifications  
- [ ] Script rehearsed once without recording  
- [ ] Export MP4; upload unlisted YouTube or Drive  
- [ ] Add link to renewal email (see snippet below)

---

## Suggested email line (after upload)

Add under **Major deliverables** or a new **Supplemental video** bullet:

> **Supplemental walkthrough (2 videos):**  
> 1. [Building the Ch. 4 simulation engine](YOUR_LINK_1) — architecture, tools, direct manipulation  
> 2. [Layout, scope, and figure placement](YOUR_LINK_2) — FigureWithSim, theme sync, pedagogical layout

---

## Quick reference — commits to mention

| Topic | Commit / artifact |
|-------|-------------------|
| Multi-chapter rollout | `d1e3e0e` |
| Revert to Ch. 4 only | `e1abb1f` |
| OpenStax restore + gallery | `50f4e15` |
| FigureWithSim + theme | `5f0dbe4` |
| Chrome separation | `9e6b9b5` / tag `pre-fit-canvas-sweep` |
| Fit plots in frame | `30f066b` |

Update latest commit hash in email if branch has moved since renewal docs were drafted.
