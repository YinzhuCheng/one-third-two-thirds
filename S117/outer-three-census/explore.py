from math import comb,prod
from collections import Counter
from pathlib import Path
import json,time
V={1:3,2:9,3:29};M={1:3,2:19,3:90}

def pairs(a):
 return [(u,b) for u in range(2,V[a]+1) for b in range(1,M[a]+1) if 3*prod(range(b,b+a+1))<prod(range(b+u,b+u+a+1))]

def uppers(a,u):
 s=0
 while 3*prod(range(s+1,s+a+1))<=2*prod(range(s+u+1,s+u+a+1)):s+=1
 return s

def lowers(a,u,b):
 h=0
 while comb(a+b+h+u,u)<=3*comb(a+b+u-1,u):h+=1
 return h

def main():
 start=time.time();ps={a:pairs(a) for a in V};up={(a,u):uppers(a,u) for a in V for u in range(2,V[a]+1)};lo={(a,u,b):lowers(a,u,b) for a in V for u,b in ps[a]}
 print('pair_counts',{a:len(p) for a,p in ps.items()},'upper thresholds',up,flush=True)
 summary={};survivors=[]
 for a,d in ((1,3),(2,3),(3,1),(3,2),(3,3)):
  counts=Counter();maxn=0;maxw=[]
  for u,b in ps[a]:
   for v,c in ps[d]:
    low=max(1,2*u-a-b-v+1,2*v-u-c-d+1);high=(b+c+min(u,v)-1)//2
    if low>high:continue
    counts['candidates']+=high-low+1
    n=u+a+b+c+high+d+v
    if n>maxn:maxn=n;maxw=[(u,a,b,c,high,d,v)]
    elif n==maxn:maxw.append((u,a,b,c,high,d,v))
    low=max(low,up[a,u]-b-v)
    if low>high:continue
    counts['upper1']+=high-low+1
    low=max(low,up[d,v]-c-u)
    if low>high:continue
    counts['upper2']+=high-low+1
    low=max(low,lo[a,u,b]-v)
    if low>high:continue
    counts['lower1']+=high-low+1
    low=max(low,lo[d,v,c]-u)
    if low>high:continue
    counts['lower2']+=high-low+1
    survivors.extend((u,a,b,c,t,d,v) for t in range(low,high+1))
  summary[f'{a},{d}']={'counts':dict(counts),'maxn':maxn,'maxw':maxw}
  print(a,d,summary[f'{a},{d}'],'seconds',time.time()-start,flush=True)
 Path(__file__).with_name('analytic_survivors.json').write_text(json.dumps(survivors,separators=(',',':'))+'\n')
 Path(__file__).with_name('domain_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
if __name__=='__main__':main()
