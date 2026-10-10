#!/usr/bin/env python3
"""Bounded exact seven-chain inflation census; Python 3.10+, stdlib only.

No floating point is used for probabilities or exclusion decisions. Elapsed
seconds are metadata only. The finite-cone proof is an external audited result;
its exact source and approval status are supplied in cone_audit.json.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import product, combinations
from math import comb
from pathlib import Path
import argparse, hashlib, json, time

COVERS=((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5))
UP=(40,124,104,32,32,0,0)
DOWN=tuple(sum(1<<i for i in range(7) if UP[i]>>j&1) for j in range(7))
PRED=tuple(tuple(i for i,jj in COVERS if jj==j) for j in range(7))

def is_chain(mask,up):
    return all(all(i==j or up[i]>>j&1 or up[j]>>i&1 for j in range(7) if mask>>j&1)
               for i in range(7) if mask>>i&1)

def forced_edges(up):
    down=tuple(sum(1<<i for i in range(7) if up[i]>>j&1) for j in range(7))
    return tuple((i,j) for i in range(7) for j in range(7) if i!=j
      and not ((up[i]|down[i])>>j&1) and down[i]&~down[j]==0
      and is_chain(up[j]&~up[i],up))

BOTTOM=forced_edges(UP)
TOP=tuple((j,i) for i,j in forced_edges(DOWN))
ARROWS=tuple(('B',i,j) for i,j in BOTTOM)+tuple(('T',i,j) for i,j in TOP)
ARROW_NAMES=tuple(f'{p}{i}<{p}{j}' for p,i,j in ARROWS)
OLD_NAMES=('B1<B0','T6<T5','T2<T0','B6<B3')
OLD=tuple(ARROW_NAMES.index(n) for n in OLD_NAMES)
MIDDLE=tuple(ARROW_NAMES.index(n) for n in ('B2<B4','T4<T3'))
DUAL=(6,5,3,2,4,1,0)

def dual_weights(w): return tuple(w[i] for i in DUAL)

def count_formula(w):
    u,a,b,c,t,d,v=w
    return sum(comb(b+j-1,j)*comb(a+b+i+j-1,i)*comb(u-i+c+t-j,t-j)
               *comb(u-i+c+t-j+d+v,v) for i in range(u+1) for j in range(t+1))

def old_formula_counts(w):
    u,a,b,c,t,d,v=w;z=count_formula(w)
    top0=sum(comb(b+j-1,j)*comb(a+b+u+j-1,u)*comb(c+t-j,t-j)*comb(c+t-j+d+v,v)
             for j in range(t+1))
    x=dual_weights(w);uu,aa,bb,cc,tt,dd,vv=x
    b3=sum(comb(bb+j-1,j)*comb(aa+bb+uu+j-1,uu)*comb(cc+tt-j,tt-j)
           *comb(cc+tt-j+dd+vv,vv) for j in range(tt+1))
    return (count_formula((u,a-1,b,c,t,d,v)),count_formula((u,a,b,c,t,d-1,v)),z-top0,z-b3)

def cone_vectors(spine):
    """Exactly enumerate port conditions and FOUR strict integer inequalities.
    New bound proof pending until cone_audit.json records independent PASS.
    """
    a,b,c,d=spine;s=b+c;alpha=a+b-1;beta=c+d-1
    U=(2*alpha+beta)//3;V=(alpha+2*beta)//3;T=s-1+min(U,V)
    for t in range(1,T+1):
        lo=max(2,2*t-s+1)
        for u in range(lo,t+U+1):
            for v in range(max(lo,2*u-t-alpha),(u+t+beta)//2+1):
                w=(u,a,b,c,t,d,v)
                assert cone_membership(w)
                yield w

def cone_membership(w):
    u,a,b,c,t,d,v=w
    return min(w)>=1 and u>=2 and v>=2 and 2*u<a+b+t+v and 2*v<u+c+t+d and 2*t<b+c+u and 2*t<b+c+v


def block_endpoint_dp(w):
    """Independent of double sum: ideal DAG in seven chain-prefix coordinates.
    Every node is an actual inflated-poset ideal; no quotient extension measure.
    Returns total, all 18 forced endpoint orientation counts, and ideal count.
    """
    dag={}
    @lru_cache(None)
    def suffix(q):
        if q==w:return 1
        choices=[]
        for i in range(7):
            if q[i]<w[i] and all(q[j]==w[j] for j in PRED[i]):
                qq=list(q);qq[i]+=1;qq=tuple(qq)
                choices.append((i,qq))
        dag[q]=choices
        return sum(suffix(qq) for i,qq in choices)
    zero=(0,)*7;z=suffix(zero);fwd={zero:1};counts=[0]*len(ARROWS)
    by_source=defaultdict(list)
    for k,(port,i,j) in enumerate(ARROWS):
        r,s=(1,1) if port=='B' else (w[i],w[j])
        by_source[(i,r)].append((k,j,s))
    for q in sorted(dag,key=sum):
        f=fwd[q]
        for i,qq in dag[q]:
            fwd[qq]=fwd.get(qq,0)+f
            queries=by_source.get((i,qq[i]),())
            if queries:
                ways=f*suffix(qq)
                for k,j,s in queries:
                    if q[j]<s:counts[k]+=ways
    assert fwd[w]==z
    return z,tuple(counts),len(dag)+1


def actual_label_dp(w):
    """Separate implementation on actual labelled-element bitmask ideals.
    Computes every pair count in one forward/backward DAG pass. This code uses
    neither chain-prefix state coordinates nor binomial count identities.
    """
    offsets=[sum(w[:i]) for i in range(7)];n=sum(w);pred=[0]*n
    labels=[(i,r) for i in range(7) for r in range(1,w[i]+1)]
    for i,wi in enumerate(w):
        for r in range(1,wi):pred[offsets[i]+r]|=1<<(offsets[i]+r-1)
    for i,j in COVERS:pred[offsets[j]]|=1<<(offsets[i]+w[i]-1)
    full=(1<<n)-1;dag={}
    @lru_cache(None)
    def suffix(mask):
        if mask==full:return 1
        missing=full^mask;choices=[]
        while missing:
            bit=missing&-missing;missing-=bit;x=bit.bit_length()-1
            if pred[x]&mask==pred[x]: choices.append((x,mask|bit))
        dag[mask]=choices
        return sum(suffix(nm) for x,nm in choices)
    z=suffix(0);forward={0:1};counts=[[0]*n for _ in range(n)]
    for mask in sorted(dag,key=int.bit_count):
        f=forward[mask]
        for x,nm in dag[mask]:
            forward[nm]=forward.get(nm,0)+f
            ways=f*suffix(nm);missing=full^nm
            while missing:
                bit=missing&-missing;missing-=bit;y=bit.bit_length()-1
                counts[x][y]+=ways
    assert forward[full]==z
    delta=0;pairs=[];balanced=[];maximizers=[]
    for x in range(n):
        for y in range(x+1,n):
            nx=counts[x][y];ny=counts[y][x]
            assert nx+ny==z
            if nx==0 or ny==0:continue
            item={'x':labels[x],'y':labels[y],'numerator_x_before_y':nx}
            pairs.append(item);score=min(nx,ny)
            if score>delta:delta=score;maximizers=[item]
            elif score==delta:maximizers.append(item)
            if z<=3*nx<=2*z:balanced.append(item)
    endpoints=[]
    for port,i,j in ARROWS:
        x=offsets[i]+(0 if port=='B' else w[i]-1)
        y=offsets[j]+(0 if port=='B' else w[j]-1)
        endpoints.append(counts[x][y])
    return {'weights':w,'order':n,'extensions':z,'ideal_states':len(dag)+1,
      'delta_numerator':delta,'delta_denominator':z,'delta_reduced':str(Fraction(delta,z)),
      'balanced_pairs':balanced,'maximizing_pairs':maximizers,'incomparable_pairs':pairs,
      'forced_endpoint_numerators':dict(zip(ARROW_NAMES,endpoints))}


def minimum_covers(records):
    """All minimum arrow subsets rejecting every full-menu-rejected vector.
    Survivors are explicitly excluded from the set-cover universe.
    """
    universe=0;cover=[0]*len(ARROWS)
    for k,r in enumerate(records):
        failures=r['failed_forced_arrow_indices']
        if failures:universe|=1<<k
        for j in failures:cover[j]|=1<<k
    for size in range(len(ARROWS)+1):
        matches=[]
        for subset in combinations(range(len(ARROWS)),size):
            union=0
            for j in subset:union|=cover[j]
            if union==universe:matches.append([ARROW_NAMES[j] for j in subset])
        if matches:return {'universe':'all weights rejected by full 18-arrow menu',
          'universe_size':universe.bit_count(),'minimum_size':size,'minimum_subsets':matches}


def summarize(records,m):
    selected=[r for r in records if max(r['spine'])<=m]
    rejected=Counter();exclusive=defaultdict(list);cumulative=[]
    alive=set(range(len(selected)))
    ordered=list(OLD)+[j for j in MIDDLE if j not in OLD]+[j for j in range(len(ARROWS)) if j not in OLD+MIDDLE]
    for j in ordered:
        alive={k for k in alive if j not in selected[k]['failed_forced_arrow_indices']}
        cumulative.append({'added_arrow':ARROW_NAMES[j],'remaining':len(alive)})
    for r in selected:
        for j in r['failed_forced_arrow_indices']:rejected[ARROW_NAMES[j]]+=1
        if len(r['failed_forced_arrow_indices'])==1:exclusive[ARROW_NAMES[r['failed_forced_arrow_indices'][0]]].append(r['weights'])
    survivors=[r['weights'] for r in selected if not r['failed_forced_arrow_indices']]
    old=[r['weights'] for r in selected if not set(OLD).intersection(r['failed_forced_arrow_indices'])]
    six=[r['weights'] for r in selected if not set(OLD+MIDDLE).intersection(r['failed_forced_arrow_indices'])]
    return {'spine_box':f'each a,b,c,d in {{1,...,{m}}}', 'spine_count':m**4,'cone_vectors':len(selected),
      'max_total_order':max(r['order'] for r in selected),'old_four_menu_survivors':old,
      'six_menu_survivors':six,'full_18_menu_survivors':survivors,
      'standalone_rejections':dict(rejected),'exclusive_rejections':dict(exclusive),
      'cumulative_menu':cumulative,'minimum_arrow_covers':minimum_covers(selected)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--max-spine',type=int,default=3);p.add_argument('--output',default='census.json');args=p.parse_args()
    assert 1<=args.max_spine<=3,'This task is explicitly bounded at spine maximum 3.'
    start=time.monotonic();records=[];full_reports=[];old_reports=[];states=0
    for spine in product(range(1,args.max_spine+1),repeat=4):
        for w in cone_vectors(spine):
            z,counts,nstates=block_endpoint_dp(w);states+=nstates
            assert z==count_formula(w),(w,'formula denominator')
            assert tuple(counts[j] for j in OLD)==old_formula_counts(w),(w,'old endpoint formulas')
            failures=[j for j,n in enumerate(counts) if 3*n<=2*z]
            rec={'weights':w,'spine':spine,'order':sum(w),'extensions':z,'ideal_states':nstates,
                 'forced_endpoint_numerators':counts,'failed_forced_arrow_indices':failures}
            records.append(rec)
            if not set(OLD).intersection(failures):
                witness=actual_label_dp(w)
                assert witness['extensions']==z and tuple(witness['forced_endpoint_numerators'][name] for name in ARROW_NAMES)==counts
                assert witness['delta_numerator']*3>=z,('unexpected bounded balanced-pair failure',w)
                old_reports.append(witness)
                if not failures:full_reports.append(witness)
        print('finished spine',spine,'vectors',len(records),'elapsed',round(time.monotonic()-start,3),flush=True)
    records.sort(key=lambda r:(r['order'],r['weights']))
    old_reports.sort(key=lambda r:(r['order'],r['weights']));full_reports.sort(key=lambda r:(r['order'],r['weights']))
    by_weights={tuple(r['weights']):r for r in records};dual_arrow=[]
    for port,i,j in ARROWS:
        target=('T' if port=='B' else 'B',DUAL[j],DUAL[i]);dual_arrow.append(ARROWS.index(target))
    for r in records:
        rr=by_weights[dual_weights(tuple(r['weights']))]
        assert r['extensions']==rr['extensions']
        assert all(r['forced_endpoint_numerators'][i]==rr['forced_endpoint_numerators'][j] for i,j in enumerate(dual_arrow))
    out={'status':'EXACT_ARITHMETIC_PASS_CONE_AUDIT_SEPARATE','scope_max_spine':args.max_spine,
      'arrows':ARROW_NAMES,'bottom_edges':BOTTOM,'top_edges_in_original_order':TOP,
      'old_four_arrow_indices':OLD,'middle_arrow_indices':MIDDLE,'dual_arrow_indices':dual_arrow,
      'elapsed_seconds':round(time.monotonic()-start,6),'aggregate_ideal_states':states,
      'endpoint_count_comparisons_against_old_formula':4*len(records),'extension_formula_checks':len(records),
      'full_actual_label_dp_vectors':len(old_reports),'duality_vectors_checked':len(records),
      'summaries':[summarize(records,m) for m in range(1,args.max_spine+1)],
      'records':records,'old_four_menu_survivor_actual_dp':old_reports,'full_menu_survivor_actual_dp':full_reports,
      'interpretation':'Menu survival never establishes a counterexample. All exact balanced-pair witnesses are reported independently. Cone completeness requires the separately frozen independent audit PASS.'}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','old_four_menu_survivor_actual_dp','full_menu_survivor_actual_dp')},indent=2))

if __name__=='__main__':main()
