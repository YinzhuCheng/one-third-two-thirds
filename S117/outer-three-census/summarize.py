#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
P=Path(__file__).parent

def require(ok,*why):
 if not ok:raise RuntimeError(why)
def dual(w):u,a,b,c,t,d,v=w;return v,d,c,b,t,a,u

def main():
 ws=[tuple(w) for w in json.loads((P/'analytic_survivors.json').read_text())]
 rows={}
 for ln in (P/'exact_counts.txt').read_text().splitlines():
  r=list(map(int,ln.split()));require(len(r)==12,'columns',r);w=tuple(r[:7]);require(w not in rows,'duplicate',w);rows[w]=r[7:]
 require(set(rows)==set(ws),'residual_domain')
 exact_names=['B1<B0','T6<T5','T2<T0','B2<B4','B6<B3','T4<T3']
 passes=[0]*6;single=[0]*6;rejections=Counter();mins=[None,None];minw=[[],[]];final=[];eq=Counter()
 for w,(z,n10,n65,n02,n24) in rows.items():
  zd,dn10,dn65,n63,n43=rows[dual(w)]
  require(z==zd,'dual_denominator',w)
  require(n10==dn65 and n65==dn10,'dual_outer_numerators',w)
  nums=[n10,n65,z-n02,n24,z-n63,n43];ps=[3*n>2*z for n in nums]
  for k,pr in enumerate(ps):
   if pr:single[k]+=1
   if all(ps[:k+1]):passes[k]+=1
   if 3*nums[k]==2*z:eq[exact_names[k]]+=1
  if all(ps):final.append(w)
  else:rejections[exact_names[ps.index(False)]]+=1
  for k,p in enumerate((Fraction(n02,z),Fraction(n63,z))):
   if mins[k] is None or p<mins[k]:mins[k]=p;minw[k]=[w]
   elif p==mins[k]:minw[k].append(w)
 require(not final,'unresolved',final)
 summary={'status':'ALL_ANALYTIC_SURVIVORS_EXACTLY_REJECTED','analytic_survivors':len(rows),'exact_filter_order':exact_names,'cumulative_passes':passes,'standalone_passes':single,'first_rejection_counts':dict(rejections),'equalities':dict(eq),'final_survivors':final,'minimum_p_T0_before_T2':{'value':str(mins[0]),'vectors':minw[0]},'minimum_p_B3_before_B6':{'value':str(mins[1]),'vectors':minw[1]},'duality_checks':len(rows),'exact_counts_sha256':hashlib.sha256((P/'exact_counts.txt').read_bytes()).hexdigest()}
 (P/'exact_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
