"""Exact counts for P(r,g,h,t): chains Y_0<...<Y_(r-1), {x}, a<b<T_1<...<T_t,
plus a<Y_g, x<Y_h and x<T_1. Here 1<=g<=h<r, t>=1.
All non-neutral backend points are above x, and width <=3 by the given chain cover.
"""
from functools import lru_cache
from fractions import Fraction
import json
from pathlib import Path
D=Path(__file__).parent

def counts(r,g,h,t):
 # State (i,j,k): used i Y's, j x's, k A-chain elements.
 L=(r,1,t+2)
 @lru_cache(None)
 def moves(s):
  i,j,k=s;ans=[]
  if i<r and (i!=g or k>=1) and (i!=h or j>=1):ans.append((0,(i+1,j,k)))
  if j<1:ans.append((1,(i,j+1,k)))
  if k<t+2 and (k!=2 or j>=1):ans.append((2,(i,j,k+1)))
  return ans
 @lru_cache(None)
 def F(s):return 1 if s==L else sum(F(v) for c,v in moves(s))
 E=F((0,0,0));K=[0]*5;H={(0,0,0):1}
 # Pair order a<x,a<y,b<x,b<y,x<y.
 for step in range(sum(L)):
  N={}
  for s,w in H.items():
   for c,v in moves(s):
    N[v]=N.get(v,0)+w;wgt=w*F(v)
    if c==2 and s[2]==0:
     if s[1]==0:K[0]+=wgt
     if s[0]==0:K[1]+=wgt
    if c==2 and s[2]==1:
     if s[1]==0:K[2]+=wgt
     if s[0]==0:K[3]+=wgt
    if c==1 and s[0]==0:K[4]+=wgt
  H=N
 return E,K

def main():
 table=[]
 for t in range(1,41):
  E,K=counts(4,1,2,t)
  table.append(dict(t=t,n=t+7,E=E,K=K,probabilities=[str(Fraction(k,E)) for k in K],premise=all(3*K[i]>2*E for i in (0,1,4)),half_slack=2*K[2]-K[0],L_slack=3*K[2]-E))
 (D/'family_4_1_2.json').write_text(json.dumps(table,indent=2))
 eligible=[];bad=[];Lbad=[];evaluations=0
 for r in range(2,13):
  for g in range(1,r):
   for h in range(g,r):
    for t in range(1,41):
     E,K=counts(r,g,h,t);evaluations+=1
     if all(3*K[i]>2*E for i in (0,1,4)):
      row=dict(r=r,g=g,h=h,t=t,n=r+t+3,E=E,K=K,half_slack=2*K[2]-K[0],L_slack=3*K[2]-E)
      eligible.append(row)
      if row['half_slack']<0:bad.append(row)
      if row['L_slack']<0:Lbad.append(row)
 result=dict(evaluations=evaluations,qualified=len(eligible),half_counterexamples=len(bad),L_counterexamples=len(Lbad),minimum_size_half_counterexample=min(bad,key=lambda z:z['n']) if bad else None,best_half_delta=min(bad,key=lambda z:Fraction(z['half_slack'],z['E'])) if bad else None,L_counterexample_certificates=Lbad)
 (D/'family_summary.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()
