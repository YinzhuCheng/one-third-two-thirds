import json,sys
from fractions import Fraction as F
for path in sys.argv[1:]:
 d=json.load(open(path)); E=d['E_j']+[0,0]; C=d['C_j']+[[0,0]]; V=d['V_j']; f=d['f']; R=len(V)-1
 p=F(d['p']); g=[p-F(x) for x in d['q_j']]+[0,0]
 curvature=F(0); slack=F(0)
 for j in range(R+1):
  e,b,c=E[j:j+3]; delta=b*b-e*c; v,w,z=V[j]; xu,yu=C[j]; xn,yn=C[j+1]
  assert delta>=0
  if delta:
   det=v*z*c+2*w*xn*yn-v*yn*yn-z*xn*xn-w*w*c
   k=F(det,delta)
   cur=F(c,delta)*(e*(g[j+1]-g[j])-b*(g[j+2]-g[j+1]))**2 if j<R else F(0)
  else:
   assert [e*xn-b*xu,e*yn-b*yu]==[0,0]
   k=F(xu*xu,e)-v;cur=F(0)
  assert k>=0
  h=[1-p,-p]; hv=v*h[0]**2+2*w*h[0]*h[1]+z*h[1]**2
  base=2*b*g[j+1]**2-e*g[j]**2-c*g[j+2]**2+e*(g[j]-g[j+1])**2 if j<R else -e*g[j]**2
  assert -hv==base+cur+k,(j,-hv,base,cur,k)
  curvature+=f[j]*cur;slack+=f[j]*k
 old=F(d['energy'])-F(d['variance']);gap=F(d['gap'])
 assert (old+curvature+slack)/d['E']==gap
 print(path,'old=',float(old/d['E']),'curvature=',float(curvature/d['E']),'enhanced=',float((old+curvature)/d['E']),'slack=',float(slack/d['E']),'gap=',float(gap))
 print('Exact enhanced:',(old+curvature)/d['E'])
