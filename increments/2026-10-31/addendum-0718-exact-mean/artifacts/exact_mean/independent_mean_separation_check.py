from fractions import Fraction as F
from math import comb
import json
V=['v','c1','c2','b','d','e','a0','x1','x2','x3','x4','f0','f1'];A={'a0','x1','x2','x3','x4'}
E={('v','b'),('v','d'),('v','f0'),('c1','c2'),('c2','f0'),('f0','f1'),('d','e'),('e','x1'),('x1','x2'),('a0','x3'),('b','x1'),('b','x3'),('b','x4')}|{('v',x) for x in A}|{('c1',x) for x in A}
while True:
 new=E|{(a,d) for a,b in E for c,d in E if b==c}
 if new==E:break
 E=new
U=lambda a:{b for x,b in E if x==a};inc=lambda a,b:a!=b and (a,b) not in E and (b,a) not in E
AA=U('v')&U('c1')-U('c2');FF=U('c2');L=AA&U('b');M=FF-U('b');Q=set(V)-{'v','c1','c2','b'}
assert AA==A and L=={'x1','x2','x3','x4'} and M=={'f0','f1'}
assert U('v')-U('c1')=={'b','d','e'} and {x for x in V if inc('v',x)}=={'c1','c2'}
assert inc('b','d') and inc('b','e') and ('d','e') in E
out=[0,0,0]
def rec(w,left):
 if not left:
  out[0]+=1;out[1]+=min(w.index(x)+1 for x in M);out[2]+=min(w.index(x)+1 for x in L);return
 for x in left:
  if all((y,x) not in E for y in left):rec(w+[x],left-{x})
rec([],Q)
# Direct polynomial multiplication/integration, in the original t coordinate.
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
survival=mul(mul([1,0,0,-4,3],[1,0,-1]),[1,-1]);mean=sum(F(c,i+1) for i,c in enumerate(survival));kappa=F(2,3)+F(1,2)+1
assert mean==F(43,120) and kappa==F(13,6) and out==[3780,12600,13545]
result={'C2':True,'A':sorted(A),'L':sorted(L),'M':sorted(M),'inc':{x:sum(inc(x,y) for y in V) for x in V},'Q_extensions':out[0],'B':out[1],'Z':out[2],'survival_coefficients':survival,'mean':str(mean),'old_kappa':str(kappa),'six_independent_twochains_mean':str(sum(F(comb(6,j)*(-1)**j,2*j+1) for j in range(7)))}
print(json.dumps(result,indent=2))
