#!/usr/bin/env python3
"""Standard-library cross-check of every residual's integer arithmetic.
No imports from the enumerator or C++ implementation. Not peer review.
"""
from pathlib import Path
from math import factorial
from fractions import Fraction
from collections import Counter
import json,time,hashlib,argparse
P=Path(__file__).parent

def check(ok,*context):
 if not ok:raise RuntimeError(context)

FAC=[factorial(n) for n in range(349)]
C=[[FAC[n]//(FAC[k]*FAC[n-k]) for k in range(n+1)] for n in range(349)]

def exact(w):
 u,a,b,c,t,d,v=w
 z=n10=n65=n02=n24=0
 for j in range(t+1):
  q=C[b+j-1][j]
  h=1 if j==0 else C[b+j-2][j] if b>1 else 0
  for i in range(u+1):
   p=C[a+b+i+j-1][i];tail=C[u-i+c+t-j][t-j]
   g=tail*C[u-i+c+t-j+d+v][v]
   term=q*p*g
   z+=term
   n10+=q*C[a+b+i+j-2][i]*g
   n65+=q*p*tail*C[u-i+c+t-j+d+v-1][v]
   if i==u:n02+=term
   n24+=h*p*g
 return (z,n10,n65,n02,n24)

def main(output):
 start=time.time()
 A=[tuple(map(int,ln.split())) for ln in (P/'analytic_survivors.txt').read_text().splitlines()]
 B=[tuple(map(int,ln.split())) for ln in (P/'independent_domain.txt').read_text().splitlines()]
 check(len(A)==len(set(A)) and len(B)==len(set(B)) and set(A)==set(B),'independent_domain_disagreement')
 rows={}
 for ln in (P/'exact_counts.txt').read_text().splitlines():
  r=list(map(int,ln.split()));check(len(r)==12,'row_length');w=tuple(r[:7]);check(w not in rows,'duplicate');rows[w]=tuple(r[7:])
 check(set(rows)==set(A),'exact_count_domain')
 for k,(w,saved) in enumerate(rows.items(),1):
  got=exact(w);check(got==saved,'exact_counts',w,got,saved)
  z,n10,n65,n02,n24=got
  check(3*n02>=z,'failed_rejection',w)
  u,a,b,c,t,d,v=w
  for x,y,small,spine,port,other in ((a+b+t+v+u,u,a+b+u-1,a,u,b+t+v),(d+c+t+u+v,v,d+c+v-1,d,v,c+t+u)):
   check(3*C[x-spine][y]>2*C[x][y],'upper_binomial',w)
   check(3*C[small][y]<C[x][y],'lower_binomial',w)
  if k%2000==0:print('verified',k,'seconds',round(time.time()-start,3),flush=True)
 # C++ direct domain counters versus independently written interval Python summary.
 summary=json.loads((P/'domain_summary.json').read_text());total=0
 for ln in (P/'independent_domain_summary.txt').read_text().splitlines():
  a,d,raw,one,two,maxn=map(int,ln.split());s=summary[f'{a},{d}'];counts=s['counts']
  check((raw,one,two,maxn)==(counts['candidates'],counts.get('upper1',0),counts.get('upper2',0),s['maxn']),'domain_summary',a,d)
  total+=raw
 result={'status':'PASS','candidate_count':total,'residual_vectors':len(A),'integer_counts_cross_checked':5*len(A),'binomial_bounds_checked':4*len(A),'independent_domain_membership':'complete rectangle/direct checks versus monotone-threshold intervals','all_rejected_by_T2_before_T0':True,'elapsed_seconds':round(time.time()-start,3),'exact_counts_sha256':hashlib.sha256((P/'exact_counts.txt').read_bytes()).hexdigest()}
 output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=P/'verification.json');main(p.parse_args().output)
