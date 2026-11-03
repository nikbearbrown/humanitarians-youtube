# Video 8: From CLI to API — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers turning the patent agent CLI into a real, callable web API — and a real git mistake that briefly cost the whole file.

## B00 — Cold open
One new file. One git command later, it was gone. Not because the code was wrong. Because it was never actually committed.

## B01 — Why an API, not just the CLI
Method: the CLI works, but it only works from a terminal. A real HTTP endpoint means any client — a browser, a frontend, another service — can ask for a patent's reading the same way, without shelling out to Python directly.

## B02 — Wrapping the same, already-verified logic
The API doesn't reimplement anything. One route, one publication number in, the same ClaimsAgent and LineageAgent that were already tested through the CLI, called the same way. A real classify flag, same purpose as the CLI's no-classify option — skip the one part that always costs something real.

## B03 — The real mistake
Mid-build, a git pull failed — diverged branches, a forced update on the remote. Fixing that meant resetting the local main and rebasing the work branch on top of it. The rebase succeeded. The uncommitted new file didn't survive it — it was staged, not committed, and the branch switch during the fix wiped it out.

## B04 — What actually protected the work
The real file wasn't lost for good, because the same content still existed locally, outside git, from building and testing it minutes earlier. Recreated, committed immediately this time, verified again against the same two real patents that had already confirmed the CLI was correct.

## B05 — A second real find, while fixing the first
Checking the README before committing turned up something else: an earlier real update, documenting the Lineage Agent's broader testing, had never actually made it into the main branch at all. Fixed in the same pass, not left for later.

## B06 — Handoff
Your turn. Before switching branches or resetting anything in git, run git status first — a file that's staged but not committed can disappear the moment you check out somewhere else, and it won't warn you.

## B07 — Outro
From CLI to API. Built with Claude, for Humanitarians AI.
