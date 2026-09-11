# PROMPT — "Use the Tool First."

The brief, and how each constraint was resolved.

## Constraints given

Rohan, 2026-09-10:

> I also want to make a video for this weeks update. This week i only worked on
> the midjourney videos. [...] This involved working on midjourney myself,
> researching prompting techniques, taking screenshots of the interface.
> planning the video. [...] aim for a total length of 2 mins for each video.
> [...] I want the best animations and visuals and everything should be of the
> best quality. [...] Follow the same framework as last week. dont skip any
> steps.

| # | Constraint | How it was resolved |
|---|---|---|
| 1 | ~2:00 total | 122.10s measured. First pass came in at 1:51; B04 was expanded rather than padding elsewhere. |
| 2 | 16:9 and 9:16, both 4K | 16:9 at 3840×2160; 9:16 re-rendered natively at 2160×3840 through THE ONDA CHECK, never cropped. |
| 3 | Cover the Midjourney work specifically | All four body beats are Midjourney. Nothing else from the week appears. |
| 4 | "using midjourney myself, researching, screenshots, planning" | B02 is built entirely from that sequence — the plan, the screenshots, and what changed between them. |
| 5 | Best visuals and animation quality | Three purpose-built components, each with one designed event; the strike-through in B02 is bespoke motion authored for this beat. |
| 6 | Same framework as last week, no steps skipped | Full pipeline run: library-first search → beat sheet → audio → 4K landscape → native portrait → visual QC on frames → 12 docs + both QC sheets → GitHub → `./art drive`. |

## Constraints inherited from earlier feedback

| Source | Rule | Applied |
|---|---|---|
| Week-01 review | Start and end screens identical across all videos | `ClaudeComposerAsk` / `ClaudeTitleOutro`, unchanged |
| Week-01 review | Mention Humanitarians AI in intro and outro | B00 opens with it, B05 closes with it |
| Week-02 review | Name must be phonetic in narration only | `Row-Haan VeeJayKooMaar` in `narration_text`; on-screen spelling correct |
| Week-02 review | 9:16 must be a native re-render, never a letterbox | `shorts.py` + three new `916` siblings |
| Week-02 build | Round, don't truncate, when formatting durations | B01's total reads 18:59, not 18:58 |
| Week-02 build | Props a component indexes into must be in `defaultProps` | every array prop registered in `Root.tsx`, not just in the zod schema |
| Toolkit doctrine | Library-first — search before authoring | three searches, three different outcomes, all recorded in PROMPTS.md |

## The judgement call worth recording

`MedhavyTwoColumnCard` came back from the library search with **exactly** the
prop shape B02 needed. Doctrine says a hit is a lead, not a verdict — so the
file was opened. Its fixed 900px centred card, top-centre spark line and
missing eyebrow belong to a different layout grammar, and adapting it would
have changed how it renders for the medhavy channel.

Two defensible options: extend the shared component and accept the blast
radius, or build purpose-built and accept the duplication. Purpose-built won,
because a progress reel is not entitled to change another channel's look. The
rejection is documented in the new component's header so the next person does
not repeat the search.

## What "2 minutes" bought

Six beats: one opener, four body beats, one outro. Enough for receipts, the
correction, the asset, and the commitment. Not enough for a fifth body beat,
which is why the prompting-technique research is folded into B02's corrections
column rather than given a beat of its own.
