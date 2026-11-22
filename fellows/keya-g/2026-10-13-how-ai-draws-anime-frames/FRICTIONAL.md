# Frictional log — How AI Draws Anime Frames

Counts toward Week 1. I am new to AI coding, so much of this week was learning how the pieces fit together.

## Setup

- **Tried:** cloning brutalist.art and running `./setup --install` through Claude.
- **Resisted:** the linked computer's network blocked GitHub, pip and npm, so the install couldn't run there.
- **Did next:** cloned and installed Brutalist myself on my Mac.
- **Learned:** a toolkit's setup checks what is on *my* machine, so it has to run there.

## Fellow folder

- **Tried:** creating my folder in my fork of humanitarians-youtube.
- **Resisted:** GitHub has no "new folder" button.
- **Did next:** created `keya-g/README.md` through "Add file", opened a pull request, and synced my fork when it fell behind.
- **Learned:** forks, pull requests and syncing; my fork is mine, and the professor's repo changes only when he merges.

## Topic, research and script

- **Tried:** general AI topics; I asked for ones tied to my interests and picked anime frame interpolation.
- **Resisted:** some of my first notes came from AI chats and company blogs; I had optical flow and interpolation mixed up.
- **Did next:** replaced unverifiable claims with real sources (the AnimeInterp paper, Kreinin's blog), and rewrote the key ideas in my own words.
- **Claude contributed:** guiding questions, corrections and an example script from my story plan. **Accepted:** the script with my Naruto examples.
- **Also:** installed Claude Code (`claude` was not found until I fixed my PATH); gave it my folder with `/add-dir`; fixed my name's pronunciation with IPA.
- **Learned:** the difference between optical flow (the motion map) and interpolation (drawing the new frame with it), and how to tell a paper from a blog from an AI answer.

## Audio, animations, fact check, landscape master

- **Tried:** audio first, then Manim scenes timed to the measured audio, then `./art run`.
- **Resisted:**
  - "Sasuke" was mispronounced; fixed by ear from three test clips.
  - The build stopped at one gate after another: F (missing fact-check paperwork), L (channel series name "Irreducibly Human"), A, B (margins), V (empty or under-filled frames, an outro that went black early) and T (text size and contrast).
  - A build said "exit code 0" while it had actually failed, because the log command hid the real result.
- **Did next:** fixed each cause rather than bypassing the gate. After the fact check I changed beats 5 and 7, and kept the hook and beat 4 knowingly.
- **Learned:** a passing gate checks layout, not truth, so the fact check is my job; always read the real result, not just the exit code.

## Vertical master and write-up

- **Tried:** the 9:16 version with `./art vertical`.
- **Resisted:**
  - The portrait outro render froze for an hour; installing Playwright's headless Chromium fixed it.
  - Every frame failed Gate V because of a portrait-only bug in the review label.
  - The channel title, the verdict card and the typing card didn't fit portrait well.
  - Gate T keeps the bottom 14% of a phone frame clear, so several captions had to move up.
- **Did next:** fixed four small portrait bugs locally in my copy of Brutalist, saved them as a patch with a note for the Brutalist team, and pushed nothing to the professor's repo. A label nudge I asked for made things worse, so it was reverted.
- **Learned:** how to judge each approval prompt (reading versus changing versus bypassing), and that portrait is a separate layout, not a crop.
- **Still open:** the small `@HumanitariansAI` label on the portrait typing card; claims 2, 5 and 6 in the fact check.
