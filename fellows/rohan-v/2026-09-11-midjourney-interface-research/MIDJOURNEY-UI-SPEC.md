# MIDJOURNEY UI SPEC — read off the screenshots, element by element

Single source of truth for every Midjourney mockup in this series. Built by
reading all 23 captures in `Midjourney Screenshots/` directly — not from memory,
not from web research, not from an agent's summary.

**Rule: nothing goes on screen in a video that is not in this file.** If a beat
needs an element that is not here, capture it first.

Last verified 2026-09-07. All 29 captures read first-hand (`options.png`, `Moodboards tab 2/3.png` and `Editor.png` + `editor 2/3/4.png` added 2026-09-07).

**Known gaps — nothing may be depicted for these until captured:**
- **what the PIN and HEART rail-header icons do.** Two of the four are now
  resolved: the **list** icon opens the 9-item options menu (§3, from
  `options.png`), and **download** is unambiguous from its glyph *and*
  corroborated by the menu's own `Download Image` entry. The **pin** and
  **heart** remain uncaptured. Note the menu contains `Spotlight Image` behind
  a pin glyph, which SUGGESTS pin = spotlight — but suggestion is not
  evidence, and nothing may claim it until a capture shows it.
- the `Copy` and `Report` submenu contents (the two carets in the options menu)
- the **sign-in screen** and the Discord option on it
- what `Rate More Images` opens, and the ranking interface itself. The
  200-point mechanic is captured; the screen where you earn the points is not.
- a **created or applied Style Creator style**. `Style creator tab.png` shows
  `No styles found`, so the flow is evidenced and a finished style is not.
- inside the Editor: what the `sparkle` icon does · a second layer · `Restore`
  in action · a RESOLVED Smart Select selection (both Erase buttons are only
  ever seen disabled) · the finished four results of an edit (the capture stops
  at `Submitting...`)
- any **download format / resolution / tier choice**. `options.png` shows
  `Download Image` as a single immediate action with no submenu, so as far as
  the captures go there is no format step. Do not invent one by analogy with
  Suno, which did have MP3 / WAV / Stems / Video.
- the Surveys section under Tasks (heading only)

---

## 0. Look and feel

Midjourney's web app is **light**, not dark. This is the opposite of Suno and it
changes every mockup decision.

| token | value | where |
|---|---|---|
| page | near-white, faintly warm | app background |
| card | white | panels, cards, the imagine bar |
| border | pale warm grey hairline | card edges, dividers |
| ink | near-black | headings, labels |
| muted | mid grey | placeholder text, inactive segment labels |
| **accent** | **red-orange** | active nav pill, active segment, links, progress chips |

The accent is a **red-orange** — the same family as CLAUDE.SPARK `#D97757`,
which is a gift: the house palette already sits next to this product. Active
states are accent text on a **pale tinted pill**, not a saturated fill.

Corners are generously rounded. Type is a geometric sans. There is **no dark
chrome anywhere** and **no gradient on any control** — the only gradients in the
whole product are the two illustrative cards on the empty Editor canvas.

---

## 1. Global chrome (every page)

**Left sidebar**, top to bottom — ONE ENTRY PER LINE:

```
Midjourney              <- wordmark, sentence case, regular weight, NOT all caps
Explore
Create
Edit
Organize
AESTHETICS              <- small-caps section label, muted
Personalize
Moodboards
Style Creator
COMMUNITY               <- small-caps section label, muted
Tasks
[avatar] humanitari...  <- account chip pinned at the foot, name truncated, then a dot-menu
```

**Four top-level items** — Explore, Create, Edit, Organize.
**Three under AESTHETICS** — Personalize, Moodboards, Style Creator.
**One under COMMUNITY** — Tasks.
**Eight navigation items in total**, plus the account chip.

There is **no Chat item, no Subscribe item and no Help item** in the expanded
sidebar. Active item = accent text + accent icon on a pale tinted rounded pill.

**In the Editor the sidebar collapses to an icon-only rail** with `MJ` at the
top, the eight icons beneath, then help / bell / brightness / account at the foot.

### The imagine bar — present on every page

```
[image+]  What will you imagine?                              [sliders]
```

- Left: an **add-image** icon (a picture glyph with a `+`). Opens the attach panel (section 6).
  Rendered in the videos as inline SVG, never as an emoji: headless Chrome falls
  back to a monochrome font for the framed-picture glyph, which reads as a
  missing character at large sizes.
- Centre: placeholder **"What will you imagine?"**
- Right, inside the bar: a **sliders** icon — three horizontal lines with knobs.
  Opens the settings panel (section 5). **It is not a gear.** An early Part 1
  cut drew a gear here and it reached a render.
- When text is entered the bar grows into a multi-line textarea and gains a
  **scroll arrow pair** and a **send arrow** (paper-plane).

### The header cluster — right of the imagine bar

```
[folder]  |  [P v]  [bolt]  [speech]  [search: <placeholder>]
```

- **folder** — its own segment (Create / opened-image views only)
- **`P v`** — the Personalization switchboard, an italic capital P. Opens section 7.
- **bolt** — lightning glyph
- **speech** — speech bubble (Create view)
- **search** — **the placeholder changes per page**:
  `Search Images` (Explore) · `Search Prompts` (Organize) ·
  `Search Profiles` (Personalize) · `Search Moodboards` (Moodboards) ·
  `Search Styles` (Style Creator)

---

## 2. CREATE page — the core loop

The feed is grouped by date: **`Today`**, **`Yesterday`** — a plain heading, no rule.

**Each job renders as ONE ROW OF FOUR images** with a right rail beside it. It is
**not** a 2x2 quad. Four square tiles across, then the rail.

### The right rail beside each row

```
<full prompt text, wrapping, several lines>
[thumb][thumb]                 <- reference images used, if any
[ stylize 150 ] [ weird 4 ]    <- parameter chips, pale grey pills
```

On a job with no references: a single **`ar 3:2`** chip.
A video row carries a red **`Video`** badge before the prompt text.

### Progress states — the exact sequence

1. Four **flat grey tiles**, the first badged **`Starting...`** (accent text, pale pill)
2. Four **blurred colour previews**, badge now **`15% Complete`**
3. Four **finished sharp images**, no badge

### Hover on a finished tile

- **trash** top-left
- **heart** top-right
- a button row across the bottom: **`Vary Subtle`** · **`Vary Strong`** · **`Animate`**

Three hover buttons. Not four. Upscale is **not** among them.

A **`To Top`** pill floats at the top of the feed once scrolled.

---

## 3. Opened image — the action rail   <- the Part 3 spine

Clicking a tile opens: sidebar | **large image, centred** | **action rail** |
**vertical filmstrip** of every sibling image, far right.

A close **X** sits at the top-left of the rail.

### Rail header

```
Imagine   19h        [list] [download] [pin] [heart]
```

`Imagine` is the job type, `19h` its age, then four icons.
**On a video this reads `Video  20h`** and the download glyph gains an arrow.

### The list icon — the per-image options menu

From `options.png`, read first-hand. The list icon is the FIRST of the four
header icons; when open it shows active with a grey circle behind it.

ONE ENTRY PER LINE. A count is stated explicitly below, because a line-count
read off a code block is how "four submenus" reached a Suno narration draft
when the product had five.

```
Copy              >     <- submenu
Report            >     <- submenu
------------------------ visual divider
Spotlight Image
Make Private
Download Image
Search Image
Run batch as HD
Trash Image
Open in Discord
```

**9 items in total.**
**2 open a submenu** — Copy · Report.
**7 act immediately** — Spotlight Image · Make Private · Download Image ·
Search Image · Run batch as HD · Trash Image · Open in Discord.

**`Download Image` is a single action, not a format submenu.** This is a real
difference from Suno, whose Download opened MP3 / WAV / Get Stems / Video with
Pro badges. Nothing in this capture offers a format, a resolution or a tier for
the download, and nothing may be depicted that does.

Three items cross-reference material taught elsewhere in the series:
- `Run batch as HD` also appears as a row in the rail body above.
- `Make Private` is the per-image counterpart to **Stealth** in the settings panel.
- `Open in Discord` connects to the Discord sign-in route from Part 1.

The `Copy` and `Report` submenu CONTENTS are not captured. Neither may be
depicted.

### Rail body, top to bottom

```
<prompt text, scrollable>                    [+ use text]  <- chip on hover
[folder icon]
Creation Actions                              More Options
Vary        [ Subtle ]      [ Strong ]
Upscale     [ Subtle ]      [ Creative ]
More        [ Rerun                      ]   <- full width
HD          [ Run batch as HD            ]   <- full width
Use         [ Style ]       [ Prompt ]
Edit        [ Quick Edit ]  [ Open Editor ]
Animate Image  v                              Animate Manually
  Auto      [ Low Motion ]  [ High Motion ]
  Loop      [ Low Motion ]  [ High Motion ]
```

**Six labelled rows under `Creation Actions`** — Vary, Upscale, More, HD, Use, Edit.
**`Animate Image` is a separate collapsible below them**, holding **two rows** —
Auto and Loop, each offering Low Motion and High Motion.

Buttons are pale grey pills with dark text. No accent fill on any of them.

### On a VIDEO the rail body is shorter

```
<prompt text>
[source-image thumb]  [ 5.2s ]      <- the still it was animated from, plus duration
[folder icon]
Creation Actions                     More Options
More        [ Rerun                ]
Use         [ Start Frame ] [ Prompt ]
Extend Video  ^                      Extend Manually
  Auto      [ Low Motion ] [ High Motion ]
```

`Use` offers **`Start Frame`** instead of `Style`. `Extend Video` replaces
`Animate Image`. There is no Vary, Upscale, HD or Edit row.

### `More Options` — a visibility menu, not an action menu

It opens a checklist that controls **which rows appear in the rail**:

```
Vary            (checked)
Upscale         (checked)
Pan
Zoom
Remix
More actions    (checked)
Use in prompt   (checked)
```

**Seven entries. Four are checked by default** — Vary, Upscale, More actions,
Use in prompt. **Pan, Zoom and Remix are UNCHECKED**: they exist but stay hidden
until switched on. Checkmarks are accent-coloured. The menu is identical on video.

---

## 4. The `Help us improve V8` row — DO NOT DEPICT

A feedback row (`Help us improve V8 (?)` plus three face icons) sits between the
prompt and `Creation Actions`. It carries a **model version number**, which
`VIDEO-PIPELINE.md` section 7 forbids putting on screen. **Omit this row from
every mockup.** It is not a control a volunteer needs.

---

## 5. The SETTINGS panel — opened by the sliders icon   <- the Part 4 spine

**A 2x2 grid of four cards.** Not a linear panel, not a dropdown.

```
+- Aspect Ratio -----------------+ +- Aesthetics -------------------+
|  +-------+                     | |  Stylization  [--o----------]  |
|  |  1:1  |  [Portrait|Square|  | |  Weirdness    [o------------]  |
|  |       |          Landscape] | |  Variety      [o------------]  |
|  +-------+  [---------o------] | |                                |
+--------------------------------+ +--------------------------------+
+- Model ------------------------+ +- More Options -----------------+
|  Version    [ Standard | HD ]  | |  Speed            [Relax|Fast] |
|             [ 8.2          v ] | |  Stealth          [ On | Off ] |
|  Raw        [ Standard | Raw ] | |  Video Resolution [ SD | HD  ] |
|                                | |  Video Batch Size [ 1 | 2 | 4] |
+--------------------------------+ +--------------------------------+
```

**Twelve controls across four cards.**

**Aspect Ratio** — a live square preview reading **`1 : 1`**, a three-way segment
**Portrait | Square | Landscape** (Square active), and a continuous slider whose
handle sits centred for square. The preview box changes shape with the slider.

**Aesthetics** — three sliders, **no numeric readouts on the panel itself**:
`Stylization` (handle a short way in from the left),
`Weirdness` (handle hard left), `Variety` (handle hard left).

**Model** — `Version` as **Standard | HD**, then a **version dropdown**, then
`Raw` as **Standard | Raw**. Both segments default to Standard.

**More Options** — `Speed` **Relax | Fast** (Relax active) · `Stealth`
**On | Off** (Off active) · `Video Resolution` **SD | HD** (SD active) ·
`Video Batch Size` **1 | 2 | 4** (4 active).

Active segments are accent text on a pale tinted pill.

> **The version dropdown reads `8.2` in the capture. Render the dropdown as a
> control, but never show or speak the number** — `VIDEO-PIPELINE.md` section 7.

### Parameter chips are the panel's shorthand

Settings surface elsewhere as text: `stylize 150` and `weird 4` chips on the
Create rail; `--ar 3:2` and `--ar 2:3` beneath recent prompts in Style Creator.
So the `--` syntax **is** visible in the product and may be taught — sparingly,
as the written form of a panel control, never as the primary way to work.

---

## 6. Attach panel — opened by the add-image icon   <- the Part 5 spine

A wide panel drops beneath the imagine bar. **Four drop targets across the top:**

```
Attach to prompt     | Style reference   | Image Prompts    | Animate     [lock]
Edit or combine      | Use the style of  | Use the elements | Animate an
images, like "make   | an image          | of an image      | image
this car red" or
"put this hat on
this cat"
[Select images below]
```

**Four slots.** The first is active and shows a `Select images below` hint. A
padlock sits at the right end of the row.

Beneath: a dashed **`Upload a file or drop it here`** box on the left, then a
dense scrollable grid of your library images to pick from.

This one panel is where **style reference** and **image prompts** attach. There
is no separate "add reference" UI anywhere else.

---

## 7. The `P v` dropdown — the consistency switchboard

Opened from the header on **every** page:

```
Personalize                     [ On | Off ]
[ Rate More Images          ]   [ filter ]
Profiles                                  v
   Global V7 Profile              default
   Create Personalization profiles to teach
   Midjourney what you like.
   [ Create Profile             ]     <- accent outline button
Moodboards                                v
   icons
   moodboard #280
   bell the cat
   durer
   dit
   tldr
   ...
```

`Off` is the active segment in the capture. Two collapsible groups — **Profiles**
and **Moodboards** — so a single control governs both consistency systems.

---

## 8. PERSONALIZE page

Hero: two overlapping image cards captioned **`'A Person' with different
Personalizations`** with an accent refresh button, beside:

> **Teach Midjourney about what you find beautiful.**
>
> Inside every prompt are "unspoken" details. Midjourney tries to fill them in to
> make the image as compelling as possible for the entire community.
>
> But your tastes are unique! ... Making a Personalization profile helps Midjourney
> get to know you and shape images toward what you love.

Then a wide segmented control reading **`Personalization Off`**.

Then `All | Selected  |  Latest v  search` and **`New Profile`** on the right.

Then **collapsible profile groups by model generation**, each headed
`<N> Profiles  + New Profile` with a collapse caret.

**Profile card, unlocked:** a 2x4 mosaic of its images, then `Global V7 Profile`,
`200 points`, and **`Default`** in accent.

**Profile card, locked:** a flat grey card reading **`Continue ranking to unlock:
0 of 200 Points`**, then `Profile #88`, `0 points`, a dot-menu, and **`Add Rankings`**.

**200 points unlocks a profile.** That number is on the card and may be stated.

---

## 8. AESTHETICS — the four consistency systems   <- the Part 5 spine

All four are reachable from the `P` dropdown beside the imagine bar. Read
first-hand from `Moodboards tab.png`, `Moodboards tab 2.png`,
`Moodboards tab 3.png`, `Personalize tab.png`, `Personalize tab 2.png`,
`Style creator tab.png`, `explore tab - personalize.png` and
`add image to prompt.png`.

### 8.1 The attach panel — from `add image to prompt.png`

Opened by the add-image icon at the LEFT of the imagine bar. Four slots, in
this order, each with the product's own one-line description:

```
Attach to prompt   "Edit or combine images, like 'make this car red'
                    or 'put this hat on this cat'"      + [Select images below]
Style reference    "Use the style of an image"
Image Prompts      "Use the elements of an image"
Animate            "Animate an image"
```

**Four slots.** A padlock sits at the far right of the row. Beneath: an
`Upload a file or drop it here` dashed target on the left, then a dense grid of
this workspace's own images to pick from.

**`Style reference` vs `Image Prompts` is the distinction that matters** —
the *style* of an image versus the *elements* in it. Both phrases are the
product's own.

### 8.2 Moodboards index — from `Moodboards tab.png`

```
Define Your Vision. Visually.                    <- hero, verbatim
"When words aren't enough, Moodboards let you collect images to show
 Midjourney the aesthetic you want."             <- verbatim
"Focused moodboards give you consistency; diverse ones let you explore
 the frontier of creative possibilities."        <- verbatim
[ All | Selected ]  |  [ Latest v ]  [search]            [ + New Moodboard ]
<cards: a 4x2 preview mosaic + the board's name beneath>
```

Real board names seen: `icons` · `moodboard #280` · `bell the cat` · `durer` ·
`dit` · `tldr` · `moodboard #275`. Unnamed boards default to `moodboard #<n>`.

That second quoted line is the vendor stating the focused-vs-diverse tradeoff
itself. It is quotable and must be attributed, not paraphrased as our own.

### 8.3 A moodboard opened — from `Moodboards tab 2.png` / `3.png`

```
                     bell the cat                 <- name, inline-editable
[ <- Back ]     [ Set as Default ] [ Use in Prompt ]              [trash]

+-------------------+ +-------------------+ +-----------------------+
| Upload Images     | | Add from Link     | | Add from Creations    |
| "Upload images    | | "Add images from  | | "Select images from   |
|  from your        | |  around the web   | |  your creations to    |
|  computer to add  | |  to your          | |  add to your          |
|  to your          | |  moodboard."      | |  moodboard."          |
|  moodboard."      | |                   | |                       |
+-------------------+ +-------------------+ +-----------------------+

<masonry grid of the board's images; hover a tile -> trash icon top-right>
```

**Three ways to add** — Upload Images · Add from Link · Add from Creations.
**Two ways to apply** — `Set as Default` · `Use in Prompt`.
The grid is **masonry**, not uniform, and tiles keep their own backgrounds
(transparent checkerboard for PNGs with alpha).

### 8.4 Personalize — from `Personalize tab.png` / `2.png`

```
Teach Midjourney about what you find beautiful.   <- heading, verbatim
"Inside every prompt are 'unspoken' details. Midjourney tries to fill them
 in to make the image as compelling as possible for the entire community."
"But your tastes are unique! ... Making a Personalization profile helps
 Midjourney get to know you and shape images toward what you love."
        [ Personalization Off ]                   <- master switch
[ All | Selected ] | [ Latest v ] [search]            [ + New Profile ]

Profiles                       [ + New Profile ]                      ^
  <mosaic>  Global Profile          Default        200 points
  <locked>  Profile #88   ... [ Add Rankings ]     0 points
  <locked>  Profile #67                            0 points
  <locked>  Profile #65                            0 points
```

**A profile unlocks at 200 points**, earned by ranking images. A locked card
reads `Continue ranking to unlock: 0 of 200 Points`. The active one is marked
`Default` in accent. `Add Rankings` is how you earn points.

> **VERSION NUMBERS APPEAR HERE AND MUST BE OMITTED.** The product labels the
> section `V8 Profiles` (and `V7 Profiles` on an older capture) and the unlocked
> profile `Global V7 Profile`. `VIDEO-PIPELINE.md` §7 forbids a version number
> on screen. Render these as **`Profiles`** and **`Global Profile`**. This is the
> same decision already taken for the settings panel's `8.2` dropdown.

### 8.5 Style Creator — from `Style creator tab.png`

```
Style Creator                                     <- heading
"Type a prompt and hit start. Select images that match your vision.
 Your unique style evolves with each choice."     <- verbatim
[ <prompt, prefilled> ]  [ Start > ] [sliders]  [ P v ]
Have a direction in mind? Start with a style   [ Liked v ] [Search Styles]
                     No styles found              <- empty state
Or continue from a recent prompt
<cards: thumbnail + truncated prompt + `--ar 3:2` / `--ar 2:3`>
```

**This workspace has no saved styles** — the capture shows `No styles found`.
So the flow (type → Start → pick images) is evidenced, and **a finished style
being created or applied is NOT**. Nothing may depict one.

The recent-prompt cards display **`--ar 3:2`** and **`--ar 2:3`** as literal
text. That is first-hand corroboration of the parameter syntax the docs give.

### 8.6 The `P` dropdown — from `explore tab - personalize.png`

The hub. Everything above switches on here.

```
Personalize                              [ On | Off ]   <- Off active
[ Rate More Images        ^ ]  [ filter ]
--------------------------------------------------------
Profiles                                            v
   Global Profile                        default
   "Create Personalization profiles to teach Midjourney what you like."
   [ Create Profile                      ^ ]            <- accent
--------------------------------------------------------
Moodboards                                          v
   icons
   moodboard #280
   bell the cat
   durer
   dit
   tldr
```

**Two collapsible sections** — Profiles and Moodboards — under one master
On/Off. Moodboards are listed by name with no thumbnails. `Rate More Images`
and `Create Profile` both carry an external-link arrow.

**Not captured:** what `Rate More Images` opens · the ranking interface itself ·
the filter beside it · a Style Creator section in this dropdown (there is none
in the capture).


---

## 9. MOODBOARDS page

> **Define Your Vision. Visually.**
>
> When words aren't enough, Moodboards let you collect images to show Midjourney
> the aesthetic you want.
>
> Focused moodboards give you consistency; diverse ones let you explore the
> frontier of creative possibilities.

Then `All | Selected  |  Latest v  search` and **`New Moodboard`** on the right.

Then a grid of moodboard cards — each a **2x4 mosaic** of its images with the
board's name beneath (`icons`, `moodboard #280`, `bell the cat`).

---

## 10. STYLE CREATOR page

> **Style Creator**
> Type a prompt and hit start. Select images that match your vision. Your unique
> style evolves with each choice.

A prompt bar with an **accent `Start`** button, the sliders icon, and `P v`.

Then `Have a direction in mind? Start with a style`, `Liked v`, `Search Styles`.
Empty state: **`No styles found`**.

Then `Or continue from a recent prompt` — cards of thumbnail + truncated prompt +
the parameter string (`--ar 3:2`).

---

## 9. THE EDITOR   <- the Part 6 spine

From `Edit tab.png` (empty), `Editor.png`, `editor 2.png`, `editor 3.png`,
`editor 4.png`. All read first-hand. The Editor is the one surface where the
sidebar collapses.

### 9.1 Chrome

**The sidebar collapses to an ICON-ONLY RAIL**: `MJ` at the top, the eight nav
icons beneath, then help / bell / brightness / account at the foot. During a
submit one nav slot is replaced by an **accent circle with a job count**.

```
[add-image]  <prompt>            [sliders]  [ Submit Edit ]   [ P v ]
```

`Submit Edit` is **grey and disabled with an empty canvas** (`Edit tab.png`)
and **dark and enabled once an image is loaded**.

Right panel: `View All` · `+ New`, a **filmstrip** of this edit's results, then
at the foot `Export Edit` -> **`Download Image`** — disabled when empty or
mid-submit, enabled otherwise.

### 9.2 Two ways in, on an empty canvas

`Edit tab.png` shows the canvas holding two illustrated cards:

```
[link icon]   Edit from URL          ->
[upload icon] Edit Uploaded Image    ->
```

These are the only gradients anywhere in the product. A third route exists and
is captured elsewhere: **`Open Editor`** on the opened-image rail (§3).

### 9.3 The tool column — FOUR tools plus Layers

ONE ENTRY PER LINE. **Four tools. Layers is a panel, not a tool.**

```
Edit            [undo] [redo] [reset] [sparkle]     <- 4 icons, always visible
Move / Resize
Paint
Smart Select
------------------------------------- (gap)
Layers                          [+ Add]
   Layer 1   <thumbnail>                            <- accent border = selected
```

Only ONE tool is expanded at a time; the active one shows an accent icon and
accent label. All four collapse to a single title row when inactive.

**`Move / Resize` expanded** — `editor 2.png`:
```
Image Scale        100%     [-------------o]   <- handle at far right
Aspect Ratio       1 : 1
   [1:1]  3:4  2:3  9:16  1:2                  <- 1:1 spans both rows, active
          4:3  3:2  16:9  2:?
```
Hovering a preset shows a tooltip: **"Set aspect ratio to 1:2"**. In this mode
the canvas gains **square corner handles**.

**`Paint` expanded** — `Editor.png`:
```
[ Erase ]  [ + Restore ]        <- Erase active (dark fill)
Brush Size        100px   [o-----------]
```

**`Smart Select` expanded** — `editor 3.png`:
```
[ + Include ]  [ - Exclude ]    <- Include active (dark fill)
Erase Selection      (disabled)          [reset]
Erase Background     (disabled)
```
Clicking the canvas drops a small **accent `+` marker**. Both Erase buttons stay
disabled until a selection resolves.

### 9.4 The mechanic that matters

**Erasing produces TRANSPARENCY, not paint.** The erased region renders as the
transparent checkerboard, both on the canvas and in the `Layer 1` thumbnail.
You are cutting a hole, then describing what should fill it.

### 9.5 Submitting — `editor 4.png`

- The prompt bar carries a long **auto-generated description of the image**,
  ending with literal parameters: **`--stylize 150 --weird 4`**
- A **`Submitting...`** badge, accent, top-left of the canvas
- The filmstrip gains **four grey placeholder tiles with spinners** — an edit
  returns **four results**, exactly like an imagine job
- The whole tool column greys out; `Download Image` greys out
- `Layer 1`'s thumbnail is now the transparent mask

> **`--stylize 150 --weird 4` is a first-hand corroboration of three earlier
> parts at once**: parameters as literal prompt text (Part 2), the Stylization
> and Weirdness dials (Part 4), and the `stylize 150` / `weird 4` chips on the
> Create rail (Part 1). Same job, same numbers, three different surfaces.

### 9.6 Not captured

- what the `sparkle` icon in the `Edit` card does
- a second layer, or what `+ Add` produces
- `Restore` in action
- a resolved Smart Select selection (both Erase buttons are only ever disabled)
- the finished four results of an edit — the capture stops at `Submitting...`

---

## 10. ORGANIZE

From `Organize tab.png`, read first-hand.

Search placeholder: **`Search Prompts`**. The feed is a **dense grid with no
right rail** — seven tiles across — grouped by date with a `+` beside each
heading: `Today ⊕`, `Yesterday ⊕`.

### The Filters panel — SIX groups

ONE ENTRY PER LINE. All are checkboxes.

```
(ungrouped)     Spotlighted
                Liked
                Unrated
                In Trash
Media Type      Image
                Video
Type            Not Upscaled
                Upscales
Resolution      HD
                SD
Aspect Ratio    Square
                Landscape
                Portrait
Version         <version numbers>
```

**Six groups.** The first has no heading.

`Spotlighted` corroborates `Spotlight Image` in the options menu (§3) — the
same state, seen from two surfaces.

> **The `Version` group lists literal version numbers.** Per
> `VIDEO-PIPELINE.md` §7 the group is depicted with its heading and its
> checkbox shape, and its options genericised. Same call as the settings panel's
> `8.2` dropdown and Personalize's `V8 Profiles`.


---

## 11. TASKS page

> **Image Rankings**
> Help make Midjourney better by ranking images

**Three cards**, pale blue, each with a thumbs-up glyph and an arrow:

1. **Rank Image Aesthetics** — "Browse images and pick your favorites. Ranking
   images will also build your Personalization. The best 2,000 rankers each day
   will earn an extra Fast hour."
2. **Rank Images** — "Help train the aesthetic model by picking the image you
   find more beautiful in each pair."
3. **Curate Explore page** — "Help us find the best images for the Explore page.
   This will not change your Personalization. The best 2,000 rankers each day
   will earn an extra Fast hour." — carries an **`Earn Fast Hours!`** starburst.

A **`Surveys`** heading follows below.

**Ranking here is what earns the 200 points in section 8.** That causal link is
real and is why Tasks belongs beside Personalize in the same part.

---

## 12. EDIT page — the Editor

The sidebar collapses to icons. Layout: icon rail | tool column | canvas | right rail.

**Top bar:** the imagine bar, a **`Submit Edit`** button (grey/disabled when the
canvas is empty), then `P v`.

**Tool column** — cards, top to bottom:

```
+- Edit ---------------------+
|   undo  redo  reset  spark |
+----------------------------+
+- Move / Resize ------------+
+----------------------------+
+- Paint --------------------+
|  [ Erase ]  [ Restore ]    |   <- Erase active: dark fill, white text
|  Brush Size         100px  |
|  [-o---------------------] |
+----------------------------+
+- Smart Select -------------+
+----------------------------+
+- Layers            + Add --+
|    Add your first layer    |
+----------------------------+
```

**`Erase` is the one control in the whole product with a dark fill.**

**Right rail:** `View All` and `+ New` at the top; `Export Edit` and a disabled
**`Download Image`** at the foot.

**Empty canvas** shows two large gradient cards: **`Edit from URL`** (blue) and
**`Edit Uploaded Image`** (orange), each with an arrow. These are the only
gradients in the product.

---

## 13. ORGANIZE page

Date-grouped grids (`Today +`, `Yesterday +`) at a **denser tile size than
Create** — seven across — with a **Filters rail** on the right:

```
Filters                    v
[ ] Spotlighted
[ ] Liked
[ ] Unrated
[ ] In Trash
Media Type
  [ ] Image
  [ ] Video
Type
  [ ] Not Upscaled
  [ ] Upscales
Resolution
  [ ] HD
  [ ] SD
Aspect Ratio
  [ ] Square
  [ ] Landscape
  [ ] Portrait
Version
  [ ] ...
```

**Four loose checkboxes, then five labelled groups.** All unchecked by default.
The search placeholder here is `Search Prompts`.

---

## 14. EXPLORE page

Filter row: **`For You` · `Random` · `Hot` · `Top Day v` · `Likes`**, and on the
right **`Styles` | `Images` | `Videos`** with Images active in an accent pill.

Below: a masonry wall of community images. Search placeholder `Search Images`.

---

## 15. PROFILE page

Banner (`Set Banner Image`), avatar (`Set Profile Image`), the display name in
large white type over the banner with an edit pencil, `@handle` plus a YouTube
glyph, a bio paragraph, tabs **`Spotlight` · `Archive` · `Following`**,
`Random Profile` on the right, and a share icon.

The captured account is the shared **humanitarians.ai** organisation profile —
volunteers work inside it rather than in a personal account.
