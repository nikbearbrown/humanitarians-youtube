# PROMPTS — `ai-data-engineering-etl`

Beat-prefixed prompts. Two kinds live here: the prompts that appear **on screen**
(and are therefore content, governed by ASK→RESULT LAW and HANDOFF LAW), and the
build prompts used to author the scenes.

---

## On-screen prompts (content)

**B00 — the cold-open ask** (shown answered, per COLD OPEN LAW)

> here are two schemas — source postgres, target warehouse. map every column, flag
> the mismatches you cannot resolve, and do not guess.

**B02 — the ask half of the ASK→RESULT pair**

> /schema-diff source=orders.sql target=fct_orders.sql — map every column. for each
> mismatch, name the production failure it causes. do not guess a resolution.

**B08 — the HANDOFF prompt** (read aloud verbatim, then discussed)

> Here is my pipeline's source schema and my target warehouse schema. Map every
> column, and for each mismatch tell me the failure it causes in production and the
> assertion that would catch it.

Why this handoff prompt earns the slot: it is not "explain ETL to me". It asks for
the *assertion*, which is the one artefact the episode argues you should be
demanding — it turns the model's detection into your test suite, and it runs
against a pipeline the viewer already owns.

---

## Build prompts (production)

**B01 — `EtlGlueTax`**

> Build a Remotion scene on the Claude cream stage: a SOURCE node and a WAREHOUSE
> node with a pipe between them. Glue-code strips stack into the middle of the pipe
> one at a time, each labelled with a chore, until the stack is visibly taller than
> either endpoint. One terracotta accent on the pile. Pure function of `useP()`.
> Must reflow for portrait: endpoints top and bottom, stack down the middle.

**`EtlStages`** — built, then CUT from this reel at GATE P (the shortening).
It stays registered in `Root.tsx` as a reusable illustration.

> Three stage plates E → T → L. They light in narration order; E and L then dim to
> a one-word aside ("an API call", "a write") while the T plate expands and unrolls
> a ledger of transform rules inside it. `accentIndex` picks which plate carries the
> terracotta. Portrait: stack the plates vertically, arrows vertical, ledger opens
> beneath T.

**B03 — `EtlSchemaMapping`**

> A live schema diff. Two panels of typed columns face each other. Matching rows
> connect with quiet ink connectors; flagged rows connect in terracotta and unfurl a
> flag naming the production failure. A tally counts the matches up to `matched`; a
> footer counter reads "N flagged · 0 resolved" and the second number never moves.
> Carry an on-screen footnote marking the example as illustrative. Portrait: one
> full-width card per mapping — source line above, target line below, connector in
> the left gutter — because two 26-character monospace columns cannot both stay
> legible in a 1080-wide frame. (The first draft said "source panel above, target
> panel below"; that was replaced during layout QC, because stacking the two
> panels puts every connector in the same vertical band.)

**B05 — `EtlWhereAiHelps`**

> A two-sided split with a divider that draws in. Left items arrive with a filled
> terracotta check, one at a time; right items arrive as hollow ink rings that never
> fill. A verdict rule lands last. Portrait: stack the two sides, divider horizontal.

**B06 — `EtlSilentFailure`**

> Rows stream through a pipe. A row counter races to its target and locks with a
> check — the green, passing signal. Below it a second track shows value drift
> creeping away from the source line in terracotta, with no alarm. The punchline
> "runs ≠ right" stamps across both tracks at the end. Portrait: same two tracks,
> more vertical room between them.

---

## Open slots

**None.** Every beat in this reel is machine-renderable, in both aspect ratios.
`pantry/` is empty by design — there is nothing for a human to drop in, and no
beat renders as a slate.

## Beat ids

These are the ids of the signed 10-beat cut. The standalone E/T/L beat was
dropped at GATE P and the remaining beats renumbered; see `PEDAGOGY.md` →
"GATE P amendment".
