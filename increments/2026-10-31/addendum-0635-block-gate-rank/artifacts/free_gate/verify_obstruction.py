from pathlib import Path
ROOT=Path(__file__).resolve().parent
import json,itertools,collections
from functools import lru_cache
from fractions import Fraction
x=json.loads((ROOT/'EXAMPLE.json').read_text())
V=x['V'];n=len(V);idx={v:i for i,v in enumerate(V)}
lt=[[False]*n for _ in V]
for r in x['relations']:
 a,b=r.split('<');lt[idx[a]][idx[b]]=True
for k in range(n):
 for i in range(n):
  for j in range(n):lt[i][j]|=lt[i][k] and lt[k][j]
assert not any(lt[i][i]for i in range(n))
D={v:{V[j]for j in range(n)if lt[j][i]}for i,v in enumerate(V)}
U={v:{V[j]for j in range(n)if lt[i][j]}for i,v in enumerate(V)}
inc=lambda a,b:a!=b and a not in D[b]and b not in D[a]
chain=lambda S:all(not inc(a,b)for a,b in itertools.combinations(S,2))
A=(U['v']&U['c1'])-U['c2'];F=U['c2'];T=U['v']-U['c1']
assert D['v']==set() and set(V)-U['v']-{'v'}=={'c1','c2'} and lt[idx['c1']][idx['c2']]
assert T=={'b','d','e'} and D['e']&T=={'d'} and D['d']&T==set() and D['b']&T==set()
assert len(A)==5 and A-U['d']=={'s'} and inc('b','s') and F<=U['e']
inc_counts={v:sum(inc(v,w)for w in V)for v in V};assert max(inc_counts.values())==9
vg=[];adj={v:set(U[v])for v in V}
for a,b in itertools.permutations(V,2):
 if not inc(a,b):continue
 if D[a]==D[b] and chain(U[a]-U[b]) and chain(U[b]-U[a]):vg.append((a,b,'primal'))
 if U[a]==U[b] and chain(D[a]-D[b]) and chain(D[b]-D[a]):vg.append((a,b,'dual'))
 if D[a]<=D[b] and chain(U[b]-U[a]) or U[b]<=U[a]and chain(D[a]-D[b]):adj[a].add(b)
assert not vg
ind={v:sum(v in adj[w]for w in V)for v in V};q=collections.deque(v for v in V if ind[v]==0);order=[]
while q:
 v=q.popleft();order.append(v)
 for w in adj[v]:
  ind[w]-=1
  if ind[w]==0:q.append(w)
assert len(order)==n
modules=[]
for k in range(2,n):
 for Mtuple in itertools.combinations(V,k):
  M=set(Mtuple)
  if all(len({-1 if z in D[m] else 1 if z in U[m]else 0 for m in M})==1 for z in set(V)-M):modules.append(Mtuple)
# Completion DP independently for added constraints, permitting closure-free masks.
def count(extra=()):
 pred=[sum(1<<idx[a]for a in D[b])for b in V]
 for a,b in extra:pred[idx[b]]|=1<<idx[a]
 @lru_cache(None)
 def f(rem):
  if rem==0:return 1
  return sum(f(rem^(1<<i))for i in range(n)if rem>>i&1 and pred[i]&rem==0)
 return f((1<<n)-1)
N=count();R0=count([('c1','v')]);K=count([('c1','d')]);E=count([('v','c1'),('s','d')]);R=A&U['e'];G=0
# Inclusion-exclusion for existential R before c2.
base=[('v','d'),('d','e'),('e','c1')]
for k in range(1,len(R)+1):
 for B in itertools.combinations(R,k):G+=(-1)**(k+1)*count(base+[(r,'c2')for r in B])
assert (N,R0,K)==(201453,66867,137524)
assert 2*K==N+R0+E-G
assert 3*R0<N and 3*K>2*N
balanced=[]
for a,b in itertools.combinations(V,2):
 if inc(a,b):
  C=count([(a,b)])
  if N<=3*C<=2*N:balanced.append({'pair':[a,b],'numerator':C,'probability':str(Fraction(C,N))})
# Output irredundant relation presentation.
hasse=[a+'<'+b for a in V for b in U[a]if not any(c in U[a]and b in U[c]for c in V)]
result={'checked_file':'EXAMPLE.json','C2':True,'A':sorted(A),'F':sorted(F),'T':sorted(T),'S':sorted(A-U['d']),'b_incomparable_s':True,'e_below_F':True,'inc_counts':inc_counts,'very_good_pairs':vg,'mixed_graph_topological_order':order,'proper_nontrivial_modules':modules,'N':N,'R0':R0,'K':K,'E':E,'G':G,'signed_net':E-G,'root_menu_failure':True,'q0':str(Fraction(R0,N)),'pd':str(Fraction(K,N)),'balanced_pairs':balanced,'Hasse_relations':sorted(hasse)}
json.dump(result,open(ROOT/'VALIDATION.json','w'),indent=2)
print(json.dumps(result,indent=2))
