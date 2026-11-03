# PROMPTS — Walker Tower Defense: The Design Document Came Last

## On-screen prompts

**B00 — cold open (ClaudeComposerAsk).** This is an *illustrative reconstruction*, and the on-screen running line says so. No GDD-first prompt exists in the repository: the game was rebuilt from Unity scripts first, and the GDD was written afterwards. The prompt follows the godot-gdd walker pattern ("Please use Walker to convert my game design document about …") and describes the actual game:

> Please use Walker to convert my game design document about a four-element tower defense — Fire, Ice, Poison and Storm towers on a 12-by-8 grid, where every tower you build reshapes the monsters' route — into a playable Godot project.

**B18 — Your Turn (ClaudeComposerAsk, greeting "Your turn.").** This is the prompt the viewer is invited to run. It is read aloud verbatim in the narration and then discussed:

> Here is my game's design document. Pick one proposed experience goal. Rewrite it as a hypothesis a playtester could prove wrong. Then design the smallest test: the setup, what the tester does, what I measure, and the result that would make me change the design. Don't fill in a result.

## The request that produced this film

From the project owner, 2026-10-05 (paraphrased; the full text is in the session):

> Three films about my Godot game, using the godot skills, with walker bookends: godot-gdd walker, then godot-waikthrough walker, then godot-gamedev walker. Write GDD.md first from repo evidence only; do not modify the game; do not call it finished; do not say it looks like the original; do not publish.

The owner approved the GDD approach — PROPOSED labels and PENDING sign-offs — before filming. That approval is not a signed design gate.

## Generation

- **Narration:** Kokoro `am_onyx`, local, free.
- **Visuals:** Remotion scenes rendered via `runtime/scripts/remotion_scenes.py`, plus gameplay clips cut by `../walker-towerdefense-captures/reelkit.py`.
- **Cost:** no paid API calls of any kind.
