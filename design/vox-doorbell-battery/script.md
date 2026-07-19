# Why a Perfect AI Model Killed the Doorbell — vox-explainer script

Source card: `books/embedded-ai/youtube/video-ideas.md` Candidate 01
Source chapter: `books/embedded-ai/chapters/01-chapter-when-ai-meets-constrained-hardware.md`
Card exclusions honored: no Target A/B cost comparison, no edge-vs-cloud four
reasons, no FPU-emulation detail. One device, one cascade, power is the punchline.

~12 beats, ~105 s estimated. Accents: dusty blue `#5B7B9C` vs terracotta
`#D35F43` (non-partisan content pair), golden highlighter as annotation voice.
Isotype mark: square.

---

**B01 · STILL·ai·kenburns** — cold open, suburban doorbell in November light
> In late twenty nineteen, a smart doorbell that promised six months on a single charge started dying in forty-eight hours. Thousands of them. All at once.

**B02 · CARD** — title
> This is the story of how a machine-learning model that worked — killed the product it shipped in.

**B03 · COMPOSITE·ai·hold** — doorbell plate + firmware-update chips
> The hardware hadn't changed. The battery hadn't changed. Three weeks earlier, a firmware update had quietly added person detection: a neural network, running on the doorbell itself.

**B04 · DOCUMENT·own·annotate** — designed "integration test report" prop sheet, highlighter ticks each line on cue
> And the team had done their homework. Model accuracy: tested. Runs on the processor: confirmed. Fits in memory: confirmed. Every box on the checklist, checked.

**B05 · GRAPHIC** — budget waterfall, bar one
> Here's what the checklist missed. Shipping AI onto a battery is a cascade of three budgets. Budget one: memory. This model fit. Pass.

**B06 · GRAPHIC** — budget waterfall, bar two
> Budget two: time. Operations divided by processor speed — a couple of seconds per look. For a doorbell, acceptable. Pass.

**B07 · COMPOSITE·ai·hold** — doorbell plate + awake/asleep timeline strip (assembly plane)
> Budget three, nobody ran. Every look holds the processor awake — and seconds of thinking, times looks per minute, is a duty cycle. The fraction of its life spent awake.

**B08 · GRAPHIC** — current arithmetic, two magnitudes
> Awake is expensive — thousands of times the current of sleep. A few seconds of inference every thirty, and the average draw jumps from microamps to milliamps.

**B09 · GRAPHIC** — waterfall bar three misses the target line
> That's the murder weapon. A battery sized for a sleeping device now feeds one that's awake a tenth of the time. Six months becomes two days.

**B10 · GRAPHIC** — isotype count-up, returned units
> Twelve thousand doorbells came back in the first month. By December, the feature was rolled back. Deleted.

**B11 · COMPOSITE·ai·hold** — dead doorbell plate, verdict chips
> Here's the uncomfortable part: nothing failed. The model was accurate. The hardware ran it perfectly. The system did exactly what it was designed to do. The design was wrong.

**B12 · CARD** — kicker / endcard
> Before a model ships onto a battery, run three budgets: memory, latency, power. The third one is the one that kills.
