# Beat Sheet: "Why AI-Generated Code Still Needs a Human Who Understands the System"
**Creator:** Sai Pranavi Jeedigunta | Film 1 (general-AI-topic series)
**Phase:** 2 — BUILD (per PROOF protocol)

---

## Premise (Phase 1 gate — confirm before beats lock)

**Teachable claim:** A fix can look correct — it addresses the visible symptom — while being wrong at the system level, because it doesn't account for what actually happens when it fails.

**Reusable rubric — "The 3 Questions Before You Trust a Fix":**
1. **Trace** — can you point to the exact execution path this change affects, not just read what's different?
2. **Consequence** — do you know what breaks, silently, if this is wrong?
3. **Why, not just What** — can you explain *why* this is the fix in terms of the system's real behavior, not "it looked right and passed"?

**Falsifiability case:** a stateless, low-consequence utility (e.g., a date formatter). Here, quick trust is reasonable — the rubric scales with consequence, it isn't "never trust AI output."

**Viewer task (scaffolded, not vague):** before merging any AI-suggested fix —
1. Ask the tool: "what specifically breaks if this is wrong, and how would I know?"
2. Trace the one function/file it touches, by hand, for 60 seconds.
3. Write one sentence explaining *why* this fixes the root cause — not just what changed.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| Title | Video title + @HumanitariansAI, silent | No narration, brief opening card before the hook |
| Hook | Split screen: "escaped quotes" code vs. crash log | Both held ≥2s, side by side |
| Framework | 3-question rubric as a static graphic | Full rubric visible before any example starts |
| Worked example | Illustrative before/after code diff (generic example, not a specific real incident) | Font scaled to be readable at video resolution, not a thumbnail |
| Falsifiability | Date-formatter function, one line | On screen alongside the rubric, showing "low stakes" annotation |
| CTA | The 3-step checklist as copyable text | Held ≥3s, no voiceover-only recitation |

---

## Beats

**0. Title (0:00–0:03)**
Visual: opening title card — the video title and @HumanitariansAI, silent, no narration.
*[Added 2026-08-17 per fellow request — the previous cut dove straight into the hook with no title/branding intro]*

**1. Hook (0:03–0:18)**
Visual: a code diff showing quote-escaping "fixed," next to a crash log from the same bug.
VO: "This fix looks right. The quotes are escaped. And it still crashes production."
*[Source on screen: the actual before/after diff, not paraphrased]*

**2. Framework, shown before any example (0:18–0:48)**
Visual: the 3-question rubric appears as a clean graphic — Trace / Consequence / Why.
VO: "Before you trust it, ask yourself all three questions. Trace: can you point to the exact execution path this change touches — not just read what's different? Consequence: do you know what breaks, silently, if this is wrong? Why: can you explain why this is the fix in terms of what the system actually does — not just that it looks right? Three questions. Not two, not one."
*[This is the framework-first requirement — no example has appeared yet. Expanded 2026-08-17 per fellow revision: each question now gets a real explanatory sentence, not just a label. Trace line reworded 2026-08-17: "not just read the diff" -> "not just read what's different" — fellow found "diff" jargon unclear.]*

**3. Worked example (0:48–1:48)**
Visual: an illustrative before/after code diff — a hand-escaped SQL insert, side by side with a parameterized-query fix.
VO walks through each rubric question against this example, now with real explanatory depth:
"Here's a real shape of that problem. This insert escapes single quotes by hand before writing to the database. Trace it: every value gets wrapped in quotes and dropped straight into the SQL string — that's the exact line that runs. Consequence: escaping only handles apostrophes. A backslash, a null byte, an unexpected encoding — any of those slips through, and one bad row aborts the entire batch insert, not just itself. Why does the parameterized version actually fix it? Because it never builds SQL out of untrusted text at all — the values are bound separately from the query, so there's no string for a stray character to break out of. That's not a patch on the symptom. That's removing the failure mode."
*[Both versions of the code legible on screen simultaneously, held through the full explanation. Expanded 2026-08-17: explains the actual SQL-injection mechanics (why quote-escaping alone fails, why parameter binding removes the failure mode) instead of just labeling Trace/Consequence/Why.]*

**4. Falsifiability / edge case (1:48–2:08)**
Visual: a trivial date-formatter function next to the rubric.
VO: "Does this need the same scrutiny? No — and that's the point. Low consequence, low stakes, quick trust is fine. The rubric scales with what breaks if you're wrong."
*[Names the case that would break an absolutist "never trust AI code" framing]*

**5. Scaffolded task (2:08–2:43)**
Visual: the 3-step checklist as copyable on-screen text, each step elaborated as it's spoken.
VO: "So here's what to actually do. Step one: ask the tool directly — what specifically breaks if this is wrong, and how would you know? Don't accept a vague answer. Step two: open the one function or file it touches, and trace it by hand — just sixty seconds, not a full audit. Step three: write one sentence explaining why this fixes the root cause — not just what changed. If you can't write that sentence, you don't understand the fix yet — and neither did the tool that gave it to you."
*[No "just ask Claude" — an actual concrete, repeatable procedure. Expanded 2026-08-17 per fellow revision: each of the 3 steps now gets a real explanatory sentence instead of just being named.]*

**6. Close (2:43–2:53)**
Visual: return to the hook's crash log, now with a checkmark over the corrected fix.
VO: "The code that looks right and the code that is right aren't always the same thing. That gap is where you're still the one doing the job."

**7. Sign-off (2:53–2:58)**
Visual: brand card — @HumanitariansAI, in for Sai Pranavi Jeedigunta.
VO: "This is Bella, in for Sai Pranavi Jeedigunta, for Humanitarians AI."
*[Added 2026-08-17 per the fellowship's compliance requirement that videos demonstrably come from the volunteer, matching this fellow's other two videos]*

---

## Production Gate Self-Check (pre-review)

- [ ] Rubric graphic appears before the worked example — not narrated after
- [ ] Before/after code diff legible simultaneously, not sequential cuts
- [ ] Falsifiability case shown, not just claimed in voiceover
- [ ] CTA is the literal 3-step text, not a paraphrase or "ask your AI tool"
- [ ] No claim made without a visible on-screen artifact backing it
- [ ] Channel/fellow sign-off card present
- [ ] Opening title card present before the hook

**Estimated runtime:** ~2:58 (revised 2026-08-17 twice: first B01/B02/B04 expanded from labels to real explanation per fellow feedback that the first cut was too vague; then a silent title card added before the hook and the Trace line's "diff" jargon reworded to "what's different") — within a short-form target, all eight beats intact.