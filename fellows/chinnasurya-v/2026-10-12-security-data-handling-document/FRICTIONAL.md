# Frictional log — security and data handling document

Dated entries, appended as the work happened. Earlier entries are never rewritten.

## 2026-10-14 — the section that would not write

What I expected: the access-control section would be a description of something
already correct. What resisted: I could not write a true sentence about instructor
access, because an instructor's textbook access was not scoped to the courses they
teach. The document stalled on a paragraph, and the paragraph was right.

What I did: fixed the code before writing the section, with six tests across the
three paths that grant access. Writing a security document against code you have
not re-read is how a document ends up describing a system that does not exist.

## 2026-10-20 — claims I took out

What I expected: a verification pass that confirmed what I had written. What
happened: two claims came out. A backup posture I had stated confidently and could
not substantiate when I went looking, and a multi-factor authentication claim that
had simply never been checked by anyone. Both had been written because they were
probably true.

What I did: moved both into the gaps section. A gap stated plainly is reviewable. A
reassurance that turns out to be unverified is the thing that ends a review badly.

Claude's contribution: drafted the subprocessor inventory from the dependency list.
I rejected the first version, which described what each vendor's marketing page
says it does rather than what our code actually sends it, and redid it against the
call sites.

## 2026-10-22 — TLS, tested rather than read

The hosting provider's documentation states the supported TLS versions. I used it
as the source at first. Then I negotiated each version individually against the dev
endpoint, because a document that cites a vendor page is citing a vendor, not a
test. The result matched the claim, which is not the point: it is now a measurement
I can repeat in front of a reviewer.

## 2026-10-24 — what is still open

- The launch audit retention figure appears three different ways across the
  document, the schema default and the cleanup function. One of the three is the
  real one. I have not yet established which.
- A signature-verification fallback still accepts an unverified payload on one
  route. Found during this pass, documented, not fixed.
- The document renders from a single-source LaTeX build now, so it no longer
  carries a browser print stamp. That was cosmetic and took longer than it should.
