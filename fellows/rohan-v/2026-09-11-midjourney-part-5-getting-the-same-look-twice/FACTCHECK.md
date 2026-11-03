# MIDJOURNEY PART 5 — fact check

Every claim, on screen or in the voice, with its source.

**Two evidence standards, kept separate.** Product UI facts come from captures
only. Craft guidance would come from Midjourney's docs — this part needs almost
none, because the four systems are UI, not technique.

Sources: `add image to prompt.png` · `Moodboards tab.png` · `Moodboards tab
2.png` · `Moodboards tab 3.png` · `Personalize tab.png` · `Personalize tab
2.png` · `Style creator tab.png` · `explore tab - personalize.png`. All read
first-hand. Recorded element-by-element in `../MIDJOURNEY-UI-SPEC.md` §8.

---

## 1. Claims and sources

### B02 — the attach panel

| Claim | Source |
|---|---|
| The add-image icon opens four slots | `add image to prompt.png` |
| `Style reference` — "Use the style of an image" | Same, verbatim |
| `Image Prompts` — "Use the elements of an image" | Same, verbatim |
| `Attach to prompt` and `Animate` are the other two | Same |

The look-versus-contents distinction is drawn from those two verbatim strings.
The *phrasing* of the contrast ("one borrows the look, the other the contents")
is ours.

### B03/B04 — moodboards

| Claim | Source |
|---|---|
| The hero and both sublines | `Moodboards tab.png`, verbatim |
| Board names incl. `moodboard #280` | Same — unnamed boards get a number |
| Three ways to add | `Moodboards tab 2.png`, product labels + copy |
| `Set as Default` / `Use in Prompt` | Same |
| Hover a tile for a bin | `Moodboards tab 3.png` |

**"Focused moodboards give you consistency; diverse ones let you explore the
frontier of creative possibilities"** is Midjourney's own line, shown in
quotation marks and attributed on the card. It is not presented as our advice.

**Set as Default = everything next, Use in Prompt = once** is our reading of
the two labels. The labels are captured; that gloss is inference from plain
English, and it is the one interpretive step in the part.

### B05 — personalization

| Claim | Source |
|---|---|
| Heading and the "unspoken details" passage | `Personalize tab.png`, verbatim |
| The master switch reads `Personalization Off` | Same |
| A profile unlocks at **200 points** | `Personalize tab 2.png` — three locked cards read `Continue ranking to unlock: 0 of 200 Points`; the unlocked one reads `200 points` |
| Points come from ranking | Same — the button is `Add Rankings` |
| The active profile is marked `Default` | Same |

The 200 is read off the capture and lives in `MJ_PERSONAL.unlockPoints`, so the
figure the voice states and the figure the card renders cannot diverge.
`check_beats.py` fails the build if they do.

### B06 — Style Creator

| Claim | Source |
|---|---|
| Type a prompt, hit Start, pick what matches | `Style creator tab.png` — the vendor's own subline, verbatim |
| The page reads `No styles found` | Same |
| Recent prompts display `--ar 3:2` / `--ar 2:3` | Same — first-hand corroboration of the parameter syntax Part 4 taught as dials |

### B07 — the `P` dropdown

| Claim | Source |
|---|---|
| A master On/Off governs everything, and ships Off | `explore tab - personalize.png` |
| Two collapsible sections: Profiles, Moodboards | Same |
| Moodboards are listed by name, no thumbnails | Same |
| Style Creator is **not** in this dropdown | Same — it is absent from the capture |

---

## 2. Deliberately NOT claimed

| Not claimed | Why |
|---|---|
| **Any version number** | The product labels these `V8 Profiles` and `Global V7 Profile`. Both render stripped, per `VIDEO-PIPELINE.md` §7. Same call as Part 4's `8.2` dropdown. `check_beats.py` fails on either versioned form. |
| **What the ranking interface looks like** | `Rate More Images` is captured as a button; what it opens is not. The part says you rank images and never shows the screen. |
| **A finished or applied Style Creator style** | The capture reads `No styles found`. B06 teaches the flow and says out loud that nobody here has built one. The checker blocks "finished style" / "applied style". |
| **What `Copy` or `Report` submenus contain** | Not captured (Part 3's options menu). |
| Any price, plan or credit figure | Register rule, checked by script. |
| The number of videos in the series | Checked by script. |

---

## 3. Deliberate visual simplifications

| Product | Ours | Why |
|---|---|---|
| The moodboard grid is **masonry** | A grid of squares | `MjTile` is square-only. Building a second, non-square art renderer would risk it drifting from `MjTile`'s look across five parts. The beat's point — many pictures sharing a look — survives squares. The narration never claims masonry. |
| Board previews are real images | Seeded abstract tiles | REBUILD LAW: no screenshot is composited into any frame. |

---

## 4. Register compliance

| Rule | Status |
|---|---|
| B00 opens "Hi, I'm Rohaan from Humanitarians AI" | checked by script |
| Full name spoken exactly once, in BOUT | 1 occurrence, checked |
| No pricing, no promotion | checked |
| Series count never stated | checked |
| Every `MjL5*` scene carries the Part 5 kicker | checked |
| No cue resolves with under 1.8s left | checked |

**`check_beats.py`: 0 blockers, 1 warning.**

The warning is `use` in B04 — unavoidable, because `Use in Prompt` is the
product's own button label.

### Narration fixes made before audio lock

| Was | Now | Why |
|---|---|---|
| "Personalization is different again" | "**Personalize, in the sidebar,** is different again" | Part 4's tease promises the *sidebar label*. `verify_all.py`'s continuity check caught that Part 5 only ever said "Personalization", which is not what a volunteer hunts for. |
| B05 ended on "it ships switched off" | Off stated *before* the points | Its cue resolved at 0.94, leaving the card 1.2s. Reordered the narration and the rail cards together. |

---

## 5. Outstanding — needs your ears

1. **`Rohaan`** in BOUT.
2. **`use`** in B04 — "two ways to use the board". Verb, but it is a heteronym.
3. **"moodboard two eighty"** in B03 — spelled as words so Kokoro does not read
   digits, but worth confirming it lands as intended.
