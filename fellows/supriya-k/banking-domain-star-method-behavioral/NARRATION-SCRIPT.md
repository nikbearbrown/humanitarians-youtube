# Narration Script — "The STAR Method Banking Panels Actually Score"

**Format:** Deep-explainer, B00 → ACT I-IV → VERDICT → YOUR TURN → OUTRO · **Persona:** none
(compliance override — "in for Supriya," no default name, no channel) · **Register:** Pragmatist ·
**Voice:** Kokoro `af_bella` · **Estimated runtime:** ~268s (~4:28) at planning pace; real Kokoro
audio typically runs slower than the 2.9 words/sec planning estimate, so expect the locked duration
to land higher, likely in the 5-6+ min range. **Source:** `chapters/12-behavioral-round.md`,
`chapters/14-full-loop-mock-interviews.md` (Stage 4).

---

## OPEN

**B00**
> Hi — in for Supriya. Banks don't grade a STAR answer differently. They're listening to a
> different half of the same story.

## ACT I — The STAR Framework

**B01** (act card)
> Part one: the framework itself — four parts, the same everywhere.

**B02**
> Situation. Task. Action. Result. Situation sets the scene. Task is your responsibility in it.
> Action is what you specifically did. Result is the outcome — and what changed because of it.

**B03**
> The generic STAR failure is all Situation, no Result. Candidates set the scene, and never say
> what happened.

## ACT II — What a Banking Panel Listens For

**B04** (act card)
> Part two: what a banking panel listens for, on top of the generic.

**B05**
> A banking panel is listening for three things the generic rubric doesn't name. Risk awareness —
> did you notice a problem before you were told about it. Regulatory and control judgment — did
> you understand why a rule existed, not just that it did. And comfort under audit or examiner
> scrutiny — can you describe defending your work without sounding defensive.

**B06**
> Three situations show up often enough to prepare a story for each. Flagging a data-quality issue
> before it reaches a report. Working through an internal-audit or examiner-style request. And
> navigating conflicting pressure between a business stakeholder and a control function.

**B07**
> Here's the banking-specific failure. "I noticed the numbers looked off" is not a Result a
> risk-aware panel accepts. "I flagged it to my lead before it went into the report, and we caught
> the error before quarter-end close" is.

**B08**
> And when you deliver it, be specific. "We fixed it" is weaker than "we added a validation check
> that catches that specific error before it reaches the report." The second version proves you
> understood why the problem mattered — not just that you solved it once.

## ACT III — Weak Answer, STAR Rewrite

**B09** (act card)
> Part three: a weak answer, and the STAR rewrite.

**B10**
> "Yeah, actually one time I found a mistake in a report a coworker made. The numbers were off. I
> mentioned it and we fixed it before it went out. It worked out fine."

**B11**
> Situation: reviewing a monthly revenue-by-region dashboard, two days before it reaches the VP of
> Sales. Task: not formally assigned to QA it — but this is the data model underneath it. Action:
> one region's numbers had roughly doubled with no business reason — traced to a schema change,
> flagged the same day, the publish held until it's confirmed. Result: the VP never sees the bad
> number, and a data-quality check goes into the dbt test suite, so the same bug can't reach a
> report undetected again.

**B12**
> Three things get scored here. Risk awareness — treating "is this plausible" as a check worth
> running. Escalation — raising it immediately, to the right people. Outcome — naming the specific
> control that now exists because of the incident.

## ACT IV — Daniel's Full-Loop Mock

**B13** (act card)
> Part four: Daniel's full-loop mock — stage four.

**B14**
> A realistic banking loop runs five stages back to back. Domain vocabulary. SQL. Case.
> Behavioral. Systems design. Daniel — three and a half years into his analyst career — runs all
> five in one sitting, under time pressure. Stage four is behavioral.

**B15**
> "Tell me about a time you found an error in your own or a colleague's work."

**B16**
> Daniel describes finding a mis-joined table that inflated a retention metric. Then he stops: "I
> fixed it and let my manager know." No new check. No changed process. No number.

**B17**
> Scored against the book's own rubric: a one. STAR shape — but no named escalation, no named
> control, no stated outcome. And Daniel's not alone up there — his other four stages all landed
> the same one place short of a three.

**B18**
> Behavioral is Daniel's only one — it gets the bulk of his remaining hours. His four twos share
> one gap: correct, but missing the final detail that makes it a three. His lesson for himself:
> finish the thought out loud.

## CLOSE

**B_VERDICT**
> The STAR method doesn't change in a bank. What a bank panel is listening for in the Result does:
> name the control, name the escalation, or the story doesn't score — no matter how real it is.

**B_YOURTURN**
> Your move: draft one STAR story for a time you flagged a problem before being asked to.
> Situation, Task, Action — then don't stop at "and I fixed it." Name exactly who you told, when,
> and what changed as a result.

**B_OUTRO**
> The STAR method banking panels actually score. In for Supriya — building it with Claude, then
> taking it apart.

---

**Word count:** ~780 words across 22 beats. **Pace:** planning estimate ~2.9 words/sec (this
skill's stated rate) → ~268s; measured Kokoro audio is the only real clock, and typically runs
slower in practice (the SQL video measured closer to ~2.3-2.6 words/sec) — actual duration will be
locked once `generate_audio_kokoro.py` runs.
