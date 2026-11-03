# MIDJOURNEY PART 1 — fact check

Every claim this video makes, on screen or in the voice, with its source.

**Source of record:** `../MIDJOURNEY-UI-SPEC.md`, built by reading all 23
captures in `../Midjourney Screenshots/` first-hand. Where a claim traces to a
specific capture, that capture is named.

**Nothing in this video comes from web research.** Four errors shipped in the
Suno series and every one of them came from a source that was not a screenshot.

---

## 1. Claims made, and where each comes from

### B02 — access

| Claim | Source |
|---|---|
| Access runs through Discord; join the HAI server, then choose Discord at midjourney.com | Stated by the author (project owner), 2026-09-06. Same route as the Suno series. |
| You land in the shared humanitarians.ai account | `Profile tab.png` — the profile is `humanitarians.ai`, `@humanitarians.ai`, with the 501(c)(3) bio. The sidebar account chip reads `humanitari…` on all 23 captures. |
| The account chip sits at the foot of the sidebar | Every capture. |

**Not depicted:** the sign-in screen itself. There is no capture of it. The beat
uses a Claude-language instruction card, and the `Continue with Discord` control
shown is a *generic* representation, not a recreation of Midjourney's button.

### B03 — the sidebar

| Claim | Source |
|---|---|
| Eight items, in three groups | `Create Tab.png` and 20 others. Counted per capture, one entry per line. |
| Four on their own: Explore, Create, Edit, Organize | Same. |
| Three under AESTHETICS: Personalize, Moodboards, Style Creator | Same — the section label is rendered in small caps in the product. |
| One under COMMUNITY: Tasks | Same. |
| Create is where you work; Organize is where things end up | `Create Tab.png` (the feed) and `Organize tab.png` (the full library with filters). |

**Verified by script.** `check_beats.py` reads `MJ_NAV_MAIN`,
`MJ_NAV_AESTHETICS` and `MJ_NAV_COMMUNITY` out of `midjourneyKit.tsx` and fails
if the narration's spoken numbers disagree with the arrays the scene renders.
This check exists because Suno shipped "four submenus" against a five-item menu.

### B04 — the imagine bar

| Claim | Source |
|---|---|
| Placeholder reads "What will you imagine?" | Every capture with an empty bar. |
| An add-image icon sits at the left of the bar | Every capture. Its panel is in `add image to prompt.png`. |
| A sliders icon sits at the right, inside the bar | Every capture. Its panel is `prompt settings.png`. |
| A `P` with a caret sits beside the bar | Every capture. Its dropdown is `explore tab - personalize.png`. |
| The search placeholder changes with the page | Four captured variants: `Search Images` (`Explore Tab + Prompt typed.png`), `Search Prompts` (`Organize tab.png`), `Search Profiles` (`Personalize tab.png`), `Search Moodboards` (`Moodboards tab.png`). |

### B05 — the three progress states

| Claim | Source |
|---|---|
| Four tiles appear as flat grey boxes | `In progress creation.png` |
| The first is badged `Starting…` | `In progress creation.png` — the badge is on tile one only. |
| They become blurred colour with a percentage | `In progress creation 2.png` — badge reads `15% Complete`. |
| Then they sharpen into four finished images | `grid of 4 finished.png`, `Create Tab.png` |
| One job returns four results, not four attempts | Structural: one prompt in the right rail serves all four tiles in the row, in every capture. |

### B06 — the rail beside a row

| Claim | Source |
|---|---|
| The prompt sits to the right of the row, in full | `Create Tab.png`, `grid of 4 finished.png` |
| Reference thumbnails appear beneath it | `In progress creation.png` — two thumbnails under the prompt. |
| Parameter chips record the job's settings | `In progress creation.png` (`stylize 150`, `weird 4`) and `Create Tab.png` (`ar 3:2`). |
| Different jobs carry different chips | The two captures above show different chip sets. |

### B07 — hover

| Claim | Source |
|---|---|
| Three buttons on hover: Vary Subtle, Vary Strong, Animate | `Create Tab.png` — the hovered tile shows exactly these three. |
| A trash icon top-left, a heart top-right | `Create Tab.png` |
| Upscale is **not** on the hover row | Same capture — it is absent. Upscale appears in the opened-image rail (`Image opened.png`). |

---

## 2. Deliberately NOT claimed

Things research or intuition suggested, which the captures did not support or
did not cover. Recorded so a later part does not quietly reintroduce them.

| Not claimed | Why |
|---|---|
| That the four results are a "grid of four" or a 2x2 quad | They are a **row of four**. The scaffolding plan assumed a quad; the captures disproved it. `check_beats.py` fails the build if "grid of four", "quad" or "2x2" reaches the narration. |
| That Upscale, Download or Remix are reachable from the feed | Upscale is in the opened rail; Remix is hidden behind `More Options` until switched on; no download control is captured at all. |
| Anything about the sign-in page's layout | Not captured. |
| Any model version number | `8.2` is visible in the settings dropdown and `Help us improve V8` in every image rail. `VIDEO-PIPELINE.md` section 7 forbids both on screen. The settings panel is not in this part, and the V8 feedback row is omitted from every mockup in the series. |
| Any pricing, plan name, credit balance or GPU-hour figure | Register rule. `check_beats.py` fails on a list of pricing terms. |
| The number of videos in the series | Suno Part 1 said "the first of three" and that forced a cramped Part 3. `check_beats.py` fails on a stated count and on "first of …". |
| That `stylize 150` or `weird 4` are good values | They are **that job's record**. The settings panel shows no numeric readouts at all, so presenting a number as advice would be inventing product behaviour. |
| That Midjourney is only an image tool | Video is first-class — `Animate` is on the hover row and named in B07. Its depth is Part 2. |
| A "Chat" section | The scaffolding plan listed one from research. **It does not exist.** |

---

## 3. On-screen text that is NOT a product string

Everything the product actually says is quoted verbatim. These are this
series' own words, written in the Claude annotation language, and no viewer
should mistake them for Midjourney UI:

- All annotation-card titles and bodies on the cream rails
- The three step labels in B01 ("You write one line", "It returns four",
  "You take one further")
- `always four` in B01 — a teaching chip in Midjourney's chip *style*, not a
  chip the product shows
- The B02 `Continue with Discord` control — generic, not a recreation
- Every spark line

Product strings reproduced verbatim: `What will you imagine?` · `Starting…` ·
`15% Complete` · `Today` · `Vary Subtle` · `Vary Strong` · `Animate` ·
`stylize 150` · `weird 4` · `ar 3:2` · `ar 1:1` · `Search Images` ·
`Search Prompts` · `Search Profiles` · `Search Moodboards` · `Midjourney` ·
the eight nav labels · `Aesthetics` · `Community` · `humanitari…`

**No screenshot is composited into any frame.** Every surface is a native
Remotion recreation (REBUILD LAW). Tile imagery is deterministic seeded
gradients — abstract stand-ins, never a claim about what Midjourney produced.

---

## 4. Register compliance

| Rule | Status |
|---|---|
| Host opens "Hi, I'm Rohaan from Humanitarians AI" | B00 — checked by script |
| Full name spoken exactly once, in BOUT | 1 occurrence — checked by script |
| Phonetic spellings preserved (`Rohaan`) | Deliberate for Kokoro G2P; not to be "corrected" |
| Access stated once, mechanically | B02 only, plus the verdict recap — checked by script |
| No promotion of the organisation's generosity | Nothing about what is provided; only the route in |
| Body beats 45–75 words | B01 55 · B02 64 · B03 52 · B04 66 · B05 55 · B06 69 · B07 74 |
| Recap + next-part tease, not "Your Turn" | BVDT + BHTF |

### Heteronyms rewritten before audio lock

`VIDEO-PIPELINE.md` section 6. The build cannot listen back, so these were
reworded rather than gambled on:

| Original | Shipped | Risk |
|---|---|---|
| "chips **record** the settings" | "chips showing what that job **ran with**" | /ˈrɛkərd/ vs /rɪˈkɔːrd/ |
| "that **lives** in the panel" | "that one **sits** in the panel" | /lɪvz/ vs /laɪvz/ — this exact trap shipped on Suno |
| "four **separate** attempts" | "four **independent** attempts" | adjective vs verb |
| "**Read** the chips" | "**Look at** the chips" | /riːd/ vs /rɛd/ |
| "**close** to this one or further from it" | "a small step from this image or a large one" | /kloʊs/ vs /kloʊz/ — caught by `check_beats.py` |

### Corrections made during the build

Both were caught by looking at rendered frames, not by any gate.

| Corrected | Was | Now |
|---|---|---|
| The control at the right of the imagine bar | Drawn as a **gear** | A **sliders** icon - three lines with knobs, per spec section 1 |
| The add-image affordance | The framed-picture **emoji**, which headless Chrome renders in a monochrome fallback font - a missing-character box at 46px | **Inline SVG**: a framed picture with a `+` badge |

The gear is the more serious of the two: `MIDJOURNEY-UI-SPEC.md` said "sliders"
from the first draft, and the scene contradicted the spec I had written from the
captures. It survived nine render passes because a wrong icon at 19px still
looks like an icon. B04 magnifies it to 64px, which is the only reason it
surfaced. Recorded in the spec so Part 3 - which walks the panel that icon
opens - cannot repeat it.

**Two ear-checks outstanding on the rendered audio:**
1. `Rohaan` in BOUT
2. `stylize` in B06 — an invented product word, and Kokoro has not been heard
   saying it
