# FRICTIONAL: fellowship renewal and MoE Causal Atlas videos

## 2026-11-23: covers Nov 16 – 23 (written Nov 23)

**Working on:**
- The MoE Causal Atlas G0(b) and G0(c) results.
- Seven Brutalist videos turning project findings into practices people can apply.
- This renewal report.

**Tried / expected:**
- Expected the 9:16 versions to come straight out of `art vertical` once the 16:9 masters passed every gate.
- Expected each video to take one finish pass per ratio.

**Where it resisted, and what I did:**
- **Portrait text size.** The type gate's portrait floor (1.9% of 3840 px) allows about 25 characters per line, so the code and table scenes failed. In 9:16, I moved them onto the portrait verdict card. The code card is labeled "key lines, condensed".
- **Handle placement.** The @HumanitariansAI handle burned into the intro sat outside the 9:16 title-safe area. On the logo outro it was below the type floor and inside the Shorts UI strip. I moved it and scaled it for portrait only, then re-exported all seven 9:16 masters.
- **One video kept an old sheet.** Video 5's code scene still had the old title and small text. I fixed the sheet and re-rendered it.
- **Windows toolkit issues.** The npx path, ffmpeg drawtext font-path escaping, and a missing `ClaudeCodeBeat916` composition. Each got a small local patch.

**Claude's contribution, and what I accepted or changed:**
- Claude drafted the scripts from the repo records and ran the render and gate loop.
- I chose one topic per week and the Bella voice, and required that the AI narration is disclosed.
- I accepted the portrait card conversions and rejected nothing.

**Now understood / still open:**
- The gates measure the frame the checker samples, so a pass can be luck. The outro passed in six reels only because it was sampled mid-animation.
- Still open: two distinct videos per week from Dec 1, a weekly `slides.html`, and a Frictional entry written during the week rather than after it.

Evidence: [RENEWAL.md](./RENEWAL.md) · [G0(b) d54b861](https://github.com/GeneralMing/moe-causal-atlas/commit/d54b861) · [D4 plan 2fcb0a6](https://github.com/GeneralMing/moe-causal-atlas/commit/2fcb0a6)
