# SCRIPT — "Brutalist, Installed."

Skill: ai-explainer · Channel: claude-hai (@HumanitariansAI) · Voice: Kokoro `af_bella`
Status: **DRAFT v2 — awaiting narration approval (GATE P). No audio generated.**
Spine: cold open → hesitant-writer overview → body → verdict page → Your Turn → title outro.
No dates or times appear in narration or on screen.

v2 changes: both installs credited to Claude Code · second install condensed to 3 beats
(B04–B06) · "hidden assumptions" framing replaced with "agentic video-creation pipeline".

---

## B00 — Cold open (ClaudeComposerAsk)
**Show:** Claude composer, greeting `Hi, Nidhi`. Typed ask: *"Can this laptop run Brutalist? Check every dependency for real."* Running indicator, then result lines land: `audio ✓ · Manim ✓ · Remotion ✓ · equations: needs LaTeX`.
**Narration:**
> Hi, I am Nidhi, and this video is about getting Brutalist running on my laptop. The voice you're hearing is Bella, an AI narrator, telling my story. Spoiler: the answer on screen is yes. It took two attempts, both with Claude Code.

## B01 — Overview (BrutalistHesitantWriter)
**Show:** Writer types *"Brutalist is a video editor."* — hesitates, strikes "a video editor", replaces it with "an agentic video-creation pipeline using Claude". Then: *"I installed it twice with Claude Code. Only the second one worked."*
**Narration:**
> Brutalist is an agentic video-creation pipeline using Claude. You write the script; Claude builds the voice, the animation and the cut. I installed it twice with Claude Code. Only the second one worked.

## B02 — The first attempt
**Show:** Two test-reel folders slide in (`binary-search-test`, `claude-liam-ribosomes-read-mrna`). Each opens its real `build-state.json`; the card types `"status": "failed"` and `"Review pipeline failed (exit 2)"` — terracotta on "failed".
**Narration:**
> My first install, with Claude Code, got further than you'd think. I built two test videos. The narration was generated. Some animations even rendered. But both builds ended the same way: the build-state file says failed, review pipeline, exit two. Neither video made it to a finished cut.

## B03 — What went wrong
**Show:** Left: a real frame from the first attempt's Manim clip, labelled "rendered". Right: the pipeline as a row of stages — audio ✓, animation ✓, review ✗. Two problems drop in under the ✗: *packages wanting an older Python* and *gate checks*.
**Narration:**
> Two problems sat underneath. Some packages needed an older Python than the one on my machine. And the build kept stopping at its gates: deliberate checks that halt the pipeline when something isn't right. I spent hours patching symptoms. Eventually I deleted the old install and started over.

## B04 — Second attempt: a false alarm
**Show:** Code-block `git clone https://github.com/nikbearbrown/brutalist.art.git` → fresh folder. Then the real terminal line: `ElevenLabs reference found — this toolkit is Kokoro-only for narration.` The flagged `youtube/brutalist` folder lifts out of the toolkit; guard flips to `clean`.
**Narration:**
> Second attempt: a clean copy, and Claude Code again, but this time every error got read before anything was fixed. The setup check stopped at once, claiming a paid voice service. It was a false alarm: videos explaining that check, stored inside the toolkit. Moved out, the check passed.

## B05 — The Python fix
**Show:** Left: real Windows output `Python was not found; run without arguments to install from the Microsoft Store…`. Right: a version line — the animation library's supported range shaded, 3.14 outside, 3.12 inside. Then the three real commands light in order: `py -3.12 -m venv .venv` · `cp …python.exe …python3.exe` · `./setup --install`.
**Narration:**
> Then the first attempt's problem came back. My Python was too new for the animation library, and on Windows the scripts couldn't even find it by name. One fix covered both: a separate Python three point twelve environment, a python three command inside it, then the toolkit's own installer.

## B06 — The proof
**Show:** The real readiness table builds row by row, each turning ✅ ready: audio, captions, Manim, Remotion, compile, fonts. The last row stays ❌ "equation beats — needs LaTeX", tagged "not needed for this video".
**Narration:**
> Then the check that matters. Voice: ready. Captions, animation, scenes, compiling: ready. One row stays blocked: equations need LaTeX. This video has no equations, so that one can wait.

## B07 — Verdict
**Show:** Artifact page, "What I learned", three lines arriving in order: *Read the error first.* · *Gates are checks, not bugs.* · *Isolate your Python.*
**Narration:**
> Three lessons. Read the error before fixing anything; the first wall wasn't what it looked like. Gates are checks, not bugs; they stop a build so a broken video doesn't ship. And isolate your Python. Same tool both times. The difference was the approach.

## B08 — Your Turn (ClaudeComposerAsk, greeting "Your turn.")
**Show:** Composer types the prompt; running text `paste this into Claude…`.
**Prompt on screen:** *"Check whether my machine can run this repo. Test each dependency for real, and before installing anything, explain why each failure happens."*
**Narration:**
> Your turn. Here's a prompt to try in Claude Code before your next install: "Check whether my machine can run this repo. Test each dependency for real, and before installing anything, explain why each failure happens." The last part matters most: it makes Claude find the cause before it changes anything. That's what made my second install work.

## B09 — Outro (title restate)
**Show:** `Brutalist, Installed.` in serif, terracotta period. Handle `@HumanitariansAI` beneath, HAI mark full size. Subline: *Made with this install.*
**Narration:**
> This video is proof that my Brutalist installation works as expected. Brutalist, Installed. At Humanitarians AI.
