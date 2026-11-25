"""Every number the film shows (pure python, no ML libraries)."""
import math
def softmax(z):
    m = max(z); e = [math.exp(x - m) for x in z]; s = sum(e); return [x / s for x in e]
z = [2.0, 1.0, 0.1]
p = softmax(z)
print("logits", z, "-> probs", [round(x, 4) for x in p], "sum", round(sum(p), 6))
print("loss if class 0 is right: -ln p0 =", round(-math.log(p[0]), 4))
print("gradient p - y:", [round(p[0] - 1, 4), round(p[1], 4), round(p[2], 4)])
print("loss if class 2 is right: -ln p2 =", round(-math.log(p[2]), 4))
print("-ln p curve:")
for q in (0.99, 0.9, 0.5, 0.1, 0.01, 0.001):
    print(f"   p={q:<6} loss={-math.log(q):.3f}")
# two models, same 3 predictions right/wrong pattern
A = [0.9, 0.9, 0.1]   # prob given to the true class
B = [0.6, 0.6, 0.4]
for name, t in (("A confident", A), ("B hedged", B)):
    acc = sum(1 for x in t if x > 0.5) / len(t)
    print(name, "true-class probs", t, "accuracy", round(acc, 3),
          "mean loss", round(sum(-math.log(x) for x in t) / len(t), 4))
# one gradient step on logits, lr 1.0
lr = 1.0
z2 = [z[i] - lr * (p[i] - (1 if i == 0 else 0)) for i in range(3)]
p2 = softmax(z2)
print("after 1 step (lr 1):", [round(x, 3) for x in z2], "probs", [round(x, 4) for x in p2],
      "loss", round(-math.log(p2[0]), 4))
# floor
print("clip floor 1e-12 -> loss", round(-math.log(1e-12), 2))
