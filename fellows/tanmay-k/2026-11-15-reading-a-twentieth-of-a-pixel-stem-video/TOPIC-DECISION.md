# Week 31 — Topic selection (2026-11-16)

**Rule:** the topic comes from a `claude-for-<topic>/<topic>` folder in `humanitarians-youtube`, and is available only if no fellow (including us) has covered it.

## Method (read-only)
- 90 branches and their trees were read through the GitHub API with GET requests only; nothing was fetched, checked out, pushed or written in the shared repository.
- Pool: every `claude-for-*/<topic>` path with variant prefixes stripped gave 1,338 topic keys.
- "Taken": a `fellows/*/*` folder on any branch whose name matches the topic's key words, or a topic word that appears in our own Weeks 15 to 30 angle and README notes. 920 keys were taken and 363 free.
- Excluded by hand: chapter lectures, numbered volume series, political items, our own past topics, topics rejected earlier, person-profile and tool-demo folders. 264 candidates remained.
- Draw: five names picked with `random.SystemRandom`: stationary-phase, helium-superfluidity, hpv-vaccination-elimination, vol4-chsh-angle-explorer, sir-epidemic-hub.

## Draw 1: `claude-for-quantum-mechanics/stationary-phase` (rejected by Tanmay)
No fellow folder matched it, but it was rejected and a redraw was requested.

## Draw 2: `claude-for-design/galaxy-doppler` (chosen)
- The library holds one persona variant (`medhavy-vox-galaxy-doppler`) and a copy under `claude/claude-youtube`: the library film "How Astronomers Weigh a Galaxy Using Only Light". No fellow folder matches doppler, redshift, galaxy, Hubble or cosmology, and none of our Weeks 15 to 30 notes use the idea (the Week 18 to 20 notes list it only as a library item).
- The library film sets up the Doppler formula, Andromeda's blueshift and rotation curves. It does not say how finely a shift can be read or what that costs. Our film starts from the same puzzle and answers that: **a shift is read to a twentieth of a pixel, and the price is photons** (`ANGLE.md`).

## Uniqueness check on the angle
The library film was read before the angle was formed (`ANGLE.md` lists what it states and what it leaves open); it does not state the width over square-root-of-photons rule or measure it. The fellow-folder and Weeks 15 to 30 note checks are the ones above; a fuller narration-by-narration sweep of our earlier videos was not run for this topic video. Boundaries and what the film does not claim are in `ANGLE.md` and `FACTCHECK.md`.
