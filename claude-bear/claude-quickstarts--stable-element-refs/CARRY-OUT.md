# CARRY-OUT — claude-quickstarts--stable-element-refs

**Carry-out line (written before the body, per CARRY-OUT LAW):**

> A pixel coordinate describes where a button was, once. A ref names the button
> itself — so it survives every resize the coordinate doesn't.

**Test:** repeatable by someone half-listening next week, and still true — yes.
It compresses the distinction (location vs. identity), not the topic (browser
automation).

**The wrong guess it's built to defeat:** that remembering a button's on-screen
pixel position is a stable way for automation to find that button again later. It
looks reasonable because the coordinate worked the first time — the failure is
invisible until the page reflows.

**Falsifying case:** resize the browser window. The page reflows and the button's
on-screen position changes — the source's own worked example moves a "Confirm
Order" button from (960, 540) on a 1920×1080 page to roughly (720, 405) on a
1440×900 page. The remembered pixel coordinate now points at empty space, or at
whatever else drifted into that spot. Only an identifier attached to the element
itself — not to a location — survives the reflow.
