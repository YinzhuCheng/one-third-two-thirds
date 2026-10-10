#!/usr/bin/env python3
"""Alternate implementation: independent candidate grid and actual-label ideal DP.
Imports no census implementation. All checks survive python -O. This is author
cross-validation, not a claim of independent peer review.
"""
import argparse,hashlib,json
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import factorial
from pathlib import Path

EDGES=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))

def check(value,*context):
    if not value:raise RuntimeError(context)

def choose(n,k):
    return factorial(n)//factorial(k)//factorial(n-k)

def rising(x,n):
    ans=1
    for k in range(n):ans*=x+k
    return ans

def independent_region():
    answer=[]
    # Rectangular over-enumeration; reject by direct inequalities.  Bounds are
    # proved in THEOREM.md, and boundary values are checked separately below.
    for a,d in product((1,2),repeat=2):
      for u,v in product(range(2,10),repeat=2):
       if (a==1 and u>3) or (d==1 and v>3):continue
       for b,c in product(range(1,20),repeat=2):
        if 3*rising(b,a+1)>=rising(b+u,a+1):continue
        if 3*rising(c,d+1)>=rising(c+v,d+1):continue
        for t in range(1,24):
         if 2*u>=a+b+t+v or 2*v>=u+c+t+d:continue
         if 2*t>=b+c+u or 2*t>=b+c+v:continue
         answer.append((u,a,b,c,t,d,v))
    return set(answer)

def quotient_arrows():
    rel=[[False]*7 for _ in range(7)]
    for i,j in EDGES:rel[i][j]=True
    for k,i,j in product(range(7),repeat=3):
      rel[i][j]=rel[i][j] or rel[i][k] and rel[k][j]
    upper=[{j for j in range(7) if rel[i][j]} for i in range(7)]
    lower=[{i for i in range(7) if rel[i][j]} for j in range(7)]
    def chain(s):return all(i==j or rel[i][j] or rel[j][i] for i,j in product(s,repeat=2))
    bottom=[];top=[]
    for i,j in product(range(7),repeat=2):
      if i==j or rel[i][j] or rel[j][i]:continue
      if lower[i]<=lower[j] and chain(upper[j]-upper[i]):bottom.append(('B',i,j))
      if upper[j]<=upper[i] and chain(lower[i]-lower[j]):top.append(('T',i,j))
    return bottom+top

ARROWS=quotient_arrows()
NAMES=[f'{p}{i}<{p}{j}' for p,i,j in ARROWS]

def labels_dp(w):
    n=sum(w);full=(1<<n)-1;labels=[(b,r) for b,m in enumerate(w) for r in range(1,m+1)]
    address={br:k for k,br in enumerate(labels)};pred=[0]*n
    for block,m in enumerate(w):
      for rank in range(2,m+1):pred[address[block,rank]]|=1<<address[block,rank-1]
    for i,j in EDGES:pred[address[j,1]]|=1<<address[i,w[i]]
    transitions={}
    @lru_cache(None)
    def back(mask):
      if mask==full:return 1
      missing=full^mask;choices=[];ways=0
      while missing:
        bit=missing&-missing;missing-=bit;i=bit.bit_length()-1
        if pred[i]&mask==pred[i]:
          nxt=mask|bit;choices.append((i,nxt));ways+=back(nxt)
      transitions[mask]=choices
      return ways
    z=back(0)
    specs=[]
    for p,i,j in ARROWS:
      specs.append((address[i,1 if p=='B' else w[i]],address[j,1 if p=='B' else w[j]]))
    # Rank-chain upper bounds; last two lower-bound queries duplicate or
    # complement an endpoint but are reconstructed separately here.
    specs.extend(((address[1,w[1]],address[0,1]),(address[6,w[6]],address[5,1]),
                  (address[0,w[0]],address[2,w[2]]),(address[3,1],address[6,1])))
    requests=defaultdict(list)
    for k,(x,y) in enumerate(specs):requests[x].append((k,1<<y))
    nums=[0]*len(specs);forward={0:1}
    for mask in sorted(transitions,key=int.bit_count):
      f=forward[mask]
      for x,nxt in transitions[mask]:
        forward[nxt]=forward.get(nxt,0)+f
        if x in requests:
          ways=f*back(nxt)
          for k,y in requests[x]:
            if not mask&y:nums[k]+=ways
    check(forward[full]==z,'full_forward_count',w)
    return z,nums,len(transitions)+1

def inspect_special(w):
    """All-pair actual-label count only for the one short-menu residual."""
    n=sum(w);offset=[sum(w[:i]) for i in range(7)];pred=[0]*n
    for i,size in enumerate(w):
      for r in range(1,size):pred[offset[i]+r]=1<<(offset[i]+r-1)
    for i,j in EDGES:pred[offset[j]]|=1<<(offset[i]+w[i]-1)
    full=(1<<n)-1;dag={}
    @lru_cache(None)
    def suffix(mask):
      if mask==full:return 1
      ready=[x for x in range(n) if not mask>>x&1 and pred[x]&mask==pred[x]]
      dag[mask]=ready
      return sum(suffix(mask|1<<x) for x in ready)
    z=suffix(0);forward={0:1};counts=[[0]*n for _ in range(n)]
    for mask in sorted(dag,key=int.bit_count):
      for x in dag[mask]:
        nxt=mask|1<<x;forward[nxt]=forward.get(nxt,0)+forward[mask]
        term=forward[mask]*suffix(nxt)
        for y in range(n):
          if not nxt>>y&1:counts[x][y]+=term
    labels=[(i,r) for i,wi in enumerate(w) for r in range(1,wi+1)]
    pairs=[];balanced=[];best=0;witnesses=[]
    for x in range(n):
      for y in range(x+1,n):
        p=counts[x][y];q=counts[y][x];check(p+q==z,'pair_partition',w,x,y)
        if not p or not q:continue
        r={'x':labels[x],'y':labels[y],'numerator_x_before_y':p};pairs.append(r)
        if z<=3*p<=2*z:balanced.append(r)
        score=min(p,q)
        if score>best:best=score;witnesses=[r]
        elif score==best:witnesses.append(r)
    return {'weights':w,'extensions':z,'delta':str(Fraction(best,z)),'balanced_pairs':balanced,
            'maximizing_pairs':witnesses,'all_incomparable_pairs':pairs}

def main(source,out):
    data=json.loads(source.read_text());records=data['records'];region=independent_region()
    ws=[tuple(r['weights']) for r in records]
    check(len(ws)==len(set(ws)) and region==set(ws),'region_mismatch')
    check(len(ARROWS)==18,'arrow_count',ARROWS)
    for outer,port,inner in ((1,3,4),(2,9,20)):
      check(3*rising(inner,outer+1)>=rising(inner+port,outer+1),'inner_cap_boundary')
    totalstates=0;maxstates=0;passed=[];all18survivors=[];analytic_eq=Counter()
    for k,r in enumerate(records):
      w=tuple(r['weights']);u,a,b,c,t,d,v=w
      expected=((choose(b+t+v+u,u),choose(a+b+t+v+u,u)),
                (choose(c+t+u+v,v),choose(d+c+t+u+v,v)),
                (choose(a+b+u-1,u),choose(a+b+t+v+u,u)),
                (choose(d+c+v-1,v),choose(d+c+t+u+v,v)))
      check(tuple(map(tuple,r['analytic_bounds']))==expected,'bound_mismatch',w)
      passing=[]
      for j,(num,den) in enumerate(expected):
        compare=3*num-(2*den if j<2 else den)
        if compare==0:analytic_eq[str(j)]+=1
        passing.append(compare>0 if j<2 else compare<0)
      check(passing==r['analytic_passing'],'passing_mismatch',w)
      if not all(passing):
        j=passing.index(False);rr=r['rejection']
        check(rr=={'kind':'analytic','name':data['analytic_filter_order'][j],
                   'numerator':expected[j][0],'denominator':expected[j][1]},'analytic_reason',w)
        continue
      z,nums,states=labels_dp(w);totalstates+=states;maxstates=max(maxstates,states)
      check(z==r['extensions'],'denominator',w)
      computed=[nums[NAMES.index(name)] for name in data['exact_filter_order']]
      check(computed==r['exact_numerators'],'six_numerators',w,computed,r['exact_numerators'])
      exactpassing=[3*x>2*z for x in computed]
      check(exactpassing==r['exact_passing'],'six_flags',w)
      j=exactpassing.index(False);check(r['rejection']=={'kind':'exact','name':data['exact_filter_order'][j],
            'numerator':computed[j],'denominator':z},'exact_reason',w)
      for j,((num,den),actual) in enumerate(zip(expected,nums[-4:])):
        check(actual*den<=num*z if j<2 else actual*den>=num*z,'actual_analytic_bound',w,j)
      failed=[name for name,num in zip(NAMES,nums) if 3*num<=2*z]
      if not failed:all18survivors.append(w)
      balanced=[{'name':name,'numerator':num} for name,num in zip(NAMES,nums) if z<=3*num<=2*z]
      passed.append({'weights':w,'extensions':z,'ideal_states':states,'all_18_numerators':nums[:18],
                     'four_analytic_event_numerators':nums[18:],'failed_arrows':failed,'balanced_endpoints':balanced})
      if len(passed)%250==0:print('actual_label_DP_vectors',len(passed),flush=True)
    specials=[inspect_special(tuple(r['weights'])) for r in data['summary']['middle_only_after_first_three']]
    summary={'status':'PASS','candidate_count':len(region),'all_candidate_analytic_arithmetic_checks':4*len(region),
        'actual_label_DP_vectors':len(passed),'all_18_endpoint_checks':18*len(passed),
        'formula_numerator_cross_checks':6*len(passed),'actual_analytic_bound_checks':4*len(passed),
        'total_ideal_states':totalstates,'maximum_ideal_states':maxstates,
        'analytic_equalities':dict(analytic_eq),'all_18_survivors':all18survivors,
        'survivors_requiring_all_pair_test':0,'special_short_menu_residual_all_pair_tests':len(specials),
        'census_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
    check(not all18survivors,'unexpected_18_survivors')
    out.write_text(json.dumps({'summary':summary,'arrow_order':NAMES,'per_vector':passed,'special_all_pair_results':specials},separators=(',',':'))+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,default=Path(__file__).with_name('census.json'))
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('verification.json'))
    args=parser.parse_args();main(args.source,args.output)
