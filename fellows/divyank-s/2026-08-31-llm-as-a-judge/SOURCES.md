# SOURCES.md — Claude, Judged.

## Primary citation

Zheng, L., Chiang, W-L., Sheng, Y., et al. (2023). *"Judging LLM-as-a-Judge
with MT-Bench and Chatbot Arena."* Referenced for the position/verbosity/
self-enhancement bias taxonomy (beats A2-3–A2-5) and the human-preference
validation methodology (beat A4-6). See `FACTCHECK.md` for exactly which
on-screen claims trace to it.

## Archival images (6 total, all real photographs, none AI-generated)

All used as **illustrative metaphor imagery** — none depict LLM evaluation
literally, since the topic (a 2023-era software pattern) has no historical
photographic referent. Each beat's `shot.prompt` and its `media/<BID>.source.txt`
sidecar say so explicitly.

| Beat | Image | Source | License |
|---|---|---|---|
| A1-1 | Folding filing-folders, Boston Index Card Co. | Library of Congress via Wikimedia Commons | No known copyright restrictions |
| A1-3 | "Courtroom One Gavel" | Flickr (Joe Gratz) via Wikimedia Commons | CC0 |
| A2-1 | Helen Campbell, wireless telegraph operator | Library of Congress via Wikimedia Commons | Public domain |
| A2-3 | Scales of Justice statue, Middlesbrough | Wikimedia Commons | CC BY 3.0 |
| A3-1 | Airacobra P-39 assembly line | Library of Congress via Wikimedia Commons | Public domain |
| A4-1 | Douglas SBD-5 Dauntless production line, Aug. 1943 | Wikimedia Commons | Public domain |

All sourced via the Wikimedia Commons API (`commons.wikimedia.org/w/api.php`);
Smithsonian's own search page returns `HTTP 403` to non-browser fetches, so
Wikimedia Commons was used instead, consistent with the standing instruction
this session to source real archival imagery when a beat needs a "character"
or historical image.

## Toolkit / environment note

Two new Remotion compositions, `DivergentFates916` and `BinaryBranch916`,
were added to `runtime/remotion/src/Root.tsx` for this build's 9:16 Short
(see `BUILD-LOG.md`) — no new component code, both patterns already read
their own width/height from `useVideoConfig()`.

## Corrections applied

None.
