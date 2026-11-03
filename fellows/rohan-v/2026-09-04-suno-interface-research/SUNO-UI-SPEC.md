# SUNO UI SPEC — read off the screenshots, element by element

Single source of truth for every Suno mockup in this series. Built by reading
all 14 captures in `Suno Screenshots/` directly, not from memory or notes.

**Rule: nothing goes on screen in a video that is not in this file.** If a beat
needs an element that is not here, capture it first.

Last verified 2026-08-30. All 14 captures read directly, first-hand:
`Create.png` · `Advanced Tab 1-8.png` · `Sounds Tab.png` · `Home.png` ·
`Library.png` · `Explore.png` · `Profile.png`.

**Known gaps — nothing may be depicted for these until captured:**
the Share submenu contents · the Manage submenu contents · the Publish dialog ·
the Studio page · the Mashup / Sample "pick another song" step.

---

## 1. Global chrome (every page)

**Left sidebar**, top to bottom:

```
SUNO                       ← ALL CAPS, heavy, letterspaced, + panel-collapse icon
Home
Explore
Create
Studio
Library
Hooks
[orb] humanitarians        ← workspace chip, conic-gradient orb
                           ← visual gap
Earn Credits
Labs
Notifications
More
[ Upgrade to Premier ]     ← pinned at the foot
```

There is **no Search and no Radio** nav item. Search lives in the page header
(Home) or above the result list (Library / Create).

**Bottom player bar** spans the full width on every page:
shuffle · prev · play/pause · next · repeat, centred; scrub line beneath.
When a track is loaded the left end shows artwork + title + workspace name and
the right end gains: queue · thumbs-up · thumbs-down · comment · share · more ·
volume · info. Elapsed / total times flank the scrub bar.

---

## 2. Create page — shared header

```
[ ♪ 2.5k ]   [ Simple | Advanced | Sounds ]   [ v5.5 ⌄ ]
```

Credits pill left, three-way segmented mode control centre (active = light pill
on a dark track), model dropdown right. **There is no "Custom" tab.**

Right-hand column on Simple and Advanced — the workspace result list:

```
Workspaces  ›  My Workspace
[ Search ]  [ ▽ Filters (3) ]  [ ⇅ Newest ⌄ ]  [ ☰ List ⌄ ]  [ ‹ ] [ 1 ] [ › ]
<track rows>
```

**Track row:** square artwork with a duration badge in its lower-right corner ·
title · **magenta `v5.5` version badge** · truncated description · action icons
(play+count, thumbs-up, thumbs-down, comment, share) · `⋯` at the far right.
**No waveform in list rows.**

---

## 3. SIMPLE tab — panel order

```
[ + Audio ] [ + Voice ] [ + Inspo ]
┌─ Song Description ──────────────── [dice icon] ─┐
│  <textarea>                                     │
└─────────────────────────────────────────────────┘
[ + Lyrics ]                        [ ✓ Instrumental ]
Suggestions
[ turntable scratches ] [ heavy drop ] [ complex structure ] [ japanes… ]
┌─────────────── ♪ Create ───────────────┐   ← muted dark control, NOT a gradient
```

---

## 4. ADVANCED tab — panel order  ← **the Part 2 spine**

Verified across `Advanced Tab 1.png` (top) → `2.png` → `3.png` → `4.png` (bottom).

```
[ + Audio ] [ + Voice ] [ + Inspo ]

⌄ Lyrics                    [undo] [redo] [edit] [library] [expand]
   "Start writing lyrics…"
   [ ✎ Help me write lyrics ]

⌄ Styles                                              [library icon]
   "Enter style description"   ← real example: "japanese city pop,
                                  african, clear vocal, ethereal synth, resonant"
   [library] [wand] [shuffle]  [ acoustic folk ] [ fingerpicked guitar ] [ … ]

⌄ More Options                        ← SIX controls, in this order:
   1. Lyrics          [ Write | Prompt | Instrumental ]
   2. Exclude styles  <field>
   3. Vocal Gender ⓘ  [ Male | Female ]        ← neither preselected
   4. Weirdness ⓘ     [———●———]  50%           ← magenta handle
   5. Style Influence ⓘ [———●———] 50%
   6. Duration ⓘ      [ Custom | Auto ]        ← Auto active

   ♪ Song Title (Optional)
   📁 Save to…                    [ My Workspace ]

┌─────────────── ♪ Create ───────────────┐
```

### Two structural facts that are easy to get wrong

1. **Lyrics is ABOVE Styles.** Not the other way round.
2. **The `Write / Prompt / Instrumental` control is INSIDE More Options** — it is
   *not* attached to the Lyrics box at the top. So More Options must already be
   open for it to be visible.
3. **`Create` is pinned to the foot of the panel.** It sits at the same y in all
   four captures while the content scrolls behind it. It is not part of the flow.

### Slider semantics (from Suno's own help article)

- **Weirdness** — Safe ↔ Chaos. How conventional the result is willing to be.
- **Style Influence** — Loose ↔ Strong. How literally the Styles tags are followed.
- Both ship at **50%**. That is read off the UI, not inferred.
- No numeric recommendation is authoritative. Do not put one on screen.

---

## 5. SOUNDS tab

```
"Create short samples — effects, loops, and one-shots.
 Ready to drop into anything."                              [×]

⌄ Sound
   "Describe the sound you want"

⌄ Advanced Options            ← NOTE: "Advanced Options", not "More Options"
   Type ⓘ  [ One-Shot | Loop ]     ← One-Shot active
   BPM ⓘ   [ Auto ]
   Key ⓘ   [ Any ]

[🗑]  ┌────────── ♪ Create ──────────┐
```

---

## 6. The three attach buttons  (Part 3 material)

**`+ Voice`** → a **Voice** modal:
`My Voices | Favorites` tabs · Search · a highlighted
**`Create Voice`** row badged **New** ("Record or upload your voice") · then a
grid of saved voices with names and descriptions (e.g. "Zora — Traditional
nursery rhyme, simple chil…").

**`Create Voice`** → the **"Create a Voice"** modal, badged **Beta**:
> "Add your voice to the mix. Record or upload a sample and we'll use this
> content to influence how your generated songs sound." · "Drag an audio file here."

Buttons: `● Record` · `⬆ Upload Audio` · `❘❘❘ Select from library`.
Four tip cards beneath:
- *Sing in the style and language you want* — Pop, Rock, Rap or whatever you like.
- *A good microphone helps* — Your built-in mic works just fine, too.
- *Pick a quiet spot* — No roommates, no traffic, no barking dogs.
- *Record at least 10 seconds* — of your voice.

**`+ Inspo`** → a playlist picker:
> "Pick a playlist of your own songs to inspire your next creation.
> **Only your music will be used to shape the sound.**"

Search · `+ Create New Playlist` · your playlists with cover art and song counts
(Voices 42 songs · Untitled 1 song · LL1 0 songs · Humanitarians 10 songs).

**`+ Audio`** → a small dropdown, three items: **Browse** · **Upload** · **Record**.

Note: the attach row reads `+ Audio` `+ Voice` `+ Inspo`. When a track is already
attached, `+ Inspo` is not shown — the row becomes `+ Audio` `+ Voice` only.

---

## 7. Other pages

**Home** — hero "Let the music out" over a large rounded description box
("Describe the song you want to make") holding a `+` control, a dice button and
`Create`. Search pill top-right. Feature cards below with `NEW FEATURE` badges.

**Library** — page title `Library`, `+ Audio` and a trash icon top-right.
Sub-tabs: Songs · Playlists · Workspaces · Studio Projects · Voices · Lyrics ·
Styles · Cover Art · Hooks · Liked Hooks · History (Songs active, underlined).
Wide Search, then `▽ Filters (2)` · `⇅ Newest` · `Liked` · `Public` · `Uploads`.
Then track rows. Pagination floats near the foot.

**Explore** — full-width search ("Search for songs, playlists, creators, or
genres"). **Jump Back In**: Liked Songs · My Songs (n songs) · Recently Played.
**Staff Picks** with `See all ›` — a scrolling row of square cover art, each with
title, version badge and creator (some creators carry a verified check).
**Made in Suno Studio** with `See all ›` beneath.

**Profile / workspace page** — gradient banner; avatar orb, display name,
`@handle`, play count and like count; an `✎ Edit` button and a large play button.
Stat pills: `♪ n songs` · `n followers` · `n following`, with `⋯` and share at the
right. Then a `Songs ›` section as a grid of cover-art cards (title · version
badge · play count). Note older tracks carry older version badges (`v3.5`), so
the badge is per-track, not global.

---

## 8. Palette

Near-black, low-chroma greys. The **one** saturated colour is the magenta used
for version badges, slider handles and focus rings. The Create button is a muted
dark control. Purple gradients do not appear in this product — an early cut of
`sunoKit` invented them.

| token | value | use |
|---|---|---|
| `BG` | `#0A0A0B` | page ground |
| `CARD` | `#161618` | panels, description card |
| `CARD_HI` | `#1E1E20` | active nav pill, raised control |
| `BORDER` | `#26262A` | hairlines |
| `TEXT` / `MUTED` / `DIM` | `#FFFFFF` / `#9A9AA0` / `#6B6B73` | type |
| `ACCENT` | `#EC4899` | version badge, slider handle, focus ring |


---

## 9. The track `⋯` menu  ← **the Part 3 spine**

Identical in the Library list and the Create workspace list. On row hover a
**`Remix`** button also appears beside the `⋯`.

ONE ENTRY PER LINE. An earlier version of this block put Remix and Edit on the
same line, which made a line-count read "four submenus" when there are five. That
error reached a narration draft. Ten entries, split exactly 5 open / 5 act:

```
⌄ Remix           ▸     ← opens a submenu
⌄ Edit            ▸     ← opens a submenu
  Publish               ← acts immediately
⌄ Share           ▸     ← opens a submenu
⌄ Download        ▸     ← opens a submenu
⌄ Manage          ▸     ← opens a submenu
  Add to Queue          ← acts immediately
+ Add to Playlist       ← acts immediately
  Song Radio            ← acts immediately
🗑 Move to Trash         ← acts immediately
```

**5 open a submenu** — Remix · Edit · Share · Download · **Manage**.
**5 act immediately** — Publish · Add to Queue · Add to Playlist · Song Radio ·
Move to Trash.

**Download ▸** — `MP3 Audio` · `WAV Audio` **Pro** · `Get Stems` **Pro** ·
`Video` **Pro**. MP3 is the only unbadged option.

**Remix ▸** (from the Library capture) — `Cover` · `Reuse Prompt` · `Mashup` ·
`Sample this song` · `Use as Inspiration` **Pro** · `Voice` **Pro**.

### What actually happens when you pick one

Remix and Edit actions do **not** open a dialog. They load the track into the
**Advanced Create panel** as attached **Audio**, with a mode dropdown set to the
action you chose. This is why Part 2 is the prerequisite: the whole of Part 3's
final act happens in the panel Part 2 already taught.

Panel in that state:

```
[ + Audio ] [ + Voice ]              ← + Inspo drops off once audio is attached

┌─ Audio ───────────────── [ ⟳ Cover ⌄ ] [🗑] ─┐
│  ▶  Deckside Hornpipe   00:00 / 02:31        │
│  <waveform>                                  │
└──────────────────────────────────────────────┘

⌄ Lyrics   …                          ← pre-filled, e.g. "[Instrumental]"
┌──────────── ♪ Create ────────────┐  ← ARMED: warm orange→magenta GRADIENT
```

**In Extend mode** the waveform gains a split: a magenta **`KEEP`** region and a
hatched **`RECREATE`** region, plus `Extend from  01:45.0` and a `Select All`
button. You drag the boundary to choose where the continuation starts.

### The Audio-mode dropdown — the master list

Two groups. This is the definitive structure; the `⋯` submenus map onto it.

**REMIX** — make something new *from* this song
| item | description | tier |
|---|---|---|
| Cover | Recreate this song with a different genre or feel | — |
| Mashup | Blend with another song you pick | — |
| Sample | Use a slice of audio inside a new track | — |
| Inspo | Take loose inspiration — vibe, not specifics | Pro |

**EDIT** — change *this* song
| item | description | tier |
|---|---|---|
| Extend | Continue this song where it left off | — |
| Crop | Trim to a sub-section | — |
| Remove Section | Remove a section from the middle | — |
| Reverse | Play the audio backwards | — |
| Speed | Change playback speed | — |
| Edit instruments | Add or replace the song's instrumentation | Pro |
| Edit vocals | Add or replace the song's vocal performance | Pro |
| Replace section | Swap out a portion of the song | Pro |
| Fade in | Soften the start | Pro |
| Fade out | Soften the end | Pro |
| Add stem | Layer in a new stem (drums, bass, lead, …) | Premier |

**Extend is under EDIT, not Remix.** Three plan tiers appear: unbadged, `Pro`,
`Premier`.

### Track detail panel

Clicking a track opens a right-hand panel: artwork, a counts row
(plays · likes · comments · share), the title, `Add a Caption`, the full
description with a copy icon, and `Show More ⌄`.

---

## 10. The Create button has TWO states

| state | look |
|---|---|
| idle / empty panel | muted dark control (`SUNO.BTN_A`), music-note glyph |
| armed — audio attached or lyrics present | **warm orange → magenta gradient**, clearly the primary action |

Earlier spec text said "never a gradient". That was true only of the idle state
and is corrected here. The gradient is the armed state and appears in every
Extend / Remix capture.
