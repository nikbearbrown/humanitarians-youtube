# Renewal videos — book-wide sims + parallel agents

**Fellow:** Charitha Sree Veluru  
**Project:** Physics Vol. 1 — OpenStax interactive textbook (book-wide)  
**Branch:** `VelCharitha77/chat-anims`  
**Period covered:** Chapter 4 contract → Chapters 1–17 interaction parity  

**Format:** Two screen + voiceover explainers (PM gate).  
**Build:** [`build_videos_bookwide.py`](./build_videos_bookwide.py) · cards [`brutalist-title-cards-bookwide.html`](./brutalist-title-cards-bookwide.html)  
**Storyboard:** [`STORYBOARD_BOOKWIDE.md`](./STORYBOARD_BOOKWIDE.md)

---

## Video 1 — Parallel specialist agents

**Title:** Why one agent can't polish seventeen physics chapters  
**Intro line:** This is Charitha Sree Veluru in for Sanjana about why one agent can't polish seventeen physics chapters.

### Full VO script

> Someone gives one agent the whole textbook and calls it a rollout. That isn't how Chapter 4 got good.  
>  
> So why can't one agent polish seventeen physics chapters the way a single chapter actually teaches?  
>  
> Take accuracy versus precision — Figure 1.12. One mega-pass put the “high precision” cluster on the bullseye. That's accuracy, not precision. Slider-only graphs auto-scaled the Y axis so changing time looked like nothing happened. Students could see a sim and still couldn't learn from it.  
>  
> Now run it differently. One specialist agent per chapter. Same contract for every embed: Chapter 4 layout, canvas drag handles, Play that pauses when you grab a tip, stable axes so parameters are visible. Thirteen agents in parallel — chapters five through seventeen — each owning one folder under public slash embeds.  
>  
> Here's why it works. The contract is shared. The context is not. An agent that only sees Chapter 9 collisions can drag velocity tips correctly. An agent that sees the whole book invents half-finished chrome and ships uneven quality. Parallel specialists share utils and style from Chapter 4 — they don't share one overloaded prompt.  
>  
> Look at it directly. Chapter 1 orders of magnitude: a click highlights the row. Chapter 5 incline: drag the block and the angle tip. Chapter 9 elastic collision: drag v-one and v-two. Same Play. Same pause-on-drag. Same brutalist chrome.  
>  
> One agent on seventeen chapters is a volume metric. Specialist agents are a teaching metric.  
>  
> Your turn. Open two embeds from different chapters — say chapter six Atwood and chapter sixteen traveling wave. Drag a handle on each. If the interaction language matches, the parallel pass worked.

---

## Video 2 — Project update (book-wide)

**Title:** What shipped when Chapter 4's sim contract went book-wide  
**Intro line:** This is Charitha Sree Veluru in for Sanjana about what shipped when Chapter 4's sim contract went book-wide.

### Full VO script

> We had one chapter done well. The rest of the book still trained students not to click.  
>  
> So what shipped when Chapter 4's sim contract went book-wide?  
>  
> Before: decorative canvases, images missing next to sims, relative-uncertainty graphs where time and delta did nothing you could see. After: FigureWithSim keeps the OpenStax figure on the left and the live embed on the right. Every linked sim uses the Chapter 4 stack — HUD, canvas, readout, controls — with drag handles and Play.  
>  
> Here's why that matters. The sentence in the textbook creates a pointer. The UI has to resolve it with a tool that moves. Sharing Chapter 4's utils across chapters one through seventeen means bindCanvasInteraction and animationDt stay consistent. We unlinked decorative photo sims where a photograph teaches better than a fake diagram — and kept the embed code.  
>  
> Look at the book directly. Chapter 1: click orders of magnitude. Chapter 8 energy skate: drag the skater. Chapter 13: drag the satellite. Chapter 17 beats: scrub the waveform. Heights locked at 620. Light and dark theme still sync without wiping scrub state.  
>  
> Scope discipline from the Chapter 4 revert still holds: one contract done well, then multiplied — not seventeen brittle inventions.  
>  
> Your turn. Open any section from chapters five through seventeen. Find a FigureWithSim. Without scrolling away from the citation, drag once. If the handle moves and Play pauses, the book-wide pass landed.

---

## Regenerate

```bash
cd /home/velcherry/physics-vol-1 && npm start   # keep running on :3002

cd /home/velcherry/agreement_renewal_docs/video
source .venv/bin/activate
# Prefers ELEVENLABS_API_KEY; falls back to edge-tts if key is invalid
# VIDEO_TTS=edge python build_videos_bookwide.py   # force edge
python build_videos_bookwide.py
```

Outputs in `output/`:
- `physics_vol_1_bookwide_Charitha_Sree_Veluru_video1_16x9.mp4`
- `physics_vol_1_bookwide_Charitha_Sree_Veluru_video1_9x16.mp4`
- `physics_vol_1_bookwide_Charitha_Sree_Veluru_video2_16x9.mp4`
- `physics_vol_1_bookwide_Charitha_Sree_Veluru_video2_9x16.mp4`
