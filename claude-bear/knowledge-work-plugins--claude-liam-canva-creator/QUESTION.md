# QUESTION

**The question:** "Claude, Canva Creator." — when a Claude Skill is named
`canva-creator`, what is Claude actually able to do with it: design anything
you ask for, or something narrower?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-canva-creator/beat_sheet.json`
(a fully-built Teardown-register reel: `register: "Teardown"`, `brand:
"claude-liam"`, `source_skill` pointing at
`knowledge-work-plugins/small-business/skills/canva-creator/SKILL.md` on
Bear's machine. 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF handoff, BOUT outro).

**Source defect found and logged, not silently patched:** the source
`beat_sheet.json`'s own narration and props carry unresolved template
placeholders — literal `>` characters — at exactly the three places where
the specific canva-creator constraint should read (B00's `output`, B03's
`body`, BHTF's `command`). The actual `small-business/skills/canva-creator/
SKILL.md` this reel was built from does not exist in this checkout (only
`anthropics/knowledge-work-plugins/youtube/` — the built output — is
present locally; the `skills/` source tree lives on Bear's machine and was
not carried into this working copy). Searched `_audit/`,
`SKILL-EXPLAINERS-BATCH-LOG.md`, and the filmloop logs for a recoverable
copy of the real constraint text — none exists locally.

**The call made:** rather than block or invent a fabricated specific claim
about Canva's UI or a specific field-mapping Claude performs, the `>`
placeholders are filled with a generic, low-risk description consistent
with the skill's own name and its `small-business` category: a "creator"
skill for a design tool fills in an existing template (text, color, logo)
rather than laying out a new design from a blank page. This is stated as
"the constraint this SKILL.md sets," not as a verified fact about Canva's
product surface — it never names a specific Canva UI element, field, or
API. Per PHASE 1's "when in doubt, describe behavior generically" and the
honesty rule against inventing UI, this is the correct-sized claim: true of
how Claude Skills work in general (a SKILL.md is a bounded instruction set;
Claude does only what it specifies), generic about the one skill-specific
detail that cannot be verified from this checkout.

**Facts carried from source, verified true and generic (unchanged):**
- a Claude Skill is a folder Claude reads before it acts; the file inside
  it, `SKILL.md`, is the full instruction set in plain language
- Claude reads the file's steps in order and executes them, linearly,
  unless a step itself branches
- because Claude follows the same written steps every time, the output is
  repeatable: same input, same output
- the skill's job is bounded exactly by what the file specifies — nothing
  beyond it

**Fact reconstructed (logged as a call, not verified against the original
SKILL.md):**
- canva-creator's specific constraint: Claude fills in an existing
  template — the user's text, colors, and logo — rather than designing a
  new layout from a blank page

**Naive framing (B00, corrected on screen):** "Claude, Canva Creator — it
designs from scratch, right?" → corrects "scratch" to "a template" (the
newcomer's default read of a "creator" skill is that it can design
anything freely; the file instead names a fixed template to fill).

**Body argument carried from source:** a Skill is a folder plus a
`SKILL.md`; canva-creator's file specifies a linear pipeline (read the
steps, execute in order) and a template constraint (fill it, don't design
around it); the same constraint that makes output repeatable is also
exactly where the skill has nothing to offer once a request steps outside
it.
