# FACTCHECK — Suno, Part Two.

Every factual claim the narration or on-screen text makes, and how it was
verified. DOUBLE-CHECK LAW: nothing invented, nothing that will date, and the
recreated UI must match the live product (REBUILD LAW — rebuilt as Remotion
scenes, never screen-recorded).

Researched 2026-08-30. Sources at the foot.

## Interface claims

| # | Claim (beat) | Status | Note |
|---|---|---|---|
| 1 | Create has three modes: **Simple**, **Advanced**, **Sounds** (B07) | VERIFIED | Confirmed by the author's `Create.png` screenshot AND Suno's own site. Simple = one sentence; Advanced = full control over lyrics/style; Sounds = short sound effects, one-shots and loops (experimental). |
| 2 | The tab is **Advanced**, not "Custom" | VERIFIED — with a caveat worth knowing | Suno's product page says "Advanced mode"; the live UI says **Advanced**. But `help.suno.com` still says **"Custom mode"** in places — their docs lag a rename. Volunteers googling older guides will see "Custom". Same control. |
| 3 | Advanced gives a **Lyrics box** you write yourself (B07) | VERIFIED | Official: Advanced lets you "define lyrics, choose style, name the song, toggle instrumental/vocals". |
| 4 | Structure tags go in square brackets on their own line (B07) | VERIFIED | Official guidance: "Suno works best when you guide it with structure tags such as [Verse], [Chorus], and [Bridge]." Placement on its own line before the section is the documented convention. |
| 5 | Negatives read poorly in the **Styles** field (B03, BVDT card) | VERIFIED | `Exclude styles` is a real field, visible under **More Options** in `Advanced Tab 2/3.png`. Part 2 teaches only the principle (say what you want); the field itself moves to Part 3. Earlier draft said it was Pro/Premier-gated — the screenshots show no such gating, so that claim was dropped rather than repeated. |
| 6 | Simple mode writes the lyrics for you (B07) | VERIFIED | Simple generates lyrics, melody, arrangement and vocals from one description. |

## Prompting claims

| # | Claim (beat) | Status | Note |
|---|---|---|---|
| 7 | Be specific — genre, mood, instrumentation (B01, B02, B03) | VERIFIED | Official guidance says be "specific: mention genre, mood, keywords, and instrumentation", and warns against vague prompts like "happy pop song". |
| 8 | Naming instruments moves the result more than the genre word alone (B03) | VERIFIED (widely attested) | Suno is highly sensitive to named instruments — "fingerpicked nylon guitar" gives more to work with than "acoustic guitar". Stated as a tendency, not a guarantee. |
| 9 | Style splits into genre / instruments / production (B03) | VERIFIED as a teaching frame | Matches the documented components (genre, mood, instrumentation, vocal character, production, tempo). Our three-way split is a simplification of that list, not a claim about internal mechanics. |
| 10 | Negatives read poorly in the style field (B03) | VERIFIED | Negative instructions in the Style field are unreliable; the Exclude field is the official control. |
| 11 | Some words carry a genre with them — "epic" may bring cinematic drums (B04) | SOFTENED, deliberate | Phrased as *may*, not *will*. It illustrates a real tendency (genre-loaded adjectives) without asserting a specific deterministic behaviour. |
| 12 | Artist names are blocked; describe the sound instead (BVDT card) | VERIFIED | Suno blocks many artist names; musical descriptors are the documented workaround. |
| 13 | Change one dimension at a time (B06) | REASONING, not a product claim | This is experimental method, not a Suno feature. It is true by construction: if several variables change together, the result cannot attribute the improvement. Framed as method throughout. |

## Deliberately NOT claimed

Each of these was found in research and **excluded** because it will date or is
not authoritative:

- **Character limits** (e.g. "5,000 characters in the lyrics box"). Real, but
  stated per model version — exactly the kind of number that dates a video.
- **"5–8 tags is optimal", "past 10–12 tags contradict each other".** Widely
  repeated in third-party guides but not in official documentation. Not stated.
- **"Suno weights earlier words more."** Plausible and widely repeated; no
  authoritative source found. Not stated.
- **Model version numbers** (v4.5 / v5 / v5.5) and version-gated features such
  as voice cloning. The Create page shows a version dropdown; the video never
  names a version.
- **Slider values.** Weirdness (Safe↔Chaos) and Style Influence (Loose↔Strong)
  are real Advanced Options, but specific percentage guidance is community lore.
  Part 2 does not teach them; Part 3 may, from the official help article.
- **Plan gating** for Exclude Styles. Some sources say Pro/Premier only. Left
  unstated — plan tiers change, and this series does not sell the plan.


## The Advanced panel — verified inventory

Read directly off the author's screenshots (`Advanced Tab 1-4.png`), top to
bottom. This is the ground truth the B07 mockup is built against.

| Element | Detail |
|---|---|
| Top row | credits pill `♪ 2.5k` · segmented `Simple / Advanced / Sounds` (Advanced active) · model dropdown `v5.5 ⌄` |
| Attach row | `+ Audio` · `+ Voice` · `+ Inspo` |
| **Lyrics** (collapsible) | textarea, placeholder *"Start writing lyrics…"*; toolbar undo / redo / edit / library / expand; a `Help me write lyrics` button |
| **Styles** (collapsible) | textarea of **comma-separated tags** — the real example reads *"japanese city pop, african, clear vocal, ethereal synth, resonant"*; library / wand / shuffle icons; tag chips below |
| **More Options** (collapsible) | `Lyrics: Write / Prompt / Instrumental` · `Exclude styles` · `Vocal Gender: Male / Female` · `Weirdness` slider **50%** · `Style Influence` slider **50%** · `Duration: Custom / Auto` |
| Footer | `Song Title (Optional)` · `Save to… My Workspace` · `Create` |

**The teaching point this unlocked.** In Simple mode the description is one box.
In Advanced it **splits in two** — a Styles box for the vocabulary taught in
B03–B05, and a Lyrics box for the words. That is a cleaner and more accurate
framing of "moving to Advanced" than the earlier draft, which described only a
lyrics box and missed the Styles field entirely.

**Defaults now stated with confidence:** Weirdness and Style Influence both sit
at **50%** out of the box — visible in the UI, so this is observation rather
than lore. Part 2 does not teach them; Part 3 does.

## Deferred to Part 3 (author's call, 2026-08-30)

- **Create a Voice** — modal reads *"Create a Voice"* with a **Beta** badge:
  *"Add your voice to the mix. Record or upload a sample…"* with Record /
  Upload Audio / Select from library. Beta, so it will move; deferring is also
  the safer call for a training video.
- **More Options** in full: Exclude styles, Vocal Gender, Weirdness, Style
  Influence, Duration.
- The **Sounds** tab (sound effects, one-shots, loops).
- `+ Inspo`, Personas, extend / remix, and export.

## Continuity with Part 1

| Check | Status |
|---|---|
| Part 1 B05: "Advanced is where you control lyrics and song structure — that is Part 2" | **HONOURED.** B07 teaches the lyrics box and structure tags, rather than deferring to Part 3. An earlier draft of this beat sheet deferred it, which would have broken the promise. |
| Part 1 BHTF: "When to leave Simple mode for Advanced" | HONOURED by B07. |
| Part 1 BHTF: "How wording changes the sound you get back" | HONOURED by B02. |
| Part 1 BHTF: "Style, mood and topic vocabulary that actually shifts the output" | HONOURED by B03/B04/B05. |
| No "Custom" tab anywhere | Verified — Part 1 was corrected and re-rendered on 2026-08-30. |
| Worked example carried from Part 1 B06 | Yes — the acoustic folk / reading sentence runs through B02–B05. |
| Part 3 scope | More Options (sliders, Exclude, Vocal Gender, Duration) · Create a Voice · Sounds · extend/remix · export. The Advanced *fields* moved into Part 2 to honour Part 1's promise; the Advanced *controls* stay in Part 3. |

## Sources

- [Suno — How to Make a Song](https://suno.com/hub/how-to-make-a-song) (official)
- [Suno Help — How to Use: Creative Sliders](https://help.suno.com/en/articles/6141377) (official)
- [Suno Help — Suno Sounds](https://help.suno.com/en/articles/10625537) (official)
- [Suno Help — Making Music](https://help.suno.com/en/categories/550017-making-music) (official)
- [Suno AI Lyrics Tags guide](https://www.votemyai.com/blog/suno-ai-lyrics-tags-guide.html) (third-party, corroborating)
- [Suno Prompt Guide 2026](https://hookgenius.app/learn/suno-prompt-guide-2026/) (third-party, corroborating)
- [Suno Exclude Styles & Negative Prompts](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/negative-prompting-suno-v5-guide) (third-party, corroborating)
- Author-supplied screenshots: `youtube/Suno Screenshots/` — Create · Library · Home · Explore · Profile


---

# REFOCUS — 2026-08-30 (author's direction)

Part 2 is now a tour of the **Advanced tab in panel order**. Prompt-writing craft
is compressed from five beats to one (B02, taught inside the Styles box).
Create a Voice, the Sounds tab and the `+ Inspo` / `+ Audio` / `+ Voice` attach
row all move to Part 3.

That means Part 2 now teaches **More Options**, which the earlier cut explicitly
excluded. New claims, and how each is sourced:

| # | Claim (beat) | Status | Note |
|---|---|---|---|
| 14 | Lyrics has three modes: **Write / Prompt / Instrumental** (B03) | VERIFIED (UI) | Visible as a segmented control in `Advanced Tab 2/3.png`. |
| 15 | Write = you type the lyrics; Prompt = you describe them and Suno writes them; Instrumental = no vocals (B03) | **INFERRED — flagged** | No official doc defines "Prompt" mode by name. It follows from the labels plus Suno's own statement that Advanced lets you "write lyrics or let the AI create them based on your ideas", and from Instrumental's meaning in Simple mode. Narration states it in the plainest form that cannot be wrong; no mechanism is asserted. **Re-check if Suno documents this.** |
| 16 | `Exclude styles` keeps things out of the track (B04) | VERIFIED | Real field under More Options. The official control for unwanted elements; negatives in the Styles field are unreliable. |
| 17 | `Vocal Gender` is Male / Female, and optional (B04) | VERIFIED (UI) | Both options visible, neither preselected in the screenshots — so "leave it and Suno decides" is what the UI shows. |
| 18 | **Weirdness** and **Style Influence** both default to **50%** (B05) | VERIFIED (UI) | Both read `50%` in `Advanced Tab 3/4.png`. Observation, not lore. |
| 19 | Weirdness runs *safe to chaos*; Style Influence runs *loose to strong* (B05) | VERIFIED | Both ranges named in Suno's own help article on the creative sliders. |
| 20 | Raise Style Influence when a tag is ignored; raise Weirdness when results feel samey (B05) | REASONING from 19 | A direct restatement of what each slider controls, not a numeric recommendation. Still no percentage guidance — that remains community lore. |
| 21 | `Duration` is Auto by default, Custom available (B06) | VERIFIED (UI) | `Duration: Custom / Auto` with Auto active. |
| 22 | `Song Title` is optional; `Save to` selects a workspace (B06) | VERIFIED (UI) | Field literally reads "Song Title (Optional)"; `Save to… My Workspace`. |

## Still deliberately NOT claimed

Unchanged from the earlier pass — character limits, "5–8 tags", "Suno weights
earlier words more", model version numbers, and any **numeric** slider
recommendation. Teaching what a slider *does* is sourced; telling volunteers to
set it to a particular number is not.
