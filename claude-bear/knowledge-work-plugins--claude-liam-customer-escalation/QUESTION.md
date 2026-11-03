# QUESTION

**The question:** "Claude, Customer Escalation." — when you ask Claude to
escalate a customer issue, does it just forward the complaint to whichever
team seems right, the way flagging a message in chat works — or is
something else going on first?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-customer-escalation/beat_sheet.json`
(a Teardown-register batch build, brand `claude-liam`, `@NikBearBrown`, 7
beats: B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro).

**Source fully readable, unlike some `knowledge-work-plugins` siblings:**
the real skill file IS present in this workspace:
`/Users/nik/Documents/Cowork/anthropics/knowledge-work-plugins/customer-support/skills/customer-escalation/SKILL.md`.
This redo is built from the actual skill text, not from the source
sheet's compressed narration alone.

**Facts carried from the real SKILL.md (verified, not invented):**
- The workflow runs six steps before anything is generated or sent:
  (1) Understand the issue — what's broken, who's affected, how long,
  what's been tried, why escalate now; checked against the "Escalate vs.
  Handle in Support" criteria before proceeding; (2) Gather context from
  connected sources (support platform, CRM, chat, project tracker,
  knowledge base); (3) Assess business impact across five dimensions —
  breadth, depth, duration, revenue, time pressure; (4) Determine the
  escalation target using a fixed tier ladder; (5) Structure reproduction
  steps, for bugs; (6) Generate the escalation brief itself (severity,
  impact, issue description, what's been tried, repro steps, customer
  communication, what's needed, deadline).
- The escalation tiers are fixed, not a guess: L1 → L2 (support
  escalation), L2 → Engineering (confirmed bug, infra issue), L2 →
  Product (feature gap, design decision needed), Any → Security
  (bypasses the normal tier ladder entirely — escalates immediately
  regardless of level), Any → Leadership (high-revenue churn risk, SLA
  breach on a critical account, cross-functional decision).
- The skill's own "Handle in Support When" list means the same checklist
  can also conclude that nothing should be escalated at all — a
  documented solution, a configuration fix, or a previously-resolved
  pattern stays in support.
- After the brief is generated, the skill does not act on its own — it
  offers next steps ("Want me to post this in a chat channel for the
  target team?" / "Should I update the customer?" / "Want me to set a
  follow-up reminder?") and needs a yes before doing any of them.
- Four documented usage examples ship in the skill's own README-style
  usage block, including "API returning 500 errors intermittently for
  Acme Corp" — used here as the anchor scenario. It is the skill's own
  illustrative example, not a real support ticket or a claim about a
  real customer.

**Anchor (the skill's own documented example, not invented):** "API
returning 500 errors intermittently for Acme Corp." Introduced at B01,
paid off at B03.

**Naive framing (B00, corrected on screen):** "Escalate this bug to
engineering — just forward it, right?" → corrects "forward" to "package"
(the newcomer's default read of "escalate" is a one-click handoff; the
skill's actual first move is building a structured case, not relaying
the raw complaint).

**Your Turn (generalized):** the skill's own template names support
platforms, a CRM, and a project tracker as optional connected sources a
given viewer may not have wired up. The lesson generalizes cleanly:
describe a real or made-up support issue to Claude, ask it to run the
customer-escalation checklist on it, and watch whether it drafts a full
brief and asks before sending or posting anything — or just reacts.
