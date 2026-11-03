# Midjourney series — scope and plan

**Programme:** Lyrical Literacy (same as Suno).
**Status:** captures received and read. UI spec populated first-hand.
**Part 1 is SHIPPED** — 3:24, 4K, 0 BLOCKER — see `midjourney-part-1/PLAN.md`.
Parts 2, 3 and 4 are unblocked. Part 5 waits on three Editor captures.

The kit now carries `MjWindow`, `MjTile`, `MjFeedRow`, `MjChip`, `MjSeg`,
`MjRing`, `MjRingBox`, `MjIconImage` and `MjIconSliders` — all built from the
spec and all proven against a shipped part. Part 2 needs `MjActionRail` (the
six-row `Creation Actions` grid) and Part 3 needs `MjSettingsCards` (the 2x2
panel); everything else is in place.

Framework: `../../VIDEO-PIPELINE.md` (shared, tool-agnostic)
UI ground truth: `MIDJOURNEY-UI-SPEC.md` — **23 captures, all read directly**

---

## What the captures changed

The scaffolding plan was built on web research. Reading the screenshots
overturned five things in it. This is the same pattern as Suno — and the reason
`VIDEO-PIPELINE.md` section 8 exists.

| The plan assumed | The captures show |
|---|---|
| Sections: Create, Organize, Explore, Personalize, **Chat**, Tasks | **No Chat.** Explore, Create, Edit, Organize, then AESTHETICS (Personalize, Moodboards, Style Creator), then COMMUNITY (Tasks) |
| A grid **of four** as a 2x2 quad | **One row of four**, with the prompt in a right rail beside it |
| "upscale, vary and download" as the core actions | A **six-row action grid**, plus a hidden-by-default menu holding Pan, Zoom and Remix |
| A linear settings panel | A **2x2 grid of four cards, twelve controls** |
| An image tool | **Video is first-class.** `Animate` is on every hover, `Animate Image` is in every rail, and three of the twelve settings are video settings |

Two whole surfaces were missing from the plan entirely: **Style Creator** (its
own section) and **video**. And the Editor is deeper than "inpaint" — it has
Move/Resize, Paint with Erase/Restore and a brush size, Smart Select, and Layers.

---

## Recommendation: five parts, not four

Four parts cannot hold this surface without cutting something a volunteer needs.
Video alone is a body beat that did not exist in the old plan.

| Part | Title (working) | Body beats | Est. |
|---|---|---|---|
| 1 | **Your First Image** | access · the sidebar · the imagine bar · type and submit · the three progress states · the rail beside your row · hover | **3:20 SHIPPED** |
| 2 | **Writing The Prompt** | the seven documented elements · subject and medium · environment and lighting · colour and mood · composition · a real prompt scored · what to leave out | **3:16 SHIPPED** |
| 3 | **What To Do With One You Like** | the opened view · Vary vs Upscale · Rerun and HD · Use Style / Use Prompt · More Options · Animate · the options menu | **3:02 SHIPPED** |
| 4 | **The Settings Panel** | four cards · Aspect Ratio · Stylization · Weirdness and Variety · Model and Raw · Speed and Stealth · the two video settings | **3:23 SHIPPED** |
| 5 | **Getting The Same Look Twice** | the attach panel’s four slots · the `P` switchboard · Moodboards · Personalize · Style Creator · which to reach for | **2:59 SHIPPED** |
| 6 | **The Editor, And Where Your Work Lives** | three ways in · Move / Resize · Paint and transparency · Smart Select · Submit Edit · Organize and getting files out | **2:56 SHIPPED** |

**COMPLETE — six parts, 18:58 of finished runtime.** All 3840x2160, all 0 BLOCKER,
`verify_all.py` clean across the set including the continuity chain.

### Nothing outstanding

Every part is shipped. All six are 3840x2160, all 0 BLOCKER, `verify_all.py`
clean across the set including the continuity chain, and each part has its own
`check_beats.py` and `FACTCHECK.md`.

The remaining capture gaps are all NARROW and none of them blocks anything
already shipped — they are recorded in `MIDJOURNEY-UI-SPEC.md` so a future
edit cannot quietly fill them by inference:

- the **pin** and **heart** rail-header icons (2 of 4 resolved)
- the `Copy` and `Report` submenu contents
- the **sign-in screen** itself
- what `Rate More Images` opens, and the ranking interface
- a created or applied **Style Creator** style (the workspace has none)
- inside the Editor: the `sparkle` icon · a second layer · `Restore` in
  action · a resolved Smart Select selection · the finished results of an edit

### Previously needed, now closed

**Part 5** — one capture: a **moodboard opened**. The index is captured;
what is inside one is not.

**Part 6** — three captures: the **Editor with an image loaded** (only the
empty state exists), **Smart Select or Move/Resize mid-action**, and any
**download format choice** if one exists at all. `options.png` shows
`Download Image` as a single immediate action with no submenu, so as far as the
evidence goes there is no format step — which is itself the answer to
"how do I get the file out".

Also uncaptured and therefore undepicted: the **pin** and **heart** rail-header
icons, and the `Copy` / `Report` submenu contents.

### Why prompt-writing is Part 2

It was not in the original five-part plan at all — a real gap, raised by the
author on 2026-09-07. It sits at 2 because **teaching dials before words is
backwards**: varying a vague prompt returns four vague variations, and no
stylize value fixes an unclear subject.

Placing it here cost a re-cut of Part 1, which had already shipped a spoken
promise that Part 2 was the action rail. That was the author’s call, made with
the cost stated. Part 1’s BHTF was re-locked and three beats re-rendered:
BHTF (narration), B04 (two rail cards reading “Part 4”/“Part 3”) and B07 (the
Upscale handoff reading “Part 2”). Part 1 never states the series count, which
is the only reason this was possible at all — see `VIDEO-PIPELINE.md` §7.

**Its evidence is already in hand.** The captures contain four real prompts from
this workspace (undead wolf, vampire mother, vampire boy, graveyard zombie) that
all share one ten-slot skeleton. Part 2 needs **no new screenshots**.

**Why Part 5 stays its own part.** Consistency is the highest-value area for this
audience — a storybook or a song series needs the same character and the same
look across many images. Midjourney has **four separate systems** for it
(references, moodboards, Personalization, Style Creator) all reachable from one
`P` dropdown. Folding that into another part would repeat the Suno Part 3 squeeze.

**Why video is not its own part.** `Animate` sits in the image rail, and its
settings sit in the settings panel. Splitting it out would mean teaching the same
two surfaces twice. It closes Part 2 instead.

> **Part 1 must not state the number.** Suno Part 1 said "the first of three
> training videos"; it shipped, it was spoken, and it then forced a cramped
> Part 3. Midjourney Part 1 says "this series" and nothing more until the count
> is locked. Recorded in `VIDEO-PIPELINE.md` section 7.

---

## The beat budget

You lifted the 3:00 cap, so these are sized to what the content needs rather than
to a ceiling. From measured Suno bookend costs:

| Slot | Cost |
|---|---|
| B00 cold open | ~16s |
| B01 BLUF | ~17s |
| BVDT verdict | ~18s |
| BHTF recap + next-part tease | ~17s |
| BOUT outro | ~3s |
| **bookend subtotal** | **~71s** |

```
16 + 17 + (6 x 18) + 18 + 17 + 3  =  179s  =  2:59
16 + 17 + (7 x 18) + 18 + 17 + 3  =  197s  =  3:17
```

**Six body beats is the design point** (~3:00); seven where a part earns it
(~3:17). That sits between Suno Part 2 (3:09) and Part 1 (3:57) — comfortably
inside the register, and no part runs long for its own sake.

---

## Settled

**Kicker:** `LYRICAL LITERACY - MIDJOURNEY TUTORIAL PART N` on every scene.
Channel `claude-hai-lyrical` is reused as-is — it already exists in
`runtime/qc/brand_labels.json`, so GATE L passes with no new registration.

**Access:** identical to Suno. Fellows join the Humanitarians AI Discord, then at
midjourney.com choose the **Discord** sign-in option. A genuine series callback —
a volunteer who watched Suno Part 1 already knows the move — stated **once,
mechanically**, with no selling and no pricing on screen.

The captures confirm volunteers land inside the shared **humanitarians.ai**
organisation profile rather than a personal account. Worth one clause in Part 1:
what you make is visible to the team.

**Version numbers:** never on screen, never spoken. The settings panel's version
dropdown renders as a control with no value, and the `Help us improve V8` row is
omitted from every mockup. See `MIDJOURNEY-UI-SPEC.md` section 4.

**Pricing:** not taught. No plan, price or GPU-hour figure. The one number that
may appear is **200 points** to unlock a Personalization profile — it is a
product mechanic on the card, not a price.

---

## Build notes for the kit

`sunoKit.tsx` is the chassis and is not Suno-specific, but Midjourney needs a new
window component because **the product is light, not dark**:

- **`MjWindow`** — light app chrome: sidebar with the two small-caps section
  labels, the imagine bar, the header cluster. Every beat in every part uses it.
- **`MjActionRail`** — the six-row `Creation Actions` grid. Part 2 leans on it for
  five beats; build it once, from the spec. This is the `sunoAdvancedPanel` lesson.
- **`MjSettingsCards`** — the 2x2 settings grid. Part 3's spine.

The accent red-orange sits in the same family as `CLAUDE.SPARK #D97757`, so the
cream page and the product read as one design rather than two. Watch the reverse
of the Suno trap: **light cards on the cream page are near-invisible to Gate V**
(`INK_DELTA = 28`). Every Midjourney window needs a dark border or a dark header
strip to register as ink. See `VIDEO-PIPELINE.md` section 4.

---

## Still needed before some parts can be authored

**Part 1 is fully unblocked.** So are Parts 2, 3 and 4.

**Part 5 is partly blocked** — the Editor is captured only in its empty state:

1. The **Editor with an image loaded**, tool column visible
2. The Editor **mid-action** — a paint/erase selection on the canvas, or Smart Select
3. The **download control expanded**, showing any format or size choices

Without 1 and 2 the Editor beats would have to depict an interface I have not
seen, which is exactly the failure this pipeline is built to prevent. Part 5 can
be planned now and authored when they land.

**Optional, would improve Part 4:** a **moodboard opened**, showing what is inside
one. The index view is captured; the interior is not.

**Not needed:** the sign-in screen. Part 1 states the Discord route in the voice
over a Claude-style card rather than recreating a login page — a screen nobody
needs taught, and one I have no capture of.
