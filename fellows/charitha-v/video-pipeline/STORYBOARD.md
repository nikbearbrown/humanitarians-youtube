# CapCut Storyboard — Physics Vol. 1 Ch. 4 (2 videos)

**Pattern source:** [humanitarians ai](https://www.youtube.com/@humanitariansai) — e.g. [Why wrapping the same text in XML changes the answer Claude gives](https://www.youtube.com/watch?v=I5eBnDGoRCM)  
**Target length:** ~3:00 each (not 4+ lecture blocks)  
**Format:** Screen capture + voiceover · branded title card + outro (Descript/CapCut)  
**Visual theme:** [`VISUAL_THEME.md`](./VISUAL_THEME.md) · pre-built frames: [`title-cards.html`](./title-cards.html)

---

## The pattern (every humanitarians ai explainer)

One video = **one claim**. Not a tour. Not a status report. A tension the viewer can feel, then a demo that resolves it.

| Beat | Job | Duration |
|------|-----|----------|
| **1. Hook** | Challenge a false assumption | ~10 sec |
| **2. Claim** | Restate the title as a question or paradox | ~15 sec |
| **3. Contrast demo** | Same situation, two treatments — show the difference on screen | ~45–60 sec |
| **4. Why** | One mechanism. No stack dump. | ~30 sec |
| **5. Show it directly** | Live proof — cursor, drag, toggle, scroll | ~45 sec |
| **6. Reframe** | One memorable line (X isn't a trick; it's Y) | ~10 sec |
| **7. Recap** | Three-part formula, spoken fast | ~5 sec |
| **8. Your turn** | Viewer can reproduce in 60 sec | ~30 sec |
| **9. Outro** | Title card + channel/project tag | ~5 sec |

**Title rule:** claim, not topic.  
✗ "Chapter 4 simulations" · ✓ "Why a green build still ships a broken physics demo"

**Branding (PM gate):** Physics **brutalist** template — ink `#121212`, red `#C8102E`, ochre `#C8860E`, white cards, **Inter** + **JetBrains Mono**. Cards: `brutalist-title-cards.html` (4K). Legacy HAI palette in `title-cards.html` is superseded for submissions.

**Required intro line (first beat):** *"This is Charitha Sree Veluru in for Sanjana about [topic]."* — see [PM approval gate video](https://www.youtube.com/watch?v=8SAmUN0qxRA).

**Export:** 4K source · both **16:9** and **9:16** · naming `physics_vol_1_ch4_Charitha_Sree_Veluru_videoN_16x9.mp4` (via `build_videos.py`).

---

## Production setup

- `npm start` → `http://localhost:3002` · Chrome 1280×800 · zoom 100% · `Ctrl+Shift+R` before recording
- Record beats 3–5 as one continuous screen take; hook/recap/your-turn can be voice-over on frozen frame or B-roll
- CapCut: auto-captions · fix `FigureWithSim`, `utils.js`, commit hashes · export 1080p MP4

---

# VIDEO 1

**YouTube title:** Why a green build still ships a broken physics demo  
**Subtitle (title card):** Physics Vol. 1 · Ch. 4 · canvas embeds  
**Outcome:** Viewer can **contrast** integrated chart UX vs iframe canvas UX and **name** why Play + drag matter for a textbook reader.

---

### Beat 1 — Hook (~0:00–0:10)

| | |
|---|---|
| **Say** | Someone ships when the build passes. That isn't when the sim is done. |
| **Screen** | Green CI checkmark or `npm run build` success — 2 sec. Cut to static textbook figure. |

---

### Beat 2 — Claim (~0:10–0:25)

| | |
|---|---|
| **Say** | So why does a textbook figure need its own canvas page in an iframe — instead of another React chart inside the app? The physics is the same. The reader experience isn't. |
| **Screen** | Ch. 4 prose citing "Figure 4.7." Hold on static image. |

---

### Beat 3 — Contrast demo (~0:25–1:20)

| | |
|---|---|
| **Say** | Take projectile motion. Wire it as a generic integrated chart: sliders move numbers, click resets the animation, Play is too fast to see the path. Now open the same scenario as a standalone canvas embed: drag the launch pad, press Play, scrub the trajectory. Same chapter. Same physics. Different result — because one lets you explore; the other trains you not to click. |
| **Screen** | **A:** Brief flash of in-app/chart feel (or describe over projectile embed with sliders only — no drag). **B:** `projectile.html` — drag pad → Play → scrub path. Split or hard cut between A and B. |

---

### Beat 4 — Why (~1:20–1:50)

| | |
|---|---|
| **Say** | Here's why. Thirteen sims in `public/embeds/ch04/`, each loaded through a thin React wrapper. Shared `utils.js` — bindPlay, drag handles, scene fitting. The iframe is a boundary: tune teaching UX without redeploying the whole textbook. Build green inside Next.js didn't mean the mechanism was explorable. |
| **Screen** | Flash file tree: `embeds/ch04/` → `DemoEmbed.tsx` → back to embed. |

---

### Beat 5 — Show it directly (~1:50–2:35)

| | |
|---|---|
| **Say** | Look at the difference directly. Vector 2D: drag a tip — Play pauses while you interact. Newton's cannon: change speed — orbit stays in frame. Every embed has the same Play control. That consistency is deliberate. |
| **Screen** | `vector-2d.html` — drag tip, switch preset chip. Cut to `newtons-cannon.html` — Play, full orbit visible. |

---

### Beat 6 — Reframe (~2:35–2:45)

| | |
|---|---|
| **Say** | A passing build isn't a teaching pass. If exploring resets the sim, you're not adding interactivity — you're punishing curiosity. |
| **Screen** | Hold on Play button + drag handle. |

---

### Beat 7 — Recap (~2:45–2:50)

| | |
|---|---|
| **Say** | Same physics. Iframe boundary. Reader-first UX. |

---

### Beat 8 — Your turn (~2:50–3:20)

| | |
|---|---|
| **Say** | Your turn. Open `localhost:3002/embeds/ch04/projectile.html`. Drag the launch point. Press Play. Scrub the path. Then ask: would a slider-only chart have shown you the same thing? |
| **Screen** | Cursor follows the steps live. URL visible in address bar. |

---

### Beat 9 — Outro (~3:20–3:25)

| | |
|---|---|
| **Screen** | Title card: **Why a green build still ships a broken physics demo** · Physics Vol. 1 Ch. 4 · branch link |

---

# VIDEO 2

**YouTube title:** Why putting the simulation at the bottom breaks the lesson  
**Subtitle (title card):** FigureWithSim · Ch. 4 scope  
**Outcome:** Viewer can **compare** bottom-gallery vs side-by-side placement and **explain** why the sim must resolve where the citation lands.

---

### Beat 1 — Hook (~0:00–0:10)

| | |
|---|---|
| **Say** | The sim worked. The student still couldn't use it. |
| **Screen** | Working embed playing — then scroll **away** from the paragraph that cites the figure. |

---

### Beat 2 — Claim (~0:10–0:25)

| | |
|---|---|
| **Say** | So why does putting the simulation at the bottom of the section break the lesson? The code runs. The pointer in the prose says "see Figure 4.7" — three scroll lengths above the only place you can touch it. |
| **Screen** | Stop cursor on in-text citation. Scroll down to bottom gallery — show the gap. |

---

### Beat 3 — Contrast demo (~0:25–1:20)

| | |
|---|---|
| **Say** | Same chapter, two layouts. Bottom gallery: one iframe, many preset chips, far from the sentence that references the figure. Side by side: OpenStax figure on the left, live sim on the right — citation and tool in one viewport. We tried rolling embeds across the whole book first. We reverted to Chapter 4 only. One chapter done well beats a whole book halfway. |
| **Screen** | **A:** Bottom gallery (screenshot or reconstructed scroll). **B:** `FigureWithSim` — figure + sim adjacent. Hard cut. |

---

### Beat 4 — Why (~1:20–1:50)

| | |
|---|---|
| **Say** | Here's why. The sentence creates a pointer. The UI has to resolve it there — not later, not at the bottom. We restored inline OpenStax figures, mapped twenty-eight plus figure-to-sim pairs, and synced theme with postMessage so dark mode doesn't remount the iframe and wipe scrub state. |
| **Screen** | Pause on figure caption number aligned with sim. Toggle light/dark — sim state holds. |

---

### Beat 5 — Show it directly (~1:50–2:35)

| | |
|---|---|
| **Say** | Look at the layout directly. HUD and legend above the canvas — not on top of it. Narrow the window: chrome scrolls horizontally; the drawable band stays. Orbit sim: vectors inside the frame, not clipped past the edge. |
| **Screen** | Resize to ~400px width. Open `orbit.html` or circular-motion — geometry inside gray canvas band. |

---

### Beat 6 — Reframe (~2:35–2:45)

| | |
|---|---|
| **Say** | Layout isn't decoration. It's part of the physics lesson. Reverting a large rollout isn't failure if the reader stops getting lost. |
| **Screen** | Figure + sim in same frame. |

---

### Beat 7 — Recap (~2:45–2:50)

| | |
|---|---|
| **Say** | Citation here. Sim here. Not three scrolls later. |

---

### Beat 8 — Your turn (~2:50–3:20)

| | |
|---|---|
| **Say** | Your turn. Open any Ch. 4 section. Find a figure citation in the prose. Without scrolling, can you see the matching sim? If not, the layout is still teaching the wrong lesson. |
| **Screen** | Live scroll — stop when citation and sim share the viewport. |

---

### Beat 9 — Outro (~3:20–3:25)

| | |
|---|---|
| **Screen** | Title card: **Why putting the simulation at the bottom breaks the lesson** · Substack article link · GitHub branch |

---

## CapCut timeline (both videos)

```
[Intro title card 3s]
→ Hook (voice + B-roll)
→ Claim (voice + scroll/citation)
→ CONTRAST (longest block — record clean)
→ Why (voice + quick file flash)
→ Show directly (live demo)
→ Reframe (voice + hold frame)
→ Recap (voice only or text overlay)
→ Your turn (voice + cursor follows)
→ Outro title card 5s
```

## Email links (after upload)

```
1. [Why a green build still ships a broken physics demo](YOUR_LINK_1)
2. [Why putting the simulation at the bottom breaks the lesson](YOUR_LINK_2)
```

---

## What changed from the old storyboard

| Old (lecture arc) | New (humanitarians ai pattern) |
|-------------------|--------------------------------|
| 45-sec context monologue | 10-sec hook + 15-sec claim |
| "What we did" inventory | Contrast demo (A vs B) |
| Four problems listed | One mechanism in "Why" |
| 4+ minutes | ~3 minutes |
| Topic titles | Claim titles |

`VIDEO_SCRIPTS.md` is the long-form source. **Record from this file.**
