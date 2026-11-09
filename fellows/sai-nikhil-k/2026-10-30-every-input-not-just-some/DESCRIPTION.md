Software is full of bugs, and AI keeps getting better at finding them. Anthropic now says AI can do something rarer: prove that a program won't crash, on every input. What does a proof give you that a million tests can't, and what doesn't it give you?

This week's second reel walks through Anthropic's post "LLMs are making formal software verification feasible at a much larger scale" (Frontier Red Team, with Theorem, Oct 22, 2026).

The price of a proof. The seL4 kernel took 2 person-years to write and 20 to verify: ten times the work. Anthropic says Claude wrote about 180 million lines of Rocq proof for 239 fuzz-test entry points in 123 open-source libraries, in a few weeks: on average around 750,000 lines each (a typical proof is about 600,000).

Tests vs a proof. A fuzzer throws millions of random inputs at a program and knows only about those. A proof is a statement about every input, here up to 64 MB, made about the compiled RISC-V machine code, and checked by a machine. The recipe: take an existing OSS-Fuzz test, compile it, state "no crash for any input up to 64 MB", let Claude write the proof, let the Rocq checker verify it. You trust the machine model, the theorem's wording and the checker, not the 180 million lines.

Our toy version. A decoder whose bug only fires on files over 16 MiB:
- 1,000,000 random tests under 1 MiB (the way fuzzers cap inputs): 0 crashes
- A solver (Z3) searching every input up to 64 MiB: finds the crash, a 16,777,220-byte file, in 0.013 s
- After the patch: the solver proves no crashing input exists up to 64 MiB
(Our example and Z3, not Anthropic's code or Rocq.)

What came out: hundreds of bugs fixed along the way; agents sharing a workspace reuse each other's proof files (30 of 34 proofs cheaper than working alone); Opus 5.5 finishes half of the post's test tasks with about 40% fewer tokens than Opus 5. Theorem has published 90 of the proved entry points (32 libraries) so far.

Verified isn't bug-free. Inside the theorem, every input up to 64 MB is covered. Outside it: the x86 and ARM builds with glibc that most people run (the proofs are about static RISC-V binaries on musl), wrong answers that never crash, and code nobody proved. A proof is exactly as good as the theorem it states.

Try it yourself: pick a function you wrote, ask an assistant to state one property it should hold for every input, then ask what you'd have to assume about the compiler, chip and OS for a proof of it to mean anything.

Chapters:
0:00 Can AI prove there's no crash?
0:13 The price of a proof, then and now
0:31 A fuzzer samples, a proof covers
0:48 The recipe
1:06 A million tests vs one solver
1:23 What came out
1:42 Verified isn't bug-free
2:00 Verdict
2:14 Your turn: state the theorem
2:30 Outro

Sources:
Anthropic, "LLMs are making formal software verification feasible at a much larger scale" (Oct 22, 2026) — https://www.anthropic.com/research/formal-verification
Theorem, OSS Verify proofs (MIT) — https://github.com/theorem-labs/oss-verify-proofs
Z3 theorem prover — https://github.com/Z3Prover/z3

Images:
Charts and illustration — Anthropic, © Anthropic PBC, shown with credit
Repository screenshot — Theorem, oss-verify-proofs (MIT)
Dice — Anton Ehrola, CC BY-SA 4.0, Wikimedia Commons
RISC-V board (StarFive VisionFive 2) — Teeks99, CC BY-SA 4.0, Wikimedia Commons

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the arithmetic typeset locally as SVG. The toy demo is our own code, run on a MacBook Pro with Z3. The post's figures are Anthropic's; we did not re-run their proofs. No image was generated. No human-performed audio or video.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: formal verification, Anthropic, Claude, Rocq, Coq, proof assistant, fuzzing, OSS-Fuzz, RISC-V, software security, memory safety, Theorem, seL4, Z3, SMT solver, AI for code, Humanitarians AI, Computational Skepticism

#AI #FormalVerification #SoftwareSecurity #Fuzzing #Claude #OpenSource #HumanitariansAI #ComputationalSkepticism
