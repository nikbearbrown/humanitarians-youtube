# FACTCHECK — Testing AI Video Editors, and a Setup Guide for New Fellows

Every spoken and on-screen claim, where it comes from, and its verdict. Checked
2026-09-25. "Session record" means the Claude Code transcript of the HyperFrames
test on 2026-09-16 (project `D:\Rohan\Claude\HyperFrames`), read directly — not
recalled.

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` §Two videos, four files — required wording | ✅ verbatim |
| 2 | B00 | Narration is an AI voice (Kokoro af_bella) | `metadata.ai_disclosure`; on-screen disclosure line | ✅ disclosed |
| 3 | B01 | Every tutorial is built scene by scene, by hand | The Suno (3) and Midjourney (6) series: every screen rebuilt as a Remotion component (`fellows/rohan-v/*-suno-*`, `*-midjourney-*` READMEs) | ✅ |
| 4 | B01 | New fellows have to ask around to get into the tools | Rohan, week-02 progress reel B03 ("tribal knowledge: you find out by asking someone") | ✅ his own earlier statement |
| 5 | B02 | Rohan looked at Remotion, HyperFrames, OpenReel and the DaVinci Resolve MCP | Rohan, in chat, 2026-09-25 | ✅ his list |
| 6 | B02 | Remotion: a video written as code; Brutalist is built on it | Brutalist `runtime/remotion/` — every scene in this reel is a Remotion component | ✅ |
| 7 | B02 | HyperFrames: from HeyGen, a video written as a web page (HTML), built for agents | HyperFrames README ("Write HTML. Render video. Built for agents."), repo `heygen-com/hyperframes`, cloned locally at v0.8.43 | ✅ |
| 8 | B02 | OpenReel: open-source editor that runs in the browser | github.com/Augani/openreel-video — "Professional video editing in your browser", MIT, runs client-side | ✅ |
| 9 | B02 | OpenReel's desktop app connects to Claude | OpenReel Desktop is installed on Rohan's machine with an MCP shim registered in `~/.claude.json` (`mcpServers.openreel` → `@openreeldesktop/…/mcp-shim/index.js`) | ✅ — **scoped**: it is configured; it failed to connect in this build session, and no hands-on test is claimed |
| 10 | B02 | DaVinci Resolve via community connectors that let an agent drive it | github.com/samuelgursky/davinci-resolve-mcp (and several forks): MCP server over Resolve's scripting API | ✅ |
| 11 | B02 | …work best with the paid Studio version | Same README: "Blackmagic gates external scripting to Studio"; the free edition is reachable only through an in-app bridge | ✅ — wording kept to "work best", not "require" |
| 12 | B03 | Rohan gave HyperFrames the finished Suno Part 1 footage and narration | Session record, 2026-09-16: footage from `lyrical-literacy/youtube/suno-part-1/media`, audio from `…/mp3` | ✅ |
| 13 | B03 | …asked for word-by-word lit captions and a new intro | Session record: "subtitles … white but the words should light up as the words are being spoken"; "create a beautiful intro sequence" | ✅ |
| 14 | B03 | It came back with a four-minute cut | `out/suno-part-1-glass.mp4`: ffprobe 245.17 s = 4:05 | ✅ measured |
| 15 | B03 | Ninety-four caption lines, none overlapping | Session record: "655 tokens, 94 lines, verified 0 overlaps" | ✅ from the agent's own check; not independently re-counted |
| 16 | B03 | On-screen frames are the agent's real output | Extracted from `suno-part-1-glass.mp4` at t = 2, 12, 44, 78 s (`pantry/hf-t*.png`); source SHA-256 in `pantry/hf-source.sha256` | ✅ |
| 17 | B04 | The glass look disappeared against the cream backgrounds; footage moved onto a dark stage | Session record: "Glass-on-cream mostly disappears"; "the glass card holds your cream footage as a lit object on a dark stage" | ✅ |
| 18 | B04 | Captions copied the phonetic spelling of the name until fixed | Session record: "Your script is spelled phonetically for the TTS. Subtitles now read **Rohan** … not 'Rohaan'" | ✅ |
| 19 | B04 | The render needed about sixty gigabytes of scratch and filled the main drive | Session record: "The render needed ~61 GB of frame scratch and was writing to C:\Users\…\Temp"; "C: is 98% full … the actual reason both earlier renders failed" | ✅ |
| 20 | B04 | Scratch and caches moved to D: | Session record: `.tooling\` layout on D:, junction on C: | ✅ |
| 21 | B04 | The file came out at 1080p, not 4K | ffprobe: 1920 × 1080 | ✅ measured |
| 22 | B05 | Good at captions, titles and an intro | Claims 13–15 | ✅ |
| 23 | B05 | It didn't add new teaching visuals; those came from our scenes | Session record: the agent found the footage "already carries" the graphics and added none of its own | ✅ |
| 24 | B05 | OpenReel and DaVinci Resolve haven't had a hands-on test | No test exists in any session record; Rohan did not report one | ✅ — first draft said "the other three tools", which wrongly included Remotion (in daily use); corrected before render |
| 25 | B06 | The setup guide is in progress | Rohan, in chat, 2026-09-25: "i havent created it yet. just say its in progress" | ✅ — no page of it is shown or claimed |
| 26 | B06 | Discord first; Suno signs in with Discord; Midjourney through the HAI Discord | Suno: Rohan 2026-08-29 ("used the discord option while logging into Suno"); Midjourney: Midjourney Part 1 ("getting in through the Humanitarians AI Discord") | ✅ |
| 27 | B06 | Canva is in the guide | Rohan, 2026-09-25 | ✅ — **how** Canva access works is not stated anywhere in the reel, because it is not yet documented |

## Excluded on purpose

- The HyperFrames output frames between ~1:36 and ~2:05 (the Suno workspace
  mockups) — the source scene hard-codes real Suno users' handles.
- The output's end card (t ≈ 243 s) — its caption and credit line carry the
  presenter's surname, which the fellows repository forbids.
- Any ranking of the four tools: one hands-on test cannot rank four tools, and
  B05 says so.

## Portrait (9:16) wording

The vertical cut carries shortened on-screen strings (`vertical/beat_sheet.json`)
so its text meets the 9:16 type floor. Narration is identical in both cuts. Each
short form was checked against the claims above: "glass look vanished" (17),
"phonetic captions" (18), "61 GB on a full drive" (19), "1080p output" / "1080p, not
4K" (21), "captions, 0 overlaps" (15), "no new diagrams" (23 — "no new visuals" was
rejected: the agent did add captions and an intro), "OPENREEL · RESOLVE" untested
(24), "DISCORD SIGN-IN" / "VIA HAI DISCORD" (26).
