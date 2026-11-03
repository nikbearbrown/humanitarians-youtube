# QUESTION

**The question:** If every person on a team is individually careful with
Claude, is the team automatically safe?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-liam-vox-team-fence-gap/beat_sheet.json`
("Why Individual Caution Does Not Add Up to Team Safety," Teardown-register,
`brand: "claude-liam"`, cold open `ClaudeComposerAsk`, GRAPHIC/CARD body beats
B01–B08 with Manim scenes in `scenes_std.py`, `YOURTURN`, `OUTRO`, plus three
unused empty BOOKEND placeholders). The source's body narration (B01–B08) was
fully written; the facts carry forward compressed for the Plain register and
the hai-simple ten-beat shape.

**Why it earns a reel:** the natural assumption is that careful individuals
add up to a careful team — five people, each sensible with their own agent,
should sum to a team with nothing to worry about. But agents act on shared
assets, not just personal ones. A connector added by one person for their own
use can be added at the *account* level, which every teammate's agent then
inherits — nobody voted on that, and nobody watches the boundary between
five individually careful practices.

**Naive framing (B00, corrected on screen):** "Five careful people using
Claude on a team. Does that make us safe?" → corrects "us" to "the team" (the
real frame: personal safety and team safety are not the same question).

**Body facts carried from source (unchanged):**
- five teammates each use Claude carefully and individually, with no shared
  rules across the team (source B01)
- one adds a connector (an MCP server) to read the shared team Dropbox; it
  is added at the *account* level, not scoped to that one person (source B01,
  B05)
- all five teammates' agents now have read access to every file in Dropbox,
  including a client contract marked confidential — no one intended this,
  no one knew (source B01, B05)
- individual practice does not aggregate into team safety when agents act on
  shared assets; the accountability gap sits at the boundary between people,
  not inside anyone's careful practice (source B03, B04)
- the fix is shared rules that exist *before* individual use begins: name
  what data each agent can reach, name who approves an account-level
  connector, name who is accountable if something leaks (source B06, B07)

**Compression, per the constitution/IVP/IAG/MPC redo precedent:** ten
beats — B00 (writer) + B01–B06 (body) + BCRY + BHTF + BOUT. B01 plants the
anchor (five fenced individuals, one unfenced shared folder) and states the
concrete case. B02 states the wrong guess (careful individuals should sum to
a careful team). B03 breaks it with the anchor's own case and locates the gap
at the boundary. B04 states the mechanism plainly (the shared folder belongs
to everyone, which in practice means no one). B05 covers direction A (not
every shared thing needs a rule — a private, unshared read isn't a team-level
risk). B06 covers direction B (the fix was never "be more careful," it's
naming the fence before anyone connects anything) and pays off the anchor
with the fence now drawn around the shared center.

**No inference flag.** Every claim here describes an access-control fact
(what an account-level connector does, where the shared asset sits) rather
than an empirical claim about model internals needing a hedge. Per `simple`'s
ONE-FLAG LAW: "if the source genuinely supports everything, there is no
flag."
