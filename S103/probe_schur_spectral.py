import numpy as np,random
rng=np.random.default_rng(711)
def low(a,E):
 R=len(a)-1;c=np.diff(np.r_[0,a]);f=np.cumsum(a); m=c*E
 if min(m)<=0:return None
 K=-np.diag(m);I=np.eye(R+1)
 for j in range(R):
  v=I[j]-I[j+1];K+=f[j]*E[j]*np.outer(v,v)
 for j in range(R-1):
  delta=E[j+1]**2-E[j]*E[j+2]
  if delta<=0:return None
  v=E[j]*(I[j+1]-I[j])-E[j+1]*(I[j+2]-I[j+1]);K+=f[j]*E[j+2]/delta*np.outer(v,v)
 mi=np.sqrt(m);S=K/mi[:,None]/mi[None,:];Q=np.linalg.qr(np.c_[mi,I[:,1:]])[0][:,1:];return np.linalg.eigvalsh(Q.T@S@Q)[0]
best=1e9
for k in range(10000):
 R=random.randrange(2,16)
 ratios=np.sort(rng.uniform(1.001,3,R))[::-1];a=np.r_[1,np.cumprod(ratios)]
 er=np.sort(rng.uniform(.02,.999,R))[::-1];E=np.r_[1,np.cumprod(er)]
 z=low(a,E)
 if z is not None and z<best:
  best=z
  if z< -1e-8:print('NEG',z,a.tolist(),E.tolist());break
else:print('No negative; minimum=',best)
