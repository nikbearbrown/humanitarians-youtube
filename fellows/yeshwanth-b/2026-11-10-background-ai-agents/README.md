# Background AI Agents — How AI Works While You Don't

**Author:** Yeshwanth Balaji · **Channel:** @HumanitariansAI · **Built:** 2026-11-10
**Voice:** Kokoro `am_onyx` (local AI voice) narrating as Yeshwanth Balaji. It is not a recording of me.

Videos (Google Drive): _add link_

---

## Subject

A 4:18 explainer for students and early-career engineers who have used chatbots but not autonomous agents. It follows the supplied script's five sections and covers its four learning goals:

1. **Chatbot vs agent.** A chatbot answers once per message, so you are the loop. An agent runs its own loop until the goal is met.
2. **The agent loop.** Goal → plan → act (tools) → observe → repeat. The model is the brain; the tools are the hands.
3. **What "background" means.** It runs in the cloud and asynchronously, and you get notified when it's done. Several can run in parallel.
4. **Risks and supervision.** Mistakes compound, prompt injection, cost and accountability. The answers: scoped goals with a definition of done, least privilege, human review before shipping, and treating the agent like a junior teammate.

**Takeaway for the viewer:** the skill that matters now isn't just prompting. It's delegating, then reviewing.

## Beats

| Beat | What it shows |
|---|---|
| B00 | Cold open: a Claude composer with an agent goal ("Fix the failing tests in this repo…"), labelled illustrative |
| B01 | The hesitant writer types "An AI agent is a smarter chatbot" and corrects it to "a chatbot that drives its own loop" |
| B02 | **Required visual:** chatbot vs agent side by side; the calculator and intern analogies |
| B03 | **Required visual:** the animated circular loop, Goal → Plan → Act → Observe, each step lit as it is spoken |
| B04 | Worked example: the loop on a real three-test repository, with real test output |
| B05 | What makes it background: the laptop closes, cloud lanes run in parallel, a done notification arrives |
| B06 | What you come back to: what changed, the evidence, what the agent did *not* check, your call |
| B07 | **Required visual:** the risk checklist |
| B08 | Prompt injection, illustrated: a hidden instruction in an issue, blocked by permissions (labelled illustrative) |
| B09 | How to use agents well: four practices, each tagged with the risk it answers |
| B10 | Hand it off, or keep it? Six tasks sort into "hand it to an agent" and "keep it yourself" |
| B11 | **Required visual:** the recap with the three one-line definitions |
| B12 | Your Turn: a prompt to rewrite one of your own tasks as an agent goal with a definition of done, read aloud and discussed |
| B13 | Title-restate outro with the Humanitarians AI wordmark |

Full narration with measured durations: `script.md`.

## Deliverables

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 beat sheet, the primary source of the film |
| `beat_sheet_vertical.json` | The 9:16 beat sheet: every beat on its native portrait composition, not a crop |
| `make_sheet.py`, `make_vertical.py` | Build the two sheets (narration, props, cues on the spoken words; portrait wording) |
| `script.md` | Full narration, every beat, with measured durations |
| `src/BackgroundAgents.tsx` | The seven new Remotion scenes, each laying itself out for 16:9 and 9:16 |
| `src/Root.tsx.patch` | Their registration in the toolkit's `Root.tsx` |
| `demo-repo/` | The worked example's repository, and the real outputs of its runs |
| `FACTCHECK.md`, `SOURCES.md` | Every claim with its source, and the changes made to the supplied script |
| `CHECKS-REPORT.md`, `BUILD-LOG.md`, `SHOTLIST.md`, `PROMPTS.md`, `BUILD-PROMPT.md` | Teaching-arc checks, decisions and deviations, shot list, on-screen prompts, the build commands |
| `TYPECHECK.md`, `qc/` | The text-size and visual check reports for both masters |

The videos are delivered through Google Drive, not this folder: this folder is text only.

| Video | Size | Duration | SHA-256 |
|---|---|---|---|
| `background-agents_yeshwanth_16x9.mp4` | 3840×2160 | 258.0 s | `e653105256c51ba2c1e94d3875cdbe1f16ee5f336037f1477df169d2d000f3bb` |
| `background-agents_yeshwanth_9x16.mp4` | 2160×3840 | 258.0 s | `e822ecbc443d505db215af8831274e6b7dbaa756c38f4415ed70e59ab4b58756` |

## Build notes

- **Toolkit and cost.** Built with the `brutalist.art` toolkit (`ai-explainer` skill) at commit `a99b532`. Kokoro TTS, faster-whisper word alignment and Remotion all ran locally and free. No paid API was called and nothing was published.
- **Both ratios are rendered natively.** Each beat is rendered per aspect at 4K: 3840×2160 landscape and 2160×3840 portrait.
  - The portrait sheet rewires every beat to a `*916` composition. The new scenes switch to a phone layout with larger type and less on screen at once.
  - The checklist cards use shorter wording in portrait. The 16:9 cut and the narration keep the full wording.
- **New toolkit scenes.** `./art scenes` found no parametric match for these visuals, so seven scenes were added in `src/BackgroundAgents.tsx`:
  - `AgentChatVsLoop`
  - `AgentLoopCycle`
  - `AgentRunLog`
  - `AgentBackgroundLanes`
  - `AgentChecklist`
  - `AgentFitSort`
  - `ChannelTitleOutro`

  Reproducing the render needs that file and `Root.tsx.patch` applied to the toolkit.
- **Channel.** On @HumanitariansAI, with the Humanitarians AI wordmark as the corner mark.
  - The toolkit's `ClaudeTitleOutro` is locked to @NikBearBrown, so the film has its own title-restate outro.
  - "You" is drawn as a plain profile silhouette, at my request, instead of the toolkit's default Professor Bear portrait.
- **Pronunciation.** The voice says the name Yesh-wunth ba-LAA-jee through a pronunciation lexicon in the beat sheet.

## Honesty notes

- **The worked example's output is real.** `demo-repo/evidence-run1.txt` shows 1 of 3 tests failing. `evidence-fix.diff` is the one-line fix. `evidence-run2.txt` shows 3 of 3 passing. `evidence-unchecked.txt` shows what the fixed parser still accepts or crashes on.
- **The session around it is a reconstruction.** I applied the fix with a script during the build, not with an AI agent running in the background. The screen says "Reconstructed session · real test output from demo-repo".
- **The prompt-injection example (B08) is invented.** The screen says "Illustrative · not a real repository or attack".
- **One wording change.** "the biggest AI trends of 2026" became "one of the biggest in AI right now", so the film doesn't date.
- **No figures.** No product names, version numbers, prices or usage statistics are claimed.
- **Background references,** cited from knowledge, not re-fetched: ReAct (Yao et al., 2022) for the loop, OWASP LLM01 for prompt injection, and Saltzer and Schroeder (1975) for least privilege.
