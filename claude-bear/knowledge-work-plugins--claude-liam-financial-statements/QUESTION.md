# QUESTION

**The question:** "Claude, Financial Statements." — when Claude flags a
variance as material inside a financial-statements skill, is that Claude's
own accounting judgment, or is something else going on?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-financial-statements/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION, no
puppet/AI-video/pantry beat to replace beyond the WRITER LAW swap).

**Source fact base (unlike the `cash-flow-snapshot` sibling in the same
batch, this source's template slot filled correctly at every occurrence):**
the skill's own description survives intact in B00/B03/BVDT's narration —
"Generate financial statements (income statement, balance sheet, cash
flow) with period-over-period comparison and variance analysis. Use when
preparing a monthly or quarterly P&L, closing the books and need to flag
material variances, comparing actuals to budget, building a financial
summary for leadership review, or looking up GAAP presentation
requirements and period-end adjustments." No local copy of the skill's
`SKILL.md` itself exists on this machine (source metadata's
`source_skill` path resolves on a different machine), so this redo states
only what the source's own beats already confirm and never invents a
specific variance threshold, GAAP line item, or output format.

**Why it earns a reel:** "material variance" sounds like a judgment call —
the kind of thing an experienced accountant decides by feel. It isn't,
here. `financial-statements` is a written spec: a `SKILL.md` file Claude
reads before it works, telling it to build the income statement, balance
sheet, and cash flow statement, compare each period to the last, and flag
what crosses a threshold — a rule the file sets, not a judgment Claude
applies. Run the same request twice and the same steps run twice,
producing the same statements and the same flags both times. That
determinism is the whole guarantee the skill makes; it is also the whole
limit — only what the file says, nothing outside the spec.

**Naive framing (B00, corrected on screen):** "Claude decides what's a
material variance. Right?" → corrects "decides" to "checks" (Claude does
not apply its own accounting judgment; it checks the numbers against a
rule already written in the file).

**Body facts carried from source (unchanged):**
- a skill is a folder/file Claude reads before it works, not a judgment
  module it improvises
- `financial-statements`'s job, verbatim from the source: generate the
  income statement, balance sheet, and cash flow statement, with
  period-over-period comparison and variance analysis
- used for a monthly/quarterly P&L, closing the books and flagging
  material variances, comparing actuals to budget, a leadership summary,
  or GAAP presentation/period-end adjustment lookups
- the pipeline lives in the Steps section; Claude executes each step in
  order — linear, no branching unless a step says so
- same input → same output, every run — the whole guarantee a skill makes
- the limit is only what the file says — nothing outside the spec
- Your Turn: ask Claude to read the skill's own SKILL.md before running it
  and explain, in its own words, what makes a variance count as material

**Deliberately not claimed:** the specific numeric threshold, GAAP line
items, or exact output layout the skill's SKILL.md defines for "material" —
that level of detail is not in the source and is not invented here. See
CARRY-OUT.md.
