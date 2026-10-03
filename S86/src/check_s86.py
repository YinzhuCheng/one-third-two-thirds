#!/usr/bin/env python3
"""S86 diagnostics, standard library only. The theorems have separate proofs.
Run: python S86/src/check_s86.py --output S86/evidence/check_s86.json
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
import json
from pathlib import Path
import random

CORE = (0, 1, 0, 3, 15, 3, 31)
GOOD = ((0, 120), (0, 112), (7, 80), (15, 64))
BAD = (3, 112)

def close(pred):
    p = list(pred); n = len(p)
    for k in range(n):
        for v in range(n):
            if p[v] >> k & 1:
                p[v] |= p[k]
    if any(p[v] >> v & 1 for v in range(n)):
        raise ValueError('Cycle')
    if any(x >> n for x in p):
        raise ValueError('Invalid predecessor')
    return tuple(p)

def induced(p, vv):
    return tuple(sum(1 << i for i, u in enumerate(vv) if p[v] >> u & 1)
                 for v in vv)

def extensions(p):
    n = len(p); full = (1 << n) - 1; out = []
    def go(used, order):
        if used == full:
            out.append(order); return
        for v, need in enumerate(p):
            if not used >> v & 1 and not need & ~used:
                go(used | (1 << v), order + (v,))
    go(0, ())
    return out

def count(p, pair=None):
    full = (1 << len(p)) - 1
    @lru_cache(None)
    def f(used):
        if used == full:
            return 1
        ans = 0
        for v, need in enumerate(p):
            if used >> v & 1 or need & ~used:
                continue
            if pair is not None and v == pair[1] and not used >> pair[0] & 1:
                continue
            ans += f(used | (1 << v))
        return ans
    return f(0)

def brute(p):
    edges = [(i,j) for j,z in enumerate(p) for i in range(len(p)) if z>>i&1]
    out = []
    for tau in permutations(range(len(p))):
        pos = {v:i for i,v in enumerate(tau)}
        if all(pos[i] < pos[j] for i,j in edges):
            out.append(tau)
    return out

def width(p):
    n = len(p)
    for k in range(n, 0, -1):
        if any(all(not ((p[a]>>b&1) or (p[b]>>a&1)) for a,b in combinations(s,2))
               for s in combinations(range(n), k)):
            return k
    return 0

def types_in(p, vv, outside):
    return tuple((sum(1 << i for i,v in enumerate(vv) if p[z]>>v&1),
                  sum(1 << i for i,v in enumerate(vv) if p[v]>>z&1))
                 for z in outside)

def attach(q, types, edges=()):
    n = len(q); p = list(q) + [0]*len(types)
    for j,(d,f) in enumerate(types):
        p[n+j] |= d
        for i in range(n):
            if f>>i&1: p[i] |= 1 << (n+j)
    for i,j in edges: p[n+j] |= 1 << (n+i)
    p = close(p)
    if induced(p, tuple(range(n))) != q:
        raise ValueError('Changed core')
    if types_in(p, tuple(range(n)), tuple(range(n,len(p)))) != types:
        raise ValueError('Changed exact type')
    return p

def window(tau, typ, s):
    d,f = typ; pos = {v:i+1 for i,v in enumerate(tau)}
    return all(pos[v] <= s for v in pos if d>>v&1) and all(pos[v] > s for v in pos if f>>v&1)

def event_mask(ext, typ, s):
    return sum(1 << i for i,tau in enumerate(ext) if window(tau, typ, s))

def family(ext, types):
    """All intersections, with one explicit conjunction witnessing each mask."""
    full = (1 << len(ext))-1
    generators = [(event_mask(ext,t,s),(j,s)) for j,t in enumerate(types)
                  for s in range(len(ext[0])+1)]
    witnesses = {full: ()}; todo = [full]
    for mask in todo:
        for g,key in generators:
            z = mask & g
            if z not in witnesses:
                witnesses[z] = witnesses[mask] + (key,)
                todo.append(z)
    return witnesses

def promoted_check(q, htype, newtypes):
    """Check every new window-intersection and each old/new pair count."""
    n = len(q); q1 = attach(q, (htype,)); ex = extensions(q); ex1 = extensions(q1)
    oldtypes = tuple(dict.fromkeys((htype,)+tuple((d&((1<<n)-1),f&((1<<n)-1)) for d,f in newtypes)))
    oldfam = family(ex, oldtypes); newfam = family(ex1, newtypes)
    index = {tau:i for i,tau in enumerate(ex)}
    old_pair_masks = {(a,b): sum(1<<i for i,tau in enumerate(ex) if tau.index(a)<tau.index(b))
                      for a,b in combinations(range(n),2)}
    pointed = {(r,x): sum(1<<i for i,tau in enumerate(ex) if tau.index(x)+1>r)
               for r in range(n+1) for x in range(n)}
    sections = oldchecks = newchecks = 0
    for mask, conditions in newfam.items():
        sec = []
        for r in range(n+1):
            z = event_mask(ex, htype, r)
            for j,s in conditions:
                d,f = newtypes[j]
                if (d>>n&1 and not r<s) or (f>>n&1 and not r>=s):
                    z=0; break
                oldcut = s-int(r<s)
                z &= event_mask(ex, (d&((1<<n)-1),f&((1<<n)-1)), oldcut)
            # Empty is adjoined to the intersection family, even when not generated.
            assert z == 0 or z in oldfam
            direct=0
            for i,tau1 in enumerate(ex1):
                if mask>>i&1 and tau1.index(n)==r:
                    tau=tuple(v for v in tau1 if v!=n)
                    direct |= 1<<index[tau]
            assert z==direct
            sec.append(z);sections+=1
        assert sum(z.bit_count() for z in sec)==mask.bit_count()
        for (a,b),am in old_pair_masks.items():
            got=sum((z&am).bit_count()for z in sec)
            want=sum(bool(mask>>i&1) and tau.index(a)<tau.index(b)for i,tau in enumerate(ex1))
            assert got==want;oldchecks+=1
        for x in range(n):
            got=sum((z&pointed[r,x]).bit_count()for r,z in enumerate(sec))
            want=sum(bool(mask>>i&1) and tau.index(n)<tau.index(x)for i,tau in enumerate(ex1))
            assert got==want;newchecks+=1
    return {'core_size':n,'old_extensions':len(ex),'new_extensions':len(ex1),
            'old_events':len(oldfam),'new_events':len(newfam),'sections':sections,
            'old_pair_identities':oldchecks,'new_pair_identities':newchecks}

def chain_singleton(n):
    return tuple((1<<j)-1 for j in range(n))+(0,)

def main():
    rng=random.Random(861003)
    promotion=[]
    for iteration in range(120):
        nn=rng.randint(4,8)
        p=close([sum(1<<i for i in range(j) if rng.random()<0.38)for j in range(nn)])
        vv=tuple(sorted(rng.sample(range(nn),rng.randint(2,min(4,nn-1)))))
        others=[i for i in range(nn)if i not in vv];h=rng.choice(others)
        remaining=tuple(v for v in others if v!=h)
        q=induced(p,vv)
        ht=types_in(p,vv,(h,))[0]
        nts=tuple(dict.fromkeys(types_in(p,vv+(h,),remaining)))
        promotion.append(promoted_check(q,ht,nts))
    # A larger S85 core, with all individually compatible lifted old types.
    q1=attach(CORE,(GOOD[2],)); nt=[]
    for d,f in GOOD:
        for rel in (-1,0,1):
            t=(d|((1<<7)if rel==1 else 0),f|((1<<7)if rel==-1 else 0))
            try:attach(q1,(t,))
            except ValueError:continue
            nt.append(t)
    promotion.append(promoted_check(CORE,GOOD[2],tuple(nt)))
    ex1=extensions(q1);fm1=family(ex1,tuple(nt))
    am=sum(1<<i for i,t in enumerate(ex1)if t.index(1)<t.index(2))
    assert all(3*(h&am).bit_count()>=h.bit_count() and 5*(h&am).bit_count()<=3*h.bit_count()for h in fm1)
    brute_cases=0
    for p in [(0,0,1,3),(0,1,0,3,5),CORE,q1]:
        assert set(brute(p))==set(extensions(p));brute_cases+=1
    # A bad layout really realizable in a width-three environment.
    badp=attach(CORE,(BAD,GOOD[2],GOOD[2],GOOD[3]),((0,1),(1,2),(1,3)))
    assert width(badp)==3 and count(badp)==349
    ex=extensions(CORE)
    constraints=((BAD,2),(GOOD[2],3),(GOOD[2],5),(GOOD[3],4))
    singleton=[tau for tau in ex if all(window(tau,t,s)for t,s in constraints)]
    assert singleton==[(0,1,2,3,5,4,6)]
    # Check all proper nonchain cores in C_n disjoint union {y}.
    no_core=[]; inflation_checks=0; rank_checks=0
    for n in range(2,11):
        subtotal=0
        for bits in range(1,(1<<n)-1):
            selected=[i for i in range(n)if bits>>i&1];k=len(selected)
            z=next(i for i in range(n)if not bits>>i&1)
            left=sum(i<z for i in selected)
            typ=((1<<left)-1,((1<<k)-1)^((1<<left)-1))
            q=chain_singleton(k);ex=extensions(q)
            H=event_mask(ex,typ,left)&event_mask(ex,typ,left+1)
            target=tuple(range(left))+(k,)+tuple(range(left,k))
            assert H.bit_count()==1 and ex[H.bit_length()-1]==target
            r=2*n-2;big=chain_singleton(n+r-1);den=n+r
            assert count(big)==den
            for old in selected:
                new=old if old<z else old+r-1
                u=count(big,(len(big)-1,new))
                assert u==new+1 and 3*min(u,den-u)<den
                inflation_checks+=1
            gaps=[selected[0]]+[selected[j]-selected[j-1]-1 for j in range(1,k)]+[n-1-selected[-1]]
            weights=[g+1 for g in gaps]
            counts=Counter()
            full=chain_singleton(n)
            vv=tuple(selected)+(n,)
            for tau in extensions(full):
                projection=tuple(vv.index(v)for v in tau if v in vv)
                counts[projection]+=1
            for j in range(k+1):
                target=tuple(range(j))+(k,)+tuple(range(j,k))
                assert counts[target]==weights[j]
                rank_checks+=1
            # One actual core promotion at the median if it is not already present.
            med=(n+1)//2-1
            if med not in selected:
                gap=sum(i<med for i in selected)
                prev=selected[gap-1] if gap else -1
                within=med-prev-1
                split=(within+1,gaps[gap]-within)
                assert min(split)>=1 and sum(split)==weights[gap]
                assert sum(weights[:gap])+split[0]==med+1
            assert 3*min(med+1,n-med)>=n+1
            subtotal+=1
        no_core.append({'chain_length':n,'all_proper_nonchain_cores_checked':subtotal})
    # Exact extrema over independent bounded positive gap weights.
    capacity_cases=0
    for _ in range(100):
        k=rng.randint(1,4)
        lower=[rng.randint(1,3)for _ in range(k+1)]
        upper=[z+rng.randint(0,2)for z in lower]
        for j in range(1,k+1):
            vals=[Fraction(sum(w[:j]),sum(w))for w in product(*(range(l,u+1)for l,u in zip(lower,upper)))]
            low=Fraction(sum(lower[:j]),sum(lower[:j])+sum(upper[j:]))
            high=Fraction(sum(upper[:j]),sum(upper[:j])+sum(lower[j:]))
            assert min(vals)==low and max(vals)==high
            assert (low>=Fraction(1,3)and high<=Fraction(2,3)) == (2*sum(lower[:j])>=sum(upper[j:])and sum(upper[:j])<=2*sum(lower[j:]))
            capacity_cases+=1
    return {'round':'S86','status':'passed','seed':861003,
            'scope':'Diagnostic checks only; general statements are proved in notes/PROOF.md. No main conjecture certified.',
            'promotion_cases':len(promotion),'promotion_totals':dict(Counter({key:sum(p[key]for p in promotion)for key in ('sections','old_pair_identities','new_pair_identities')})),
            'promotion_examples':promotion[:2]+promotion[-1:],'independent_full_permutation_cases':brute_cases,
            'width_three_bad_layout':{'predecessor_masks':badp,'linear_extensions':349,'width':3,
              'core_order':singleton[0],'exterior_order':[7,8,10,9],'slots':[2,3,4,5],
              'core_event_constraints':constraints,
              'refutes':'Width-three constraints alone do not eliminate every bad S85 window cell; not a conjecture counterexample.'},
            'no_proper_core_family':no_core,'inflated_fixed_pair_checks':inflation_checks,
            'gap_projection_checks':rank_checks,'capacity_extremum_checks':capacity_cases,
            'novelty_claim':False,'minimality_claim':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    result=main();text=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items()if k!='promotion_details'},ensure_ascii=False,indent=2))
