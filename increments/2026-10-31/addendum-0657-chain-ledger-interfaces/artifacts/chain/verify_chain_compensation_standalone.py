"""Exact audit of the supplied finite witness, not a proof of the general theorem."""
import json,itertools,sys
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent / 'chain_compensation_witness_delayed_validation.json'
j=json.loads(p.read_text());V=j['vertices'];D={x:set()for x in V}
for edge in j['hasse_edges']:
 a,b=edge.split('<');D[b].add(a)
for k in V:
 for b in V:
  if k in D[b]:D[b]|=D[k]
assert not any(x in D[x]for x in V)
U={a:{b for b in V if a in D[b]}for a in V};inc=lambda a,b:a!=b and a not in D[b]and b not in D[a]
chain=lambda S:all(not inc(a,b)for a,b in itertools.combinations(S,2))
A=U['v']&U['c1']-U['c2'];F=U['c2'];L=A&U['b'];M=F-U['b'];C=F&U['b'];Q=set(V)-{'v','c1','b','c2'};K=j['K'];R=Q-set(K)-M;q,l,m=j['q_l_m']
assert set(V)-{'v'}-U['v']=={'c1','c2'} and 'c1'in D['c2']
assert U['v']-U['c1']=={'b','d','e'} and 'd'in D['e'] and inc('b','d') and inc('b','e')
assert len(A)==5 and max(len(V)-1-len(D[x])-len(U[x])for x in V)==9
assert len(K)==q+l and set(K[q:])==L and len(M)==m and l>m and l<=m*(q+1)
assert all(K[i]in D[K[i+1]]for i in range(len(K)-1)) and chain(M)
assert all(inc(k,x)for k in K for x in M)
mm=next(x for x in M if not U[x]&M)
assert D[mm]&R<=D[K[0]]&R and U[K[0]]&R<=U[mm]&R
assert not [(a,b)for a,b in itertools.combinations(V,2)if inc(a,b)and((D[a]==D[b]and chain(U[a]-U[b])and chain(U[b]-U[a]))or(U[a]==U[b]and chain(D[a]-D[b])and chain(D[b]-D[a])))]
adj={a:set(U[a])for a in V}
for a,b in itertools.permutations(V,2):
 if inc(a,b)and((D[a]<=D[b]and chain(U[b]-U[a]))or(U[b]<=U[a]and chain(D[a]-D[b]))):adj[a].add(b)
for k in V:
 for a in V:
  if k in adj[a]:adj[a]|=adj[k]
assert not any(a in adj[a]for a in V)
for mask in range(1,(1<<len(V))-1):
 if mask.bit_count()<2:continue
 S={V[i]for i in range(len(V))if mask>>i&1}
 assert not all(len({-1 if x in D[y]else 1 if y in D[x]else 0 for y in S})==1 for x in set(V)-S)
def count(removed=()):
 W=[x for x in V if x not in removed];ix={x:i for i,x in enumerate(W)};P=[sum(1<<ix[a]for a in D[b]&set(W))for b in W];full=(1<<len(W))-1
 @lru_cache(None)
 def dp(mask):
  if mask==full:return 1
  return sum(dp(mask|1<<i)for i in range(len(W))if not mask>>i&1 and P[i]&mask==P[i])
 return dp(0)
z={'N':count(),'R0':count({'c1'}),'R1':count({'v','c1'}),'B':count({'v','b','c1'}),'Z':count({'c1','c2'})}
assert z==j['counts'] and z['R0']==z['R1']+z['Z'] and z['B']<z['Z']
assert str(Fraction(z['R0'],z['N']))==j['q0'] and str(Fraction(z['R0']+z['R1']+z['B'],z['N']))==j['pd']
assert Fraction(1,3)<Fraction(z['R0'],z['N'])<Fraction(2,3)
print('PASS: C2 A5 Δ9, true full L/M, nonautonomous chain compensation, no VG/S112/module, all exact counts. q0 itself is balanced.',z)
