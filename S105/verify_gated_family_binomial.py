"""Independent exact binomial count for a gated three-chain MC3 counterexample.
No imports from previous DP implementations. No network or remote writes.
"""
from math import comb
from fractions import Fraction
import json
from pathlib import Path


def counts(m, r, h, t):
    assert 1 <= h <= m and 1 <= t <= r
    M, R = m+2, r+1
    N = M+R
    def S(i,j):
        alpha, beta = M-i,R-j
        H,T = h+2-i,t+1-j
        assert 0<=H<=alpha and 1<=T<=beta
        if H==0:
            return comb(alpha+beta,alpha)
        return sum(comb(H+k-1,k)*comb(alpha+beta-H-k,beta-k)
                   for k in range(T))
    rows=[]
    for i in range(3):
      for j in range(t+1):
        if i==0 and j>1:continue
        if i==0 and j==0:
            total, ay, by = S(1,0)+S(1,1),S(1,0),S(2,0)
        elif i==0:
            total, ay, by = S(1,1),0,0
        elif j==0:
            total=ay=S(i,0)
            by=S(2,0)
        else:
            total=(2 if i==1 else 2*j+1)*S(i,j)
            ay=(1 if i==1 else j+1)*S(i,j)
            by=0 if i==1 else S(i,j)
        weight=N-i-j+1
        rows.append(dict(i=i,j=j,suffix_weight=weight,
                         raw_total=total,raw_ay=ay,raw_by=by,
                         total=weight*total,ay=weight*ay,by=weight*by))
    E=sum(d['total'] for d in rows)
    K=[sum(d['total'] for d in rows if d['i']>=1),
       sum(d['ay'] for d in rows),
       sum(d['total'] for d in rows if d['i']==2),
       sum(d['by'] for d in rows),
       sum(d['total'] for d in rows if d['j']==0)]
    return dict(m=m,r=r,h=h,t=t,n=m+r+5,E=E,K=K,
                probabilities=[str(Fraction(k,E)) for k in K],
                majority_slacks=[3*K[k]-2*E for k in [0,1,3,4]],
                minority_slack=E-3*K[2],
                coupling_identity=K[3]-(2*K[1]-E),
                K_c1y=3*N*S(3,0),rows=rows)

if __name__=='__main__':
    result=counts(54,13,50,8)
    expected=[91743653083395,117303434549811,45491483154535,
              97129099799325,106960274991892]
    assert result['E']==137477769300297
    assert result['K']==expected
    assert min(result['majority_slacks'])>0
    assert result['minority_slack']>0
    assert result['coupling_identity']==0
    assert result['E']<3*result['K_c1y']<2*result['E']
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('gated_family_binomial_certificate.json').write_text(
        json.dumps(result,indent=2)+'\n')
