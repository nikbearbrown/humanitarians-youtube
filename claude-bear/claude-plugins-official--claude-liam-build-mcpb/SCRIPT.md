# Build MCPB — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-build-mcpb`). Register: **Plain**.
11 beats ≈ 2:20. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** BrutalistHesitantWriter (Remotion, free, machine-rendered — no
puppet, no human step). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "You'd guess bundling your server as an MCPB is what makes it safe to run. It isn't. Bundling only means it runs without your dev toolchain installed — safety is still entirely on you." | Writer types "Does bundling it / as an MCPB / make it safe to run?", hesitates on "safe", corrects to "easy" — lands on the real question |
| B01 | 1 stakes | Hear "package my server as an MCPB" and it's easy to assume the bundle itself has been made safer — like putting the code in a container. | chips: MCPB = PACKAGED SERVER → SAFER, BY DEFAULT? |
| B02 | **2 wrong guess, broken** | But open the manifest and there's no permissions block, no sandbox field — nothing to check. A packaged MCPB runs with exactly the same file access as the original, unpackaged script. Package a path bug into it, and it walks outside its own folder exactly as easily. | chips: SAFER, BY DEFAULT? (struck) → SAME FILE ACCESS AS THE RAW SCRIPT (accent) |
| B03 | **4 anchor planted** | Here's the anchor: say your manifest launches the server with one setting — an environment variable named ROOT_DIR — pointing at the folder the user picked at install time. | THE ANCHOR — chips: manifest.json → mcp_config.env → ROOT_DIR |
| B04 | 3 mechanism | An MCPB is a zip: manifest.json, a server folder with your code and dependencies, and an icon. The host reads the manifest and launches mcp_config's command exactly as written — dollar-dirname for bundle-relative paths, dollar-user-config for install-time values like that folder the user picked. | chips: ZIP: manifest.json + server/ + icon.png → HOST LAUNCHES mcp_config, EXACTLY |
| B05 | 3 mechanism | The env var name is exactly what you wrote in the manifest — no auto-prefix, no transform. Write ROOT_DIR in the manifest but read ROOT_DIRECTORY in your server code, and the value comes back silently empty. No error, no crash — the config is just quietly ignored. | chips: ROOT_DIR (manifest) → ROOT_DIRECTORY (code) → SILENTLY EMPTY (accent) |
| B06 | **4 anchor payoff** | So back to ROOT_DIR: get the name right, and that path flows straight into your handler with no check on it at all. Because there's no sandbox, one unvalidated "../" in a filename walks the server right out of its own folder. | THE ANCHOR RETURNS — same chips, accented, arrow to UNVALIDATED PATH ESCAPES THE FOLDER |
| B07 | **5 both directions** | A packaged MCPB that runs fine on your machine doesn't prove it's safe anywhere else — it may only prove your own dev toolchain quietly filled a gap. And an MCPB that fails on a clean machine doesn't mean the packaging step is broken — it usually means one dependency never actually got bundled in. | stack: RUNS FINE ON YOUR MACHINE → PROVES IT'S SAFE ELSEWHERE? (struck) / FAILS ON A CLEAN MACHINE → PROVES PACKAGING IS BROKEN? (struck) |
| **BCRY** | **6 carry-out** | Packaging a server as an MCPB makes it runnable without a toolchain — it doesn't make it safe. The env var name still has to match exactly, and every path check is still yours to write. | WantQuote — the sentence, alone |
| BHTF | handoff | Your turn. Paste this into Claude: build an MCPB that reads files from a directory the user configures at install time. Watch three things: does the env var name in the manifest's mcp_config exactly match what the server code reads? Does the server validate that every requested path stays inside that configured root, or would a dot-dot-slash escape it? And does the build script bundle dependencies with esbuild, or does it assume node_modules will already be there? | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Build MCPB. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B01 states the "packaging = safety" read; B02 breaks it — the manifest has no permissions block or sandbox field, so a packaged MCPB keeps the same file access as the unpackaged script |
| One anchor, planted early, paid off late | B03 → B06 (the ROOT_DIR env var: name-match trap at B05, then unvalidated-path trap at B06) |
| Both failure directions | B07 |
| No design judgment (Teardown → Plain) | Source's verdict framing ("gets five things right… here's where it bites") dropped entirely — no ranking of the skill file's documentation quality, no verdict beat; only the underlying mechanism facts (manifest anatomy, no-auto-prefix, no-sandbox, build pipeline, test-without-toolchain) carry over as plain mechanism statements |
| One flag | N/A — every claim is a generic, directly-stated mechanic carried from the source's own narration; the ROOT_DIR example is illustrative but the two traps it demonstrates are both stated directly in source, not inferred |

## Deliberately not claimed

- **No claim about the exact manifest JSON syntax beyond what the source
  itself states** — `${__dirname}`, `${user_config.*}` tokens, the
  `server.mcp_config` block, `user_config` with `type: "directory"` and
  `sensitive: true`, and `compatibility` are all named generically per the
  source's own narration; no manifest file was read from disk (none exists
  locally for this skill).
- **No ranking of whether the source skill's documentation buries any
  particular trap well or badly** — the source's own Teardown verdict made
  that judgment (env-var prefix rule "buried in a code comment," native
  extensions "buries a blocking constraint," etc.); Plain register states
  the mechanism and stops, so none of that ranking survives into this cut.
- **ROOT_DIR is an illustrative variable name, not a documented example
  from the source** — built to satisfy the ANCHOR LAW's need for one
  concrete, recurring case; the two traps it carries (name-mismatch silent
  failure, unvalidated path traversal) are both stated directly in the
  source's own narration text, not invented.

## Handoff prompt (BHTF, read aloud)

> "Build an MCPB that reads files from a directory the user configures at
> install time. Watch three things: does the env var name in the manifest's
> mcp_config exactly match what the server code reads? Does the server
> validate that every requested path stays inside that configured root, or
> would a dot-dot-slash escape it? And does the build script bundle
> dependencies with esbuild, or does it assume node_modules will already be
> there?"

Why it's worth running: it forces the viewer to check both traps the reel
just named — the silent name-mismatch and the missing path check — against
a Claude Code build they actually watch happen.

---
**GATE P — signed:** ______________________  (human)
