from fractions import Fraction as F
from itertools import permutations, combinations
import json
labels=('d','q','y','z')
orders=[p for p in permutations(labels) if p.index('d')<p.index('q')]
base={('y','z','d','q'):24,('d','y','q','z'):20,('d','q','y','z'):1,('d','q','z','y'):1}
def window(p): return sum(p.index(i)>p.index('q') for i in ('y','z'))
def coeffs(weights, pair=None):
    a=[0,0,0]
    for p in orders:
        if pair is None or p.index(pair[0])<p.index(pair[1]): a[window(p)]+=weights.get(p,0)
    return a
def prob(v,s): return v[0]+v[1]*(s+1)+v[2]*F((s+1)*(s+2),2)
def derivative_shift(v,T):
    # N(s) = A*s²+B*s+C, etc. Return derivative numerator in x=s-1 >=0
    def ordinary(t): return (F(t[2],2),t[1]+F(3*t[2],2),sum(t))
    A,B,C=ordinary(v); D,E,G=ordinary(T)
    # N'T - NT' : (AE-BD)s² +2(AG-CD)s +(BG-CE)
    h2=A*E-B*D; h1=2*(A*G-C*D); h0=B*G-C*E
    return [h2,h1+2*h2,h0+h1+h2]
report={}
for name,weights in [('sparse',base),('full_support',{p:base.get(p,1) for p in orders})]:
    T=coeffs(weights)
    pairs={}
    for pair in combinations(labels,2):
        v=coeffs(weights,pair)
        vals={s:prob(v,s)/prob(T,s) for s in (1,2)}
        h=derivative_shift(v,T)
        sign=1 if all(x>=0 for x in h) else -1 if all(x<=0 for x in h) else 0
        assert sign or all(x==0 for x in h), (name,pair,h)
        assert vals[2]<F(1,3) or vals[2]>F(2,3)
        pairs[str(pair)]={'coefficients':v,'p1':str(vals[1]),'p2':str(vals[2]),'derivative_shift_coefficients':[str(x) for x in h],'monotone_sign':sign}
    assert F(1,3)<=F(pairs[str(('d','y'))]['p1'])<=F(2,3)
    report[name]={'denominator':T,'pair_data':pairs}
# TV formula and common direction formulas: exact rational tests on arbitrary nonnegative coeffs.
for a,b,c in [(24,20,2),(1,1,1),(0,1,2),(3,0,2),(0,0,1)]:
    for m in range(2,15):
        Tm=prob((a,b,c),m)
        qm=[F(a,Tm),F(b*(m+1),Tm),F(c*(m+1)*(m+2),2*Tm)]
        old_tv=F(0)
        for k in range(m-1,0,-1):
            Tk=prob((a,b,c),k)
            qk=[F(a,Tk),F(b*(k+1),Tk),F(c*(k+1)*(k+2),2*Tk)]
            tv=sum(abs(x-y) for x,y in zip(qk,qm))/2
            assert tv==max(qk[0]-qm[0],qm[2]-qk[2])
            assert tv>=old_tv
            old_tv=tv
            if a:
                A=qk[0]-qm[0]; B=qm[2]-qk[2]
                theta=F(c*(a*(m+k+3)+b*(m+1)*(k+1)),a*(2*b+c*(m+k+3)))
                assert B/A==theta
report['checks']='PASS'
print(json.dumps(report,ensure_ascii=False,indent=2))
