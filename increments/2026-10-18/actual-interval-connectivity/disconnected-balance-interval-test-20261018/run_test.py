"""Frozen 96-case, 1152-pair actual t=2 disconnected balance experiment."""
import sys, json, hashlib, time
from math import comb
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,'/workspace/shared/external-pair-length-intervals-20261018')
from interval_solver import threshold_polynomials, positive_intervals, intersect, binomial_kernel_coefficients
OUT=Path(__file__).resolve().parent
LENGTHS=[(3,5),(4,7),(5,9),(7,10),(8,13),(10,15),(12,17),(14,20),(17,23),(20,27),(24,30),(27,31)]
def ceilfrac(x,k):return (x+k-1)//k
def gates(p,q):
    return [((ceilfrac(p,5),ceilfrac(4*q,5)),(ceilfrac(4*p,5),ceilfrac(q,5))),
            ((0,ceilfrac(3*q,4)),(ceilfrac(3*p,4),0)),
            ((ceilfrac(p,3),q),(p,ceilfrac(q,3))),
            ((1,q-1),(p-1,1)),
            ((ceilfrac(p,2),q),(p,0)),
            ((0,q),(p,ceilfrac(q,2))),
            ((ceilfrac(p,4),ceilfrac(3*q,4)),(ceilfrac(3*p,4),ceilfrac(q,4))),
            ((ceilfrac(p,3),ceilfrac(2*q,3)),(ceilfrac(2*p,3),ceilfrac(q,3)))]
def d_event(p,q,r,s):
    k=r+s-1
    return sum(comb(k,h)*comb(p+q-k,p-h) for h in range(max(r,k-q),min(p,k)+1))
def select_pairs(p,q):
    choices=[(r,s,d_event(p,q,r,s)) for r in range(1,p+1) for s in range(1,q+1) if r!=s]
    total=comb(p+q,p); chosen=[]
    for den in [1,2]:
        target=Fraction(den,3)
        key=lambda x:(abs(Fraction(x[2],total)-target),x[0],x[1])
        for zone in range(3):
            zoneof=lambda r,s:0 if 3*(r+s)<=p+q else 1 if 3*(r+s)<=2*(p+q) else 2
            pool=sorted([x for x in choices if zoneof(*x[:2])==zone and x[:2] not in chosen],key=key)
            take=pool[:2]
            if len(take)<2:
                pool2=sorted([x for x in choices if x[:2] not in chosen and x not in take],key=key)
                take+=pool2[:2-len(take)]
            chosen += [x[:2] for x in take]
    assert len(chosen)==len(set(chosen))==12
    return [dict(r=r,s=s,c_E=2*d_event(p,q,r,s),limit=str(Fraction(d_event(p,q,r,s),total))) for r,s in chosen]
def freeze():
    cases=[]
    for p,q in LENGTHS:
        pairs=select_pairs(p,q)
        gs=gates(p,q)
        assert len(set(gs))==8
        for idx,(y,z) in enumerate(gs,1):
            assert 0<=y[0]<z[0]<=p and 0<=z[1]<y[1]<=q
            cases.append(dict(case_index=len(cases)+1,label=f'A{p}-B{q}-gate{idx}',p=p,q=q,n=p+q+2,y=list(y),z=list(z),pairs=pairs))
    assert len(cases)==96
    return cases

def count(p,q,y,z,event=None):
    # Each state records which prefixes of the two chains and I have occurred.
    # Stop just after the last D: everything then left in I is in the window.
    dp=[[[0]*4 for j in range(q+1)] for i in range(p+1)]
    dp[0][0][0]=1
    for i in range(p+1):
        for j in range(q+1):
            if i==p and j==q:continue
            for mask in [0,1,2,3]:
                v=dp[i][j][mask]
                if not v:continue
                if i<p:dp[i+1][j][mask]+=v
                if j<q and (event is None or j+1!=event[1] or i>=event[0]):dp[i][j+1][mask]+=v
                if not mask&1 and i>=y[0] and j>=y[1]:dp[i][j][mask|1]+=v
                if not mask&2 and i>=z[0] and j>=z[1]:dp[i][j][mask|2]+=v
    final=dp[p][q]
    return (final[3],final[1]+final[2],2*final[0])
def deriv(total,event):
    A,B,C=binomial_kernel_coefficients(*total);a,b,c=binomial_kernel_coefficients(*event)
    return (a*B-b*A,2*(a*C-c*A),b*C-c*B)
def variation(vals):
    s=[1 if x>0 else -1 for x in vals if x]
    return sum(a!=b for a,b in zip(s,s[1:]))
def main():
    start=time.monotonic();cases=freeze()
    raw=json.dumps(cases,indent=2,ensure_ascii=False)+'\n'
    (OUT/'frozen_cases.json').write_text(raw)
    digest=hashlib.sha256(raw.encode()).hexdigest()
    print('Frozen before count:',len(cases),'structures; sha256',digest,flush=True)
    results=[];witnesses=[];nonmonotone=[];multi_threshold=[];hist={};vcounts={}
    for case in cases:
        p,q,y,z=case['p'],case['q'],case['y'],case['z']
        total=count(p,q,y,z)
        assert total[2]==2*comb(p+q,p)
        entries=[]
        for pair in case['pairs']:
            r,s=pair['r'],pair['s'];event=count(p,q,y,z,(r,s))
            assert event[2]==pair['c_E'] and all(0<=e<=t for e,t in zip(event,total))
            low,high=threshold_polynomials(total,event)
            np=lambda v:positive_intervals(-v[0],-v[1],1-v[2])
            bal=intersect(np(low),np(high));hist[len(bal)]=hist.get(len(bal),0)+1
            der=deriv(total,event);diff=(der[0],der[0]+der[1],der[1]//2+der[2])
            pos,neg=positive_intervals(*diff),positive_intervals(*[-v for v in diff])
            lseq=[t-3*e for t,e in zip(total,event)];hseq=[3*e-2*t for t,e in zip(total,event)]
            vs=(variation(lseq),variation(hseq));vcounts[str(vs)]=vcounts.get(str(vs),0)+1
            entry=dict(**pair,event=event,low=low,high=high,balanced=bal,derivative=der,discrete_difference=diff,
                       difference_positive=pos,difference_negative=neg,low_window_coefficients=lseq,high_window_coefficients=hseq,threshold_variations=vs)
            entries.append(entry)
            base=dict(case_index=case['case_index'],label=case['label'],p=p,q=q,n=case['n'],y=y,z=z,total=total,**entry)
            if len(bal)>=2:
                witnesses.append(base)
                print('TWO PIECES',json.dumps(base),flush=True)
            if pos and neg:nonmonotone.append(base)
            if max(vs)>=2:multi_threshold.append(base)
        results.append(dict(**case,total=total,counts=entries))
    summary=dict(structures=len(cases),distinct_structures=len({(c['p'],c['q'],tuple(c['y']),tuple(c['z'])) for c in cases}),
                 pairs=sum(len(c['pairs']) for c in cases),frozen_sha256=digest,balance_component_histogram=hist,
                 threshold_variation_histogram=vcounts,two_component_pairs=len(witnesses),nonmonotone_pairs=len(nonmonotone),
                 two_variation_threshold_pairs=len(multi_threshold),elapsed_seconds=time.monotonic()-start,
                 witnesses=witnesses,nonmonotone_examples=nonmonotone,multi_threshold_examples=multi_threshold)
    (OUT/'all_counts.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if not k.endswith('examples') and k!='witnesses'},indent=2),flush=True)
if __name__=='__main__':main()
