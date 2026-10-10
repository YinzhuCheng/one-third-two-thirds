import json,sys
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
D=Path(__file__).parent
c=json.loads((D/(sys.argv[1] if len(sys.argv)>1 else 'COUNTEREXAMPLE.json')).read_text())
L=c['shape'];n=sum(L);chains=[];off=0
for length in L: chains.append(list(range(off,off+length)));off+=length
edges=[(u,v) for ch in chains for u,v in zip(ch,ch[1:])]+[tuple(e) for e in c['extra_edges']]
pred=[0]*n
for u,v in edges:pred[v]|=1<<u
for k in range(n):
 for v in range(n):
  if pred[v]>>k&1:pred[v]|=pred[k]
assert all(not (pred[z]>>z&1) for z in range(n))
a,b=chains[2][:2];x,y=chains[0][0],chains[1][0]
if c['orientation']:x,y=y,x
assert not pred[x] and not pred[y] and not pred[a] and pred[b]==1<<a
assert [z for z in range(n) if z not in (x,y) and not (pred[z]>>x&1 or pred[z]>>y&1)]==[a,b]
# A full LE enumeration, independent of chain-state DP.
pairs=[(a,x),(a,y),(b,x),(b,y),(x,y)];K=[0]*5;E=0
full=(1<<n)-1

def enumerate_le(mask,order):
 global E
 if mask==full:
  E+=1;rank={v:i for i,v in enumerate(order)}
  for q,(u,v) in enumerate(pairs):K[q]+=rank[u]<rank[v]
  return
 for z in range(n):
  if not(mask>>z&1) and pred[z]&mask==pred[z]:enumerate_le(mask|1<<z,order+[z])
enumerate_le(0,[])
expected=[int(c['K'][1]),int(c['K'][0]),int(c['K'][3]),int(c['K'][2]),int(c['E'])-int(c['K'][4])] if c['orientation'] else list(map(int,c['K']))
assert E==int(c['E']) and K==expected
assert all(3*K[i]>2*E for i in (0,1,4))
assert 2*K[2]<K[0]
# Independently check every full-poset event by adding an order relation and ideal DP.
def count(extra=()):
 p=pred[:]
 for u,v in extra:p[v]|=1<<u
 @lru_cache(None)
 def f(mask):
  if mask==full:return 1
  return sum(f(mask|1<<v) for v in range(n) if not(mask>>v&1) and p[v]&mask==p[v])
 return f(0)
assert count()==E
assert [count(((u,v),)) for u,v in pairs]==K
# Delete a,b and reconstruct the exact slot fibers (no assumed uniform projection).
Q=[z for z in range(n) if z not in (a,b)];qm=sum(1<<z for z in Q);fibers=[]
def enumQ(mask,order):
 if mask==qm:
  rank={z:i+1 for i,z in enumerate(order)};A=min([rank[z] for z in Q if pred[z]>>a&1]+[len(Q)+1]);B=min([rank[z] for z in Q if pred[z]>>b&1]+[len(Q)+1]);kx,ky=rank[x],rank[y];N=A*B-A*(A-1)//2
  def F(k):return sum(B-i+1 for i in range(1,min(A,k)+1))
  def G(k):return sum(min(A,j) for j in range(1,min(B,k)+1))
  fibers.append((A,B,kx,ky,N,F(kx),F(ky),G(kx),G(ky)))
  return
 for z in Q:
  if not(mask>>z&1) and (pred[z]&qm)&mask==pred[z]&qm:enumQ(mask|1<<z,order+[z])
enumQ(0,[])
assert sum(f[4] for f in fibers)==E
assert [sum(f[j] for f in fibers) for j in (5,6,7,8)]+[sum(f[4] for f in fibers if f[2]==1)]==K
covers=[(u,v) for v in range(n) for u in range(n) if pred[v]>>u&1 and not any(w!=u and pred[v]>>w&1 and pred[w]>>u&1 for w in range(n))]
out=dict(n=n,E=E,K_oriented=K,pairs=pairs,probabilities=[str(Fraction(k,E)) for k in K],hypothesis_integer_slacks=[3*K[i]-2*E for i in (0,1,4)],half_integer_slack=2*K[2]-K[0],lower_bound_integer_slack=3*K[2]-E,chain_cover=chains,covers=covers,Q_extensions=len(fibers),verification=['full linear-extension enumeration','independent event-added ideal DP','exact two-deletion fiber sum'])
(D/(sys.argv[2] if len(sys.argv)>2 else 'verified_counterexample.json')).write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
