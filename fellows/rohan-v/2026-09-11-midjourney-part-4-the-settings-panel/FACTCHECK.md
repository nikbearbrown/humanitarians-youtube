# MIDJOURNEY PART 4 — fact check

Every claim this video makes, on screen or in the voice, with its source.

**Two evidence standards, kept separate on purpose:**

- **Product UI facts** come from captures only. `VIDEO-PIPELINE.md` §8 exists
  because web research shipped four UI errors on the Suno series.
- **Documented figures** (parameter names, ranges, defaults) cannot be read off
  a screenshot at all. Their authority is Midjourney's own documentation,
  fetched 2026-09-07 and cited per claim.

---

## 1. The panel itself — from `prompt settings.png`

| Claim | Source |
|---|---|
| The sliders icon in the imagine bar opens this panel | `prompt settings.png` — the icon shows active/accent while the panel is open |
| It is a **2×2 card grid**, not a list | Same. Aspect Ratio and Aesthetics on top, Model and More Options beneath |
| Aspect Ratio holds a live preview, a three-way preset, and a slider | Same |
| The preview reads `1 : 1` and Square is the active preset | Same |
| Aesthetics holds exactly three sliders: Stylization, Weirdness, Variety | Same, in that order |
| **No numeric readout appears on any Aesthetics slider** | Same — the labels carry no values |
| Model holds Version (Standard/HD), a dropdown, and Raw (Standard/Raw) | Same |
| More Options holds Speed, Stealth, Video Resolution, Video Batch Size | Same, in that order |
| Defaults: Relax · Off · SD · 4 | Same — read off the active pills |

### Slider rendering — settled by cropping, not by memory

An earlier cut drew a dark fill on all four sliders. Cropping the capture
showed that is wrong:

| Slider | Real | Now |
|---|---|---|
| Aspect Ratio | Uniform light track, dark handle, **no fill** | no fill |
| Stylization | **Dark fill** from left edge to handle | fill |
| Weirdness / Variety | Handle hard left, no fill visible | fill (invisible at 0) |

Also corrected in the same pass: control rows are separated by **faint
hairlines** (between the three dials, above the Aspect Ratio slider, and
between every More Options row) which had been omitted entirely; and the handle
is a **solid dark dot**, not a dot with a white ring.

### The slider positions are themselves evidence

Stylization's handle sits ~10% along its track; Weirdness and Variety sit hard
left. Against the documented ranges that reads as **stylize 100** (the
documented default), **weird 0** and **variety 0** — a first-hand
corroboration of the docs rather than an inference from them.

---

## 2. Documented figures — Midjourney's docs, fetched 2026-09-07

| Claim | Source |
|---|---|
| Stylize is `--stylize` / `--s` | Parameter List |
| Its steps are Low 50 · Med 100 · High 250 · Very High 750, **Med default** | Stylize |
| Chaos/Variety is `--chaos` / `--c`, range **0 to 100**, default 0 | Chaos / Variety |
| Higher Variety strays further from the prompt | Chaos / Variety, paraphrased |
| Weird is `--weird` / `--w` | Parameter List |
| Aspect is `--aspect` / `--ar` | Aspect Ratio |

---

## 3. Deliberately NOT claimed

| Not claimed | Why |
|---|---|
| **Any range for Weirdness** | The docs search returned ranges for stylize and chaos but **not** for weird. A remembered "0–3000" is not evidence. The beat teaches direction only, and `check_beats.py` fails the build if a Weirdness figure other than zero appears. |
| **Any model version number** | The capture plainly shows `8.2`. `VIDEO-PIPELINE.md` §7 forbids it: a version dates the video and sources disagree. The dropdown is drawn as a real control with its caret and **no value**, and a rail card says why. `check_beats.py` fails on `8.x`, `V<n>` and `version <n>`. |
| That HD costs a specific amount | "Costs more of your allowance" is directional. No figure is captured or documented. |
| Any price, plan name or credit balance | Register rule. Checked by script. |
| That Stealth is available on every plan | Not captured. The beat says only what the toggle is and what Off means. |
| What the Aspect Ratio slider's endpoints are | The capture shows a handle mid-track with no numeric bounds. |
| The number of videos in the series | Suno Part 1 said "the first of three" and that forced a cramped Part 3. Checked by script. |

---

## 4. On-screen text that is NOT a product string

Product strings reproduced verbatim: `Aspect Ratio` · `Aesthetics` · `Model` ·
`More Options` · `Portrait` · `Square` · `Landscape` · `1 : 1` · `Stylization` ·
`Weirdness` · `Variety` · `Version` · `Standard` · `HD` · `Raw` · `Speed` ·
`Relax` · `Fast` · `Stealth` · `On` · `Off` · `Video Resolution` · `SD` ·
`Video Batch Size` · `1` `2` `4`

Everything else on screen is this series' own annotation language — every rail
card tag and body, every spark line, and the `— —` placeholder standing in for
the omitted version value.

**No screenshot is composited into any frame.** Every surface is a native
Remotion recreation (REBUILD LAW).

---

## 5. Register compliance

| Rule | Status |
|---|---|
| Host opens "Hi, I'm Rohaan from Humanitarians AI" | B00 — checked by script |
| Full name spoken exactly once, in BOUT | 1 occurrence — checked by script |
| Phonetic spellings preserved (`Rohaan`) | Deliberate for Kokoro G2P |
| No promotion, no pricing | Checked by script |
| Series count never stated | Checked by script |
| Every `MjL4*` scene carries the Part 4 kicker | Checked by script |

**`check_beats.py`: 0 blockers, 0 warnings.**

### Heteronyms reworded before audio lock

| Was | Now | Why |
|---|---|---|
| "A **live** square shows you…" | "A **preview** square…" | Kokoro read "live" as /laɪv/ when /lɪv/ was wanted on Suno; not worth the gamble in either direction |
| "Four **separate** systems" | "Four **different** systems" | adjective /ˈsɛpərət/ vs verb /ˈsɛpəreɪt/ |

`Part 4` / `Part 5` as spoken numerals are **exempt** from the bare-numeral
check: that exact form is spoken in three already-delivered videos, so flagging
it here would only make this part inconsistent with them. It stays on the
ear-check list.

---

## 6. Outstanding — needs your ears

I cannot hear the rendered audio. Two items:

1. **`Rohaan`** in BOUT.
2. **`Raw`** — used as a proper noun throughout B05. Kokoro should read it
   plainly, but it is a short word carrying a lot of the beat.
