from functools import lru_cache
from fractions import Fraction
from itertools import combinations,permutations
import json,sys
E=json.load(open(sys.argv[1]));V=E['vertices'];D={x:set()for x in V}
for rel in E['relations']:
 a,b=rel.split('<');D[b].add(a)
for k in V:
 for j in V:
  if k in D[j]:D[j]|=D[k]
assert all(x not in D[x] for x in V)
U={x:{y for y in V if x in D[y]}for x in V};ic=lambda a,b:a!=b and a not in D[b]and b not in D[a];chain=lambda S:all(not ic(a,b)for a,b in combinations(S,2))
A=U['v']&U['c1']-U['c2'];F=U['c2'];R=A&U['e'];S=A-U['d'];HA=A-{'s'}-R
ix={v:i for i,v in enumerate(V)};full=(1<<len(V))-1
pre=[sum(1<<ix[d]for d in D[v])for v in V]
def count(extra=()):
 pp=pre.copy()
 for a,b in extra:pp[ix[b]]|=1<<ix[a]
 @lru_cache(None)
 def f(mask):
  if mask==full:return 1
  return sum(f(mask|1<<i)for i,p in enumerate(pp)if not mask>>i&1 and p&mask==p)
 return f(0)
vg=[]
for a,b in combinations(V,2):
 if ic(a,b)and ((D[a]==D[b]and chain(U[a]-U[b])and chain(U[b]-U[a]))or(U[a]==U[b]and chain(D[a]-D[b])and chain(D[b]-D[a]))):vg.append([a,b])
adj={a:set(U[a])for a in V}
for a,b in permutations(V,2):
 if ic(a,b)and ((D[a]<=D[b]and chain(U[b]-U[a]))or(U[b]<=U[a]and chain(D[a]-D[b]))):adj[a].add(b)
ind={a:sum(a in adj[b]for b in V)for a in V};q=[a for a in V if not ind[a]];order=[]
while q:
 a=q.pop();order.append(a)
 for b in adj[a]:
  ind[b]-=1
  if not ind[b]:q.append(b)
mods=[]
for mask in range(1,full):
 if mask.bit_count()<2:continue
 M={V[i]for i in range(len(V))if mask>>i&1}
 if all(len({-1 if x in D[y]else 1 if y in D[x]else 0 for y in M})==1 for x in set(V)-M):mods.append(sorted(M))
assert set(V)-{'v'}-U['v']=={'c1','c2'} and U['v']-U['c1']=={'b','d','e'} and 'c1' in D['c2'] and 'd' in D['e']
assert S=={'s'} and 'b' in D['s'] and F<=U['e']
N=count();K=count([('c1','d')]);R0=count([('c1','v')]);EA=count([('v','c1')])-count([('v','c1')]+[('d',s)for s in S]);G=count([('e','c1')])-count([('e','c1')]+[('c2',r)for r in R]);mx=min([len(R&D[f])for f in F] or [len(R)]);ms=min([len(R&D[u])for u in U['s']] or [len(R)]);common=[r for r in R if F|U['s']<=U[r]]
Eearly=count([('v','c1'),('s','d')]+[('c2',r)for r in R]);Elate=EA-Eearly
GA_base=[('e','c1'),('c1','s')]+[('s',u)for u in U['e']]+([('b','e')]if 'b' in D['s']else [])
GA=count(GA_base)-count(GA_base+[('c2',r)for r in R]);assert GA==Elate
assert 2*K==N+R0+EA-G
res={'C2':True,'N':N,'K':K,'R0':R0,'E_A':EA,'E_A_late_compensated':Elate,'E_A_early_residual':Eearly,'G_A_exact_image':GA,'G':G,'net':2*K-N-R0,'q0':str(Fraction(R0,N)),'pd':str(Fraction(K,N)),'A':sorted(A),'F':sorted(F),'R':sorted(R),'S':sorted(S),'H_A':sorted(HA),'mx':mx,'ms':ms,'common_anchors':common,'inc':{v:len(V)-1-len(D[v])-len(U[v])for v in V},'VG':vg,'mixed_acyclic':len(order)==len(V),'modules':mods,'rank_profiles_F':{f:sorted(R&D[f])for f in F},'rank_profiles_Us':{f:sorted(R&D[f])for f in U['s']}}
print(json.dumps(res,indent=2));json.dump(res,open(sys.argv[1]+'.checked.json','w'),indent=2)
