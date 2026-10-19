from itertools import permutations, product, combinations
from fractions import Fraction as F
from pathlib import Path
import json

OUT=Path(__file__).parent
CASES=[
 ('singleton',1,[]),
 ('antichain3',3,[]),
 ('chain4',4,[(0,1),(1,2),(2,3)]),
 ('diamond4',4,[(0,1),(0,2),(1,3),(2,3)]),
 ('fork5',5,[(0,2),(1,2),(2,3),(2,4)]),
 ('crown6',6,[(0,3),(0,4),(1,4),(1,5),(2,3),(2,5)]),
]

def mean(xs):return F(sum(xs),len(xs))
def LE(n,edges):
 ans=[]
 for p in permutations(range(n)):
  f=[0]*n
  for i,v in enumerate(p,1):f[v]=i
  if all(f[a]<f[b] for a,b in edges):ans.append(tuple(f))
 return ans

def audit_case(name,n,edges):
 fs=LE(n,edges); out={'name':name,'n':n,'extensions':len(fs)}
 principal=0; mixed=0; smaller=0; subsets=0
 for x in range(n):
  As=[f[x] for f in fs];mu=mean(As);va=mean([a*a for a in As])-mu*mu
  assert va <= mu*(mu-1)
  for mask in range(1,1<<n):
   B=[i for i in range(n) if mask>>i&1];Gs=[min(f[i] for i in B) for f in fs]
   nu=mean(Gs);H=mean([min(a,b) for a,b in zip(As,Gs)])
   M=mean([a*b for a,b in zip(As,Gs)])
   assert M+H-mu*nu<=va+mu
   r=mu-1;s=nu-1
   N=mean([(a-1)*(b-1)+min(a-1,b-1) for a,b in zip(As,Gs)])
   assert N-r*s==M+H-mu*nu-1
   assert N<=r*s+r*r+2*r
   mixed+=1
   if r<=s:
    assert N<=r*s+min(r*r+2*r,s*s+2*s);smaller+=1
   # Exact continuous mixed moment and long-chain corrected inequalities.
   EX=mu/F(n+1);EY=nu/F(n+1)
   EXY=(M+H)/F((n+1)*(n+2))
   EX2=(mean([a*a for a in As])+mu)/F((n+1)*(n+2))
   cov=EXY-EX*EY;var=EX2-EX*EX
   assert cov<=var-EX*(EY-EX)/F(n+2)
   for k in (1,2,7,100):
    kap=F(k,(n+2)*(n+k+1))
    assert cov<=var-kap*EX*(EY-EX)
   # Restrict the actual slot interpretation to upsets.
   if all(not(mask>>a&1) or (mask>>b&1) for a,b in edges):subsets+=1
  for y in range(n):
   Bs=[f[y] for f in fs];nu=mean(Bs);r=mu-1;s=nu-1
   N=mean([(a-1)*(b-1)+min(a-1,b-1) for a,b in zip(As,Bs)])
   assert N<=r*s+min(r*r+2*r,s*s+2*s);principal+=1
 out.update(principal_pairs=principal,mixed_subset_pairs=mixed,smaller_principal_pairs=smaller,upset_pairs=subsets)
 return out

def audit_grid(name,n,edges,m):
 raw=[p for p in product(range(m+1),repeat=n) if all(p[a]<=p[b] for a,b in edges)]
 allcenters=[]
 for b in range(n):
  coords=[i for i in range(n) if i!=b]
  # Coordinates are q0=-Fb followed by qv=Fv-Fb, all scaled by m.
  ds=[(-p[b],)+tuple(p[v]-p[b] for v in coords) for p in raw];dset=set(ds)
  for p in ds:
   for q in ds:
    assert tuple(min(i,j) for i,j in zip(p,q)) in dset
    assert tuple(max(i,j) for i,j in zip(p,q)) in dset
  for a in range(n):
   aa=[(0 if a==b else q[1+coords.index(a)]) for q in ds]
   for mask in range(1,1<<n):
    BB=[i for i in range(n) if mask>>i&1]
    hh=[min(0 if v==b else q[1+coords.index(v)] for v in BB) for q in ds]
    assert mean([i*j for i,j in zip(aa,hh)])>=mean(aa)*mean(hh)
  allcenters.append({'center':b,'points':len(ds),'lattice_pairs':len(ds)**2})
 return {'name':name,'mesh_denominator':m,'centers':allcenters}

results={'status':'PASS','cases':[audit_case(*c) for c in CASES], 'grid_checks':[audit_grid(*c,2) for c in CASES[:4]],'scope':'Six fixed actual posets; finite checks diagnose signs and boundary handling and do not replace the proof.'}
(OUT/'verification.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
