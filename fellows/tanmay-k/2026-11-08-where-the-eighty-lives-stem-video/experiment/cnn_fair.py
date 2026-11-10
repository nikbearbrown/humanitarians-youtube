import os
os.environ.update(OMP_NUM_THREADS="1",OPENBLAS_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1")
import numpy as np,time
rng=np.random.default_rng(0)
K,C,L=5,128,100
Ws=[rng.standard_normal((K*C,C)).astype(np.float32)*.03 for _ in range(2)]  # 2 layers
x=rng.standard_normal((L,K*C)).astype(np.float32)
def cnn():
    y=x
    for W in Ws: y=np.maximum(y@W,0); y=np.tile(y,(1,K))
    return y
cnn(); n=300; t=time.perf_counter()
for _ in range(n): cnn()
print("CNN MACs",2*L*K*C*C/1e6,"M, params",2*K*C*C,"time ms",round((time.perf_counter()-t)/n*1e3,3))
