It's Not the AI Draining the Battery. It's the Radio.

This is Kore for Humanitarians AI. Halo, Kore. This is Kore, in for Humanitarians AI. The team optimized the neural network for weeks and the battery life barely moved — because inference was never what was eating it.

What you'll see:
• Here is why It's Not the AI Draining the Battery. It's the Radio. belongs in your working knowledge. The systems, policies, and tools shaped by it affect decisions at your level — whether or not you understand the mechanism. Knowing the underlying logic gives you the frame; missing it means reasoning from output with no access to the inputs.
• This is the book's battery-life curve — inference period on the x-axis, months on the y-axis. See where the curve flattens? That's where the radio becomes the ceiling, not inference.
• Start with the baseline: sleep current. The microcontroller in deep sleep draws about 5 microamps — essentially zero on the trace. This is the floor the device returns to between events. Every other activity is a spike above this line.
• Inference: the model runs. Current spikes to 15 milliamps for 22 milliseconds, then returns to sleep. Energy: 0.33 milliamp-seconds per inference. Even 1,000 inferences a day is 330 milliamp-seconds. The spike is real — but narrow. It looks dramatic on the trace and is small in the energy budget.
• Now the radio. A single LoRa transmission: 35 to 40 milliamps for 100 milliseconds. Energy: 3.5 milliamp-seconds. That is ten times the cost of one inference, from a single transmit event. On the trace, the radio envelope dominates — tall and wide, dwarfing everything that came before. Ten transmissions a day: 35 milliamp-seconds. One thousand inferences: 330 milliamp-seconds. At that ratio, the radio wins the budget.

Playlist: Claude for Computer Science

Narrated by Kore for Humanitarians AI.
@HumanitariansAI

#ClaudeAI #HumanitariansAI #Education #ComputerScience
