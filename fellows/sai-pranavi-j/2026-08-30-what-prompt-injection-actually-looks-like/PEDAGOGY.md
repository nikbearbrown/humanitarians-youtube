# PEDAGOGY — Prompt Injection: The Vulnerability Hiding in Plain Text

Single-topic `ai-explainer` reel (147.94s), general-AI-topic series (distinct from this fellow's
weekly work-report series). Audience: engineers building AI agents. Thesis: an AI agent that reads
text from outside the conversation (a web page, an email, a file) has no built-in way to tell a
sentence from a command — unless something teaches it to ask three questions first.

This video's genre — framework-first explainer with a worked example + a falsifiability case +
a scaffolded task — is the same genre `PROOF.md` targets, and the same genre as this fellow's
`2026-08-17-why-ai-generated-code-still-needs-a-human/` (which scored 11/12). A real,
non-genre-mismatched score is expected here.

## Act structure

- B00 TITLE — silent title card (title + @HumanitariansAI)
- B01 EXEC-SUMMARY — spoken personal-intro card, name + one-line summary
- B02 HOOK — a summarizer agent's page view; a buried near-invisible instruction, revealed by a
  callout, not just narrated
- B03 FRAMEWORK — the 3-question rubric (Source / Instruction-or-Data / Consequence), shown in
  full, before any example, with an OWASP LLM01 citation
- B04 WORKED-EXAMPLE — the hidden instruction, legible, walked through all 3 rubric questions,
  resolved together on screen — verdict: ATTACK
- B05 FALSIFIABILITY — the recipe-blog line (a genuinely similar-looking imperative sentence),
  walked through the same 3 questions, resolved differently — verdict: BENIGN
- B06 SCAFFOLDED-TASK — the 3 questions restated as a distinct audit checklist, not a copy of B03
- B07 TAKEAWAY — statement card
- B08 SIGN-OFF — channel/fellow credit

## Self-score against the PROOF.md rubric (0-2 each, /12)

| Criterion | Score | Note |
|---|---|---|
| Explicit framework | 2 | B03's rubric card (Source / Instruction-or-Data / Consequence) lands before B04's or B05's example, with all 3 questions shown together, not narrated after the fact |
| Reusable rubric | 2 | The same 3 axes are applied twice, to two different cases (B04, B05), reaching opposite verdicts — this is the strongest evidence the rubric is a real, reusable method and not decorative labels |
| Worked example | 2 | B04 shows the reasoning step for each axis (why it's the page not the user; why it's a command not content; why it's irreversible), not just the ATTACK conclusion |
| Falsifiability / edge case | 2 | B05 is a genuine stress test, not a strawman — "preheat your oven to four hundred degrees" is grammatically identical in form (an imperative sentence) to the B04 attack, and the video runs the *same three questions* to reach the opposite, correct verdict |
| Active task | 2 | B06's task hands over the literal 3 questions plus a decision rule ("can't answer consequence with 'nothing bad happens'? harden it") — not "ask Claude" |
| Friction | 1 | The recipe-blog tension is real (same sentence shape, opposite verdict), but B05 resolves it within the same beat the question is posed, in step with narration — the viewer is walked to the answer rather than made to sit with the ambiguity first. Same category of note as the AI-code sibling's own Friction score |

**Total: 11/12** (self-check only — not a fellow sign-off; this project's `beat_sheet.json` Gate P
was approved on narrative content, not against this specific rubric).

## Production gate self-check

- [x] Framework (B03) shown fully, before any example
- [x] The hidden instruction text (B02, B04) is legible on screen, not narration-only — confirmed
  via rendered frames and `_qc/contact_sheet.png`
- [x] B04's 3 rubric answers all shown together, not implied — confirmed on the rendered master
- [x] Falsifiability case (B05) uses a genuinely similar-looking sentence, not a strawman, and
  shows a visibly different resolution from B04 (crimson/dark-theme ATTACK vs. teal-sage/
  light-theme BENIGN — a deliberate accent-color and background contrast, not just different text)
- [x] Scaffolded task (B06) is a concrete action with a decision rule, not a restatement of B03 —
  distinct checklist/checkbox visual treatment confirmed against B03's numbered-badge treatment
- [x] Silent title card present; brand/fellow sign-off card present
- [x] Worked example is clearly generic/illustrative, not a real disclosed exploit — see
  `FACTCHECK.md`
- **[~] Side-by-side at the moment of comparison** — PROOF.md's production gate asks for A and B
  on screen *together* when the video claims "X but not Y." Here, B04 (attack) and B05 (benign) are
  two separate, sequential beats — each fully legible and held for its own multi-second hold, but
  never simultaneously in the same frame. This is a genuine partial-pass, not a fabricated PASS:
  the comparison is legible and narration explicitly calls back ("same sentence shape as the
  attack" in B05), but a viewer would need to remember B04's card rather than see it beside B05's.
  Fixing this to a true side-by-side would require a 10th beat or a split-screen redesign of B04/
  B05 — out of scope for this build; noted here for a future revision rather than silently passed.

## Evidence discipline (source: FACTCHECK.md)

| Claim | Verdict |
|---|---|
| Prompt injection as a named, real vulnerability class (B03) | PASS — sourced to OWASP Top 10 for LLM Applications (LLM01), cited on screen |
| Hidden-instruction worked example (B02, B04) | PASS — explicitly generic/hypothetical, not attributed to a real incident |
| Recipe-blog falsifiability case (B05) | PASS — editorial/illustrative, no factual claim requiring a source |
| The 3-question rubric itself (B03, B06) | PASS — editorial framework, not an empirical claim |

## Compliance

Sign-off card present (B08: "@HumanitariansAI, in for Sai Pranavi Jeedigunta"), matching this
fellow's other videos and the fellowship's requirement that videos demonstrably come from the
volunteer.

## Friction protected

- Kept: the falsifiability case (B05) even though it complicates the hook's simplicity — cutting it
  would let the rubric read as "any imperative sentence in fetched text is suspicious," which is
  exactly the naive over-trigger this video argues against.
- Deliberately excluded: any real product, company, or CVE name for either example, and any
  step-by-step attack-construction detail beyond what's needed to make the rubric legible — this is
  defensive/educational content, not an exploit tutorial. See `FACTCHECK.md`.

## Gate P sign-off

Beat-by-beat outline (`BEAT-SHEET.md`) reviewed and approved by the fellow, 2026-08-30, before any
audio generation.

VERDICT: PASS
