#!/usr/bin/env python3
"""Exact independent full-set checks of the universal two-conditioning corollary.
Standalone enumeration, no imports from proposal scripts or prior stage checks.
"""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json
OUT=Path(__file__).resolve().parent

def transitive(r):
 r=list(r)
 for k in range(len(r)):
  for i in range(len(r)):
   if r[i]>>k&1:r[i]|=r[k]
 assert all(not (v>>i&1) for i,v in enumerate(r))
 return tuple(r)

def preds(r):return tuple(sum(1<<j for j in range(len(r)) if r[j]>>i&1) for i in range(len(r)))
def extensions(r):
 p=preds(r); n=len(r)
 def walk(mask,order):
  if mask==(1<<n)-1:yield order;return
  for v in range(n):
   if not mask>>v&1 and p[v]&mask==p[v]:yield from walk(mask|1<<v,order+(v,))
 return set(walk(0,()))
def posets(n):
 pairs=list(combinations(range(n),2)); seen=set()
 for mask in range(1<<len(pairs)):
  r=[0]*n
  for bit,(a,b) in enumerate(pairs):
   if mask>>bit&1:r[a]|=1<<b
  r=transitive(r)
  if r not in seen:seen.add(r);yield r

def cells(r,a,b,es):
 p=preds(r); out=[[0]*4 for _ in range(2)]
 for e in es:
  q={v:i for i,v in enumerate(e)}; side=int(q[a]>q[b]); x,y=(b,a) if side else (a,b)
  s=any(q[v]<q[y] for v in range(len(r)) if r[x]>>v&1)
  t=any(q[v]>q[x] for v in range(len(r)) if p[y]>>v&1)
  out[side][int(s)+2*int(t)]+=1
 return out

report=[]
for n in range(2,6):
 c=Counter(n=n)
 for r in posets(n):
  c['posets']+=1;p=preds(r);es=extensions(r)
  for a,b in combinations(range(n),2):
   if r[a]>>b&1 or r[b]>>a&1:continue
   c['incomparable_pairs']+=1
   z=cells(r,a,b,es);(h,rr,ll,k),(hh,rp,lp,kp)=z
   assert h==hh and h>0 and rr*rp<=h*h and ll*lp<=h*h
   D=p[a]|p[b];U=r[a]|r[b]; rd=list(r);ru=list(r)
   for v in range(n):
    if D>>v&1:rd[v]|=(1<<a)|(1<<b)
   ru[a]|=U;ru[b]|=U
   rd=transitive(rd);ru=transitive(ru);pd=preds(rd);pu=preds(ru)
   assert pd[a]==pd[b]==D and rd[a]==r[a] and rd[b]==r[b]
   assert ru[a]==ru[b]==U and pu[a]==p[a] and pu[b]==p[b]
   ed=extensions(rd);eu=extensions(ru)
   fd={e for e in es if all(e.index(v)<min(e.index(a),e.index(b)) for v in range(n) if D>>v&1)}
   fu={e for e in es if all(e.index(v)>max(e.index(a),e.index(b)) for v in range(n) if U>>v&1)}
   assert ed==fd and eu==fu
   assert cells(rd,a,b,ed)==[[h,rr,0,0],[h,rp,0,0]]
   assert cells(ru,a,b,eu)==[[h,0,ll,0],[h,0,lp,0]]
   rdstar=preds(ru);edstar=extensions(rdstar)
   assert edstar=={tuple(reversed(e)) for e in eu}
   assert cells(rdstar,a,b,edstar)==[[h,lp,0,0],[h,ll,0,0]]
   E=len(es);forward=h+rr+ll+k;s=rr+k;t=ll+k;sp=rp+kp;tp=lp+kp
   assert (E-t-tp)*(s-k)<= (forward-t)**2
   assert (E-s-sp)*(t-k)<= (forward-s)**2
   neutral=[v for v in range(n) if v not in(a,b) and not (p[a]|p[b]|r[a]|r[b])>>v&1]
   c['nonchain_neutral_pairs']+=any(not ((r[x]>>y&1) or (r[y]>>x&1)) for x,y in combinations(neutral,2))
 report.append(dict(c)); print(json.dumps(dict(c)),flush=True)
(OUT/'audit_universal_conditioning_exact.json').write_text(json.dumps({'status':'PASS','by_n':report},indent=2)+'\n')
print('ALL CONDITIONING CHECKS PASS')
