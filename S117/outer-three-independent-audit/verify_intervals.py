#!/usr/bin/env python3
"""Check every compressed t interval against independently located thresholds."""
from pathlib import Path
from math import comb,prod
from collections import defaultdict
from functools import lru_cache
import json,gzip
P=Path(__file__).parent

def check(ok,*msg):
 if not ok:raise RuntimeError(msg)

def first_true(test):
 # Exponentially bracket, then bisect a monotone predicate over nonnegative ints.
 lo=-1;hi=1
 while not test(hi):lo=hi;hi*=2
 while hi-lo>1:
  mid=(lo+hi)//2
  if test(mid):hi=mid
  else:lo=mid
 check(test(hi) and (hi==0 or not test(hi-1)),'threshold_boundary',lo,hi)
 return hi
@lru_cache(None)
def rank(a,u):
 return first_true(lambda s:3*prod(s+r for r in range(1,a+1))>2*prod(s+u+r for r in range(1,a+1)))
@lru_cache(None)
def lower(a,u,b):
 return first_true(lambda h:comb(a+b+h+u,u)>3*comb(a+b+u-1,u))

def main():
 counters=defaultdict(lambda:[0]*5);rows=0
 path=P/'interval_certificate.tsv'
 stream=path.open() if path.exists() else gzip.open(str(path)+'.gz','rt')
 with stream as f:
  next(f)
  for line in f:
   u,a,b,c,d,v,L,H,*observed=map(int,line.split());rows+=1
   check(L==max(1,2*u-a-b-v+1,2*v-u-c-d+1),'L')
   check(H==(b+c+min(u,v)-1)//2 and 1<=L<=H<=104,'H')
   firsts=[L];cur=L
   for cutoff in (rank(a,u)-b-v,rank(d,v)-c-u,lower(a,u,b)-v,lower(d,v,c)-u):
    cur=max(cur,cutoff);firsts.append(cur if cur<=H else 105)
   check(firsts[1:]==observed,'interval_threshold',u,a,b,c,d,v,firsts,observed)
   for k,lo in enumerate(firsts):counters[a,d][k]+=max(0,H-lo+1)
 ds=[]
 with (P/'domain_summary.tsv').open() as f:
  names=next(f).split()
  for line in f:
   r=dict(zip(names,map(int,line.split())));ds.append(r)
   check(counters[r['a'],r['d']]==[r[n] for n in ('candidates','rank_left','rank_right','lower_left','lower_right')],'total_interval_lengths',r)
 check(rows==sum(r['nonempty_intervals'] for r in ds),'interval_coverage')
 report={'status':'EXHAUSTIVE_INTERVAL_PASS','intervals_checked':rows,'candidates':sum(r['candidates'] for r in ds),'survivors':sum(r['lower_right'] for r in ds),'by_outer_spines':ds,'rank_thresholds':{f'{a},{u}':rank(a,u) for a in (1,2,3) for u in range(2,{1:3,2:9,3:29}[a]+1)},'lower_threshold_count':lower.cache_info().currsize,'notes':'Direct pointwise counts equal sum of independently reconstructed interval lengths, certifying no holes or omitted boundary integers.'}
 (P/'interval_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
