#!/usr/bin/env python3
"""Exact complete global domain enumeration after accepted finite reduction.
All pruning uses integer arithmetic. Emits interval compression, not a box cutoff.
"""
from math import prod
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent
V={1:3,2:9,3:29,4:43}

@lru_cache(None)
def inner_max(a,u):
    lo,hi=0,(a+1)*u
    while lo+1<hi:
        b=(lo+hi)//2
        if 3*prod(range(b,b+a+1))<prod(range(b+u,b+u+a+1)):lo=b
        else:hi=b
    return lo

@lru_cache(None)
def rank_min(a,u):
    def good(s):return 3*prod(range(s+1,s+a+1))>2*prod(range(s+u+1,s+u+a+1))
    lo,hi=-1,1
    while not good(hi):hi*=2
    while lo+1<hi:
        s=(lo+hi)//2
        if good(s):hi=s
        else:lo=s
    return hi

def outer_pairs():
    for a in range(1,5):
        for d in range(a,{1:50,2:92,3:181,4:36}[a]+1):
            for u in range(2,V[a]+1):
                vm=V[d] if d<=4 else (25*d+25*a+(85-16*a)*u-1)//(16*d-60)
                for v in range(2,vm+1):
                    if 16*(a*u+d*v)<60*(u+v)+25*min(u,v)+25*(a+d):yield a,d,u,v
    for a in range(5,21):
        for d in range(a,42-a):
            for u in range(2,109):
                for v in range(2,111-u):
                    if 16*(a*u+d*v)<60*(u+v)+25*min(u,v)+25*(a+d):yield a,d,u,v

def main():
    tic=time.time(); ledger={}; rows=0; survivors=0; maxn=0; globals=Counter()
    with (P/'domain_intervals.txt').open('w') as out:
      for a,d,u,v in outer_pairs():
        stats=ledger.setdefault((a,d),Counter()); stats['port_tuples']+=1; globals['port_tuples']+=1
        if d<=3:
            stats['covered_by_prior_census']+=1;globals['covered_by_prior_census']+=1;continue
        bm,cm=inner_max(a,u),inner_max(d,v);ra,rd=rank_min(a,u),rank_min(d,v);m=min(u,v)
        top=(bm+cm+m-1)//2
        if max(1,2*u-a-bm-v+1,2*v-u-cm-d+1,ra-bm-v,rd-cm-u)>top:
            stats['no_inner_interval']+=1;globals['no_inner_interval']+=1;continue
        stats['port_tuples_with_intervals']+=1;globals['port_tuples_with_intervals']+=1
        for b in range(1,bm+1):
          cmin=max(1,2*ra-3*b-2*v-m+1,(2*rd-b-2*u-m+3)//3,4*u-2*a-3*b-2*v-m+3,(4*v-2*u-2*d-b-m+5)//3)
          for c in range(cmin,cm+1):
            low=max(1,2*u-a-b-v+1,2*v-u-c-d+1,ra-b-v,rd-c-u)
            high=(b+c+m-1)//2
            if low>high:raise RuntimeError(('bad cmin',a,d,u,v,b,c,low,high))
            out.write(f'{u} {a} {b} {c} {d} {v} {low} {high}\n')
            q=high-low+1;rows+=1;survivors+=q;stats['intervals']+=1;stats['weight_vectors']+=q
            maxn=max(maxn,u+a+b+c+high+d+v)
    summary={'status':'COMPLETE','port_domain':'all a<=d under global finite reduction; prior a,d<=3 skipped','counts':dict(globals),'intervals':rows,'weight_vectors':survivors,'maximum_order':maxn,'elapsed_seconds':time.time()-tic,'by_outer_weights':{f'{a},{d}':dict(s) for (a,d),s in sorted(ledger.items())}}
    (P/'domain_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items() if k!='by_outer_weights'},indent=2),flush=True)
if __name__=='__main__':main()
