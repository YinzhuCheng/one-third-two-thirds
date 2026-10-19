#!/usr/bin/env python3
"""Independent labeled-ideal DP: no word/fiber/rank mixture used."""
import json
from itertools import combinations
from functools import lru_cache
from pathlib import Path
HERE=Path(__file__).parent
results=json.loads((HERE/'counts.json').read_text())
verification=[]
for r in results:
 n=r['n'];N=n*n;rel={tuple(x) for x in r['edges']};pred=[0]*N
 for p in range(n):
  for a in range(n):
   v=p*n+a
   for q in range(n):
    for b in range(n):
     if (q,p) in rel or (q==p and (b,a) in rel):pred[v]|=1<<(q*n+b)
 FULL=(1<<N)-1
 @lru_cache(None)
 def succ(mask):
  return tuple((v,mask|(1<<v)) for v in range(N) if not(mask>>v&1) and (pred[v]&~mask)==0)
 @lru_cache(None)
 def suffix(mask):
  if mask==FULL:return 1
  return sum(suffix(mm) for v,mm in succ(mask))
 E=suffix(0)
 assert E==r['E']
 layers=[{0:1}]
 for d in range(N):
  nxt={}
  for mask,F in layers[-1].items():
   for v,mm in succ(mask):nxt[mm]=nxt.get(mm,0)+F
  layers.append(nxt)
 assert layers[-1][FULL]==E
 pairs=[(u,v) for u,v in combinations(range(N),2) if not(pred[v]>>u&1) and not(pred[u]>>v&1)]
 counts={uv:0 for uv in pairs}
 for layer in layers[:-1]:
  for mask,F in layer.items():
   for u,mm in succ(mask):
    w=F*suffix(mm)
    for v in range(u+1,N):
     if (u,v) in counts and not(mask>>v&1):counts[u,v]+=w
 checked=0
 for t in r['cross_records']:
  p,q=t['core'];a,b=t['inner'];assert counts[p*n+a,q*n+b]==t['count'];checked+=1
 for p in range(n):
  for pair,num in r['base_pair_counts'].items():
   a,b=map(int,pair.split(','));assert counts[p*n+a,p*n+b]==num*E//r['eP'];checked+=1
 assert checked==len(pairs)
 item={'name':r['name'],'labeled_elements':N,'labeled_ideal_states':sum(len(x) for x in layers),'E':E,'all_incomparable_pair_counts_checked':checked,'agrees':True}
 print(item,flush=True);verification.append(item)
(HERE/'direct_ideal_verification.json').write_text(json.dumps(verification,indent=2)+'\n')
