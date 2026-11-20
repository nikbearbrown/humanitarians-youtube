import torch, torchvision
import torch.nn as nn
m = torchvision.models.resnet18(weights=None).eval()
torch.onnx.export(m, torch.randn(1, 3, 224, 224), "data/resnet18_raw.onnx",
                  opset_version=13, do_constant_folding=False,
                  input_names=["input"], output_names=["output"])
mlp = nn.Sequential(nn.Linear(256, 512), nn.ReLU(), nn.Linear(512, 128),
                    nn.ReLU(), nn.Linear(128, 10)).eval()
torch.onnx.export(mlp, torch.randn(1, 256), "data/mlp.onnx", opset_version=13,
                  input_names=["input"], output_names=["output"])
print("exported")
