# PEDAGOGY — serving-the-panel-over-mcp-and-freezing-the-signal-contract (week 10)
*Serving the Panel over MCP and Freezing the Signal Contract — Week 10 progress update · ai-explainer / claude-hai*

Ninth episode of the Private AI Valuation Agent series. Same chassis, same channel, same
persistent voice as weeks 1, 2, 4, 5, 6, 7, 8 and 9. Source: `narration_script.md`
(author-written, 3:00 target) plus `README.md`'s figure-to-beat map.

**This is the first episode whose subject is an interface rather than a finding.** For nine
weeks the deliverable was a number or a method. This week it is two things other people use: a
server and a contract. The failure mode of an interface episode is a feature tour, so the cut
is built around three constraints instead — what bounding costs, what the server cannot do, and
what the contract refuses.

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Carries the requested self-introduction: "Hi, I'm Om Mali. This video is about…" ✓ |
| B01 | EXECUTIVE SUMMARY | Both deliverables named by what they are FOR, and the assumed difficulty struck ✓ |
| B02 | THE SIZE PROBLEM | One query, measured twice ✓ |
| B03 | WHAT BOUNDING COSTS | What the envelope costs on the five tools that did not need it ✓ |
| B04 | SIX TOOLS, NONE WRITES | The surface, and three things none of it can do ✓ |
| B05 | THE CONTRACT | Nine keys carried against ten names refused, checked on the frame ✓ |
| B06 | SUPPRESSED, NOT MISSING | A reason in the slot where a missing key would be — and two counts reconciled ✓ |
| B07 | THE GUARD THAT WASN'T ENOUGH | The author's expectation, and the draft that disproved it ✓ |
| B08 | WHAT THE CHECKS STILL MISS | Two late failures, three setup bugs, and what none of it shows ✓ |
| B09 | VERDICT | One-page recap, five findings, one per spoken clause ✓ |
| B10 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B11 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → PROBLEM → COST → SURFACE → CONTRACT → REFUSAL →
FALSIFICATION → LIMITS → VERDICT → HANDOFF → OUTRO ✓

**The structure refuses to be a feature tour.** Only one beat (B04) describes what the server
*has*. Two describe what it costs, two describe what it will not do, and two describe where the
checks fail. A viewer who finishes this reel knows the shape of the constraints, not the API.

**Where this cut departs from the script.** The script has six sections; they become eight body
beats. Each split is a genuine seam:

1. *B03 is new.* The script's 0:35 section presents bounding on the one tool where it wins.
   `figdata.json` shows it **costs** 19–49% on the other five. That is not a footnote to the
   deliverable, it is the deliverable's price, and it gets its own frame.
2. *B06 is new.* The tools figure says eleven companies; the contract figure says ten. Both
   appear in this reel's own source material. A viewer who notices and is not told would be
   right to distrust everything else on screen, so the reconciliation is a beat.
3. *1:50 carried both the contract AND the suppression rule* — split into B05 and B06, so the
   refusal and the withholding each get a frame.
4. *2:55's close carried the three setup bugs AND the two late misses* — promoted together into
   B08, because a closing sentence at 2:55 would be heard as sign-off patter.
5. *0:00 and the two-deliverables description split into B00 and B01* — the standard bookends.

No claim was added or dropped by the splits, and **every added FIGURE is injected from
`figdata.json` or read out of `signal_example.json` under an assertion**, with the three
exceptions named below. Four wording changes are logged in `FACTCHECK.md`.

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B00 carries the requested opening line: *"Hi, I'm Om Mali. This video is about making this
  dataset usable by something other than me."* ✓
- B01 states both deliverables in plain language. No "MCP", no "cursor", no "schema version"
  until B02–B05 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W10Bluf` — two deliverable cards, a struck assumption, the real constraints | illustration ✓ |
| B02 | `W10Bounding` — two bars to scale from one measurement | illustration ✓ |
| B03 | `W10Envelope` — a diverging track from a zero line, five right and one left | illustration ✓ |
| B04 | `W10Tools` — six rows of returned-against-available, then three struck absences | illustration ✓ |
| B05 | `W10Contract` — nine key chips against ten names striking through | illustration ✓ |
| B06 | `W10Suppressed` — reason chips in the slot, then two counts reconciled | illustration ✓ |
| B07 | `W10Guards` — has-versus-lacks, three drafts, and a fourth below a dashed rule | illustration ✓ |
| B08 | `W10Limits` — two misses, a numbered stack of three, a rule, and the limits | illustration ✓ |
| B09 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B10 | ClaudeComposerAsk | UI — the handoff ✓ |
| B11 | ClaudeTitleOutro | UI — the outro ✓ |

Eight body beats, eight different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B10 ✓

**B02 and B03 are adjacent and both about the same measurement.** B02 is TWO bars sharing one
scale, and its argument is the ratio between them. B03 is six rows on a **diverging** track, and
its argument is the *sign* of each change — which is why the geometry has a zero line and a left
and a right, something a plain bar cannot carry. One asks "how much smaller", the other asks
"smaller for whom".

**B04 and B06 both draw lists of rows and must not read as the same slide.** B04's rows are
tools with numbers; B06's rows are companies with a chip in place of a value, and B06 then
breaks into two large counts that B04 never does. B05 sits between them and is two columns of
chips, which looks like neither.

**The struck line is used three times and means one thing each time.** B01 strikes an
assumption that turned out to be wrong, B04 strikes capabilities that do not exist, and B05
strikes field names the contract refuses. All three are "this is not here", which is the one
reading the primitive carries in this series.

---

## Utility-framing lint

- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT as a framing device. B00 says "This video is about…" **once**,
  as the author's explicitly requested opening line, and then never again ✓

Style: narration written dash-free per the author's confirmed preference ✓

---

## Honesty check

An interface episode can go wrong by selling the interface. The cut is built so that every
claim about what the server does is paired with what it costs or cannot do.

- **The reel contradicts its own source figures, on purpose.** Both figures show bounding where
  it wins. B03 shows it costing 19–49% on five of six tools. The injection asserts five
  costlier and exactly one cheaper, so a future measurement that made bounding free would fail
  the build rather than ship a beat whose framing had gone stale while its arithmetic held ✓
- **Two of the reel's own numbers disagree, and the reel says why.** The server lists eleven
  companies; the signal publishes ten. The eleventh has zero marks. B06 reconciles it on the
  frame rather than keeping the two numbers on separate beats where nobody would notice ✓
- **"Read-only" is drawn as an absence, not claimed as a feature.** B04's three struck lines are
  things that do not exist. The reason is stated — a resolution decision needs a named human —
  rather than implied ✓
- **The refusal is checked, not asserted.** B05's refused column is read from the emitted file,
  and the injection asserts that none of the ten names appears in it. The frame carries the
  result of that check ✓
- **The episode's centre is the author's expectation being wrong.** One check was expected to be
  enough. A draft passed it and still contradicted itself inside a paragraph. The draft is
  quoted verbatim, and the number in it was real ✓
- **The fourth guard is drawn as younger than the other three.** `w11-guards.png` says three;
  this reel says four. The fourth sits below a dashed rule with its provenance on the frame, so
  a viewer can see which part of the claim postdates the figure ✓
- **An empty answer is shown as an answer.** `list_unresolved` returns zero rows, and B06 shows
  that with the server's own summary note rather than omitting the tool ✓
- **The reel ends on its limits.** B08 is the last body beat: two failures the checks still
  miss, three setup bugs that were the author's, and a closing block that says there is no
  company valuation here, no timeliness, and no verified claim in the model's prose ✓
- **No invented figures on screen.** Everything else is a prop injected from `figdata.json` or
  read out of `signal_example.json` under assertions that fail the build ✓

---

## Length law

**Measured: 211.96s (3:32.0)** of narration across twelve beats, from the Kokoro MP3s. Duration
is an OUTPUT. The script targets 3:00; the four bookends are additive, and the series has run
2:35 → 3:00 → 3:22 → 3:35 → 3:21 → 3:35 → 3:45 → 3:38 → 3:32.

Per-beat narration budget, counted against the final narration (body beats only; bookends
exempt):

B01 50w · B02 56w · B03 58w · B04 62w · B05 52w · B06 57w · B07 65w · B08 68w

**All eight sit inside the 45–70 band.** B08 is the longest at 68 words because it carries both
late misses and all three setup bugs; it is the beat the episode's honesty rests on.

---

## Both orientations, from one source

As weeks 5–9, at the author's standing request: **16:9 (3840×2160) and 9:16 (2160×3840)**. The
vertical cut is a **re-layout, not a crop**.

**Portrait values in this file are TUNED, not inherited.** Week 9 shipped four beats whose 9:16
cut was the landscape composition scaled down — B05's seven rows filled 266 of 1728 safe pixels
— and only reading the portrait frames caught it. This week every component was written with
both orientations in mind from the start: B02's figures move *below* the bar in portrait rather
than beside it, because the long bar cannot have 1,560px and the ratio is the argument; B03's
diverging track narrows and its rows get more vertical pitch; B07's guard rows stack the guard
name above its draft instead of beside it. Both cuts render from the same components and the
same props, so a number cannot differ between them, and they carry the identical narration MP3s.

---

## Source fidelity

Every number traces to `figdata.json` or `signal_example.json` — see `FACTCHECK.md`, 20 rows,
with rows 6, 12, 15 and 18 flagged as the ones worth challenging. Rows 12, 18 and 19 are the
three values that are not in the figure data at all; row 12 is the load-bearing one.

**Six rows were additionally confirmed against the live server during this build** — a verdict
type this series has not used before. The MCP server was running, and rows 2, 3, 9, 14, 15 and
17 were checked by calling the tool and reading the response rather than by trusting the figure.
That is how the eleven-against-ten was resolved: `list_companies` reports 11 companies and 10
with marks, and names the one with zero.

The four source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). They were moved there from the
folder root because `run.sh` uses `images/` for compile OUTPUT and the series keeps reference
art in `pantry/`.

## Palette deviation (logged, deliberate)

Identical to weeks 1, 2, 4–9: this rebuild renders in the Claude fidelity skin (cream
`#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a
fidelity brand that may not be retinted. **Palette change only — no datum, ordering, or label
altered.** The source figures' rule that red is the primary series and never a warning colour is
preserved in effect: terracotta marks the bounded page, the one tool the envelope pays for, the
refused names, the suppressed reason and the draft that should not have passed — the subject of
each beat, never a hazard.

---

**What the author is being asked to sign off on**, having watched
`serving-the-panel-over-mcp-and-freezing-the-signal-contract-slate.mp4`:

1. The five structural changes above (6 script sections → 8 body beats), in particular **adding
   B03 and B06**, neither of which is in the script or either figure.
2. Stating on camera that bounding **costs** 19–49% on five of the six tools, where the script
   and both figures present it as a straight win.
3. Reconciling the server's eleven companies against the signal's ten, rather than keeping the
   two numbers apart.
4. `FACTCHECK.md` rows 6, 12, 15 and 18 — the envelope cost, the fourth guard that postdates its
   own figure, the eleven-against-ten, and the two late misses.
5. Drawing the fourth guard below a dashed rule as a later addition, so the frame shows three
   checks and one younger one rather than four of equal provenance.
6. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
7. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS — signed by the author (Om Mali), 2026-10-02.

Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than
passed silently. **The gate has since been re-run WITHOUT the override and passes on its own.**
The audio was NOT regenerated after signing: the mp3s that were measured, locked and rendered
against are the mp3s in the masters, so the signed cut is bit-for-bit the cut that cleared
GATE V.

**Both cuts are built and measured.** 3840×2160 and 2160×3840, 24fps, 211.96s each — the same
narration files, not two renderings of the same script. GATE L clean; **GATE V clean on both
cuts**, 24 frames sampled each, 0 BLOCKER and 0 MAJOR, re-run explicitly with `--mp4` against
the exact files being delivered.

Nine frame-level defects were found and fixed before this cut, every one by LOOKING at a
rendered frame. Two are worth the author's attention because they put the WRONG WORDS on screen
rather than ugly ones: B09 rendered another project's placeholder copy ("Verdict / The split /
Chat: synchronous judgment") and B11's outro read "bot vs bot, season one". Misnamed props; zod
drops unknown keys and substitutes that field's default, silently. Both passed every automated
check. `BUILD-LOG.md` has the full table, and the toolkit now lints for it.
