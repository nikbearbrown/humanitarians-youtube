# CARRY-OUT.md — healthcare--claude-liam-clinical-trial-protocol-skill

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Clinical-trial-protocol-skill drafts the protocol to a fixed spec — it
> doesn't decide how the trial should run; that call still belongs to a
> person.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction that matters (drafts vs. decides)
without needing the topic re-explained, and it survives being repeated cold.

**The wrong guess it's built to defeat:** that a skill named for something as
consequential as a clinical trial protocol must be exercising clinical or
regulatory judgment — choosing endpoints, setting dosing, weighing risk.
`clinical-trial-protocol-skill` is deliberately narrower: it is an
instruction set that produces a document to a spec (`SKILL.md`), the same
way for the same request every time. It never decides the trial design
itself. That narrowness is stated as a design fact, not judged as a strength
or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill designs the trial" → "the
skill drafts the document; a person still designs the trial."
