# CARRY-OUT.md (GATE C)

**Carry-out sentence (BCRY):**
> That single HTML file isn't handwritten — it's bundled from a real React project.
> One script provisions the stack, one script collapses it back down to a file
> you can share.

**Wrong guess it defeats:** a newcomer assumes a complex claude.ai artifact — a
dashboard, a multi-tab tool — is still just Claude typing one HTML file directly,
the way a simple page would be. It isn't. The Web Artifacts Builder first
provisions a full React 18 + TypeScript + Tailwind + shadcn/ui project with one
init script, develops inside that real project, then runs a separate bundle
script that inlines everything — JS, CSS, every dependency — into one
self-contained `bundle.html`. The single file at the end is a compiled output,
not a first draft.

**Test:** "that file isn't handwritten, it's bundled from a real project — one
script sets up the stack, one script collapses it into something shareable"
survives being repeated by someone who wasn't paying full attention, and stays
true — it compresses the actual distinction (provision-then-bundle, not
write-directly), not the topic ("this video is about an artifact-building skill").
