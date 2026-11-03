# FRICTIONAL — Automating the YouTube Review Pipeline

Append-only. Newest entry at the bottom.

*Reconstructed on 2026-09-24 from this folder's own paperwork — `FACTCHECK.md`,
`BUILD-PROMPT.md`, `SHOTLIST.md` and the notes in `beat_sheet.json` — because
no log was kept at the time. Entries below record what those documents show.*

---

## 2026-09-04 — A claim that survived two rounds of hedging, then died in a minute

**Tried / expected.** A beat (B05) arguing that failures cluster because some
fellows run an older copy of the toolkit, from before the render default
changed from 1080 to 2160. The `# 4K-native master (was 1080)` comment in
`run.sh` looked like evidence.

**Where it resisted.** It wasn't true. `brutalist.art`'s first commit —
`279e925`, 22 July 2026 — already reads `HEIGHT=2160`. No version of that repo
ever shipped 1080. The comment refers to a parent toolkit that predates the
repo.

**What I did next.** Cut the beat entirely rather than hedge it further. The
component and its render stayed on disk, unused, and `beat_sheet.json` carries
a note saying not to reinstate it.

**Understood now.** Recorded in `FACTCHECK.md` in the form it deserves: *"a
hedge is not a substitute for a source. Checking `git log` took one minute and
would have prevented the beat being written at all."* The claim had already
survived two rounds of softening the wording — softening is what you do when
you can't source something, and it should have been the signal.

**Rejected.** An accurate replacement was available — the publishing guide
landed five days after the toolkit, so a fellow who pulled in that window has a
working tool and no guide. It was turned down deliberately: it still puts an
individual's process on screen, which is not what the reel is for.

---

## 2026-09-04 — Three more claims cut as false

**Where it resisted.** Fact-checking against primary sources killed three more:

- **"Roughly six uploads a day is a constraint."** Taken from the toolkit's own
  `docs/PUBLISHING.md`, which is out of date. `videos.insert` costs 1 unit
  against a dedicated 100/day allowance. At this volume it isn't a constraint.
- **"The script has to be authorised as a manager."** Delegation is impossible
  — invited channel managers can't act through the API, and service accounts
  return `NoLinkedYouTubeAccount`. Reframed: the owner authorises personally,
  once, and the credential never comes near me.
- **"Liam in for Bear is a branding mistake volunteers forget to fix."** It is
  required behaviour under the IN-FOR-BEAR LAW. Flagging it would have flagged
  correct work. Replaced with the wrong-channel-outro check.

**Understood now.** Two of the three came from trusting the toolkit's own
documentation rather than the upstream source it summarised. The standing rule
set for this reel — nothing on camera without a row in `FACTCHECK.md` — is
what caught them.

---

## 2026-09-04 — The component estimate was wrong by half

**Tried / expected.** Four new Remotion components.

**Where it resisted.** Eight. `SHOTLIST.md` records the correction plainly:
*"The earlier estimate of 'four new components' was low. The honest number is
eight."*

**Understood now.** Only four beats could reuse what already existed. Until the
other eight were built they compiled as labelled request cards, which is how
the tool is meant to behave — the first cut is a watchable previz rather than
a failure.

---

## 2026-09-04 — Windows

**Where it resisted.** `todo.py` writes with no encoding and crashes on cp1252.
`remotion_scenes.py` calls `npx`, which Windows resolves only as `npx.cmd` and
`CreateProcess` will not run — `WinError 2`. `python3` is a Microsoft Store
stub; the real interpreter is `python`. `./setup --install` checks for ffmpeg
and Node but cannot install them.

**What I did next.** `PYTHONUTF8=1` for the first, and drove `npx remotion
render` by hand for the second — writing each beat's props to its own
`_props_B*.json` so they could be passed with `--props=`. Those twelve files
are still in this folder.

**Understood now.** Both are one-line fixes: `encoding="utf-8"`, and
`shutil.which("npx")`.

---

## 2026-09-24 — The components are gone

**What happened.** The eight components were written into a working copy of
`brutalist.art` that has since been replaced with a fresh download. They are
not in the current toolkit: `HaiReviewPipeline.tsx` is absent and none of the
ids are registered in `Root.tsx`.

**Consequence.** This beat sheet cannot be rebuilt as-is. Eight of its twelve
beats reference components that no longer exist.

**What survives.** `PROMPTS.md` holds a full build prompt and prop contract for
each one, `_props_B*.json` holds the exact props each beat rendered with, and
`BUILD-PROMPT.md` holds the end-to-end instruction. Reconstruction is possible;
recovery is not.

**Understood now.** Reel-local Manim scenes live in the reel folder and travel
with it. Remotion components must be registered in the toolkit, so a
Remotion-only reel keeps its visual code somewhere the reel folder cannot
protect. The two reels built on 17 September went through Manim for a different
reason — not modifying someone else's tree — and were self-contained as a side
effect. This reel is the demonstration of what the other choice costs.

**Still open.** Whether to rebuild the eight components from `PROMPTS.md`, and
whether this reel gets a 9:16 companion. It currently has none, which does not
meet the both-formats review gate.
