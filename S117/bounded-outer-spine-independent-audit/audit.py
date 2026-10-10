#!/usr/bin/env python3
"""Independent audit: no author implementation imported or called.

Reconstructs the full rectangular finite domain and counts actual labelled
extensions through seven-chain occupancy states. Explicit checks survive -O.
"""
import argparse, hashlib, json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path

EDGES=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
EXACT=('B1<B0','T6<T5','T2<T0','B2<B4','B6<B3','T4<T3')
ANALYTIC=('rank_T1_B0_upper','rank_T6_B5_upper','T0_T2_lower','B3_B6_lower')
REL=set(EDGES)
while True:
    enlarged=REL|{(i,k) for i,j in REL for jj,k in REL if j==jj}
    if enlarged==REL:break
    REL=enlarged
PRE=tuple(tuple(i for i in range(7) if (i,j) in REL) for j in range(7))
POST=tuple(tuple(j for j in range(7) if (i,j) in REL) for i in range(7))

def check(ok,*why):
    if not ok:raise RuntimeError(why)

def binomial(n,k):
    check(n>=k>=0,'bad_binomial',n,k)
    return factorial(n)//(factorial(k)*factorial(n-k))

def multiply(values):
    ans=1
    for x in values:ans*=x
    return ans

def rectangular_region():
    candidates=[];reasons=Counter()
    for a,d,u,v,b,c,t in product(range(1,3),range(1,3),range(2,10),range(2,10),range(1,20),range(1,20),range(1,24)):
        reason=None
        if u>(3 if a==1 else 9):reason='terminal_left_cap'
        elif v>(3 if d==1 else 9):reason='terminal_right_cap'
        elif 3*multiply(b+i for i in range(a+1))>=multiply(b+u+i for i in range(a+1)):reason='left_product'
        elif 3*multiply(c+i for i in range(d+1))>=multiply(c+v+i for i in range(d+1)):reason='right_product'
        elif 2*u>=a+b+t+v:reason='left_linear'
        elif 2*v>=u+c+t+d:reason='right_linear'
        elif 2*t>=b+c+u:reason='left_shuffle'
        elif 2*t>=b+c+v:reason='right_shuffle'
        else:candidates.append((u,a,b,c,t,d,v));reason='candidate'
        reasons[reason]+=1
    check(sum(reasons.values())==4*8*8*19*19*23,'rectangular_coverage')
    return sorted(candidates,key=lambda w:(sum(w),w)),dict(sorted(reasons.items()))

def dual(w):
    return (w[6],w[5],w[3],w[2],w[4],w[1],w[0])

def bounds(w):
    u,a,b,c,t,d,v=w
    return ((binomial(u+b+t+v,u),binomial(u+a+b+t+v,u)),
            (binomial(v+c+t+u,v),binomial(v+d+c+t+u,v)),
            (binomial(u+a+b-1,u),binomial(u+a+b+t+v,u)),
            (binomial(v+d+c-1,v),binomial(v+d+c+t+u,v)))

def bound_tests(bs):
    return [3*num>2*den if j<2 else 3*num<den for j,(num,den) in enumerate(bs)]

def chain(subset):
    return all(i==j or (i,j) in REL or (j,i) in REL for i,j in product(subset,repeat=2))

ARROWS=[]
for p in ('B','T'):
    for i,j in product(range(7),repeat=2):
        if i==j or (i,j) in REL or (j,i) in REL:continue
        lower=set(PRE[i])<=set(PRE[j]) and chain(set(POST[j])-set(POST[i]))
        upper=set(POST[j])<=set(POST[i]) and chain(set(PRE[i])-set(PRE[j]))
        if lower if p=='B' else upper:ARROWS.append((p,i,j))
ARROWNAMES=tuple(f'{p}{i}<{p}{j}' for p,i,j in ARROWS)

def requested_pairs(w):
    pairs=[((i,1 if p=='B' else w[i]),(j,1 if p=='B' else w[j])) for p,i,j in ARROWS]
    pairs += [((1,w[1]),(0,1)),((6,w[6]),(5,1)),((0,w[0]),(2,w[2])),((3,1),(6,1))]
    return pairs

def occupancy_count(w,allpairs=False):
    """Prefix/suffix edge counts; each path is a unique labelled extension."""
    if allpairs:
        labels=[(i,r) for i,wi in enumerate(w) for r in range(1,wi+1)]
        pairs=[(x,y) for x in labels for y in labels if x!=y]
    else:pairs=requested_pairs(w)
    requests=defaultdict(list)
    for j,(x,y) in enumerate(pairs):requests[y].append((j,x))
    n=sum(w);zero=(0,)*7;layers=[{zero:1}];dag={}
    for level in range(n):
        nxtlayer=defaultdict(int)
        for q,f in layers[-1].items():
            transitions=[]
            for i in range(7):
                if q[i]==w[i]:continue
                if q[i]==0 and any(q[p]!=w[p] for p in PRE[i]):continue
                nxt=q[:i]+(q[i]+1,)+q[i+1:]
                transitions.append((i,nxt));nxtlayer[nxt]+=f
            check(transitions,'dead_ideal',w,q)
            dag[q]=transitions
        layers.append(dict(nxtlayer))
    check(set(layers[-1])=={w},'terminal_layer',w)
    z=layers[-1][w];suffix={w:1};nums=[0]*len(pairs)
    for layer in reversed(layers[:-1]):
        for q,f in layer.items():
            ways=0
            for i,nxt in dag[q]:
                remaining=suffix[nxt];ways+=remaining
                for j,(xb,xr) in requests.get((i,nxt[i]),()):
                    if q[xb]>=xr:nums[j]+=f*remaining
            suffix[q]=ways
    check(suffix[zero]==z,'forward_backward_total',w)
    if allpairs:
        counts=dict(zip(pairs,nums))
        for (x,y),num in counts.items():check(num+counts[y,x]==z,'pair_partition',w,x,y)
    return z,nums,len(suffix),pairs

def by_spines(ws):
    return {f'{a},{d}':sum(w[1]==a and w[5]==d for w in ws) for a,d in product((1,2),repeat=2)}

def actual_structural_check(w):
    """Check full actual-label set hypotheses, including within-chain parts."""
    labels=[(i,r) for i,wi in enumerate(w) for r in range(1,wi+1)]
    def less(x,y):return (x[0],y[0]) in REL or x[0]==y[0] and x[1]<y[1]
    lower={x:{y for y in labels if less(y,x)} for x in labels}
    upper={x:{y for y in labels if less(x,y)} for x in labels}
    def ischain(s):return all(x==y or less(x,y) or less(y,x) for x,y in product(s,repeat=2))
    for (p,i,j),(x,y) in zip(ARROWS,requested_pairs(w)):
        check(not less(x,y) and not less(y,x),'comparable_arrow',w,p,i,j)
        good=(lower[x]<=lower[y] and ischain(upper[y]-upper[x])) if p=='B' else (upper[y]<=upper[x] and ischain(lower[x]-lower[y]))
        check(good,'bad_lift',w,p,i,j)

def main(source,out):
    author=json.loads(source.read_text());authorrecords=author['records']
    ws,rectangle=rectangular_region();check(len(ws)==len(set(ws)),'duplicates_independent')
    aws=[tuple(r['weights']) for r in authorrecords]
    check(len(aws)==len(set(aws)) and set(ws)==set(aws),'candidate_set_mismatch')
    check(ws==aws,'record_order')
    check(len(ARROWS)==18 and all(x in ARROWNAMES for x in EXACT),'arrow_menu')
    check({dual(w) for w in ws}==set(ws),'domain_duality')
    boundaries=[]
    for a,cap,inner in ((1,3,3),(2,9,19)):
        ratios=[Fraction(multiply(x+i for i in range(a+1)),multiply(x+cap+i for i in range(a+1))) for x in (inner,inner+1)]
        check(ratios[0]<Fraction(1,3)<ratios[1],'product_boundary',a)
        boundaries.append({'outer':a,'terminal_cap':cap,'inner_cap':inner,'last_allowed_ratio':str(ratios[0]),'first_excluded_ratio':str(ratios[1])})
    # The structural pattern stabilizes at lengths 1/2/3; include extrema too.
    structural_vectors=list(product((1,2,3),repeat=7))+[(9,2,19,19,23,2,9)]
    for w in structural_vectors:actual_structural_check(w)
    ledger=[];occupancy=[];reasoncounts=Counter();equalities=Counter();cumulative=[0]*4;standalone=[0]*4;exactcumulative=[0]*6
    totalstates=maxstates=0;special=[]
    for w,r in zip(ws,authorrecords):
        bs=bounds(w);passing=bound_tests(bs)
        check([list(x) for x in bs]==r['analytic_bounds'],'analytic_bound',w)
        check(passing==r['analytic_passing'],'analytic_flags',w)
        for j,(num,den) in enumerate(bs):
            standalone[j]+=passing[j];cumulative[j]+=all(passing[:j+1])
            if 3*num==(2*den if j<2 else den):equalities[ANALYTIC[j]]+=1
        rec={'weights':w,'order':sum(w),'analytic_bounds':bs,'analytic_passing':passing}
        if not all(passing):
            j=passing.index(False);reason={'kind':'analytic','name':ANALYTIC[j],'numerator':bs[j][0],'denominator':bs[j][1]}
        else:
            z,nums,states,_=occupancy_count(w);totalstates+=states;maxstates=max(states,maxstates)
            six=[nums[ARROWNAMES.index(name)] for name in EXACT]
            flags=[3*x>2*z for x in six]
            check(z==r['extensions'],'extensions',w,z,r['extensions'])
            check(six==r['exact_numerators'],'exact_numerators',w,six,r['exact_numerators'])
            check(flags==r['exact_passing'],'exact_flags',w)
            for j in range(6):exactcumulative[j]+=all(flags[:j+1])
            check(not all(flags),'unexcluded_candidate',w)
            for j,((num,den),actual) in enumerate(zip(bs,nums[18:])):
                check(actual*den<=num*z if j<2 else actual*den>=num*z,'analytic_vs_actual',w,j)
            failed=[name for name,num in zip(ARROWNAMES,nums[:18]) if 3*num<=2*z]
            balanced=[name for name,num in zip(ARROWNAMES,nums[:18]) if z<=3*num<=2*z]
            j=flags.index(False);reason={'kind':'exact','name':EXACT[j],'numerator':six[j],'denominator':z}
            rec.update(extensions=z,exact_numerators=six,exact_passing=flags)
            occupancy.append({'weights':w,'extensions':z,'ideal_states':states,'all_18_numerators':nums[:18],'four_analytic_event_numerators':nums[18:],'failed_arrows':failed,'balanced_arrows':balanced})
            if all(flags[:3]):special.append(w)
            if len(occupancy)%250==0:print('occupancy_vectors',len(occupancy),'states',totalstates,flush=True)
        check(reason==r['rejection'],'rejection_ledger',w,reason,r['rejection'])
        rec['rejection']=reason;ledger.append(rec);reasoncounts[reason['name']]+=1
    special_results=[]
    for w in special:
        z,nums,states,pairs=occupancy_count(w,True)
        best=0;balanced=[];maximizers=[]
        for (x,y),num in zip(pairs,nums):
            if x>=y or num in (0,z):continue
            item={'x':x,'y':y,'numerator_x_before_y':num}
            if z<=3*num<=2*z:balanced.append(item)
            score=min(num,z-num)
            if score>best:best=score;maximizers=[item]
            elif score==best:maximizers.append(item)
        special_results.append({'weights':w,'extensions':z,'delta':str(Fraction(best,z)),'balanced_pairs':balanced,'maximizing_pairs':maximizers})
    s=author['summary']
    check(s['candidate_count']==len(ws) and s['candidate_counts_by_outer_spines']==by_spines(ws),'summary_candidates')
    maximum=max(map(sum,ws));extremes=[w for w in ws if sum(w)==maximum]
    check(s['maximum_order']==maximum and s['maximum_order_vectors']==[list(w) for w in extremes],'summary_maximum')
    check(s['analytic_standalone_pass_counts']==dict(zip(ANALYTIC,standalone)),'summary_standalone')
    for j,row in enumerate(s['analytic_cumulative']):
        stage=[w for w in ws if all(bound_tests(bounds(w))[:j+1])]
        check(row=={'filter':ANALYTIC[j],'remaining':cumulative[j],'by_outer_spines':by_spines(stage)},'summary_analytic',j)
    check(s['analytic_survivor_count']==len(occupancy),'summary_analytic_count')
    check(s['exact_cumulative_survivors']==exactcumulative and s['first_rejection_counts']==dict(reasoncounts),'summary_rejections')
    check(s['final_survivors']==[] and s['status']=='EXACT_FINITE_CERTIFICATE_PASS','summary_conclusion')
    check([tuple(r['weights']) for r in s['middle_only_after_first_three']]==special,'summary_special')
    summary={'status':'PASS_FINITE_ARITHMETIC_AND_ACTUAL_LABEL_OCCUPANCY','source_census_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'rectangular_box_size':sum(rectangle.values()),'rectangular_first_rejection_counts':rectangle,'product_boundaries':boundaries,
        'candidate_count':len(ws),'by_outer_spines':by_spines(ws),'maximum_order':maximum,'maximum_order_vectors':extremes,
        'analytic_standalone_counts':dict(zip(ANALYTIC,standalone)),'analytic_cumulative_counts':cumulative,'analytic_equalities':dict(equalities),
        'occupancy_vectors':len(occupancy),'total_occupancy_states':totalstates,'maximum_occupancy_states':maxstates,
        'all_18_endpoint_counts':18*len(occupancy),'six_author_endpoint_cross_checks':6*len(occupancy),
        'actual_analytic_bound_checks':4*len(occupancy),'actual_structural_lift_vectors':len(structural_vectors),
        'exact_cumulative_counts':exactcumulative,'first_rejection_counts':dict(reasoncounts),'unexcluded_candidates':[],
        'special_after_first_three_exact_filters':special_results}
    out.mkdir(exist_ok=True,parents=True)
    (out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    (out/'reason_ledger.json').write_text(json.dumps({'analytic_order':ANALYTIC,'exact_order':EXACT,'records':ledger},separators=(',',':'))+'\n')
    (out/'occupancy_counts.json').write_text(json.dumps({'arrow_order':ARROWNAMES,'analytic_event_order':['T1<B0','T6<B5','T0<T2','B3<B6'],'records':occupancy},separators=(',',':'))+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();main(a.source,a.output)
