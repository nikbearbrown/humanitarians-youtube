# Frictional — Encrypted Twice

## 2026-10-28 — the beat that made me write the reel honestly

The obvious version of this explainer is "we encrypt credentials, here is how
strong it is." That version is a pitch. Writing it properly meant admitting two
things on camera.

The first is that **the storage-layer claim is not mine to make.** Supabase says
it applies AES-256 at rest. I have not measured that and cannot from where I sit.
So B02 says "Supabase applies AES-256" and the fact-check marks the row
**VENDOR CLAIM**, rather than letting the reel imply I verified it.

The second is the migration path. There was data in that column before the
encryption shipped, so the decrypt path passes through anything that does not
start with `v1:`. That means an old row still reads in clear. I could have left
that out and the reel would have been tidier and slightly dishonest. B06 is the
beat where it gets named, and it says plainly that the allowance is transitional
and should be removed when the last row has been rewritten.

## 2026-10-28 — the two defects, and the second one was embarrassing

B04's field labels were drawn at a size derived from the row height with no width
check. Fine at 16:9, over the title-safe edge at 9:16. GATE V caught it as a
blocker on two frames, which is exactly what that gate is for.

So I fixed it by measuring the longest label — and wrote
`max(f"{a}   {b}" for a, b in parts)` without `key=len`. That is a lexicographic
maximum, not the longest string. It returned `v1   VERSION` and happily sized the
font to fit that, so `iv   INITIALISATION VECTOR` still bled off the frame. The
gate failed again, identically, and I spent a render cycle before reading my own
line properly.

Worth recording because it is the same shape of mistake as all the geometry ones:
I asked for a measurement and then measured the wrong thing. The fix is one
keyword.

## 2026-10-28 — portrait for free

Single stacked column like the role-matching reel, so the 9:16 render needed no
portrait branch. Both aspects come off the same scene functions. That is now the
pattern I would use for any new reel in this series, and the two September reels
are the proof of the alternative: their beats compute right-hand positions from
landscape width, and the portrait render of one of them crashes outright with
`x1 must be greater than or equal to x0`.

## 2026-10-28 — still open

No captions or word clock. `PEDAGOGY.md` is not self-signed. Row 7's transitional
plaintext path is a real open item in the codebase, not just in this reel.
