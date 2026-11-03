# Meet Muse: What It Is and Why It's Useful — Yeshwanth Balaji

This is a short explainer for the Humanitarians AI Fellows playlist, branded **@HumanitariansAI**. It introduces Muse, a cloud AI agent, to game engineering graduate students who have never used an AI agent. Built with the Brutalist `ai-explainer` skill.

| Film | Landscape | Vertical |
|---|---|---|
| Meet Muse: What It Is and Why It's Useful | 3840×2160, 3:36 | 2160×3840, 3:36 |

This folder is the recipe only: source, scripts and records. The videos are on Drive: [Meet Muse videos](https://drive.google.com/drive/folders/1v0iIpZu8E612fzj3fh_XZXwYUGpiFxYm?usp=sharing).

## This week's contribution

**Question.** What is Muse, what can it do, and how could a game engineer use it?

**Built.** One film, in 16:9 and native 9:16. It covers:

- six key terms: agent, token, MCP, headless, asset, virtual machine;
- the problem Muse addresses: long, multi-step work that ties up your own computer;
- what Muse is: a cloud AI agent that takes a goal, plans, works the steps and checks in before consequential actions;
- your computer vs the cloud: Muse runs on its own virtual machine;
- what it can run: Blender (including headless) for 3D models and art, Godot for simple game prototypes, and possibly Unity and Unreal;
- Muse vs Claude Code;
- ways to use it: offload heavy jobs, run overnight tasks, get first drafts, pair it with other tools;
- three cautions: verify output, limit access, disclose AI work;
- a three-line recap, and a "Your turn" prompt viewers can paste into Claude.

## Human and AI work

**My decisions:**

- the topic, audience and content of the brief;
- showing Muse as a labelled illustration;
- making both 16:9 and 9:16;
- the Fellows branding (Yeshwanth Balaji · @HumanitariansAI);
- that nothing is published from the toolkit.

**AI tools and voices:**

- Claude (Claude Code) wrote the narration, the beat sheet, the scene drawings (`scenes.py`) and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local). It says so in the first line ("I'm Liam, an AI voice, presenting for Yeshwanth Balaji"). It is not a recording of me.

**On screen:** the Muse panel and the Blender and Godot editors are simplified drawings, each tagged "ILLUSTRATION". They are not recordings of real sessions. No account or payment detail appears. Claims about Muse follow my brief (`claude-liam-meet-muse/FACTCHECK.md`).

## Files

| Path | What it is |
|---|---|
| `claude-liam-meet-muse/script.py` | Narration and on-screen text (single source of truth) |
| `claude-liam-meet-muse/scenes.py` | Draws the body scenes, recap and outro in both aspects (Pillow) |
| `claude-liam-meet-muse/make_sheet.py` | Builds `beat_sheet.json` (author → Kokoro → finish) |
| `claude-liam-meet-muse/beat_sheet.json`, `vertical/beat_sheet.json` | Final 16:9 and 9:16 beat sheets with measured durations |
| `FACTCHECK.md`, `SOURCES.md`, `PROMPTS.md`, `SHOTLIST.md`, `BUILD-LOG.md` | Records |
| `TYPECHECK.md`, `_qc/`, `*.verified.json` | GATE T, Gate V and render receipts, for both aspects |
| `BUILD-PROMPT.md` | Full command list to rebuild |

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `22264a3`, plus the one-line portrait-outro change in `ClaudeTitleOutro916.tsx` (not used by this film) |
| Voice | Kokoro-82M v1.0, `am_onyx`, local and free |
| Build | `BUILD-PROMPT.md` |
| Checks | GATE T PASS and Gate V clean (0 blockers) for both aspects. Frames reviewed by eye |
| Cost | $0 (no paid calls) |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape (`muse_yeshwanth_16x9.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1v0iIpZu8E612fzj3fh_XZXwYUGpiFxYm?usp=sharing) | 3840×2160 | 215.7 s | `5808f3ebff0d2142c662d702b725434f347f56035ab7650d47e0e10a39adf206` |
| Vertical (`muse_yeshwanth_9x16.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1v0iIpZu8E612fzj3fh_XZXwYUGpiFxYm?usp=sharing) | 2160×3840 | 215.7 s | `5fa691b487b02c69a3a043577cef38b573dee3ee15e4c3dc95a98322640c8631` |

**How the vertical was made.** It is native 9:16, not a crop.

- Every body scene is redrawn in portrait by `scenes.py` with large type.
- The bookends use the toolkit's portrait Remotion compositions.
- Narration and timing are identical to the landscape film.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
