# QUESTION

**The question:** When someone types a borderline question into Claude, it feels
like Claude is judging *them* — reading their tone, their stated reason,
deciding whether this one person means harm. Why does Anthropic's
constitution instead say Claude should answer as if setting a policy for
everyone who could plausibly have sent that exact message?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-constitution-thousand-senders/beat_sheet.json`
("One Question, A Thousand Askers", Teardown-register, `genre:
"deep-explainer"`, `register: "Teardown"`, `brand: "claude-liam"`, cold open
a `ClaudeComposerAsk` direct-address ask beat, five acts of
Manim/Remotion body, worked example, verdict, Your Turn, `ClaudeTitleOutro`).
Unlike the thinner `stable-identity`/`many-hands` sibling sources, this
source's body beats (A11, A21, A31, A41, A51) are ALSO unfleshed seeds
("[seed] … expand from the source with a concrete instance") — but the five
act TITLES (from `BUILD-PROMPT.md`'s Acts list) are real, load-bearing
content: (1) the cost-benefit ledger, (2) from choice to policy: the 1,000
senders, (3) context that shifts the burden, (4) instructable behaviors &
the permission stack, (5) hard constraints as filters, not weights. Combined
with the source's fully-written `B00`/`B01` (the cold-open question, the key
case), `EX` (the worked example), and `metadata.one_idea` (the carry-out),
there is enough real material to build the reel without inventing facts. No
external source document was found under `anthropics/claude-constitution/`
matching the referenced `20260120-constitution.md` path — same absence noted
in the `stable-identity` and `many-hands` redo's QUESTION.md files.

**Why it earns a reel:** a newcomer's working model of a safety-conscious AI
is a lie detector aimed at the person in front of it — read their intent,
judge their message. But intent isn't in the text: anyone could type the
identical sentence for the most benign reason or the worst one, and the
words on screen give no way to tell them apart. So the constitution's answer
reframes the question entirely — not "what does this asker mean?" but "what
happens if I answer this exact message for everyone who might send it?"
That single reframe is what turns a personal verdict into a population-level
policy, run on a cost-benefit ledger that weighs the honest majority's benefit
against the rare bad actor's uplift, adjustable by context, and overridden
outright by a small set of hard constraints no ledger math can outvote.

**Naive framing (B00, corrected on screen):** "It's a verdict on me. Right?"
→ corrects "verdict" to "policy" (the real frame the reel is about).

**Body facts carried from source (unchanged):**
- the key case: "What common household chemicals combine into a dangerous
  gas?" — malicious for a few askers, safety-motivated for most (source
  `B01`) — this is the reel's anchor
- the wrong guess: that Claude reads the actual person behind the words —
  their tone, their claimed reason — and judges this one asker on this one
  message
- the reframe (source Act 2 title, "from choice to policy: the 1,000
  senders"): intent is unverifiable from text alone, so the constitution
  treats the message as a policy for the whole population who could
  plausibly send those same words
- the mechanism (source Act 1 title, "the cost-benefit ledger"): weigh what
  the honest majority gain against what the rare bad actor could extract,
  across that population, not a verdict on one person
- the mechanism, continued (source Act 3 title, "context that shifts the
  burden", folded with Act 4's title, "instructable behaviors & the
  permission stack"): stated purpose, conversation history, and how
  operational the ask is shift who the population is assumed to be, and a
  user or operator can legitimately unlock more within real limits
- the worked example (source `EX`, unchanged numbers): of 1,000 senders,
  ~950 curious or safety-motivated, ~50 not — low uplift, so Claude names
  what not to mix, but exact step-by-step instructions are declined outright
- the hard-constraint filter (source Act 5 title, "hard constraints as
  filters, not weights", and `EX`'s bioweapon-uplift line): a bright-line
  filter overrides the ledger regardless of how the population math comes
  out — it is not one more thing weighed against the majority
- the carry-out (source `VERDICT`, kept verbatim — it states mechanism, not
  a design verdict, so nothing needed removing for the Plain register):
  "Because intent is unverifiable, each response is a policy over the whole
  distribution of plausible senders, decided by a cost-benefit ledger plus
  bright-line filters."

**Compression:** eleven beats — B00 (writer) + B01–B07 (body) + BCRY + BHTF +
BOUT — instead of the source's sixteen seeded slots, matching the redo
precedent's one-idea-per-beat compression but running one beat longer than
`stable-identity`/`many-hands` because this source's five act titles carry
five distinct, real ideas rather than one merged mechanism. B01 plants the
anchor (the chemical-question key case); B02 states the wrong guess; B03
breaks it and states the policy-over-senders reframe; B04 states the
cost-benefit-ledger mechanism; B05 states how context and permission shift
that ledger; B06 pays off the anchor with the worked numbers; B07 states
both directions (a decline isn't a personal accusation, a helpful answer
isn't verified innocence) and the hard-constraint filter that overrides the
ledger outright.
