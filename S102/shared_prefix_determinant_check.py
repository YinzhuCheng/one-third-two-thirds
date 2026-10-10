from fractions import Fraction as F
R=8
E=[(R-j+2)*(R-j+1) for j in range(R+1)]
a=[j+1 for j in range(R+1)]
c=[a[j]-(a[j-1] if j else 0) for j in range(R+1)]
f=[sum(a[:j+1]) for j in range(R+1)]
mu=sum(F(E[j],j+1) for j in range(R+1))/sum(E)
g=[F(1,j+1)-mu for j in range(R+1)]
assert sum(c[j]*E[j]*g[j] for j in range(R+1))==0
assert all(a[j]**2>=a[j-1]*a[j+1] for j in range(1,R))
variance=sum(c[j]*E[j]*g[j]**2 for j in range(R+1))
energy=sum(f[j]*E[j]*(g[j]-g[j+1])**2 for j in range(R))
assert variance==F(359035429,10478160)
assert energy==F(27527,840)
assert variance-energy==F(15663631,10478160)>0
print('prefix weights a:',a)
print('completion counts E:',E)
print('mean:',mu)
print('variance:',variance)
print('energy:',energy)
print('difference:',variance-energy)
print('PASS: scalar closure fails; original determinant is NOT refuted.')

# Independent complete-permutation check of the matrix decomposition and energy
# inequality on one asymmetric, seven-point, neutral-chain example.
from itertools import permutations
from functools import lru_cache
labels=('d','n1','n2','u','y','s','t')
rel={('d','u'),('d','y'),('u','s'),('y','t'),('n1','n2'),('n1','s'),('n2','t')}
while True:
    new=rel|{(x,z) for x,y in rel for w,z in rel if y==w}
    if new==rel:break
    rel=new
@lru_cache(None)
def extensions(S):
    return tuple(p for p in permutations(S) if all(p.index(x)<p.index(y) for x,y in rel if x in S and y in S))
def e(S):return len(extensions(tuple(sorted(S))))
def mins(S):return {x for x in S if not any(y in S and (y,x) in rel for y in S)}
Q=set(labels);D={'d'};N=['n1','n2'];R=2
AA=[];EE=[];CC=[];VV=[]
for j in range(R+1):
    pref=D|set(N[:j]);S=Q-pref
    AA.append(e(pref));EE.append(e(S));CC.append([e(S-{'u'}),e(S-{'y'})])
    H=e(S-{'u','y'})
    diag=[sum(e(S-{z,v}) for v in mins(S-{z}) if (z,v) in rel) for z in ['u','y']]
    VV.append([[diag[0],H],[H,diag[1]]])
ff=[sum(AA[:j+1]) for j in range(R+1)]
cc=[AA[j]-(AA[j-1] if j else 0) for j in range(R+1)]
WW=[[sum(ff[j]*VV[j][x][y] for j in range(R+1)) for y in range(2)] for x in range(2)]
RU=RY=HU=HY=0
for L in extensions(tuple(sorted(Q))):
    pos={x:L.index(x) for x in Q}
    if pos['u']<pos['y']:
        if any(x=='u' and pos[z]<pos['y'] for x,z in rel):RU+=1
        else:HU+=1
    else:
        if any(x=='y' and pos[z]<pos['u'] for x,z in rel):RY+=1
        else:HY+=1
assert HU==HY
assert WW==[[RU,HU],[HU,RY]]
ET=e(Q);pp=F(HU+RU,ET);UU=F(RU,ET)
assert ET==sum(cc[j]*EE[j] for j in range(R+1))
h=[1-pp,-pp]
xx=[sum(h[k]*CC[j][k] for k in range(2)) for j in range(R+1)]
gg=[-sum(xx[j:])/EE[j] for j in range(R+1)]
assert sum(cc[j]*EE[j]*gg[j] for j in range(R+1))==0
rhs=(sum(ff[j]*EE[j]*(gg[j]-gg[j+1])**2 for j in range(R))-sum(cc[j]*EE[j]*gg[j]**2 for j in range(R+1)))/ET
assert pp**2-UU>=rhs
print('Asymmetric full-permutation check: E=',ET,'W=',WW,'a=',AA,'E_j=',EE)
print('p^2-U=',pp**2-UU,'energy-minus-variance lower bound=',rhs)
print('PASS: decomposition and lower bound checked on one real asymmetric example; not a general proof.')
