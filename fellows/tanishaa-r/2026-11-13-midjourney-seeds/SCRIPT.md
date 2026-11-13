# Why the Same Prompt Gives Four Different Images (script draft for approval, v1)

**Fellow:** Tanishaa · **Channel:** @HumanitariansAI · **Narrator:** Bella (Kokoro `af_bella`, an AI voice; disclosed on screen and aloud)
**Topic:** Midjourney seeds (Lyrical Literacy video content; Tanishaa's assigned Midjourney topic)
**Target length:** ~2¼ minutes (about 400 spoken words) · **Exports:** 16:9 at 3840×2160, plus a native 9:16 at 2160×3840
**Audience:** fellows and students new to Midjourney.
**Evidence:** no Midjourney screenshots (Tanishaa's choice). The worked example is a small real program, `demo/seed_demo.py`, labeled on screen as **a toy, not Midjourney**. Midjourney's behaviour is quoted from its own Seeds page.
**Sync rule:** on-screen text never runs on its own clock; key points appear exactly as Bella says them, and the screen is never left empty while she talks.

Each beat lists what's **on screen** first, then what Bella **says**.

---

### B00 · Cold open: the ask (~13 s)
**On screen:** The Claude app opens with the greeting "Hi, Tanishaa". The composer types: *"Why does the same Midjourney prompt give me four different images?"* The first lines of the answer appear. A small label reads "AI narration: Bella".
**Says:** "Hi, I am Tanishaa, and this video is about why the same Midjourney prompt gives you four different images. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved."

### B01 · The puzzle (~12 s)
**On screen:** The Midjourney logo, and one prompt card: *"a sunset over hills"*. Four different pictures drop in under it, one at a time. Key point on its word: **same prompt · four different images**.
**Says:** "Type one prompt into Midjourney and you get four images, and none of them match. Type the exact same prompt again, and you get four more. So where does the difference come from?"

### B02 · Every image starts as noise (~15 s)
**On screen:** A square of random static, like an old TV. Label: **every image starts here: random noise**. A small quote card: *Midjourney: a seed is "the random noise you see on a TV screen"*.
**Says:** "Every image starts as random noise, like static on an old TV. Midjourney's own guide describes it exactly that way. The model then cleans that noise up, step by step, into a picture that matches your prompt."

### B03 · Noise in, picture out (~15 s)
**On screen:** A three-step strip: **noise → rough shapes → picture**, with the prompt card feeding in from above. Caption: **schematic: the real model takes many steps**.
**Says:** "Think of it like this. The prompt decides what the picture is about. The noise nudges where things land: the shapes and the layout. Different noise, different picture, even with the same words."

### B04 · So four images means four noises (~12 s)
**On screen:** Four static squares side by side, each becoming one of the four pictures from B01. Label on its word: **4 images = 4 different starting noises**.
**Says:** "That's why one prompt gives you four images. Each one starts from a different patch of noise. And if you don't choose, Midjourney picks new random noise every time."

### B05 · The seed picks the noise (~16 s)
**On screen:** A number dial: **seed = 1234** feeding a static square. Range label: **any whole number from 0 to 4,294,967,295**. The prompt card gains **--seed 1234** at the end.
**Says:** "The seed is the number that picks which noise you start from. It can be any whole number up to about four billion. Add dash dash seed and a number to the end of your prompt, and you lock in the starting noise."

### B06 · Worked example, run for real (~22 s)
**On screen:** Real output from `demo/seed_demo.py`, labeled **toy generator, not Midjourney**. Three rows appear on their words:
1. **No seed:** four random seeds → four different landscapes.
2. **Seed 1234, twice:** two identical pictures, **0 pixels different**.
3. **Seed 1234, "sunset" → "forest":** the same hills and sun, new colours.
**Says:** "I tested this with a tiny toy generator, not Midjourney itself, but it works the same way. With no seed, four random seeds gave four different landscapes. With seed twelve thirty-four, twice, the two pictures matched pixel for pixel. Then I kept the seed and changed one word, sunset to forest. The hills stayed put. Only the colours changed."

### B07 · What it does in Midjourney (~15 s)
**On screen:** Two Midjourney-labelled cards: **same seed + same prompt → almost the same image** (with Midjourney's note *"99% identical in V8"*). Below: **find a seed: open the image → options → Copy → Seed**, each step appearing as Bella says it (v1.1).
**Says:** "In Midjourney, the same seed and the same prompt bring back almost the same image. Its own guide says about ninety-nine percent identical. To find an image's seed, open it, use the options button, and copy the seed."

### B08 · What a seed can't do (~24 s)
**On screen:** Two columns sort themselves as each item is spoken.
**Use a seed to:** run a controlled experiment · keep the seed, change one word.
**Don't use a seed to:** carry a style across prompts · rely on it in Turbo mode.
_(v1.1, after Tanishaa's pacing note: the items now repeat what Bella says, each on its words; the references card appears on "style references".)_
At the end, a card drops in: **Same look? Use style references, moodboards, personalization.**
**Says:** "So what is a seed good for? It's a control in an experiment: keep the seed, change one word, and you see exactly what that word did. But a seed can't carry a style or a character across different prompts, and it isn't reliable in Turbo mode. For a consistent look across assets, Midjourney recommends style references, moodboards, and personalization instead."

### B09 · Verdict (~11 s)
**On screen:** A Claude-style card titled "Midjourney Seeds" with three key findings, each on its words:
1. Every image starts as random noise.
2. The seed picks the noise; same seed, same image.
3. Same look across prompts? Use references, not seeds.
**Says:** "Three things to keep. Every image starts as random noise. The seed picks the noise, so the same seed brings back the same image. And for the same look across different prompts, use references, not seeds."

### B10 · Your turn (~16 s)
**On screen (v1.1):** The Claude mark and "Your turn.", the prompt shown whole in a "paste into Claude" card (no self-typing), and the three runs appearing as Bella names them: **1. one prompt, no seed · 2. a fixed seed, twice · 3. same seed, one word changed**, then **Run it: what stays, what moves?**
> *"Act as my tutor. Help me plan a Midjourney seed test: one prompt with no seed, a fixed seed twice, then the same seed with one word changed. Tell me what to look for, then help me explain what I see."*

**Says:** "Your turn. Ask Claude to plan a seed experiment with you: one prompt, no seed, then a fixed seed twice, then one word changed. Then run it yourself and see what stays and what moves."

### B11 · Outro (~4 s)
**On screen:** The title "Midjourney Seeds." in serif with a terracotta period, and @HumanitariansAI below it. (Title is short so it fits one line.)
**Says:** "Why the same prompt gives four different images. At Humanitarians AI."

---

## Fact-check notes
- **Midjourney Seeds page** (docs.midjourney.com, read 2026-11-13): a seed is like "the random noise you see on a TV screen"; it "only influence[s] the initial layout of noise"; whole number from 0 to 4294967295; if you don't choose, "a new random one every time"; "Seeds are 99% identical in V8.X"; best practice "Lock a seed when testing different elements … like having a control in an experiment"; "Not for Saving Styles … For consistency in your images, we recommend style references, omni references, and personalization"; not reliable in Turbo mode; may not hold across sessions; finding a seed: open the image → options → Copy → Seed.
- **Correction from the topic note:** "reusing the seed is how you keep a consistent look across assets" contradicts Midjourney's own page. Tanishaa chose the corrected ending (seed = same image; references = same look).
- **Handbook 6.7** lists the same consistency tools (style reference, moodboards, personalize, Style Creator).
- **Real (from `demo/seed_demo.py` → `demo/seed_output.json`, NumPy PCG64, toy generator):** seed 42 twice → identical noise; seed 1234 twice → identical pictures (0 pixels different); four random seeds → about 21% of pixels differ between pictures on average; seed 1234 with "sunset" → "forest" → identical layout, different colours.
- **B03 is a simplification:** in the real model the prompt also shapes the layout; the toy splits "layout from noise, look from words" to make the idea visible, and the screen says it's a toy.
- **"Four images per job"**: handbook 6.1 ("Midjourney gives you four images") and glossary ("Job: one generation. It produces four images.").
