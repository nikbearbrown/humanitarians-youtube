# CapCut Storyboard — Physics Vol. 1 book-wide + agents (2 videos)

**Pattern source:** [humanitarians ai](https://www.youtube.com/@humanitariansai) · PM gate [intro line](https://www.youtube.com/watch?v=8SAmUN0qxRA)  
**Target length:** ~3:00 each  
**Visual theme:** [`VISUAL_THEME.md`](./VISUAL_THEME.md) · cards: [`brutalist-title-cards-bookwide.html`](./brutalist-title-cards-bookwide.html)  
**Build:** `python build_videos_bookwide.py` → 4K · 16:9 + 9:16

**Required intro line:** *"This is Charitha Sree Veluru in for Sanjana about [topic]."*  
**Naming:** `physics_vol_1_bookwide_Charitha_Sree_Veluru_videoN_{16x9|9x16}.mp4`

---

## How the two videos differ

| | **Video 1 — Agents** | **Video 2 — Project update** |
|---|---|---|
| **Claim** | One mega-agent on 17 chapters ships uneven sims | Ch. 4's contract can go book-wide without butchering pedagogy |
| **Question** | *How* do we scale interaction quality? | *What* shipped after the Ch. 4 pattern? |
| **Demo** | Parallel specialist agents → one chapter each | Drag handles across Ch. 1, 5, 9, 16… |

---

# VIDEO 1

**YouTube title:** Why one agent can't polish seventeen physics chapters  
**Subtitle:** Parallel specialists · Cursor agents · Physics Vol. 1  
**Outcome:** Viewer can **name** why one-agent rollouts fail and **reproduce** the specialist-agent pattern.

### Beats

| Beat | Say (summary) | Screen |
|------|----------------|--------|
| Hook | One agent on the whole book looks efficient. It ships uneven sims. | Textbook TOC / many embeds |
| Claim | Why can't one agent polish seventeen chapters the way Chapter 4 works? | Ch4 projectile drag |
| Contrast | One mega-prompt: slider-only graphs, wrong accuracy/precision, dead clicks. Thirteen specialists: one chapter each, same Ch4 contract. | Broken feel vs ch05 incline drag |
| Why | Shared contract — layout, bindCanvasInteraction, Play, stable axes. Parallel agents share the contract, not one giant context. | File tree embeds/ch05…ch17 |
| Show | Agent per chapter. Ch1 click-to-highlight orders. Ch9 collision tip drag. Same chrome. | Live demos |
| Your turn | Open two embeds from different chapters. Drag a handle. Same Play. Same pause-on-drag. | Dual embeds |

---

# VIDEO 2

**YouTube title:** What shipped when Chapter 4's sim contract went book-wide  
**Subtitle:** FigureWithSim · Ch. 1–17 · Physics Vol. 1  
**Outcome:** Viewer can **see** book-wide parity and **open** any chapter sim that drags.

### Beats

| Beat | Say (summary) | Screen |
|------|----------------|--------|
| Hook | Chapter 4 was done well. The book still had seventeen chapters of uneven interactivity. | Ch4 FigureWithSim |
| Claim | What does it take to make every linked sim drag like Chapter 4? | Book TOC |
| Contrast | Before: decorative canvases, auto-scaling axes hiding parameter changes. After: handles, Play, fixed axes, height 620. | unitSpeed time change visible |
| Why | FigureWithSim keeps OpenStax images. Embeds share ch04 utils. Scope: upgrade interaction, don't invent wrong physics. | Side-by-side figure+sim |
| Show | Ch1 orders click. Ch6 Atwood mass tips. Ch13 orbit drag. Ch16 crest scrub. | Quick tour |
| Your turn | Pick any chapter 5–17 section. Find a FigureWithSim. Drag once. | Live textbook page |

---

## Production

```bash
# Terminal A — textbook
cd ~/physics-vol-1 && npm start   # :3002

# Terminal B — build
cd ~/agreement_renewal_docs/video
source .venv/bin/activate
python build_videos_bookwide.py
```

Requires: `ELEVENLABS_API_KEY` in `.env` (preferred), or auto-fallback to `edge-tts` when the key is invalid. Playwright Chromium, ffmpeg.

```bash
# Force edge-tts only:
VIDEO_TTS=edge python build_videos_bookwide.py
```
