#!/usr/bin/env python3
"""Exact exhaustive certificate for a,d in {1,2}; Python standard library only.

Actual extension counts use a unique split after block 2. Every inequality and
check uses integers. The terminal theorem and other universal prerequisites
are declared separately in THEOREM.md and dependencies/MANIFEST.json.
"""
from collections import Counter
from itertools import product
from math import comb,prod
from pathlib import Path
import argparse,json

COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
ANALYTIC=('rank_T1_B0_upper','rank_T6_B5_upper','T0_T2_lower','B3_B6_lower')
EXACT=('B1<B0','T6<T5','T2<T0','B2<B4','B6<B3','T4<T3')
CAP={1:3,2:9};INNER_CAP={1:3,2:19}

def require(ok,*context):
    if not ok:raise RuntimeError(context)

def dual(w):
    u,a,b,c,t,d,v=w
    return v,d,c,b,t,a,u

def prerequisite(w):
    u,a,b,c,t,d,v=w
    return (a in (1,2) and d in (1,2) and min(w)>=1 and 2<=u<=CAP[a] and 2<=v<=CAP[d]
      and 3*prod(range(b,b+a+1))<prod(range(b+u,b+u+a+1))
      and 3*prod(range(c,c+d+1))<prod(range(c+v,c+v+d+1))
      and 2*u<a+b+t+v and 2*v<u+c+t+d and 2*t<b+c+min(u,v))

def candidates():
    for a,d in product((1,2),repeat=2):
      for u,v in product(range(2,CAP[a]+1),range(2,CAP[d]+1)):
       for b in range(1,INNER_CAP[a]+1):
        if 3*prod(range(b,b+a+1))>=prod(range(b+u,b+u+a+1)):continue
        for c in range(1,INNER_CAP[d]+1):
         if 3*prod(range(c,c+d+1))>=prod(range(c+v,c+v+d+1)):continue
         for t in range(1,(b+c+min(u,v)-1)//2+1):
          w=(u,a,b,c,t,d,v)
          if 2*u<a+b+t+v and 2*v<u+c+t+d:yield w

def analytic_bounds(w):
    u,a,b,c,t,d,v=w
    x=comb(a+b+t+v+u,u);y=comb(d+c+t+u+v,v)
    return ((comb(b+t+v+u,u),x),(comb(c+t+u+v,v),y),
            (comb(a+b+u-1,u),x),(comb(d+c+v-1,v),y))

def analytic_pass(bounds):
    return tuple(3*n>2*z if k<2 else 3*n<z for k,(n,z) in enumerate(bounds))

def four_counts(w):
    """Total and B1<B0,T6<T5,T0<T2,B2<B4 numerators."""
    u,a,b,c,t,d,v=w
    z=n10=n65=n02=n24=0
    for i in range(u+1):
      for j in range(t+1):
       tail=comb(u-i+c+t-j,t-j)
       common=tail*comb(u-i+c+t-j+d+v,v)
       left=comb(b+j-1,j)*comb(a+b+i+j-1,i)
       z+=left*common
       n10+=comb(b+j-1,j)*comb(a+b+i+j-2,i)*common
       n65+=left*tail*comb(u-i+c+t-j+d-1+v,v)
       if i==u:n02+=left*common
       h=1 if j==0 else comb(b+j-2,j) if b>=2 else 0
       n24+=h*comb(a+b+i+j-1,i)*common
    return z,(n10,n65,n02,n24)

def six_counts(w):
    z,(n10,n65,n02,n24)=four_counts(w)
    zd,(_,_,n63,n43)=four_counts(dual(w))
    require(z==zd,'dual_denominator',w)
    return z,(n10,n65,z-n02,n24,z-n63,n43)

def count_spines(ws):
    return {f'{a},{d}':sum(w[1]==a and w[5]==d for w in ws) for a,d in product((1,2),repeat=2)}

def main(out):
    ws=sorted(candidates(),key=lambda w:(sum(w),w))
    require(len(ws)==len(set(ws)),'duplicate')
    require(all(prerequisite(w) for w in ws),'prerequisite')
    require({dual(w) for w in ws}==set(ws),'duality')
    records=[];survivors=[];sequential=Counter();solo=Counter();exact_passes=[0]*6;final=[]
    bounds_cache={w:analytic_bounds(w) for w in ws}
    cumulative=[];alive=list(ws)
    for k,name in enumerate(ANALYTIC):
      solo[name]=sum(analytic_pass(bounds_cache[w])[k] for w in ws)
      alive=[w for w in alive if analytic_pass(bounds_cache[w])[k]]
      cumulative.append({'filter':name,'remaining':len(alive),'by_outer_spines':count_spines(alive)})
    for w in ws:
      bounds=bounds_cache[w];passing=analytic_pass(bounds)
      record={'weights':w,'order':sum(w),'analytic_bounds':bounds,'analytic_passing':passing}
      if not all(passing):
        index=passing.index(False);reason=ANALYTIC[index]
        record['rejection']={'kind':'analytic','name':reason,'numerator':bounds[index][0],'denominator':bounds[index][1]}
      else:
        z,nums=six_counts(w);ps=tuple(3*n>2*z for n in nums)
        record.update(extensions=z,exact_numerators=nums,exact_passing=ps)
        for k in range(6):
          if all(ps[:k+1]):exact_passes[k]+=1
        if all(ps):final.append(w);reason='UNRESOLVED';record['rejection']=None
        else:
          index=ps.index(False);reason=EXACT[index]
          record['rejection']={'kind':'exact','name':reason,'numerator':nums[index],'denominator':z}
        survivors.append(record)
      sequential[reason]+=1;records.append(record)
    maxorder=max(map(sum,ws))
    summary={'status':'EXACT_FINITE_CERTIFICATE_PASS' if not final else 'RESIDUALS',
      'scope':'All positive weights with a,d in {1,2}, conditional on declared proved prerequisites',
      'candidate_count':len(ws),'candidate_counts_by_outer_spines':count_spines(ws),
      'maximum_order':maxorder,'maximum_order_vectors':[w for w in ws if sum(w)==maxorder],
      'analytic_standalone_pass_counts':dict(solo),'analytic_cumulative':cumulative,
      'analytic_survivor_count':len(survivors),'exact_filter_order':EXACT,'exact_cumulative_survivors':exact_passes,
      'first_rejection_counts':dict(sequential),'final_survivors':final,
      'middle_only_after_first_three':[r for r in survivors if all(r['exact_passing'][:3])]}
    payload={'summary':summary,'weight_order':['u','a','b','c','t','d','v'],
      'analytic_filter_order':ANALYTIC,'exact_filter_order':EXACT,'records':records}
    out.write_text(json.dumps(payload,separators=(',',':'))+'\n')
    out.with_name('summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    require(not final,'unexpected_survivors',final)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('census.json'))
    main(p.parse_args().output)
