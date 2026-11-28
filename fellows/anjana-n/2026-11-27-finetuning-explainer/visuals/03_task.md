# B03 — Task-Specific Fine-Tuning

- Model block with a small task head added on top — classifier labeled "positive / negative / neutral"
- Labeled examples (text + label pairs) flow in
- Upper layers shift from blue to green (updated), lower layers stay blue (less change)
- Gradient arrows flow backward from task head through upper layers
- Label: "labeled examples teach the model what to output"
