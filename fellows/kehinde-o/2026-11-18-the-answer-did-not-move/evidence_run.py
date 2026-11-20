"""Week 11 evidence run for 'The Answer Did Not Move'.

Runs github.com/Kenny0bi/fuse on resnet18 exported per its data/export.sh
(weights=None, opset 13, constant folding off). Records: the runtime's parity
with onnxruntime (an independent reference), the optimizer's node counts and
report, the raw-vs-optimized output difference, and a direct numerical check
of the Conv+BatchNorm fold algebra on the network's first Conv/BN pair.
"""
import json, os, sys
from pathlib import Path
import numpy as np
import onnx, onnxruntime as ort
from onnx import numpy_helper

REPO = Path(os.environ.get("FUSE_REPO", "fuse")).expanduser()
sys.path.insert(0, str(REPO))
from fuse.ir import load
from fuse.passes import optimize
from fuse.runtime import Runtime

MODEL = REPO / "data/resnet18_raw.onnx"
x = np.random.default_rng(0).standard_normal((1, 3, 224, 224)).astype(np.float32)

raw = load(MODEL); before = raw.stats()
y_raw = Runtime(raw).run({raw.inputs[0]: x})[0]
sess = ort.InferenceSession(str(MODEL), providers=["CPUExecutionProvider"])
y_ort = sess.run(None, {sess.get_inputs()[0].name: x})[0]

opt = load(MODEL); report = optimize(opt); after = opt.stats()
y_opt = Runtime(opt).run({opt.inputs[0]: x})[0]

# --- the fold algebra, directly, on the first Conv -> BatchNorm pair -----------
m = onnx.load(str(MODEL)); init = {t.name: numpy_helper.to_array(t) for t in m.graph.initializer}
nodes = list(m.graph.node); prod = {o: n for n in nodes for o in n.output}
bn = next(n for n in nodes if n.op_type == "BatchNormalization")
conv = prod[bn.input[0]]
while conv.op_type == "Identity": conv = prod[conv.input[0]]
assert conv.op_type == "Conv"
def val(name):
    n = name
    while n not in init: n = prod[n].input[0]
    return init[n]
W = val(conv.input[1]); b = val(conv.input[2]) if len(conv.input) > 2 else np.zeros(W.shape[0], np.float32)
gamma, beta, mu, var = (val(bn.input[i]) for i in range(1, 5))
eps = next((a.f for a in bn.attribute if a.name == "epsilon"), 1e-5)
# weights=None gives an untrained net whose BN stats are 0 and 1; give the layer
# realistic statistics so the check exercises every term of the algebra
rng = np.random.default_rng(1)
gamma = rng.uniform(0.5, 1.5, gamma.shape).astype(np.float32); beta = rng.normal(0, .2, beta.shape).astype(np.float32)
mu = rng.normal(0, .5, mu.shape).astype(np.float32); var = rng.uniform(0.2, 2.0, var.shape).astype(np.float32)
# fold entirely in float64 so the check measures the algebra, not float32 rounding
g64, be64, mu64, v64, W64, b64 = (a.astype(np.float64) for a in (gamma, beta, mu, var, W, b))
s = g64 / np.sqrt(v64 + eps)
W_f = W64 * s[:, None, None, None]; b_f = s * (b64 - mu64) + be64
def conv2d(inp, W, b, stride=2, pad=3):
    from numpy.lib.stride_tricks import sliding_window_view
    p = np.pad(inp, ((0,0),(0,0),(pad,pad),(pad,pad)))
    win = sliding_window_view(p, W.shape[2:], axis=(2,3))[:, :, ::stride, ::stride]
    return np.einsum("nchwij,ocij->nohw", win, W, optimize=True) + b[None, :, None, None]
patch = x[:, :, :64, :64].astype(np.float64)
y_conv = conv2d(patch, W64, b64)
y_two_step = (g64[None,:,None,None] * (y_conv - mu64[None,:,None,None]) / np.sqrt(v64[None,:,None,None] + eps) + be64[None,:,None,None])
y_folded = conv2d(patch, W_f, b_f)
fold_gap_f64 = float(np.abs(y_two_step - y_folded).max())

res = {
 "model": "resnet18, torchvision weights=None, opset 13, do_constant_folding=False",
 "runtime_vs_onnxruntime_max_abs_diff": float(np.abs(y_raw - y_ort).max()),
 "argmax_runtime_equals_onnxruntime": bool(y_raw.argmax() == y_ort.argmax()),
 "nodes_before": int(sum(before.values())), "nodes_after": int(sum(after.values())),
 "ops_before": {k: int(v) for k, v in before.items()}, "ops_after": {k: int(v) for k, v in after.items()},
 "report": {k: int(v) for k, v in report.items()},
 "raw_vs_optimized_max_abs_diff": float(np.abs(y_raw - y_opt).max()),
 "argmax_raw_equals_optimized": bool(y_raw.argmax() == y_opt.argmax()),
 "output_abs_max": float(np.abs(y_raw).max()),
 "fold_check_first_conv_bn": {"conv": conv.name, "bn": bn.name, "epsilon": float(eps),
                              "max_abs_gap_float64": fold_gap_f64}}
Path(__file__).with_name("evidence.json").write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=1))
