# FACTCHECK — Why AWS Bedrock Exists

Status: claims checked by Claude Code against the primary sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the 16:9 and 9:16 review cuts and approve the claims above as spoken and shown. I'm signing off for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Without a managed service, running a model means GPUs, scaling, patching, uptime | PASS | self-hosting open-weight models requires your own compute | framed as a question |
| 2 | B03 | Each model has its own API / request format and hosting | PASS | Bedrock model-parameters doc: Anthropic `messages`, Llama `prompt`, Titan `inputText` | labelled illustrative |
| 3 | B04 | Bedrock is a managed service: one API to models from many providers | PASS | AWS "What is Amazon Bedrock"; Converse API | "+ more providers", no count |
| 4 | B05 | No servers to provision; AWS handles GPUs, scaling, patching | PASS | AWS: serverless, no infrastructure to manage | pay-per-use caveat on B09 |
| 5 | B06 | Guardrails, fine-tuning on your data, agents on the same platform | PASS | AWS docs; evidence: `guardrailConfig`, `CreateModelCustomizationJob`, `InvokeAgent` | "fine-tuning: supported models" caption |
| 6 | B07 | Switching models = changing the model ID; rest of the call stays the same | PASS | evidence/converse_shape.out.txt (same call validates for 3 IDs) | model-specific params caveat in SOURCES |
| 7 | B08 | Combine models through one integration | PASS | follows from #6: both calls are the same converse() shape | pairing illustrative |
| 8 | B09 | Bedrock isn't a model; it's the managed layer to many | PASS | AWS docs | region/feature + pay-per-use caveat line |
| 9 | B00/B11 | Narration is an AI voice | DISCLOSED | "Narrated by an AI voice." | on screen B00 + B11 |
