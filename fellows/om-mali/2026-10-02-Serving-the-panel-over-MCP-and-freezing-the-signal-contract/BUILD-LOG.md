# BUILD-LOG — serving-the-panel-over-mcp-and-freezing-the-signal-contract (week 10)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Ninth episode of the Private AI Valuation Agent series (week 1 → 2 → 4 → 5 → 6 → 7 → 8 → 9 →
10; there is no week 3 episode). Sixth episode shipped in both orientations.

**The first episode whose subject is an interface rather than a finding**, and the structure
follows from that: only one beat describes what the server *has*. Two describe what it costs,
two what it will not do, and two where the checks fail.

---

## Where the inputs came from

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | Already here | input, unmodified |
| `figdata.json` | Already here — queried from the live database and the live signal at figure-build time | **the source of truth for most on-screen numbers** |
| `signal_example.json` | Already here — a real emitted signal | **read directly by the build**; its key list is B05's key list |
| `README.md` | Already here — figure-to-beat map, three things not to get wrong, two late failures, three setup bugs | input, appended with a pointer to the built reel |
| `pantry/w10-*.png`, `pantry/w11-*.png` + `.svg` | Were loose in the folder root | **moved to `pantry/`** — the series keeps reference art there, and `run.sh` uses `images/` for compile OUTPUT |
| `lock_durations.py`, `make_vertical.py` | Copied from week 9 | `make_vertical.py` needed a fix — see the toolkit section |

---

## Every number is injected, and these groups are asserted

```
six tools; rows_returned <= rows_total for all of them
get_marks: 2,151 rows, 50 returned == limits.default_limit
          575,299 chars unbounded -> 17,976 bounded, a 96.9% cut
COSTLIER == 5 and CHEAPER == 1, and the one that saves IS get_marks   <- FRAMING
overhead band 0.18 < lo < hi < 0.50   (B03 puts "+19% to +49%" on screen)
exactly one tool paged (get_marks); exactly one returned zero rows (list_unresolved)
limits.max_response_chars == 48000, and the bounded page is UNDER it
signal: schema 1.0 in BOTH figdata and the emitted file
        top_level_keys == len(signal_example.json keys) == 9
        forbidden_fields == 10, and NONE of them appears in the emitted file
        not_supported == len(suppressed) == len(file's not_supported) == 4
list_companies rows_total 11 − signal.companies 10 == 1
guards[] has 3 rows, all caught, including the invented-ranking draft by its text
commentary_words == 388
```

**The framing assertion is `COSTLIER == 5`.** B03's claim is that the bounding envelope is not
free. If a future measurement made bounding a pure win, the build fails rather than shipping a
beat whose arithmetic still held while its framing had gone stale. Same shape as week 8's
widening assertion and week 9's feeder-dominance assertion.

**One assertion checks the artifact rather than the figure.** The ten refused field names are
asserted *absent from `signal_example.json`*, so B05's frame carries the result of a check
rather than a restatement of a claim.

`python build_beat_sheet.py --check` runs the assertions and writes nothing.

---

## Three values that are NOT in figdata.json

| Constant | Value | Used by |
|---|---|---|
| `FOURTH_GUARD` | the length check | B07, B09 |
| `LATE_MISSES` | the empty note accepted as a success; the spelled-out number | B08 |
| `SETUP_BUGS` | the three client-side registration defects | B08, B09 |

All three come from `README.md` and `narration_script.md`. Each is a named constant at the top
of `build_beat_sheet.py`, and **each beat that uses one says so on screen**. `FACTCHECK.md`
rows 12, 18 and 19.

Row 12 is load-bearing in a way the others are not: `figdata.json` carries **three** guards and
`w11-guards.png` is titled "Three guards between the model and the note", while the script says
four. B07 therefore draws the fourth below a dashed rule, labelled as postdating the figure, so
a viewer can see which part of the claim is younger rather than being shown four rows of equal
provenance.

---

## Six claims verified against the LIVE server

New this week, and a verdict type the series has not used before. The MCP server was running
during this build, so six `FACTCHECK.md` rows were checked by calling the tool and reading the
response rather than by trusting the figure:

- `list_companies` → **11 companies, 10 with marks**, and names the one with zero (Scale AI).
  This is what resolved the 11-against-10 and produced B06.
- `get_marks('Databricks, Inc.')` → `marks` 2151, `page.returned` 50, `page.remaining` 2101,
  a `next_cursor`, and a page note stating the summary describes the whole result set.
- `list_unresolved` → `open_items` 0 with an explicit "nothing is unresolved" summary.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Six script sections → eight body beats.** | Two of the eight are new (below). The 1:50 section carried both the contract and the suppression rule; the close carried both the setup bugs and the late misses. |
| 2 | **B03 is new, and contradicts the source figures.** | Both figures show bounding on `get_marks`, where it saves 97%. On the other five tools the envelope COSTS 19–49%. That is the deliverable's price, not a footnote, and it gets a frame. |
| 3 | **B06 is new.** | The tools figure says 11 companies, the contract figure says 10. Both appear in this reel's own source material. A viewer who notices and is not told would be right to distrust everything else on screen. |
| 4 | **The fourth guard is drawn below a dashed rule.** | `w11-guards.png` predates it. Four rows of equal weight would imply the figure and the script agree, and they do not. |
| 5 | **"Read-only" is drawn as three struck absences.** | SHOW-DON'T-TELL: the claim is that something does not exist, so the frame shows things that do not exist rather than listing a feature. |
| 6 | **Greeting rotated to `Moi, HAI`.** | Weeks 1–9 used `Ola`, `Hej`, `Ciao`, `Hallo`, `Salut`, `Ahoj`, `Szia`, `Tere`. Finnish short form; the lexicon never repeats a language. |
| 7 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name. Set at authoring time, so GATE L passed on the first run for the eighth episode running. |
| 8 | **`ServingThePanelOverMcp.tsx` is self-contained, and its PORTRAIT values are tuned.** | Reel-local files keep the earlier signed masters re-renderable. The portrait tuning is a direct response to week 9, which shipped four beats whose 9:16 cut was the landscape layout scaled down. |

---

## Defects found by READING frames, and fixed

The visual gate checks edge bleed, canvas fill and contrast. Everything below was found by
looking at the rendered frame.

| Beat | Defect | Fix |
|---|---|---|
| B09 | **The beat rendered another project's copy** — "Verdict / The split / Chat: synchronous judgment — you're in the loop every step." | The props were named `title`/`heading`/`lines`; the schema declares `artifactTitle`/`artifactHeading`/`artifactLines`. **zod drops unknown keys and substitutes that field's default, silently.** |
| B11 | **The outro read "bot vs bot, season one"** — a default from an unrelated show, on a Humanitarians AI research reel. | `subtitle` → `subline`. Same root cause. |
| B02 | **Edge bleed.** The whole-table bar's figures ran beside it and off the right of the safe area; "· 2,151 rows" was entirely off-frame. | Figures moved BELOW the bar in both orientations, which removes the only place this beat could bleed. |
| B02 | **"~144k tokens" against narration saying "a hundred and forty three thousand."** | 575,299 ÷ 4 = 143,825, which rounds up at whole thousands. One decimal now: `~143.8k`. A viewer can hear that mismatch — the week-7 `11.9300` defect. |
| B03 | `2k → 3k` printed beside an exact `+34%`, which implies +50%. | Exact digits below 100k. Beside a precise percentage, rounding invites a viewer to catch the frame contradicting itself. |
| B01 | `2,151 rows -> 18k chars` used an ASCII arrow. | `→`. Typography only; the week-9 `--` defect. |
| B06 | "because the 1 it drops has zero marks" | "because 1 of them has zero marks." |
| B07 | The fourth guard's label "empty or short draft" wrapped onto a second line that crowded the attribution note. | `length` — the README's own word, and it fits the column. |
| B02/B03/B07 (portrait) | Underfilled: B03's chart used 743 of 972 safe px and 180 of 1728 vertical; B02's bars were thin; B07's guard type ran small. | Portrait widths, heights and type scaled up. Caught at the "not using the canvas" stage rather than week 9's "shipped a thumbnail" stage. |

---

## What the visual gate could not have caught, in this episode

Nine episodes of evidence. The gate cannot see overlap (weeks 1, 4, 6, 7, 8), cannot tell
whether a number on screen is the RIGHT number (weeks 5, 7, 8, 9), cannot tell whether a source
line cites a file containing the claim (week 6), cannot tell whether a caption describes the
chart beneath it (week 8), and cannot tell an empty element from an intentionally empty one
(week 9). This week adds the worst one yet:

**It cannot tell whose words are on the frame.** B09 and B11 were well-formed, well-contrasted,
correctly positioned, inside the safe area, and about a different show. Every geometric check
passed. Two of twelve beats in a 4K review cut were someone else's placeholder copy.

---

## Three toolkit defects found and fixed

All three reach outside users, and none is specific to this reel.

1. **`remotion_scenes.py` now lints unknown props.** The B09/B11 failure above has a single
   root cause: zod's `.parse()` drops keys a schema does not declare and substitutes that
   field's default, silently. The script now parses every `z.object({…})` out of the Remotion
   sources (515 schemas), maps pattern → declared prop names, strips the `916` suffix, and
   warns per beat before rendering:

   ```
   [remotion] WARN B09: ClaudeVerdictArtifact has no prop(s) named
     folderLabel, heading, lines, title — zod will DROP them and render
     this beat with that field's DEFAULT text. Check the schema's spelling.
   ```

   Verified it flags week 10's B09 and B11 **and week 9's `key` prop** (the empty chip), and
   stays silent on correct props. It is a **warning, not a hard failure**: making the schemas
   `.strict()` would be stricter, but every reel from week 1 on passes a harmless extra
   `sparkLine` to `ClaudeVerdictArtifact`, and those signed masters must stay re-renderable
   byte-identically.

2. **`make_vertical.py` could not see a two-digit week number.** Its discovery regex was
   `W\d[A-Za-z]+`, which matches exactly one digit — `W10Bluf` parses as `W` + `1` + `0Bluf`,
   and `0` is not a letter. Every week-10 pattern therefore looked unregistered and the script
   **refused the whole reel**, correctly reporting "no portrait composition W10Suppressed916".
   Fixed to `W\d+[A-Za-z]\w*`.

   This is the one failure this week that did not ship quietly, and the refusal is exactly
   right: it would rather stop the build than centre-cut a landscape frame and call it a
   vertical cut. Every other defect here rendered happily.

3. (From week 9, still in this diff.) `compile.py` and 18 other scripts reconfigure stdout to
   UTF-8; the skin lint understands the `916` suffix.

---

## The recurring toolkit footgun, again

`remotion_scenes.py` loads the beat sheet at the START of a run and rewrites it at the END, so
any edit made during a long render is silently lost. It has cost an edit in every episode since
week 5. Edits made during this build's landscape render were re-applied afterwards by re-running
`build_beat_sheet.py` and `lock_durations.py`, both of which are idempotent.

---

## What shipped

| Artifact | Spec |
|---|---|
| `Mycroft_OmMali_02_10_2026.mp4` | 3840×2160, 24fps, 211.96s — the clean 16:9 master |
| `vertical/serving-the-panel-over-mcp-and-freezing-the-signal-contract-916.mp4` | 2160×3840, 24fps, 211.96s |
| `*-slate.mp4` (both) | review cuts, beat IDs + running timecode |
| `mp4/` | all four under their canonical slug names |

**GATE L clean. GATE V clean on BOTH cuts.** GATE F never triggered: there are no Manim beats.
**GATE P is signed** — `PEDAGOGY.md` carries `VERDICT: PASS`, signed by the author (Om Mali)
on 2026-10-02, and the Kokoro gate was re-run without `--no-gate` afterwards to confirm it
passes on its own. The audio was not regenerated after signing, so the masters are the same cut
GATE V cleared.

The `illustrate carries 8/12 beats (66%)` warning is expected and unchanged since week 2: all
eight body beats illustrate, which is what ILLUSTRATE LAW asks of an `ai-explainer` reel.

## Cost

`$0.00`. Kokoro TTS runs locally from a downloaded model; Remotion and ffmpeg are local. No API
key was used at any point, and no step asked for one. The MCP server queried during fact-check
is the author's own, running locally.
