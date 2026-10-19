"""One frozen 120-R experiment. No chain-length search, no new R budget."""
import sys, json, random
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from math import isqrt
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'external-pair-length-intervals-20261018'))
from interval_solver import window_counts, binomial_kernel_coefficients, threshold_polynomials, positive_intervals, intersect, radical_floor_ceil, rational_floor_ceil
OUT = Path(__file__).resolve().parent

def closure(n, edges):
    succ=[0]*n
    for x,y in edges:
        assert x != y
        succ[x] |= 1<<y
    for k in range(n):
        for x in range(n):
            if succ[x]>>k&1:succ[x] |= succ[k]
    assert all(not (succ[x]>>x&1) for x in range(n))
    pred=[sum(1<<x for x in range(n) if succ[x]>>y&1) for y in range(n)]
    return pred

def typed(label,d,u,chain,edges):
    n=d+u+2; D=set(range(d)); I={d,d+1}; U=set(range(d+2,n))
    edges=list(edges)+[(x,z) for x in D for z in U]
    if chain:edges += [(d,d+1)]
    pred=closure(n,edges)
    assert all(not any(pred[x]>>y&1 for y in I|U) for x in D)
    assert all(not any(pred[x]>>y&1 for y in U) for x in I)
    names=[f'd{j}' for j in range(d)]+['y','z']+[f'u{j}' for j in range(u)]
    return dict(label=label,n=n,d=d,u=u,I_chain=chain,pred=pred,names=names,
                relations=[[names[x],names[y]] for y in range(n) for x in range(n) if pred[y]>>x&1])

def freeze_sample():
    cases=[]
    for a in range(4):
        for b in range(a,4):
            for overlap in range(max(0,a+b-3),min(a,b)+1):
                A=set(range(a)); B=set(range(overlap))|set(range(a,a+b-overlap))
                edges=[(x,3) for x in A]+[(x,4) for x in B]
                cases.append(typed(f'antiD3-antiI-{a}-{b}-{overlap}',3,0,False,edges))
    assert len(cases)==13
    for code in [0,1,2,3,4,6,7]:
        edges=[e for j,e in enumerate([(0,1),(0,2),(1,2)]) if code>>j&1]
        edges += [(1,3),(0,4),(2,4)]
        cases.append(typed(f'D3-chainI-code{code}',3,0,True,edges))
    for d in [1,2,3,6]:
        cases.append(typed(f'old-boundary-d{d}',d,0,False,[(j,j+1) for j in range(d-1)]+[(j,d) for j in range(d)]))
    assert len(cases)==24
    rng=random.Random(20261018)
    allocations=[(3,0),(4,0),(5,0),(6,0),(3,1),(4,1),(5,1),(3,2),(4,2),(3,3),(2,2),(2,3)]
    for d,u in allocations:
        n=d+u+2; D=list(range(d)); I=[d,d+1]; U=list(range(d+2,n))
        possible=list(combinations(D,2))+list(combinations(U,2))+[(x,y) for x in D for y in I]+[(y,z) for y in I for z in U]
        for r in range(8):
            cutoff=1+r%4
            edges=[e for e in possible if rng.randrange(5)<cutoff]
            cases.append(typed(f'seed20261018-d{d}-u{u}-r{r}',d,u,bool(r%2),edges))
    assert len(cases)==120
    return cases

def radical_gt_one(p,sign,delta,q):
    t=q-p
    if sign==1:return t<0 or delta>t*t
    return t<0 and delta<t*t

def simple_roots_above_one(poly):
    A,B,C=poly
    if A==0:
        if B==0:return []
        if (-C-B)*B>0:
            floor,ceil=rational_floor_ceil(-C,B)
            return [dict(expression=f'({-C})/({B})',floor=floor,ceil=ceil)]
        return []
    delta=B*B-4*A*C
    if delta<=0:return []
    p=-B if A>0 else B; q=2*abs(A)
    out=[]
    for sign in [-1,1]:
        if radical_gt_one(p,sign,delta,q):
            floor,ceil=radical_floor_ceil(p,sign,delta,q)
            out.append(dict(expression=f'({p}{"+" if sign==1 else "-"}sqrt({delta}))/{q}',floor=floor,ceil=ceil))
    return out

def ratio_derivative(total,event):
    at,bt,ct=binomial_kernel_coefficients(*total)
    ae,be,ce=binomial_kernel_coefficients(*event)
    return (ae*bt-be*at,2*(ae*ct-ce*at),be*ct-ce*bt)

def sequence_difference(derivative):
    A,B,C=derivative
    assert B%2==0
    return (A,A+B,B//2+C)

def balanced_intervals(total,event):
    low,high=threshold_polynomials(total,event)
    nonpositive=lambda q:positive_intervals(-q[0],-q[1],1-q[2])
    return intersect(nonpositive(low),nonpositive(high))

def main():
    cases=freeze_sample()
    # Freeze the whole typed sample before its first counting call.
    (OUT/'frozen_cases.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n')
    results=[]; continuous=[]; integer=[]; twopieces=[]; pair_count=0; inc_count=0
    for index,case in enumerate(cases,1):
        n=case['n']; d=case['d']; D=set(range(d)); I={d,d+1}; U=set(range(d+2,n)); pred=case['pred']
        total=window_counts(n,pred,D,I,U)
        assert total[2]>0
        details=[]
        for x,y in combinations(range(n),2):
            event=window_counts(n,pred,D,I,U,event=(x,y))
            low,high=threshold_polynomials(total,event)
            deriv=ratio_derivative(total,event); diff=sequence_difference(deriv)
            dp=positive_intervals(*diff); dm=positive_intervals(*[-c for c in diff])
            bset=balanced_intervals(total,event)
            incomparable=not (pred[y]>>x&1 or pred[x]>>y&1)
            roots=simple_roots_above_one(deriv)
            entry=dict(pair=[case['names'][x],case['names'][y]],indices=[x,y],event=list(event),incomparable=incomparable,
                       derivative=list(deriv),simple_derivative_roots_above_1=roots,
                       discrete_difference=list(diff),difference_positive=dp,difference_negative=dm,
                       low=list(low),high=list(high),balanced=bset)
            details.append(entry); pair_count+=1;inc_count+=incomparable
            candidate=dict(case_index=index,label=case['label'],n=n,total=list(total),**entry)
            if roots:continuous.append(candidate)
            if dp and dm:integer.append(candidate)
            if len(bset)>=2:twopieces.append(candidate)
        results.append(dict(case_index=index,**case,total=list(total),pairs=details))
    key=lambda x:(x['n'],x['case_index'],x['indices'])
    continuous.sort(key=key);integer.sort(key=key);twopieces.sort(key=key)
    distinct=len({(r['d'],r['u'],tuple(r['pred'])) for r in cases})
    summary=dict(budget_R=120,distinct_typed_R=distinct,pairs=pair_count,incomparable_pairs=inc_count,
        continuous_nonmonotone_pairs=len(continuous),integer_nonmonotone_pairs=len(integer),
        two_balanced_integer_piece_pairs=len(twopieces),
        continuous_witnesses=continuous,integer_witnesses=integer,two_piece_witnesses=twopieces)
    (OUT/'all_counts.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    (OUT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if not k.endswith('witnesses')},ensure_ascii=False,indent=2))
    for title,x in [('continuous',continuous[:3]),('integer',integer[:3]),('two_piece',twopieces[:3])]:
        print(title,json.dumps(x,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
