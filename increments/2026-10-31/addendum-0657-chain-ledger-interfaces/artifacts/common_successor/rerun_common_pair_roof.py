from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from math import comb
import json
p=Path(__file__).resolve().parent;e=json.load(open(p/'BASE_EXAMPLE.json'));V=e['V'];ix={v:i for i,v in enumerate(V)};D={v:set()for v in V}
for rel in e['relations']:
 a,b=rel.split('<');D[b].add(a)
for k in V:
 for v in V:
  if k in D[v]:D[v]|=D[k]
pre=[sum(1<<ix[d]for d in D[v])for v in V];full=(1<<len(V))-1;z='a2';y='f1';zp=ix[z];yp=ix[y];hist=[[0]*16 for _ in range(2)]
def visit(mask,word):
 if mask==full:
  iz=word.index(z);iy=word.index(y);hist[iz<iy][max(iz,iy)+1]+=1;return
 for j,v in enumerate(V):
  if not mask>>j&1 and pre[j]&mask==pre[j]:visit(mask|1<<j,word+(v,))
visit(0,())
def at(k):
 nums=[sum(hist[t][j]*comb(k+15-j,k)for j in range(1,16))for t in range(2)];return nums,Fraction(nums[1],sum(nums))
rows=[]
for k in [0,1,2,3,4,5,6,7,8,9,10,15,20,50,100]:
 nums,prob=at(k);rows.append({'chain_length':k,'N':sum(nums),'z_before_y':nums[1],'probability':str(prob),'positive_good_pair_sign':nums[1]<nums[0]})
limit=Fraction(hist[1][10],hist[0][10]+hist[1][10]);res={'hist_y_before_z':hist[0],'hist_z_before_y':hist[1],'limit':str(limit),'rows':rows};print(json.dumps(res,indent=2));(p/'COMMON_PAIR_ROOF_VALIDATION.json').write_text(json.dumps(res,indent=2))
