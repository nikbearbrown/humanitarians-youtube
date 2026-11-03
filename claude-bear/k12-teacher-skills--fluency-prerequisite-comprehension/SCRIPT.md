# SCRIPT.md — The Fluency Ceiling (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `fluency-prerequisite-comprehension` (a Plain-adjacent explainer
walking the working-memory case for a fluency ceiling that caps
comprehension) — question, facts, and body argument carried over; narration
re-registered where the source drifted toward design-judgment language;
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
A teacher first types: another scaffold. Not quite — the real question is
whether decoding itself is still effortful. Here's how the fluency ceiling
limits comprehension.

*(Text typed on screen: "Every kind of / support hasn't / helped. Need /
another scaffold?" — trigger word "scaffold" (the single last content word
before the terminal "?", appearing exactly once in the whole text) corrects
to "fluency check", landing on: "Every kind of support hasn't helped. Need
another fluency check?" Per the lesson carried over from the
`cra-progression-scaffold` and `k12-lesson-differentiation` siblings' Gate V
finding: `triggerWords` must be a SINGLE whitespace token — the component
matches the trigger against one split token's punctuation-stripped core, so
a multi-word trigger never matches and the correction silently never fires.
`replacementWords` may be a phrase — typed literally, character by
character, after the trigger is deleted. GATE V FINDING (this reel): a
first-draft, longer text ("I've scaffolded everything I can think of, and
they still can't comprehend. Need another scaffold?", 101 characters) never
reached the trigger word within the beat's 9.88s duration — frame pulls
across the full clip showed the writer still mid-sentence at the last frame.
`lead_silence_s` is authored per WRITER LAW convention but is not wired into
`compile.py`, so the real typing budget is exactly the narration length, not
narration-plus-lead-silence. Shortened to the 59-character text above,
matching the char budget of the working `cra-progression-scaffold` sibling's
65-character text at identical timing props, and reconfirmed by frame pulls
after re-render.)*

## Body — the working-memory case for a fluency ceiling

**NB01 — One bar, two splits** (source B01, mechanism + THE ANCHOR planted,
ONE FLAG)
One capacity bar for the whole reading task. In an illustrative low-fluency
case, seventy-eight percent of that bar goes to decoding — sounding out
words, tracking syntax, holding letter sequences in mind. Only twenty-two
percent is left for comprehension, the starved zone where meaning-making is
supposed to happen. In a high-fluency case, decoding drops to twelve
percent, automatic and nearly free — comprehension expands to eighty-eight.
The exact numbers are a teaching illustration, not a measurement of any one
student. What they illustrate is real: the bar doesn't grow. The split just
moves.

**NB02 — Two responses to the ceiling** (source B02, mechanism)
Two different responses to a fluency ceiling. The immediate bridge:
read-aloud or partner reading offloads the decoding load for a few minutes,
so a student can practice comprehension thinking today. That's a circuit
breaker, not a fix. The real fix is a separate fluency intervention, run
outside the comprehension lesson. Comprehension scaffolds can't compensate
for a fluency ceiling — adding another graphic organiser only scaffolds the
wrong level.

**NB03 — Five roles, one non-negotiable** (source B02a, BOTH DIRECTIONS)
Fluency practice has five roles, and they don't get the same verdict. The
listener, catching errors as the student reads aloud — that role can be
handed to AI; it's the role most classrooms lack the time for. The reader
cannot be substituted. The decoding is the intervention itself, and a
text-to-speech track reading the passage to the student inverts the practice
without anyone noticing.

**NB04 — THE ANCHOR PAYOFF — the cold-read check** (source B02b, mechanism,
returns to the bar's split from NB01)
Here's how you find out if that split actually moved: the cold read. A
brand-new passage, never rehearsed, checked on a different day. A rehearsed
passage can look like the comprehension share grew, when really the student
memorized the route — that's recall, not the automatic decoding from
before. Only a passage the student has never seen shows whether the shift is
real.

## Close

**BCRY — carry-out**
Claude doesn't hand you a bigger scaffold — it helps you check whether
decoding is still effortful, because every bit of working memory spent on
decoding is memory comprehension will never get to use.

**BHTF — your turn**
Your turn. Paste this into Claude: here's a student who isn't responding to
comprehension scaffolds — grade level, scaffolds tried, how they read aloud
versus how they do when someone reads to them. Help me figure out whether
the bottleneck is fluency or comprehension strategy, give me a five-minute
diagnostic I can run tomorrow, then two plans: an immediate bridge for the
current lesson, and a separate fluency intervention for the coming weeks.

**BOUT — outro**
The Fluency Ceiling. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is the standard scaffolding assumption — comprehension not improving means the scaffold needs to be bigger |
| Wrong guess | B00 (WRITER LAW) | "scaffold" corrected to "fluency check" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no dedicated wrong-guess beat to redistribute, so none is invented beyond this |
| Mechanism | NB01–NB04 | the conserved capacity bar; the bridge-vs-real-fix distinction; the five-role AI-substitution ledger; the cold-read verification test |
| Anchor | the conserved bar and its low/high-fluency split, planted NB01, held through NB02–NB03, PAID OFF at NB04 ("if that split actually moved") | a genuine planted-and-returned case, not a single worked example with nothing to return to |
| Both directions | NB03 | states both directions of AI substitution in fluency practice: the listener/error-catcher role CAN be handed to AI (it's the bottleneck role most classrooms lack time for) AND the reader role CANNOT be substituted (decoding is the intervention; substituting it inverts the practice) |
| Carry-out | BCRY | one sentence, survives repetition, and answers B00's wrong guess directly (check decoding first, don't stack another scaffold) |

## One-flag audit

One inference flag, at NB01: the 78%/22% (low-fluency) and 12%/88%
(high-fluency) splits are, per the source reel's own `SOURCES.md`,
"illustrative approximations to make the working-memory conservation
principle visible... not empirical measurements from a specific study." The
narration flags this explicitly and once ("a teaching illustration, not a
measurement") rather than repeating a hedge across every beat that touches
the bar. Everywhere else the reel commits: the underlying
working-memory-conservation principle itself is established (Cognitive Load
Theory, Sweller 1988; the Simple View of Reading, Gough & Tunmer 1986, per
the source `SOURCES.md`), as is the read-aloud bridge, the AI-substitution
ledger, and the cold-read-vs-rehearsed distinction (source `SOURCES.md` /
k12-lesson-differentiation plugin). Per simple's ONE-FLAG LAW, exactly one
flag marks the one genuinely illustrative number set; nothing else in the
reel is hedged.

## Register note (redo)

The source reel's B02 used a design-judgment phrase ("Adding more graphic
organisers to a decoding problem is scaffolding the wrong thing") that reads
as a verdict on a teacher's choice rather than a description of the
mechanism. This redo keeps the underlying fact (comprehension scaffolds
cannot compensate for a fluency ceiling) but states it as a consequence, not
a judgment on the teacher — per Plain's "No judgment" register check. The
source's B02a used "inverts the practice silently," which is kept verbatim
in NB03 since it describes a mechanism (what text-to-speech substitution
does to the exercise), not a verdict on anyone's decision.

## Beat-count note (redo)

Source (`build.filled: 8, of: 8`) is B00 (ClaudeComposerAsk cold open) +
B01/B02/B02a/B02b (four body beats: the conserved bar, bridge-vs-real-fix,
the five-role ledger, the cold-read test) + B03 (verdict) + B04 (handoff) +
B05 (outro) = 8 beats. This redo keeps that exact 8-beat shape: B00 replaced
1:1 with BrutalistHesitantWriter; B01→NB01, B02→NB02, B02a→NB03, B02b→NB04
kept as one beat each; B03's two verdict facts (Claude can help design a
fluency diagnostic, and the distinguish-the-two-hypotheses framing) folded
into the single BCRY carry-out sentence (CARRY-OUT LAW: Plain carries one
carry-out sentence, not a bulleted verdict); B04 kept as the your-turn
handoff, source's bracketed student-description prompt kept nearly verbatim
since it was already a real, paste-ready Claude prompt; B05 kept, re-skinned
to the Humanitarians AI outro (`OutroSeries`). Total: B00 + NB01–NB04 + BCRY
+ BHTF + BOUT = 8 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source was already entirely REMOTION (`ClaudeComposerAsk`,
`K12Fig04WorkingMemory`, `ClaudeWindow`, `K12Fig11SubLedger`,
`K12Fig12ColdReadTest`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`).
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's cold open,
which this redo replaces per hai-simple's mandate anyway. The source's
`K12Fig04WorkingMemory` / `K12Fig11SubLedger` / `K12Fig12ColdReadTest`
components are Claude-fidelity-skin Remotion scenes with no ink/accent/bg
props exposed and cannot be repainted to the humanitarians palette. Per
hai-simple's channel-skin law (the whole channel skin, not only the outro,
moves to the humanitarians palette) and matching the direct precedent set by
the `k12-teacher-skills--cra-progression-scaffold` and
`k12-teacher-skills--claude-liam-k12-lesson-differentiation` siblings (same
book, same skill, same decision), NB01–NB04 are built fresh as GRAPHIC
(Manim) beats on the same generic "chip row" template those siblings used,
carrying the same teaching points as the source's Remotion figures rather
than the fixed-palette components themselves.
