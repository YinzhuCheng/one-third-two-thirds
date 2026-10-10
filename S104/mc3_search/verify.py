import json,time
from pathlib import Path
OUT=Path(__file__).parent
v=json.loads((OUT/'closest_menu_boundary.json').read_text());p=v['pred'];n=len(p);pairs=v['pairs'];E=0;K=[0]*5;positions=[0]*n;start=time.time()
def walk(mask,depth):
 global E
 if depth==n:
  E+=1
  for j,(a,b) in enumerate(pairs):K[j]+=positions[a]<positions[b]
  return
 for z in range(n):
  if not(mask>>z&1) and p[z]&mask==p[z]:positions[z]=depth;walk(mask|1<<z,depth+1)
walk(0,0)
assert E==v['E'] and K==v['K']
result={'method':'Explicit enumeration of every full linear extension; no chain-ideal DP and no deletion projection','n':n,'E':E,'K':K,'matches':True,'seconds':time.time()-start}
(OUT/'independent_enumeration.json').write_text(json.dumps(result,indent=2));print(result)
