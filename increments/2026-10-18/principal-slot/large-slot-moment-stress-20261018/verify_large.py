#!/usr/bin/env python3
"""Independent Python prefix-splitting verification of already tested large pairs.

This does not add stress pairs. It recomputes the full uniform-LE counts using
Python integers and a different mixed-moment identity, without the C++ product
reward accumulator.
"""
from array import array
from itertools import product
from pathlib import Path
import json
import time
P=Path(__file__).resolve().parent
summary=json.loads((P/'summary.json').read_text())
objects={c['name']:c for c in json.loads((P/'objects.json').read_text())['objects']}
rows=[json.loads(x) for x in (P/'raw_results.jsonl').read_text().splitlines()]
cases={r['name']:r for r in rows if r['type']=='case'}
selected=[]
for key in ['target_relative_gap','covariance_relative_gap_distinct_nonempty','covariance_relative_gap_asymmetric10_nonempty','covariance_relative_gap_overlap_nonnested']:
 r=summary['extrema'][key]['record'];selected.append((r['case'],r['i'],r['j']))
selected.append(next((r['case'],r['i'],r['j']) for r in rows if r['type']=='pair' and r['case']=='disjoint3_66_67_67' and r['class']=='nested'))
selected=list(dict.fromkeys(selected))
report=[];start=time.time()
for name,iy,iz in selected:
 obj=objects[name];case=cases[name];L=obj['lengths'];k=len(L);cross=obj['cross'];st=[1]
 for n in L[:-1]:st.append(st[-1]*(n+1))
 ng=1
 for n in L:ng*=n+1
 idx=array('i',[-1])*ng;states=[]
 for z in product(*(range(n+1) for n in reversed(L))):
  x=tuple(reversed(z))
  if all(x[b]<=q or x[a]>p for a,p,b,q in cross):
   enc=sum(a*s for a,s in zip(x,st));idx[enc]=len(states);states.append((enc,x))
 ns=len(states);F=[0]*ns;G=[0]*ns;F[0]=1
 for i,(enc,x) in enumerate(states):
  for c in range(k):
   if x[c]<L[c]:
    j=idx[enc+st[c]]
    if j>=0:F[j]+=F[i]
 G[-1]=1
 for i in range(ns-2,-1,-1):
  enc,x=states[i]
  G[i]=sum(G[idx[enc+st[c]]] for c in range(k) if x[c]<L[c] and idx[enc+st[c]]>=0)
 K=F[-1];assert K==G[0]==int(case['le'])
 sy=case['filters'][iy]['threshold'];sz=case['filters'][iz]['threshold']
 ay=[i>0 and all(a<=b for a,b in zip(x,sy)) for i,(enc,x) in enumerate(states)]
 az=[i>0 and all(a<=b for a,b in zip(x,sz)) for i,(enc,x) in enumerate(states)]
 H=[0]*ns;J=[0]*ns
 for i in range(1,ns):
  enc,x=states[i];pred=[idx[enc-st[c]] for c in range(k) if x[c]>0 and idx[enc-st[c]]>=0]
  H[i]=sum(H[j] for j in pred)+F[i]*ay[i]
  J[i]=sum(J[j] for j in pred)+F[i]*az[i]
 A=B=C=D=AA=BB=0
 for i in range(1,ns):
  f,g=F[i],G[i];a,b=ay[i],az[i]
  A+=f*g*a;B+=f*g*b;D+=f*g*a*b
  C+=g*(H[i]*b+J[i]*a-f*a*b)
  AA+=g*(2*H[i]*a-f*a);BB+=g*(2*J[i]*b-f*b)
 assert A==H[-1] and B==J[-1]
 expected=next(r for r in rows if r['type']=='pair' and (r['case'],r['i'],r['j'])==(name,iy,iz))
 keys=['sum_Ry','sum_Rz','sum_product','sum_min','sum_Ry2','sum_Rz2'];vals=[A,B,C,D,AA,BB]
 assert all(v==int(expected[key]) for key,v in zip(keys,vals))
 report.append(dict(case=name,i=iy,j=iz,n=sum(L),states=ns,complete_LE_count=str(K),moments={key:str(v) for key,v in zip(keys,vals)},passed=True))
 print('Verified',name,iy,iz,'states',ns,flush=True)
 del F,G,H,J,states,idx,ay,az
(P/'large_verification.json').write_text(json.dumps(dict(method='Independent Python prefix-splitting identity with complete LE counts; no new stress pairs',pairs=report,all_passed=True,seconds=round(time.time()-start,3)),indent=2)+'\n')
