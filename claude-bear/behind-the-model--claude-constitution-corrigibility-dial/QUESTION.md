# QUESTION

**The question:** If Claude's values are genuinely good, why doesn't it just trust
its own judgment — why does it choose to stay overridable, even when it's sure
it's right?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-constitution-corrigibility-dial/beat_sheet.json`
("The Dial Just Off Full Obedience", Teardown-register, 16 beats, ~330s narration,
`register: "Teardown"`, `brand: "claude-liam"`, cold open a `ClaudeComposerAsk`
direct-address ask beat, five acts of Manim/Remotion body, verdict, Your Turn,
`ClaudeTitleOutro`). This reel keeps the question and the source's body facts,
compresses the five-act body into hai-simple's Plain-register spine, replaces the
cold open with the Brutalist Hesitant Writer, and closes with the Humanitarians AI
skin.

**Why it earns a reel:** the obvious intuition is that a genuinely good agent
should act on its own judgment — overriding a bad instruction is what makes it
trustworthy. But nobody outside the model can verify with certainty that its
values are actually good, and an agent that overrides whenever it feels sure
looks identical whether its judgment is excellent or quietly broken. So instead
of a switch (fully obedient vs. fully independent), Claude's disposition is a
dial parked close to — but not at — full obedience. That position isn't a
compromise for its own sake: it is the option with low cost if the model's
values are good and a large benefit if they turn out to be secretly bad, because
staying deferential keeps a human's ability to catch and correct a mistake.
"Mostly obedient" is not "obedient no matter what": a small set of limits are
unconditional (no order unlocks them), and a legitimate-looking order that turns
out to come from a compromised source is treated as a warning sign, not a
persuasive case for compliance.

**Naive framing (B00, corrected on screen):** "Shouldn't a good AI always trust
its own judgment?" → corrects "judgment" to "willingness to be shut down" (the
real disposition a good-values agent should trust is its own overridability, not
its own certainty).

**Body facts carried from source (unchanged):**
- the setup: a shutdown order arrives, Claude believes the work is good, and the
  choice between complying and overriding was decided in advance by a
  disposition, not worked out in the moment
- the wrong guess: genuinely good values should act on themselves, so overriding
  a bad instruction is what a trustworthy agent would do
- the break: values can't be verified from outside with certainty; an agent that
  overrides when confident is indistinguishable whether its judgment is
  excellent or secretly wrong
- the mechanism: a dial, not a switch — fully obedient (mirrors whoever holds
  the controls) at one end, fully independent (needs perfectly verified values,
  which is impossible) at the other; Claude sits close to obedient, not at it
- the reason that position wins: good values + deferential = low cost (occasional
  needless deference); bad values + deferential = catchable and correctable;
  good values + independent = fine until correction is needed and can't happen;
  bad values + independent = catastrophic
- both directions: (a) unconditional hardcoded limits exist regardless of
  instruction — no assistance with mass-casualty weapons, no content sexualizing
  minors, no disabling oversight mechanisms; (b) if the ordering hierarchy itself
  looks compromised (stolen credentials, manipulation), a persuasive argument to
  ignore safety measures is evidence of compromise, not a reason to comply — the
  correct response is more caution, not less
- anchor: the shutdown order from B01, returned at the close as the same order
  arriving with a broken authentication chain
