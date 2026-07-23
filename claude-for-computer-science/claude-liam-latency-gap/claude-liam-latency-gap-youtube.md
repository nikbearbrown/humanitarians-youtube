Predicted 367 ms. Measured 1,200.

This is Liam for Humanitarians AI. Shalom, Liam. This is Liam, in for Bear. The spec-sheet math promised 367 milliseconds. The first run on real hardware took 1,200 — and both numbers were right.

What you'll see:
• Here is why Predicted 367 ms. Measured 1,200. belongs in your working knowledge. The systems, policies, and tools shaped by it affect decisions at your level — whether or not you understand the mechanism. Knowing the underlying logic gives you the frame; missing it means reasoning from output with no access to the inputs.
• The book's latency waterfall: three hundred sixty-seven milliseconds predicted, twelve hundred on first deployment, forty-five after profiling. The gap between prediction and reality is the story.
• The spec-sheet calculation used ideal kernel throughput — 367 milliseconds. The first hardware run measured 1,200. The 100-millisecond target line sits far below both. Three named causes put you there, and you can fix them one at a time.
• First fix: swap reference kernels for SIMD-optimized kernels. Reference C code calls one multiply per instruction. SIMD packs four int8 values into one register and runs them in a single clock. The bar drops from 1,200 to roughly 400 milliseconds.
• Second fix: stop spilling activations to external flash. When intermediate tensors overflow SRAM, the model fetches them from slow external memory on every access. Move those activations onto-chip and the bar falls from 400 to roughly 200 milliseconds.

Playlist: Claude for Computer Science

Narrated by Liam for Humanitarians AI.
@HumanitariansAI

#ClaudeAI #HumanitariansAI #Education #ComputerScience
