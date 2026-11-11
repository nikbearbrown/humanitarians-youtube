# FACTCHECK — brutalist-installed

Every factual claim in the narration and on screen. Format: claim | verdict | source | fix applied.
No dates or times appear anywhere (owner instruction).

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | Both installs were done with Claude Code | TRUE | Owner's account | — |
| B00 | Readiness: voice, Manim, Remotion, compile ready; equations need LaTeX | TRUE | `./setup --install` readiness table, this install | — |
| B01 | Brutalist is an agentic video-creation pipeline using Claude | TRUE | Owner's framing; toolkit README/HOW-TO (beat sheet → audio → visuals → compile, built by Claude) | — |
| B02 | Two test videos were built in the first attempt | TRUE | `brutalist-vids/binary-search-test/`, `brutalist-vids/claude-liam-ribosomes-read-mrna/` | — |
| B02 | Narration was generated | TRUE | `mp3/` present in both reels | — |
| B02 | Some animations rendered | TRUE | `claude-liam-ribosomes-read-mrna/manim/B02–B08.mp4` | "Some", not "all": binary-search-test has no rendered animation |
| B02 | Both builds: status failed, "Review pipeline failed (exit 2)" | TRUE | Both `build-state.json` files, verbatim | Timestamps in those files are NOT shown |
| B02 | Neither reached a finished cut | TRUE | No compiled cut in either reel | — |
| B03 | Some packages needed an older Python | TRUE (owner's account) | Owner; consistent with manim 0.18's `Requires-Python >=3.9,<3.13` | — |
| B03 | The build kept stopping at its gates | TRUE (owner's account + evidence) | Owner; `run.sh` exits 2 on any gate failure, which is the recorded exit code | Phrased as "kept stopping at its gates", not a specific gate |
| B03 | Gates are deliberate checks that halt the pipeline | TRUE | `runtime/scripts/run.sh` (GATE F/L/A/W/B/V) | — |
| B04 | Clean copy cloned from the repository | TRUE | git reflog: `clone: from https://github.com/nikbearbrown/brutalist.art.git` | — |
| B04 | Setup check stopped, claiming a paid voice service | TRUE | `setup` ElevenLabs guard; real output message | — |
| B04 | False alarm: videos explaining that check, inside the toolkit | TRUE | Matches were in `youtube/brutalist/` (videos about `./setup` quoting the guard pattern + demo fixtures) | Simplified to "videos explaining that check"; fixtures not mentioned |
| B04 | Moved out, the check passed | TRUE | Folder moved to `brutalist-vids/brutalist-playlist/`; guard grep clean | — |
| B05 | Python 3.14 too new for the animation library | TRUE | manim 0.18.1 metadata `Requires-Python >=3.9,<3.13`; requirements pin `manim>=0.18,<0.19` | — |
| B05 | On Windows `python3` opened the Microsoft Store prompt | TRUE | Real output, this machine | — |
| B05 | Fix: Python 3.12 venv, python3 copy, `./setup --install` | TRUE | Commands actually run | — |
| B06 | Readiness rows as shown | TRUE | `./setup` table, verbatim labels | — |
| B07 | Same tool both times | TRUE (owner's account) | Owner | — |
| B09 | This video is proof the installation works | CONDITIONAL | Holds only if `./art run`/`./art final` pass their gates | Re-verify before the final master is called done |
