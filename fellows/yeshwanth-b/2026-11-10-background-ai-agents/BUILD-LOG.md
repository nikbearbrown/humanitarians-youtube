# BUILD-LOG — Background AI Agents: How AI Works While You Don't

- **Skill and channel.** `ai-explainer` on the `claude-hai` channel, at Yeshwanth's request (2026-11-10), replacing the first cut's `claude-liam` default. The narrator persona is Yeshwanth Balaji ("Hola, this is Yeshwanth Balaji"; greeting "Hola, Yeshwanth"). The voice is still the local AI voice Kokoro `am_onyx`; it is not a recording of Yeshwanth. All chips, corner marks and cards read @HumanitariansAI, and the corner mark uses the Humanitarians AI wordmark (`public/hai-wordmark-outlined.svg`). The name is said Yesh-wunth ba-LAA-jee through the beat sheet's `pronounce` lexicon; the on-screen text is unchanged.
- **Outro.** OUTRO-LOCK reserves `ClaudeTitleOutro` (hardcoded @NikBearBrown handle and mascot) for claude-liam reels, so this film uses a new `ChannelTitleOutro`: the title restated with the terracotta period, the wordmark and the handle, spoken as the title then "Humanitarians AI." No mascot, no music.
- **Deviation: PROFESSOR BEAR LAW.** At Yeshwanth's request, "you" in B02 and B05 is a generic user-profile silhouette, not a Professor Bear portrait. The components keep the portrait as their default (`avatar: 'bear'`); this reel passes `avatar: 'profile'`.
- **Library first (GATE L).** `./art scenes` was searched for each visual. The closest hit, `CodingAgentsFig1Loop`, is hard-wired to one survey's numbers, and `CCShell` lays out at a fixed 1920×1080. That was a genuine miss, so six parametric components were added to the toolkit in `runtime/remotion/src/scenes/BackgroundAgents.tsx`, registered in `Root.tsx` as 16:9 ids plus `*916` portrait ids, plus `ChannelTitleOutro` / `ChannelTitleOutro916`. Each lays itself out for either aspect:
  - `AgentChatVsLoop`
  - `AgentLoopCycle`
  - `AgentRunLog`
  - `AgentBackgroundLanes`
  - `AgentChecklist`
  - `AgentFitSort`
- **Cues on the spoken word.** `runtime/scripts/align.py` (faster-whisper) writes `mp3/words.json`; `make_sheet.py finish` places every reveal on the first word of its phrase.
- **Deviation: ASK → RESULT micro-beats.** The diagrams (B02, B03, B05, B07, B09, B10) are not each preceded by a composer beat showing a generation prompt. Six extra composer beats would turn a five-minute lesson into UI wallpaper, against ILLUSTRATE LAW. The cold open's composer is itself the ask whose result is shown in B04.
- **Length.** 4:16 against the requested ~5 minutes. The supplied script read at a teaching pace is shorter than that. Three teaching beats were added (B04, B06, B08) instead of padding.
