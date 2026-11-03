# PART 2 — "The Advanced Tab"

**Goal:** a volunteer who can generate a song in Simple mode learns the entire
Advanced tab — every control, what it does, and when it actually matters.

**Target runtime:** ~3:11 (11 beats).

**Register:** internal volunteer training. See `../SERIES-PIPELINE.md` §7.

---

## Refocus (author's direction, 2026-08-30)

The first Part-2 build spent five of eight body beats on prompt-writing theory
(vague-vs-specific, style, mood, topic, iterate) and gave the Advanced tab a
single beat. That is backwards for an interface tutorial.

| | was | now |
|---|---|---|
| Prompt-writing craft | 5 beats (B02–B06) | **1 beat** (B02, inside the Styles box) |
| The Advanced tab | 1 beat (B07) | **5 beats** (B01, B03–B06) |
| Create a Voice · Sounds · Inspo | — | **moved to Part 3** |

The craft is not dropped — it is *relocated to where you actually type it*.
Genre / instruments / production is now taught as "what goes in the Styles box",
which is a better teaching frame than an abstract lesson: the viewer sees the
field while learning what to put in it.

---

## Beat table

| Beat | Act | Scene | Est. |
|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | 16s |
| B01 | BLUF — the panel, with the lid off | `SunoL2Panel` *(new)* | 19s |
| B02 | The **Styles** box — what it sounds like | `SunoL2Style` *(rebuilt)* | 20s |
| B03 | The **Lyrics** box — Write / Prompt / Instrumental + structure tags | `SunoL2Advanced` *(rebuilt)* | 21s |
| B04 | **More Options** — Exclude styles · Vocal Gender | `SunoL2Options` *(new)* | 18s |
| B05 | **Weirdness** and **Style Influence** | `SunoL2Sliders` *(new)* | 21s |
| B06 | Duration · Song Title · Save to · Create | `SunoL2Finish` *(new)* | 18s |
| B07 | Change one thing at a time | `SunoL2Iterate` *(reused)* | 18s |
| BVDT | Verdict — the whole panel | `ClaudeVerdictArtifact` | 19s |
| BHTF | Recap + Part 3 tease | `ClaudeComposerAsk` | 18s |
| BOUT | Outro | `ClaudeTitleOutro` | 3s |

**Estimated total ~3:11.** Actual comes from Kokoro at audio lock.

---

## Scene reuse

Four of the seven scenes built for the previous cut survive the refocus:

| Scene | Fate |
|---|---|
| `SunoL2Style` | **Rebuild.** Keep the genre → instruments → production ladder, but stage it inside the Styles box so it teaches the field, not an abstraction. |
| `SunoL2Advanced` | **Rebuild.** Was the whole-panel beat; now narrows to the **Lyrics** box — the three-way mode control plus structure tags. |
| `SunoL2Iterate` | **Reuse as-is.** Still correct, and it matters more now that there are sliders in play as extra variables. |
| `SunoL2Bluf` · `SunoL2Contrast` · `SunoL2Mood` · `SunoL2Topic` | **Retired.** These carried the prompt-theory beats that are being cut. Left on disk and in the scene index; simply not referenced by this beat sheet. |

New: `SunoL2Panel`, `SunoL2Options`, `SunoL2Sliders`, `SunoL2Finish`.

---

## The teaching arc (PROOF GATE)

- **Framework before detail** — B01 shows the whole panel as a labelled map, so
  every later beat lands in a place the viewer already has.
- **Walk the map in panel order** — B02 Styles → B03 Lyrics → B04 More Options →
  B05 sliders → B06 footer. The beat order *is* the top-to-bottom order of the
  real panel, so the video doubles as a reference.
- **Falsifiability** — B07. With this many controls, "change one thing at a time"
  stops being advice and becomes the only way to learn what anything does.
- **Bookends** — cold open → BLUF → body → verdict → recap/tease → title outro.

---

## Scene briefs

**`SunoL2Panel`** (B01) — the Advanced panel rendered whole, in `SunoWindow`,
with each section ruled and labelled as a map: Lyrics / Styles / More Options /
footer. Sections light in turn as the narration names the three questions
(what it sounds like · what it sings · how strictly it follows you). Ends holding
the complete labelled panel — the frame the rest of the video fills in.

**`SunoL2Style`** (B02) — the Styles box in focus. Tags type in as
comma-separated chips, accumulating genre → instruments → production, with a
`WaveBars` strip beside them tightening at each layer. Closes on the two rules:
name instruments, and stay positive.

**`SunoL2Advanced`** (B03) — the Lyrics box in focus. The
`Write / Prompt / Instrumental` segmented control actuates through all three
states, then Write is selected and `[Verse]` / `[Chorus]` type onto their own
lines with a lyric beneath each.

**`SunoL2Options`** (B04) — More Options expands. `Exclude styles` takes a tag
and a matching element visibly drops out of the result. `Vocal Gender` toggles
Male / Female / untouched.

**`SunoL2Sliders`** (B05) — the two sliders, both at their real 50% default.
Weirdness travels Safe → Chaos, Style Influence travels Loose → Strong, each with
a waveform responding to the move. States the practical rule for each.

**`SunoL2Finish`** (B06) — the footer: `Duration: Custom / Auto`,
`Song Title (Optional)`, `Save to… My Workspace`, then `Create` arming.

**`SunoL2Iterate`** (B07) — unchanged.

---

## Continuity with Part 1

| Part 1 promised | Delivered by |
|---|---|
| "When to leave Simple mode for Advanced" | B01 |
| "Advanced is where you control lyrics and song structure" (B05) | B03 |
| "Style, mood and topic vocabulary that actually shifts the output" | B02 — compressed, and now taught inside the Styles box |
| "How wording changes the sound you get back" | B02 |

**Worth flagging:** compressing five craft beats into one means "style, mood and
topic vocabulary" is covered more briefly than Part 1's tease implies. It is
still delivered — genre, instruments, production and mood vocabulary all appear
in B02 — but as a field lesson rather than a theory section. If that reads as
under-delivering on the tease, the fix is one line of Part 1's BHTF, not a
restructure here.

---

## Part 3 — scope

| Area | Detail |
|---|---|
| **Create a Voice** | Beta badge. Record / Upload Audio / Select from library. |
| **Sounds tab** | Sound effects, one-shots, loops. |
| **`+ Inspo`**, `+ Audio`, `+ Voice` | The attach row above the Lyrics box. |
| **After the track exists** | Extend, Remix, Personas, export/download. |
