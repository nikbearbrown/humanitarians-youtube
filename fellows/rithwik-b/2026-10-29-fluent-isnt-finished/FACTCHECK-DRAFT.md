# FACTCHECK — hai-fluent-isnt-finished (DRAFT — NOT SIGNED)

Status: **drafted by Claude, awaiting human review.** GATE F stays closed until a
person checks every row and renames this file to `FACTCHECK.md`.

| Beat | Claim (as narrated) | Verdict | Source | Fix applied |
|---|---|---|---|---|
| B02 | Claude writes Remotion scenes, Manim animations, the script and ffmpeg commands | TRUE (observed) | This build: every scene, the beat sheet and compile commands were written by Claude | — |
| B02 | "Faster, and more correctly, than most of us ever will" | AUTHOR'S CLAIM | HOW-TO.md §1 ("faster and more correctly than you ever will") | softened "you" → "most of us" |
| B03 | Claude cannot watch the video; taste is a step it can't do at all | TOOLKIT PREMISE | HOW-TO.md §1 | stated as the toolkit's premise, sourced on screen |
| B04 | Pipeline: Ideas → Script → Audio → Visuals → QC | TRUE | HOW-TO.md §1 pipeline line | "assemble/QC" shortened to "QC" |
| B04 | "You are the conductor … you own the result" | TOOLKIT PREMISE | HOW-TO.md §1 | — |
| B06 | AI fluency = prompting well, judging output, knowing when to trust it | CONSISTENT | User's brief; matches public AI-fluency framings | no institution named (brief's "Stanford HAI" credit unverified → dropped) |
| B06 | Brutalist = show every step, including what broke | TRUE | HOW-TO.md §1 (slates, fill-in, "first compile is always a watchable previz") | — |
| B07 | Test voice was 2.39 s; scene rendered; frame check 0 blockers | TRUE (log) | `brutalist-test/youtube/hello-test` build logs, this session | — |
| B08 | `./art final` refused: missing FACTCHECK.md | TRUE (log) | same build, verbatim REFUSED line | — |
| B09 | Review cut is enough for a personal draft | JUDGMENT | run.sh: "REVIEW built; no final exported" | framed as advice, not fact |

Omitted from the brief pending a source: "Botspeak" as HAI's AI-fluency course;
the Stanford HAI attribution; "uploading videos" (contradicts the never-publish rule).

**Sign-off:** pending. Signing = checking every row, then renaming this file to `FACTCHECK.md`.
