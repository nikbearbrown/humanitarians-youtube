# SOURCES — Why AWS Bedrock Exists

Brief supplied by the requester (Likhith): 6 points, checked 2026-10-21 against AWS's public Bedrock documentation and the local executable evidence below.

Primary (AWS docs, official name "Amazon Bedrock"):
- What is Amazon Bedrock — https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html (fully managed; foundation models from multiple providers through a single API; serverless, no infrastructure to manage)
- Converse API — https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html (one consistent interface across supported models)
- Guardrails — https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html (content filters, denied topics, sensitive-information/PII filters)
- Model customization — https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html (fine-tuning on your own data, supported models only)
- Agents — https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html (multi-step tasks that call your APIs / action groups)
- Native request bodies per provider (InvokeModel inference parameters) — https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html (Anthropic `messages`, Meta Llama `prompt`, Amazon Titan Text `inputText`)

## Executable evidence
- `evidence/converse_shape.py` → `evidence/converse_shape.out.txt`. Run with `uv run --no-project --with boto3 python -I` (throwaway env; boto3/botocore 1.43.117). No AWS account, credentials, network call or spend: botocore's Stubber intercepts the call after botocore validates the request against its bundled `bedrock-runtime` service model.
  - The same `client.converse(modelId=..., messages=...)` call validates for three providers' model IDs; only `modelId` changes (B07).
  - A malformed request is rejected client-side, so the validation is real.
  - Converse's input members include `guardrailConfig`; the `bedrock` control plane has `CreateGuardrail` and `CreateModelCustomizationJob`; `bedrock-agent-runtime` has `InvokeAgent` (B06 API names).

## Corrections / de-sensationalising
- Official name is **Amazon Bedrock**; "AWS Bedrock" is kept in narration because it is the requester's wording and common usage.
- "One API": the Converse API is consistent across supported models, but model-specific parameters still exist (`additionalModelRequestFields`). B07 says "the rest stays the same" for the call shown; the verdict card adds the region/feature caveat.
- "No servers": true for on-demand use (serverless). Bedrock still costs money per use; stated on the verdict card ("you still pay per use").
- Fine-tuning is available for supported models only; B06 caption says so.
- Titan: Amazon's newer first-party family is Nova; Titan is kept because the brief names it and Titan models are still listed. Model IDs in B07 are example IDs; availability varies by region and over time.
- B03 "Llama: you host it" means self-hosting the open weights if you integrate it on your own. Hosted Llama APIs also exist; the card is labelled illustrative.
- B08's model pairing (small model sorts, stronger model replies) is an illustrative pattern, labelled on screen.
- No prices, model counts, or provider counts on screen (they would date the video).
