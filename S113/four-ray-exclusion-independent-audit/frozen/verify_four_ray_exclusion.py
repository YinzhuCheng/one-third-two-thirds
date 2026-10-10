"""Arithmetic implementation checks for the independently proved shuffle bound.

Finite checks verify the formulas and witnesses; they are not the infinite proof.
The infinite argument is in FOUR_RAY_EXCLUSION.md.
"""
from math import comb
from itertools import product
from pathlib import Path
from fractions import Fraction
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'weighted-surviving-core'))
from weighted_core_formula import count_formula, summands, dp_oracle, endpoint_counts


def bc(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0


def conditioned_counts(a,k,t,q):
    """Chains A,S,C, all A before S_q. Return total and S_1<C_1 count.

    Our poset application always has 2<=q<=k.
    """
    assert a>=0 and k>=2 and t>=1 and 2<=q<=k
    n=k+t
    total=first_s=0
    for r in range(q,q+t+1):
        weight=comb(a+r-1,a)
        tail=bc(n-r,k-q)
        total += bc(r-1,q-1)*tail*weight
        first_s += bc(r-2,q-2)*tail*weight
    return total,first_s


def conditioned_decomposition(u,t,v):
    total=first_s=0
    for i in range(u+1):
        for f in range(v+1):
            k=f+2
            for q in range(2,k+1):
                z,n=conditioned_counts(u-i,k,t,q)
                assert n*(k+t)<=k*z
                total+=z
                first_s+=n
    return total,first_s


def validate():
    checked=0
    for u,t,v in product(range(1,7),repeat=3):
        w=(u,1,1,1,t,1,v)
        z,n=conditioned_decomposition(u,t,v)
        double_z=count_formula(w)
        double_n=sum(c for i,j,c in summands(w) if j==0)
        dp_z=dp_oracle(w)
        dp_n=dp_oracle(w,((2,1),(4,1)))
        assert (z,n)==(double_z,double_n)==(dp_z,dp_n),(w,z,n,double_z,double_n,dp_z,dp_n)
        assert n*(v+t+2)<z*(v+2),(w,z,n)
        checked+=1
    witnesses=[]
    for u,t,v in [(2,1,2),(2,2,2),(3,2,3)]:
        w=(u,1,1,1,t,1,v)
        if t==1:
            pair=((1,1),(0,1)); n=endpoint_counts(w)['bottom1_before_bottom0']
        else:
            pair=((2,1),(4,1)); n=sum(c for i,j,c in summands(w) if j==0)
        z=count_formula(w)
        assert n==dp_oracle(w,pair)
        assert z<=3*n<=2*z
        witnesses.append({'weights':w,'pair':pair,'extensions':z,'pair_numerator':n,'probability':str(Fraction(n,z))})
    out={'status':'PASS','proof':'FOUR_RAY_EXCLUSION.md',
         'finite_check_scope':'u,t,v independently in {1,2,3,4,5,6}; all four spine blocks singleton',
         'weight_vectors_checked':checked,'independent_labelled_ideal_dp_counts':2*checked,
         'identities_checked':['conditioned three-chain shuffle decomposition = double-binomial sum = labelled ideal DP',
                               'event s<C1 equals j=0 in double-binomial sum',
                               'conditional bound holds for every conditional stratum used',
                               'strict full probability bound in every tested vector'],
         'finite_checks_are_not_the_infinite_proof':True,'boundary_witnesses':witnesses}
    Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    validate()
