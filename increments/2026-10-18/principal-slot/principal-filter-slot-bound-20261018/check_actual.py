"""Small, fixed actual-poset checks; exact arithmetic, no Monte Carlo.

This is a diagnostic suite, not an exhaustive classification or a proof.
It independently enumerates linear extensions by permutations.  The finite-k
continuous covariance is computed twice: directly in C_k + U by uniform-order
statistic moments, and using the Beta decomposition on O(U).
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent
CASES = [
    ('singleton', 1, []),
    ('antichain_3', 3, []),
    ('chain_4', 4, [(0,1),(1,2),(2,3)]),
    ('chain2_plus_isolate', 3, [(0,1)]),
    ('diamond', 4, [(0,1),(0,2),(1,3),(2,3)]),
    ('two_disjoint_chains', 5, [(0,1),(1,2),(3,4)]),
    ('asymmetric_six', 6, [(0,2),(0,3),(1,3),(2,4),(3,4),(3,5)]),
]

def average(a):
    return F(sum(a),len(a))
def upsets(n, edges):
    return [b for b in range(1,1<<n)
            if all(not(b>>i&1) or b>>j&1 for i,j in edges)]
def omoment(i,j,m):
    return F(i*j+min(i,j),(m+1)*(m+2))
def omean(i,m):
    return F(i,m+1)
def rankdata(n,edges):
    rows=[]
    for p in permutations(range(n)):
        rank={v:i+1 for i,v in enumerate(p)}
        if all(rank[i]<rank[j] for i,j in edges):
            rows.append([rank[i] for i in range(n)])
    return rows

def check_case(name,n,edges):
    rows=rankdata(n,edges)
    e=len(rows)
    marginal_checks=principal_checks=one_principal_checks=beta_checks=0
    lowest_T_slack=None
    lowest_one_sided_slack=None
    for x in range(n):
        A=[row[x] for row in rows]
        mu=average(A)
        var=average([a*a for a in A])-mu*mu
        assert var<=mu*(mu-1)
        marginal_checks+=1
        a=mu/(n+1)
        vx=average([omoment(row[x],row[x],n) for row in rows])-a*a
        for B in upsets(n,edges):
            G=[min(row[j] for j in range(n) if B>>j&1) for row in rows]
            nu=average(G)
            Q=average([aa*g+min(aa,g) for aa,g in zip(A,G)])
            D=Q-mu*nu
            assert D<=var+mu
            r,s=mu-1,nu-1
            N=average([(aa-1)*(g-1)+min(aa-1,g-1) for aa,g in zip(A,G)])
            assert N-r*s == D-1
            assert N-r*s <= r*r+2*r
            one_principal_checks+=1
            slack=r*r+2*r-(N-r*s)
            lowest_one_sided_slack=slack if lowest_one_sided_slack is None else min(slack,lowest_one_sided_slack)
        for y in range(n):
            C=[row[y] for row in rows]
            nu=average(C)
            Q=average([aa*cc+min(aa,cc) for aa,cc in zip(A,C)])
            r,s=mu-1,nu-1
            N=average([(aa-1)*(cc-1)+min(aa-1,cc-1) for aa,cc in zip(A,C)])
            Tslack=r*s+min(r*r+2*r,s*s+2*s)-N
            assert Tslack>=0
            principal_checks+=1
            lowest_T_slack=Tslack if lowest_T_slack is None else min(Tslack,lowest_T_slack)
            # Check E[Xi Xj] via conditional order-statistic moments.
            b=nu/(n+1)
            exy=average([omoment(row[x],row[y],n) for row in rows])
            assert exy==Q/((n+1)*(n+2))
            cxy=exy-a*b
            for k in [1,2,5]:
                # Direct augmented-poset covariance of (F_x-F_z),(F_y-F_x).
                m=n+k
                joint=average([omoment(k+row[x],k+row[y],m)
                               -omoment(k+row[x],k+row[x],m)
                               -omoment(k,k+row[y],m)
                               +omoment(k,k+row[x],m) for row in rows])
                first=average([omean(k+row[x],m)-omean(k,m) for row in rows])
                second=average([omean(k+row[y],m)-omean(k+row[x],m) for row in rows])
                direct=joint-first*second
                ES=F(n+1,n+k+1)
                ES2=F((n+1)*(n+2),(n+k+1)*(n+k+2))
                vS=ES2-ES*ES
                assert vS/ES2==F(k,(n+2)*(n+k+1))
                via_beta=ES2*(cxy-vx)+vS*a*(b-a)
                assert direct==via_beta
                assert direct<=0
                beta_checks+=1
    return dict(name=name,n=n,edges=edges,linear_extensions=e,
                marginal_CP_checks=marginal_checks,ordered_principal_pairs=principal_checks,
                one_principal_upset_checks=one_principal_checks,
                finite_k_direct_equals_beta_checks=beta_checks,
                min_T_slack=str(lowest_T_slack),min_one_sided_slack=str(lowest_one_sided_slack))

results=[check_case(*case) for case in CASES]
summary=dict(status='all exact assertions passed',scope='Seven fixed actual posets; not exhaustive',cases=results,
             totals={key:sum(row[key] for row in results) for key in
                ['linear_extensions','marginal_CP_checks','ordered_principal_pairs','one_principal_upset_checks','finite_k_direct_equals_beta_checks']})
(OUT/'actual_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
