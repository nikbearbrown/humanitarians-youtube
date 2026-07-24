The Model Fit in Memory and Crashed Anyway

This is Humanitarians. Salaam, Kore. This is Kore, in for Humanitarians AI. 256 kilobytes of RAM, a 180-kilobyte model — simple subtraction says it fits, and it crashes 40 milliseconds into the first inference.

What you'll see:
• Here is why The Model Fit in Memory and Crashed Anyway belongs in your working knowledge. The systems, policies, and tools shaped by it affect decisions at your level — whether or not you understand the mechanism. Knowing the underlying logic gives you the frame; missing it means reasoning from output with no access to the inputs.
• From the book: the STM32H743 SRAM budget after one arena bump — you can see exactly where inference overflows the one-megabyte wall and the system crashes.
• The naive count: 180 kilobytes of weights plus 60 kilobytes of activations equals 240 kilobytes — leaving 16 kilobytes for firmware. Looks fine on paper. But the weights live in flash. The 256 kilobytes of SRAM is for runtime data only — and that's where the crash is.
• With naive allocation, every layer allocates its activation buffer and holds it until inference completes. Layer 1 takes 30 kilobytes, layer 2 adds 40, layer 3 adds 50, layer 4 adds 30 — peak SRAM reaches 150 kilobytes of activations alone, before firmware stack and heap. That's the crash.
• With buffer reuse, a layer's input buffer is freed the moment its output is written. Only the buffers live at one time count toward peak. Layer 1 in, layer 1 out, buffer recycled. Peak activation RAM drops from 150 kilobytes to 60 — the model runs.

Playlist: Claude for Computer Science

Narrated by Kore for Humanitarians AI.
@HumanitariansAI

#ClaudeAI #HumanitariansAI #Education #ComputerScience
