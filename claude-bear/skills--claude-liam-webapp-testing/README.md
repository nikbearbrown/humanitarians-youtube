# Web Application Testing

Ask Claude to test a local web app and the natural guess is that a page
which has "loaded" — arrived, visible on screen — is already safe to click
into. It isn't. Dynamic apps often finish loading their shell before their
JavaScript has actually drawn the real content, so inspecting too early
means grabbing a placeholder, not the button. The fix is one rule: wait for
the network to go idle before touching the page at all — that single wait
accounts for the single most common way this kind of testing breaks. A
helper script handles the server's own lifecycle (start it, wait for
readiness, tear it down) so the automation script itself holds only
browser logic: navigate, wait for idle, screenshot or inspect what actually
rendered, then pick a selector — text, role, or an id, never a brittle
absolute path. Watch one concrete ask — a local React app, port 3000, click
Submit on a login form, check for a success message — go in, get done
correctly once the rules are followed, and come back out right. And both
directions matter: that one wait catches the most common failure outright,
but a login wall, a failed locator, or a CI machine with no display are
real edges the documented rules don't walk you through.

**Topic:** WEB APPLICATION TESTING · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-webapp-testing

---

## Chapters

0:00 The naive framing: "can Claude click a button the moment my page loads?"
0:10 Two situations, one decision: static HTML vs. dynamic web app
0:22 The ask, planted: a local React app, port 3000
0:32 Loaded means ready? — the wrong guess
0:38 Shell loaded, not rendered — the case that breaks it
0:49 Wait for idle, first — the one rule that matters most
0:58 The server, handled for you
1:11 Look, then act
1:19 Descriptive beats brittle
1:31 The anchor returns: the same login form, done right
1:47 What one wait catches
1:58 What's not walked through — one flag
2:13 Carry-out
2:22 Your turn
2:41 Outro

---

## YOUR TURN

I have a local React app running on port 3000. Use the Web Application
Testing skill to verify that clicking the Submit button on a login form
shows a success message.

Then watch what Claude does before it ever clicks anything: does it wait
for the page to go idle before it looks for the button, or does it inspect
right away and risk grabbing a placeholder? Run it today, on your own app,
not the video's example.

---

## Deliberately not claimed

The source skill file this reel is based on could no longer be located at
its original path by the time of this build — the skills tree has been
reorganized since. Facts (the two-branch decision tree, the networkidle
rule, `with_server.py` usage, selector guidance, the three example
scripts, the documented gaps) are carried over unchanged from the locked
source script rather than re-verified against a live file, per this
series' redo contract.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear
