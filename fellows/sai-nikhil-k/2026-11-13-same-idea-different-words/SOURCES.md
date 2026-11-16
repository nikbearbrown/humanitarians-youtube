# SOURCES — Same Idea, Different Words

## What Sai supplied (2026-11-16)

> "Make the 2nd video based on this blog. https://www.oneusefulthing.org/p/fable-52-and-jagged-agi"

Then, asked: ~1 minute (same as the first reel), and "Yes, credited" to showing
Portals worlds under CC BY-NC-SA 4.0.

## Sources

| Source | What it gave | Where |
|---|---|---|
| Ethan Mollick, "Fable 5.2 and Jagged AGI", One Useful Thing, 9 Nov 2026 (© 2026 Ethan Mollick) | The thesis ("almost AGI", jagged in judgement); the working definition of AGI; the Portals story, including "three separate teams of agents created a cyclone of circling animals" and "the AI did not notice these problems itself" | https://www.oneusefulthing.org/p/fable-52-and-jagged-agi (read 2026-11-16) |
| emollick/ai-portals @ `210133f4e718acb7b461f2a40c90661a40a2397f` (release s8f, 471 worlds), CC BY-NC-SA 4.0 | `src/worlds/index.js` (471 entries), `design/descriptions.json` (472 texts), `design/shipped.json` (152 releases), the `?freeze&grab` harness | https://github.com/emollick/ai-portals (shallow clone, 2026-11-16) |
| Re-measurement | `evidence/overlap.py` → `overlap.out`; `evidence/portal_shots.mjs` → the three stills (sidecars in `images/src/`) | this reel |

The post's own figures (6 images, © Mollick, no licence) are not used. The
Portals stills are new renders from the CC BY-NC-SA code, not copies of his
images.

## Claims in the post, and what this reel did with them

| Post says | Checkable? | Here |
|---|---|---|
| Three teams built a cyclone of circling animals (reindeer, manta rays, storks) | the worlds: yes | ✔ all three in `index.js`; shown |
| "over 450" worlds | yes | 471 at `210133f` (README: 471) |
| Rule book: 84 sections, then 204 sections / 87,500 words | no — not in the repo | not used |
| ~12 worlds a day before the fix, 30+ after; 204 worlds in 20 hours; 328 in two days | no — repo is squashed to 2 commits, releases carry no dates | not used |
| "The AI did not notice these problems itself" | no (his account) | narrated as "By his account" |

## Honesty log

- **The zero depends on which text you compare.** Descriptions: 0 shared words
  for all three pairs. Captions (`index.js` `line`): reindeer and manta both say
  "cyclone" (cosine 0.167). The reel claims the descriptions and says on screen
  that the captions differ.
- **Releases:** reindeer and manta shipped in the same release (r2s), storks in
  r3g. "Separate teams" is Mollick's word; the repo can't show teams.
- **First capture attempt timed out** twice: `&seed=7` made the page hang, then
  zsh passed the whole pose list as one argument. Neither run produced an image.
