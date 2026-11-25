import os
os.environ.update(OMP_NUM_THREADS="1",OPENBLAS_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1")
import numpy as np, time
# 1) first-principles: LSTM params vs MACs per step
for h,x in [(64,64),(128,128),(128,262),(256,64)]:
    p=4*(h*(h+x)+h); macs=4*h*(h+x)
    print(f"LSTM h={h} x={x}: params={p:,}  MACs/step={macs:,}  MACs/param={macs/p:.2f}  x100 steps={100*macs/1e6:.1f}M")
print("source: params 0.2M, 14M MACs/step claimed -> MACs/param =", 14/0.2)
# 2) timing, batch 1, single thread, float32
rng=np.random.default_rng(0)
h,x,T=128,262,100
W=rng.standard_normal((h+x,4*h)).astype(np.float32)*.05; b=np.zeros(4*h,np.float32)
sig=lambda z:1/(1+np.exp(-z))
def lstm(seq):
    hh=np.zeros(h,np.float32);c=np.zeros(h,np.float32)
    for t in range(T):
        z=np.concatenate([seq[t],hh])@W+b
        i,f,g,o=np.split(z,4); c=sig(f)*c+sig(i)*np.tanh(g); hh=sig(o)*np.tanh(c)
    return hh
seq=rng.standard_normal((T,x)).astype(np.float32)
# CNN-like: same-sized conv as one big matmul (im2col), ~17M MACs
K,Cin,Cout,L=5,64,64,T
Wc=rng.standard_normal((K*Cin,Cout)).astype(np.float32)*.05
xin=rng.standard_normal((L,K*Cin)).astype(np.float32)
def cnn(): 
    y=xin@Wc
    for _ in range(4): y=np.maximum(y,0)
    return y
def bench(f,*a,n=200):
    f(*a);t=time.perf_counter()
    for _ in range(n): f(*a)
    return (time.perf_counter()-t)/n*1e3
print("LSTM params",4*(h*(h+x)+h),"MACs total",T*4*h*(h+x)/1e6,"M ; time ms",round(bench(lstm,seq,n=50),3))
print("CNN-ish MACs",L*K*Cin*Cout/1e6,"M ; time ms",round(bench(cnn),3))
