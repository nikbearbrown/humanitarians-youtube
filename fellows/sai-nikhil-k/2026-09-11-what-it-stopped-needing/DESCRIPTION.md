Is the rewrite leaner? Wrong question — "leaner" hides the difference between what you chose to cut and what stopped being necessary.

This weekly progress reel walks through clauding 1.0.0, a macOS menu bar indicator for Claude Code that got replaced whole this week: a Swift app, rewritten in Python and PyObjC. Forty-six files changed, 2,196 lines written, 2,843 deleted. What's left is ten modules, about 1,873 lines of Python, and 58 tests where there used to be three — and it makes no network requests at all. The entire feature set is three states in the menu bar: idle, clauding while a turn is running, and waiting for input, the one that actually needs you. The width barely moves between them, and that is deliberate.

The takeaway: the deletions are not one kind of deletion. One pile went because a single design decision dissolved the need for it — a plain process can own a status item, so the app bundle, the code signing, the notarization, the disk image and the Homebrew cask all stopped existing together. The other pile was taste: animations, a timer, a sound, an update checker. Worth saying out loud, because those are two different claims. And one hazard was deleted rather than defended against — the original looked up hook commands through PATH, so a binary planted in a project directory could be found first, and the installer had to harden against it. The rewrite writes an absolute path instead. No lookup happens, so there is no ordering left to get wrong. None of the Swift survived, but the behaviour did: the liveness check that asks whether the process is alive rather than timing it out, the recovery for the two cases that fire no hook at all, and the 8 KB transcript tail gated on modification time. Those were hard-won upstream and every one of them was kept. No benchmark appears anywhere in this video, because none was measured — the word "faster" is not in it.

Try it yourself: if you've just finished a rewrite, list everything it deleted, then sort that list into two piles — what you chose to cut, and what stopped being necessary because of some other decision entirely. Count both. The second pile is the interesting one, and it is the one nobody ever puts in the release notes.

Code — https://github.com/nikhil-kunapareddy/clauding

Chapters:
0:00 A Swift app, rewritten in Python
0:15 What it is — ten modules, fifty-eight tests
0:33 Three states, one width
0:50 Two kinds of deletion
1:10 The PATH hazard, deleted not defended
1:27 What survived the rewrite
1:44 Verdict — one page
2:01 Your turn

Hosted by Sai. Voice: Kokoro am_onyx — free, local, no account. AI-generated narration. Motion graphics built with Remotion; the menu bar on screen is a rendering built from the app's own colour values and logo mask, not a screenshot. No human-performed audio or video in this production.

Humanitarians AI — https://humanitarians.ai
Musinique — https://musinique.com
Medhavy AI — https://medhavy.com

#AI #ClaudeCode #ClaudeAI #Python #macOS #OpenSource #DeveloperTools #HumanitariansAI #WeeklyUpdate

TAGS

clauding, Claude Code, menu bar app, macOS menu bar, PyObjC, Python rewrite, Swift to Python, rewrite, refactoring, software design, developer tools, NSStatusItem, code deletion, simplicity, PATH hardening, supply chain security, absolute path, Claude Code hooks, release notes, open source, accessory activation policy, Humanitarians AI, weekly progress

HASHTAGS

#AI #ClaudeCode #ClaudeAI #Python #macOS #OpenSource #DeveloperTools #HumanitariansAI #WeeklyUpdate
