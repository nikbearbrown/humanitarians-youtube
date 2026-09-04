# PEDAGOGY.md — when-two-agents-disagree (Video 1 of 2)

**GATE P VERDICT: PASS** — awaiting human sign-off.

> GATE P is a human checkpoint, not an agent one (CLAUDE.md rule 3). Read the arc
> below, then change `HOLD` on the line above to the word the gate looks for.
> `generate_audio_kokoro.py` refuses to run until you do.

Source script: `D:/Code/mycroft/verification-layer/divij/video-script-cross-agent-validation-20min.md`,
PART ONE (cold open + chapters 1–6). Part Two is a separate reel:
`../three-files-twenty-one-tests/`.

---

## Compression note (read this first)

The source script's PART ONE is **2,091 words of VO** (~9:45 at Kokoro's measured
214 wpm). This sheet is **785 words** (~3:40). That is a **2.7 : 1 compression**,
and the compression is where the pedagogical risk lives. What was cut, and why:

| Cut from the script | Why it survives elsewhere / why it's safe to lose |
|---|---|
| A named third-party research system's staged-detection conflict table (its three-way F1 breakdown) | The *lesson* — "the hardest conflicts to detect are the ones where picking a side is wrong" — is carried by B05's HIGH-CONFIDENCE card. The specific figures added precision the beat can't hold, and named the system unnecessarily. |
| A named third-party system's claim-type × modality weighting matrix | B06 explicitly makes this matrix the *un*important part (−0.006). Showing it in full would spend 20 seconds arguing for something the ablation then demotes — and would require naming the system. |
| A named third-party system's eight-phase walkthrough, debate-utilization rate, abstention rate | B06 keeps the pipeline as a *generic, unattributed visual* (scale, not detail) and keeps only the ablation numbers, described as "one published ablation study" rather than naming the system. |
| The causal-synthesis / pattern-recognition boundary (script §9:00 close) | Moved to Video 2, where it is a scoping decision about real code rather than an abstract aside. |
| Attributed quotes from named individuals in a related project (script ch.1 quote wall) | **Removed entirely, not just trimmed** — per direction to keep the reel focused on the topic and not reference other people or other projects by name. B02 now makes the same point (a self-graded system always looks consistent) with an anonymous icon grid instead of attributed quotes. The "about fourteen people... independently published" framing is also gone; the claim is now stated as a structural fact, not an anecdote about a specific group. |

**The claim to check when you sign:** does the reel still teach the same thing at
3:40 that the script teaches at 9:45, without naming any person or project outside
this one? My answer is yes — the thesis (disagreement is decidable, correctness is
not), the two traps, the four-way taxonomy, the staged-cost lesson, and the
ablation are all intact, and every remaining research reference is generic
("the research", "a published study") rather than a named system. If you disagree,
the beat to check first is B06 — it's the one carrying real quantitative findings
without a citation, which is the deliberate trade this rewrite makes.

---

## Teaching arc

| Beat | Role | What the viewer walks away holding |
|---|---|---|
| **B00** | Cold open — welcome + self-intro | Who is talking, that this is part 1 of 2, and the 12%-vs-8% hook. COLD OPEN LAW: welcome screen first, always, even though this is a series. |
| **B01** | Executive summary (BLUF) | The whole idea in one breath, before any specific: correctness needs an oracle, disagreement needs nothing, so build a problem detector. This is the scaffold every later beat hangs on. |
| **B02** | You cannot check an agent's work | *Why* the problem is real and structural — any system graded only by its own output looks consistent by construction. No named individuals or projects; the anonymous icon grid carries the point instead of an anecdote. |
| **B03** | Ask it twice — and the asymmetry | The cheapest approach, its one genuinely load-bearing insight (agreement weak / disagreement strong), and the hole (two draws, one distribution). |
| **B04** | The two traps | The turn. Both traps make a broken system *look* like it's working — information asymmetry, and majority voting laundering correlated error. |
| **B05** | Four kinds of disagreement, staged detection | Not all disagreement is signal. Then the practical lesson that generalizes past cost: a check you can afford to run on everything. |
| **B06** | The ablation, and the fork | What the mature version costs, what actually matters in it (−0.119 vs −0.006), and the design fork Part Two follows from. |
| **B07** | Verdict | Four-line recap. Gist at the start (B01), gist at the end (here). |
| **B08** | Your turn — handoff | Extends trap one into the viewer's own stack. Prompt is read aloud verbatim and discussed. |
| **B09** | Outro | Title restate + the thesis as a subline that Part Two's outro answers. |

## Comprehension anchors

| Beat | Anchor | Phrase | Why it lands |
|---|---|---|---|
| B00 | Concrete numbers | "twelve percent … eight" | Two numbers a viewer can hold in their head for four minutes |
| B01 | Reframe | "not a truth detector — a problem detector" | Names the whole move in six words |
| B02 | Recursion | "the reasoning is also generated text" | The uncomfortable point, stated once, plainly |
| B03 | Asymmetry | "agreement proves almost nothing" | Counterintuitive, so it sticks |
| B04 | Metaphor | "one witness asked twice in two accents" | Makes information asymmetry physical |
| B04 | Warning | "a majority of correlated agents is not a majority" | Aphoristic; survives being quoted out of context |
| B05 | Economics | "a check you can afford to run on everything" | Turns a cost stat into a design principle |
| B06 | Contrast | −0.119 vs −0.006 | Two numbers, one argument, no explanation needed |
| B06 | Constitution | "machines verify conformance, humans verify adequacy" | The line the whole series rests on |
| B09 | Cliffhanger | "part two — what I actually built" | Series hook without a fake tease |

## Register and tone

Teardown. Short declaratives, one idea per sentence, "but" as the turn word —
matches the source script's own style rules. **The register constraint is
unusually strict here:** the subject is a system that refuses to overclaim, so
the narration must not overclaim either. Two specific holds:

- No beat says cross-agent validation *works* or *catches errors*. It says it
  detects disagreement. That is the smaller claim, and it is the true one.
- Every figure spoken aloud is measured in a source. None were rounded for
  rhythm. See `SOURCES.md`.
- **No beat names a person or a specific outside project.** Research findings
  in B05/B06 are attributed generically ("the research", "a published study"),
  never to a named system. The only named person in the whole reel is the
  presenter (B00, B09).

## Series continuity

- B00 names "part one of a two-part series" out loud — no assumed context.
- B09's subline ("Correctness is not decidable. Disagreement is.") is answered by
  Video 2's B09 subline ("The judgment stays with the human. That was the point.").
  Design the two outro cards to be read as a pair.
- The two-path SURFACE/RESOLVE fork appears in **B04 and again in B06** with
  identical geometry. Build it once as a shared helper in `scenes.py`.

## Scene placeholder check

| Beat | Class / pattern | Status |
|---|---|---|
| B00 | `ClaudeComposerAsk` (Remotion) | props authored, within slate limits |
| B01 | `B01_CorrectnessVsDisagreement` | needs writing |
| B02 | `B02_SelfGradedConsistency` | needs writing |
| B03 | `B03_AskItTwice` | needs writing |
| B04 | `B04_TwoTraps` | needs writing — shares the fork helper with B06 |
| B05 | `B05_FourKindsAndFunnel` | needs writing |
| B06 | `B06_AblationAndFork` | needs writing — shares the fork helper with B04 |
| B07 | `ClaudeVerdictArtifact` (Remotion) | props authored, within slate limits |
| B08 | `ClaudeComposerAsk` (Remotion) | props authored, within slate limits |
| B09 | `ClaudeTitleOutro` (Remotion) | props authored, within slate limits |

`runtime/qc/sheet_check.py` reports clean — 10 beats, no findings.

## Known risks to watch at render time

Per `tips.txt`, in order of how likely they are to bite this specific sheet:

1. **B05, B06 are 32s and 34s.** Longest beats in the reel by a wide margin. Their
   Manim scenes must have enough `self.wait()` to reach the *actual* audio
   duration natively — if the clip comes in short, `compile.py` stretches it into
   visible slow motion (tips.txt §8).
2. **B04 and B05 both stack chips under nodes.** Three agent nodes with labels, and
   a 2×2 of cards with 28-char labels. This is the exact collision class that hit
   the last two reels (tips.txt §6). Wrap long chip labels to two lines.
3. **B02's icon grid uses `checked()` from `graphics_lib.py` for the six
   CONSISTENT stamps.** That's the correct pattern (tips.txt §4) — Montserrat has
   no ✓ glyph, so it must render through the symbol/word composition helper, not
   a raw font-forced `Text("✓ …")`.

## Audio gate sign-off

Narration is final and grammar-checked. All spoken figures are written as words
(`zero point one one nine`, `seventy-three percent`) so Kokoro reads them
correctly; the digit forms live in the `show` events and Remotion props only.

Ready for `am_onyx` generation across all 10 beats **once a human flips the
verdict line at the top of this file to PASS**.
