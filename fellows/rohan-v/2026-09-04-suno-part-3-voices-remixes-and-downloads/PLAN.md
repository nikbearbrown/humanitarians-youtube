# PART 3 — "What You Bring In, and What You Do With What Comes Out"

**The finale.** Part 1 says *"the first of **three** training videos"* — shipped
and spoken. Everything Part 2 promised lands here.

**Target runtime:** ~3:28 (12 beats). Part 1 ran 3:56, Part 2 3:09.

**Status: fully unblocked.** All six requested captures received and read.

---

## The promise this part keeps

Part 2's BHTF, already shipped:

> "Part 3 covers the features around it — adding your own voice to the mix, the
> Sounds tab for effects and loops, the Inspo button, and what to do with a track
> once you have one you like."

| Promised | Delivered by |
|---|---|
| Adding your own voice to the mix | B03 |
| The Sounds tab | B04 |
| The Inspo button | B02 |
| What to do with a track once you have one | B05 · B06 · B07 · B08 |

---

## What the new captures changed

The six screenshots did not just fill gaps — they **overturned the assumed
model**, and one of the corrections lands on Part 1.

### 1. Remix and Edit do not open dialogs. They reopen the Advanced panel.

Choosing any Remix or Edit action loads the track into the **Advanced Create
panel** as attached **Audio**, with a mode dropdown set to what you picked. The
whole final act happens in the panel Part 2 already taught — a genuine payoff
rather than a new surface to learn. That reframes the last four beats.

### 2. `Extend` is under **Edit**, not Remix — and it is not a menu item.

The Audio-mode dropdown has two groups:

- **REMIX** — make something new *from* this song: Cover · Mashup · Sample ·
  Inspo (Pro)
- **EDIT** — change *this* song: Extend · Crop · Remove Section · Reverse ·
  Speed · Edit instruments (Pro) · Edit vocals (Pro) · Replace section (Pro) ·
  Fade in (Pro) · Fade out (Pro) · Add stem (Premier)

That distinction — *new thing from it* vs *change to it* — is the clearest
teaching frame in the whole part, and it came straight off the capture.

### 3. Extend has a real interface

Not a length preset. The waveform splits into a magenta **`KEEP`** region and a
hatched **`RECREATE`** region, with `Extend from  01:45.0` and `Select All`. You
drag the boundary to choose where the continuation begins.

### 4. Download tiers, verified

`MP3 Audio` (free) · `WAV Audio` **Pro** · `Get Stems` **Pro** · `Video` **Pro**.

### 5. The Create button has two states

Muted dark when idle; a **warm orange→magenta gradient** when armed. The spec
previously said "never a gradient" — corrected.

---

## ⚠ This corrects a claim already shipped in Part 1

Part 1 B08 tells viewers:

> "The three-dot menu on each card is where the actions sit: **Extend** to add
> more length, **Remix or Edit** to generate a variation, and Download to save
> the MP3."

and renders a menu reading `Extend` · `Remix / Edit` · `Download` · `Share` ·
`Move to Trash`, with Extend described as **"+15s or +30s"**.

Measured against the capture, four things are wrong:

| Part 1 says | Reality |
|---|---|
| `Extend` is a top-level menu item | It is inside **Edit ▸**. A volunteer opening the menu will not find it. |
| `Remix / Edit` is one item | Two separate submenus with **different purposes** |
| Extend adds "+15s or +30s" | **Invented.** Real Extend is a KEEP/RECREATE split with an "Extend from" timestamp |
| Menu has 5 items | Ten: Remix ▸ · Edit ▸ · Publish · Share ▸ · Download ▸ · Manage ▸ · Add to Queue · Add to Playlist · Song Radio · Move to Trash |

The "+15s or +30s" detail came from web research, not a capture — the same
secondhand-evidence failure as the "Custom tab". It is the last such claim in the
series.

**Recommended fix (~15 min):** rewrite B08's menu line, correct the `MENU` array
in `SunoL1SongCards.tsx`, then re-lock audio → align → sync_cues → re-render B08
→ recut. Awaiting your call; Part 3 is built either way.

---

## Beat table

| Beat | Act | Scene | Est. |
|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | 16s |
| B01 | BLUF — what you bring in, what you do with what comes out | `SunoL3Bluf` | 18s |
| B02 | The attach row: `+ Audio` · `+ Voice` · `+ Inspo` | `SunoL3Attach` | 20s |
| B03 | Create a Voice — record or upload, and the four rules | `SunoL3Voice` | 20s |
| B04 | The Sounds tab — effects, loops, one-shots | `SunoL3Sounds` | 18s |
| B05 | The `⋯` menu — ten actions, and where each leads | `SunoL3Menu` | 18s |
| B06 | Remix vs Edit — a new song *from* it, or a change *to* it | `SunoL3RemixEdit` | 20s |
| B07 | Extend — KEEP and RECREATE | `SunoL3Extend` | 19s |
| B08 | Download — MP3 free, the rest on Pro | `SunoL3Download` | 17s |
| BVDT | Verdict — the whole series on one card | `ClaudeVerdictArtifact` | 20s |
| BHTF | Series close | `ClaudeComposerAsk` | 19s |
| BOUT | Outro | `ClaudeTitleOutro` | 3s |

**Estimated ~3:28.** Actual comes from Kokoro at audio lock.

---

## Scene briefs

**`SunoL3Bluf`** — two columns: IN (the attach row) and OUT (the `⋯` menu),
with the Advanced panel between them as the thing both connect to.

**`SunoL3Attach`** — the panel's attach row. `+ Audio` opens its
Browse/Upload/Record dropdown; `+ Voice` and `+ Inspo` open as modals. Note
`+ Inspo` disappears once audio is attached — worth showing, it explains a
disappearing button.

**`SunoL3Voice`** — the `Create a Voice` modal, **Beta** badge included, with
Record / Upload Audio / Select from library and the four tip cards. The 10-second
minimum is the one hard rule.

**`SunoL3Sounds`** — the Sounds tab. Its collapsible is labelled **"Advanced
Options"**, not "More Options" — do not copy Part 2's label. Type (One-Shot /
Loop) · BPM · Key.

**`SunoL3Menu`** — the `⋯` menu rendered in full, ten items, submenu carets
visible. The teaching point is the shape, not memorising it: four submenus lead
somewhere, six act immediately.

**`SunoL3RemixEdit`** — the two groups side by side. REMIX makes a new song from
this one; EDIT changes this one. Pro/Premier badges shown as they appear, without
editorialising about plans.

**`SunoL3Extend`** — the panel in Extend mode: the KEEP/RECREATE waveform split
and the "Extend from" timestamp. Callback: this is the Part 2 panel with audio
attached.

**`SunoL3Download`** — the Download submenu. MP3 is the unbadged one; WAV, Stems
and Video carry Pro.

**New primitive:** `SunoModal` — a centred modal over a dimmed window. Four beats
need one. Same build-it-once logic that made `sunoAdvancedPanel` pay off.

**Kicker:** every `SunoL3*` scene passes
`kicker="LYRICAL LITERACY · SUNO TUTORIAL PART 3"`.

---

## Series-finale duties

**BVDT** recaps the *series*, not the video: sign in → describe → the Advanced
panel → what you bring in → getting the track out.

**BHTF** replaces the "Part N tease" with a genuine close — what a volunteer can
now do end to end, and where to go next.

---

## Still not captured — do not depict

`Share ▸` contents · `Manage ▸` contents · the `Publish` dialog · the Mashup /
Sample "pick another song" step · the **Studio** page. None are needed for the
beats above. Studio is plainly substantial and would be its own video.
