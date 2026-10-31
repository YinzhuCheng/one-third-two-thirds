"""Exact instance checks only; no claim that finite tests prove general interface lemmas."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
import itertools,json
ROOT=Path(__file__).resolve().parent
base=json.loads((ROOT/'BASE_EXAMPLE.json').read_text())

def calc(V,rels,extras=()):
 n=len(V);idx={v:i for i,v in enumerate(V)};D=[0]*n
 for r in rels:
  a,b=r.split('<');D[idx[b]]|=1<<idx[a]
 for a,b in extras:D[idx[b]]|=1<<idx[a]
 for k in range(n):
  for j in range(n):
   if D[j]>>k&1:D[j]|=D[k]
 if any(D[i]>>i&1 for i in range(n)):return 0
 @lru_cache(None)
 def C(mask):
  if mask==(1<<n)-1:return 1
  return sum(C(mask|1<<i)for i in range(n)if not mask>>i&1 and D[i]&mask==D[i])
 return C(0)

V=base['V'];rels=base['relations'];N=calc(V,rels);A=calc(V,rels,[('a2','f1')]);W=[v for v in V if v!='a2'];E=calc(W,[r for r in rels if 'a2' not in r.split('<')])
assert (N,A,E)==(201453,88349,28216)
capN=calc(V,rels,[('a2','f3')]);capA=calc(V,rels,[('a2','f3'),('a2','f1')])
assert (capN,capA)==(173237,88349) and capN==N-E and 2*capA>capN
F=json.loads((ROOT/'PRIVATE_F_EXTENSION.json').read_text());V=F['V'];rels=F['relations'];n=len(V)
D={v:set()for v in V}
for r in rels:a,b=r.split('<');D[b].add(a)
for k in V:
 for j in V:
  if k in D[j]:D[j]|=D[k]
U={v:{w for w in V if v in D[w]}for v in V}
inc=lambda a,b:a!=b and a not in D[b]and b not in D[a]
chain=lambda S:all(not inc(a,b)for a,b in itertools.combinations(S,2))
AA=(U['v']&U['c1'])-U['c2'];FF=U['c2'];T=U['v']-U['c1']
assert set(V)-U['v']-{'v'}=={'c1','c2'} and 'c1'in D['c2']
assert T=={'b','d','e'} and D['e']&T=={'d'} and D['b']&T==set() and D['d']&T==set()
assert len(AA)==5 and AA-U['d']=={'s'} and FF<=U['e'] and inc('b','s')
assert max(n-1-len(D[v])-len(U[v])for v in V)==9
VG=[];G={v:set(U[v])for v in V}
for a,b in itertools.permutations(V,2):
 if not inc(a,b):continue
 if D[a]==D[b]and chain(U[a]-U[b])and chain(U[b]-U[a]) or U[a]==U[b]and chain(D[a]-D[b])and chain(D[b]-D[a]):VG.append((a,b))
 if D[a]<=D[b]and chain(U[b]-U[a]) or U[b]<=U[a]and chain(D[a]-D[b]):G[a].add(b)
assert not VG
ind={v:sum(v in G[u]for u in V)for v in V};todo=[v for v in V if not ind[v]];order=[]
while todo:
 v=todo.pop();order.append(v)
 for u in G[v]:
  ind[u]-=1
  if not ind[u]:todo.append(u)
assert len(order)==n
modules=[]
for mask in range(1,(1<<n)-1):
 if mask.bit_count()<2:continue
 M={V[i]for i in range(n)if mask>>i&1}
 if all(len({-1 if t in D[m]else 1 if m in D[t]else 0 for m in M})==1 for t in set(V)-M):modules.append(sorted(M))
assert not modules
NF=calc(V,rels);AF=calc(V,rels,[('a2','f1')]);RF=calc(V,rels,[('c1','v')]);KF=calc(V,rels,[('c1','d')])
assert (NF,AF,RF,KF)==(825714,530536,275238,566629)
assert 2*AF>NF and RF*3==NF
result={'single_edge_cap':{'N':capN,'candidate_count':capA,'probability':str(Fraction(capA,capN)),'base_Q_extensions':E,'signed_slack_before':str(Fraction(N-2*A,E))},'private_F':{'N':NF,'candidate_count':AF,'probability':str(Fraction(AF,NF)),'R0':RF,'q0':str(Fraction(RF,NF)),'K':KF,'C2':True,'A5':True,'Delta9':True,'no_VG':True,'mixed_acyclic':True,'no_proper_nontrivial_modules':True}}
(ROOT/'REPRODUCED_VALIDATION.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
