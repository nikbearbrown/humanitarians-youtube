# Learning Brutalist: Getting to Know the Tools (script draft for approval, v2)

**Fellow:** Tanishaa · **Channel:** @HumanitariansAI · **Narrator:** Bella (Kokoro `af_bella`, an AI voice; same voice as What Is RAG, disclosed on screen and aloud)
**Type:** Video 2, progress update (Handbook 7.2) · **Target length:** ~1¾ minutes (about 290 spoken words) · **Exports:** 16:9 at 3840×2160, plus a native 9:16 at 2160×3840
**Look:** same Claude cream palette and HAI corner mark as What Is RAG, so the two read as a pair.
**Changed from v1:** the topic is now learning Brutalist and its tools (Tanishaa's request), not weeks 1–2 of the fellowship.

Each beat lists what's **on screen** first, then what Bella **says**.

---

### B00 · Opening line (~13 s)
**On screen:** The Claude app greeting "Hi, Tanishaa". The composer types: *"How does Brutalist actually make a video?"* Label: "AI narration: Bella".
**Says:** "Hi, I am Tanishaa, and this video is about learning Brutalist, the toolkit Humanitarians AI fellows use to make videos, and the tools that come with it. The voice you're hearing is Bella, an AI narrator reading a script Claude drafted and I approved."

### B01 · What Brutalist is (~16 s)
**On screen:** A five-step pipeline that lights up left to right: **Beat sheet → Audio (the clock) → Visuals → Checks → Video**.
**Says:** "Brutalist builds a video in steps. Every video starts as a beat sheet, one entry for each moment. The narration is generated first, and its measured length becomes the clock that every picture is timed to."

### B02 · Setting it up (~17 s)
**On screen:** A setup checklist ticking: **Python ✓ · Node ✓ · ffmpeg ✓ · Bella and Onyx voices ✓**, then **LaTeX ✗** with a small tag *"only needed for math equations"*. Footnote: *No Homebrew: everything lives in one micromamba environment.*
**Says:** "Setting it up was my first lesson. My Mac didn't have the usual developer tools, so Claude Code installed everything into one self-contained environment. The setup check came back ready, except LaTeX, which only matters for math equations."

### B03 · The tools (~20 s)
**On screen:** Four cards appear one at a time, each on its spoken word: **Claude Code** runs the build · **Kokoro** local AI voices · **Remotion + Manim** scenes written as code · **ffmpeg** joins the beats.
**Says:** "Then I learned what each piece does. Claude Code runs the commands and writes the scene code. Kokoro makes the voice, on my own laptop, for free. Remotion and Manim draw every graphic from code, and ffmpeg stitches the beats into one film."

### B04 · The checks (~15 s)
**On screen:** Two gates: **GATE T: type size, contrast, overlap: PASS** · **GATE V: every frame reviewed: 0 blockers**.
**Says:** "A video isn't done until it passes two automatic checks. One measures the text: is it big enough, readable, not overlapping. The other looks at every frame for layout problems."

### B05 · First test: What Is RAG (~18 s)
**On screen:** Real frames from *What Is RAG?*, landscape and vertical side by side, tagged **3840×2160** and **2160×3840**. A callout on the vertical: *Own layout, fewer words. Not a crop.*
**Says:** "My first real test was a two-and-a-half-minute explainer called What Is RAG. One surprise: the vertical version isn't a crop. Each scene needed its own portrait layout with fewer words, so the text stays readable on a phone."

### B06 · What only I could catch (~19 s)
**On screen:** The RAG "use it when / skip it when" beat, with a timeline bar showing items arriving **after** the words. Then the fix: each reveal snaps to its spoken word. Caption: *"Claude can't watch a video. I can."*
**Says:** "The biggest lesson: the checks passed, but when I watched the preview, the list appeared after Bella said each item. Claude can't watch a video, so catching that was my job. We fixed it by timing each reveal to the measured word."

### B07 · Takeaway (~14 s)
**On screen:** A card: **Learning a new toolkit?** 1. Run the setup check first · 2. Push one small video all the way through · 3. Watch every preview yourself.
**Says:** "If you're learning a toolkit like this, start with the setup check, push one small project all the way to the end, and watch every preview yourself. A passing check doesn't mean it works."

### B08 · Outro (~5 s)
**On screen:** The title "Learning Brutalist." in serif with a terracotta period, and @HumanitariansAI below it.
**Says:** "Learning Brutalist. At Humanitarians AI."

---

**Fact check:** Setup facts (micromamba environment, no Homebrew, setup check ready except LaTeX) come from the 2026-11-05 install. The pipeline and tools come from brutalist.art/HOW-TO.md and README.md. Every RAG fact (4K sizes, GATE T PASS, GATE V 0 blockers, native portrait layouts, the ~1:52 sync fix) comes from youtube/what-is-rag/BUILD-LOG.md.
**Not shown:** no terminal output with file paths from Tanishaa's Mac, no private messages, names or emails.
**Next, after approval:** build the beat sheet, generate Bella's audio, render a preview cut for Tanishaa to watch.
