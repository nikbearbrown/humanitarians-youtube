# QUESTION

**The question:** When an AI gives you a confident, well-written answer, what
actually makes that answer legitimate to act on — and is that the same thing
as it sounding right?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-liam-legitimacy-auditor/beat_sheet.json`
("Legitimacy Auditor — Pragmatic, Moral, Cognitive (Suchman 1995)",
Teardown-register, CLI-style video, `register: "Teardown"`, `brand:
"claude-liam"`, `style: "cli"`, cold open `NikBearBrownOpen`, terminal-ask
(`NikBearBrownTerminalAsk`) and code-block (`NikBearBrownCodeBlock`) beats, a
Manim comparison-card beat, Your Turn, `ClaudeTitleOutro`). The source's body
beats (B01–B08) were fully authored narration, not seeded placeholders — the
facts below carry forward largely intact, compressed for the Plain register
and the hai-simple ten-beat shape.

**Why it earns a reel:** it is easy to treat "this reads fluently and sounds
informed" as proof that an AI answer is safe to act on. But sociologist Mark
Suchman's 1995 framework splits organizational "legitimacy" into three
separate questions — does it serve the stakeholder's interest (pragmatic); is
someone accountable for it (moral); does it feel taken-for-granted and
natural (cognitive) — and an AI answer can pass the third one, cognitive,
purely on fluency while failing the second, moral, because no one is named
to answer for it if it's wrong. The same sentence, unchanged, can hold in one
room and fail in another, because the rooms differ in who is accountable, not
in how the sentence reads.

**Naive framing (B00, corrected on screen):** "The AI sounds confident. That
means it's trustworthy. Right?" → corrects "trustworthy" to "accountable"
(the real frame: confidence answers whether it *feels* right — cognitive —
not whether anyone *answers* for it — moral).

**Body facts carried from source (unchanged):**
- the anchor: one AI answer, word-for-word identical, placed in two rooms —
  a finance committee reviewing a projection, and a hospital bedside where a
  clinician is deciding on a patient (source B01/B04)
- the three-type framework itself: pragmatic (serves the interest), moral
  (someone accountable), cognitive (feels natural, trusted because fluent) —
  Suchman 1995 (source B01)
- the falsifying case: in the finance committee, the CFO is named as
  accountable, so moral legitimacy holds; at the bedside, the identical
  fluent sentence has no one named to own it if it's wrong, so moral
  legitimacy fails even though the cognitive read — it sounds right — is
  unchanged (source B04)
- the fix / mechanism: naming a specific accountable party and a review
  mechanism is what turns a fluent answer into a legitimate one — source's
  worked example is naming the attending physician and a documented review
  step for the bedside case (source B05/B06)
- the summary lesson: an AI output can pass all three types or fail all
  three depending entirely on context, and an audit makes the gap explicit
  rather than assumed (source B07)
- next steps: run the check on a real high-stakes AI output you've seen
  recently, and if the cognitive verdict is "counterfeit" — trusted for
  fluency, not traceability — the real question isn't whether the AI was
  wrong, it's whether anyone would know (source B08) — folded into the
  carry-out and the your-turn handoff rather than narrated as a separate beat

**Compression, per the constitution/IVP redo precedent:** ten beats — B00
(writer) + B01–B06 (body) + BCRY + BHTF + BOUT — instead of the source's nine
numbered beats plus Your Turn and outro. B01 plants the anchor (two rooms,
one answer) and states the three-type framework; B02 states the wrong guess
(fluent reads as already legitimate on every count); B03 breaks it with the
source's own falsifying case (CFO named vs. no one named, same sentence) and
states the mechanism (fluency only ever answers the cognitive question); B04
states the fix mechanism (name the accountable party and the review step
*before* the answer is acted on); B05 covers direction A (cognitive legitimacy
passing says nothing about moral legitimacy); B06 covers direction B (a
disclosed/hedged AI answer isn't automatically accountable either — a
disclaimer isn't a mechanism) and pays off the anchor by fixing the bedside
room with the same one-line move that already held in the finance room.

**No inference flag.** Every claim here is a description of Suchman's defined
framework and its application (name the interest test, the accountable party,
the traceability test) rather than an empirical claim about model internals —
there is no leap from evidence to conclusion that needs flagging, unlike the
constitution-family redos which made a claim about training's effect on
latent character space. QUESTION.md documents this instead of forcing a flag
where none is needed (per `simple`'s ONE-FLAG LAW: "if the source genuinely
supports everything, there is no flag").
