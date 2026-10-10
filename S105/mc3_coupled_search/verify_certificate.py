#!/usr/bin/env python3
"""Independent verifier: vertex-bitmask ideal deletion, adding each event edge.
No search module or chain-state DP imports. Arbitrary-precision Python integers.
"""
import json,sys,itertools
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
sys.setrecursionlimit(10000)
source=Path(sys.argv[1] if len(sys.argv)>1 else 'MC3_COUNTEREXAMPLE_high.json')
doc=json.loads(source.read_text()); lens=doc['shape']; n=sum(lens)
chains=[];off=0
for size in lens:chains.append(list(range(off,off+size)));off+=size
x,y,a=map(lambda chain:chain[0],chains);b=a+1
edges=[(u,v) for c in chains for u,v in zip(c,c[1:])]+list(map(tuple,doc['extra_edges']))
pred=[0]*n
for u,v in edges:pred[v]|=1<<u
anc=pred[:]
for k in range(n):
 for v in range(n):
  if anc[v]>>k&1:anc[v]|=anc[k]
assert all(not(anc[v]>>v&1) for v in range(n))
minima=[v for v in range(n) if anc[v]==0]
assert set(minima)=={a,x,y} and anc[b]==1<<a
assert set(sum(chains,[]))==set(range(n))
assert all(anc[v]>>u&1 for ch in chains for u,v in zip(ch,ch[1:]))
B=[v for v in range(n) if v not in [x,y] and not(anc[v]>>x&1 or anc[v]>>y&1)]
assert B==[a,b]
assert all(not(anc[v]>>u&1) for u,v in itertools.permutations(minima,2))
full=(1<<n)-1
# Recurrence on arbitrary vertex subsets, generating only legal ideals.
def count(extra=None):
 req=pred[:]
 if extra:
  u,v=extra;req[v]|=1<<u
 @lru_cache(None)
 def dp(I):
  if I==full:return 1
  out=0;rest=full^I
  while rest:
   bit=rest&-rest;rest-=bit;v=bit.bit_length()-1
   if req[v]&I==req[v]:out+=dp(I|bit)
  return out
 z=dp(0);return z,dp.cache_info().currsize
E,states=count();pairs=[(a,x),(a,y),(b,x),(b,y),(x,y)]
K=[];reverse=[];pair_states=[]
for u,v in pairs:
 z,s=count((u,v));r,t=count((v,u));assert z+r==E
 K.append(z);reverse.append(r);pair_states.append([s,t])
assert E==int(doc['E']) and K==list(map(int,doc['K']))
ori=doc.get('orientation',0)
OK=K if not ori else [K[1],K[0],K[3],K[2],E-K[4]]
slack=[3*OK[0]-2*E,3*OK[1]-2*E,3*OK[4]-2*E,E-3*OK[2],3*OK[3]-2*E]
balanced=[i for i,k in enumerate(K) if E<=3*k<=2*E]
record={'input':str(source),'n':n,'width':3,'chain_cover':chains,'generating_edges':edges,'minima':minima,'avoidance_B':B,'labels':{'x':x,'y':y,'a':a,'b':b},'E':E,'K':K,'reverse_K':reverse,'fractions':[str(Fraction(k,E)) for k in K],'decimals':[float(Fraction(k,E)) for k in K],'oriented_high_target_integer_slacks':slack,'balanced_menu_indices':balanced,'independent_ideal_states':states,'pair_ideal_states':pair_states,'source_counts_match':True,'verification_method':'independent bitmask-ideal recurrence, each of five event orders and all five complements added as a prerequisite','MC3_counterexample':all(s>0 for s in slack) or (all(s>0 for s in slack[:4]) and 3*OK[3]<E)}
out=source.with_name('verified_'+source.name);out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
