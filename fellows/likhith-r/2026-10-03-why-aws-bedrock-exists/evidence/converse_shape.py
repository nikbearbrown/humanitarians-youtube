"""Offline check of the Amazon Bedrock Converse call shape (B07 / B08 evidence).

No AWS account, no credentials, no network, no spend: botocore's Stubber
intercepts the call, and botocore validates the request against its bundled
bedrock-runtime service model before the stub answers. The same `converse(...)`
call is made for three providers' models; only `modelId` changes.
"""
import boto3, botocore
from botocore.stub import Stubber

MODELS = [
    "anthropic.claude-3-haiku-20240307-v1:0",
    "meta.llama3-8b-instruct-v1:0",
    "amazon.titan-text-express-v1",
]

client = boto3.client("bedrock-runtime", region_name="us-east-1",
                      aws_access_key_id="offline", aws_secret_access_key="offline")
print(f"boto3 {boto3.__version__} / botocore {botocore.__version__}")
op = client.meta.service_model.operation_model("Converse")
print("operation:", op.name, op.http["method"], op.http["requestUri"])
print("required input:", sorted(op.input_shape.required_members))

messages = [{"role": "user", "content": [{"text": "Summarize this ticket."}]}]
with Stubber(client) as stub:
    for model_id in MODELS:
        stub.add_response("converse", {
            "output": {"message": {"role": "assistant", "content": [{"text": "(stubbed)"}]}},
            "stopReason": "end_turn",
            "usage": {"inputTokens": 1, "outputTokens": 1, "totalTokens": 2},
            "metrics": {"latencyMs": 1},
        }, {"modelId": model_id, "messages": messages})
        resp = client.converse(modelId=model_id, messages=messages)
        print(f"converse(modelId={model_id!r}) -> request shape valid, stopReason={resp['stopReason']}")

# a malformed request is rejected client-side, so the check above is real
try:
    client.converse(modelId=MODELS[0], messages=[{"role": "user", "content": "plain string"}])
except botocore.exceptions.ParamValidationError as e:
    print("malformed request rejected:", str(e).splitlines()[0])

# guardrails ride on the same call: Converse accepts a guardrailConfig
print("converse input members:", sorted(op.input_shape.members))
svc = boto3.client("bedrock", region_name="us-east-1", aws_access_key_id="offline", aws_secret_access_key="offline")
ops = svc.meta.service_model.operation_names
print("bedrock control plane has:", [o for o in ops if o in ("CreateGuardrail", "CreateModelCustomizationJob")])
ag = boto3.client("bedrock-agent-runtime", region_name="us-east-1", aws_access_key_id="offline", aws_secret_access_key="offline")
print("bedrock-agent-runtime has InvokeAgent:", "InvokeAgent" in ag.meta.service_model.operation_names)
