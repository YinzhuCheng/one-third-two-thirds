#!/usr/bin/env python3
"""Exact verification of a fixed, explicitly listed set; no parameter search."""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent

def val(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {str(k): val(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [val(v) for v in x]
    return x

def actual_case(name, W, V, edges, S):
    W, V, S = set(W), set(V), set(S)
    U = W | V
    assert not W & V and V and S <= W
    assert all((x in W and y in W) or (x in V and y in V) for x,y in edges)
    # The cases supply transitive chain relations or their covers. Verify upset
    # under every edge, which is equivalent to upset under their closure.
    assert all(x not in S or y in S for x,y in edges)
    rows=[]
    for p in permutations(sorted(U)):
        pos={x:i for i,x in enumerate(p)}
        if not all(pos[x] < pos[y] for x,y in edges): continue
        w_order=[x for x in p if x in W]
        J=next(i for i,x in enumerate(p) if x in V)
        K=next((i for i,x in enumerate(w_order) if x in S),len(W))
        R=next(i for i,x in enumerate(p) if x in V | S)
        T=J
        assert R == min(J,K)
        rows.append((R,T,J,K))
    Z=len(rows); a=len(W); b=len(V)
    mean=lambda fun: sum((F(fun(row),Z) for row in rows),F(0))
    r=mean(lambda row: row[0]); s=mean(lambda row: row[1])
    ER2=mean(lambda row: row[0]**2)
    cov=mean(lambda row: row[0]*row[1])-r*s
    var=ER2-r*r; g=r*(r+1)-var
    N=mean(lambda row: row[0]*row[1]+min(row[0],row[1]))
    jc=Counter(row[2] for row in rows); kc=Counter(row[3] for row in rows)
    joint=Counter((row[2],row[3]) for row in rows)
    assert all(joint[j,k]*Z == jc[j]*kc[k] for j in jc for k in kc)
    weighted=F(0); tails=[]
    for i in range(1,a+1):
        t=mean(lambda row: int(row[2]>=i))
        q=mean(lambda row: int(row[3]>=i))
        ti=F(1)
        for j in range(i): ti *= F(a-j,a+b-j)
        assert t==ti
        assert mean(lambda row: int(row[0]>=i))==q*t
        assert mean(lambda row: row[2]*int(row[2]>=i))/t==s+F(i*b,b+1)
        weighted += i*q*t
        tails.append({'i':i,'t_i':t,'q_i':q})
    assert s==F(a,b+1) and r<=s
    assert cov==F(b,b+1)*weighted==F(b,2*(b+1))*(ER2+r)
    assert g>=0 and weighted<=r*(r+1)
    assert cov<=F(b,b+1)*r*(r+1)
    gap=r*(r+1)-cov
    assert gap==r*(r+1)/F(b+1)+F(b,2*(b+1))*g
    assert r*s+r*r+2*r-N==gap
    return {'name':name,'a':a,'b':b,'extensions':Z,
            'K_law':{k:F(c,Z) for k,c in sorted(kc.items())},
            'r':r,'s':s,'ER2':ER2,'VarR':var,'CP_gap':g,
            'CovRT':cov,'weighted_tail_sum':weighted,
            'strong_upper':F(b,b+1)*r*(r+1),
            'T_and_C_gap':gap,'N':N,'tails':tails,'all_checks':True}

cases=[
    actual_case('Nonprincipal random cap: two C2 blocks',
                ['p0','p1','q0','q1'],['v0','v1'],
                [('p0','p1'),('q0','q1'),('v0','v1')],['p1','q1']),
    actual_case('Actual random cap can include zero',
                ['p','q'],['v'],[],['p']),
    actual_case('Empty S: K=a and R=J',
                ['p0','p1','p2'],['v0','v1'],
                [('p0','p1'),('p1','p2'),('v0','v1')],[]),
    actual_case('All W in S: R=0',
                ['p0','p1'],['v0'],[('p0','p1')],['p0','p1']),
    actual_case('Empty W: a=0',[],['v0','v1'],[('v0','v1')],[]),
]

def abstract(name,jlaw,klaw):
    law=[(j,k,p*q) for j,p in jlaw.items() for k,q in klaw.items()]
    mean=lambda fun:sum((p*fun(j,k) for j,k,p in law),F(0))
    r=mean(lambda j,k:min(j,k)); s=mean(lambda j,k:j)
    ER2=mean(lambda j,k:min(j,k)**2)
    var=ER2-r*r
    cov=mean(lambda j,k:min(j,k)*j)-r*s
    return {'name':name,'r':r,'s':s,'ER2':ER2,'VarR':var,
            'r(r+1)':r*(r+1),'CP_gap':r*(r+1)-var,
            'CovRT':cov,'C_gap':r*(r+1)-cov}

controls=[
 abstract('Existing abstract control: truncated geometric J',
          {0:F(1,2),1:F(1,4),2:F(1,8),3:F(1,8)},
          {0:F(9,10),3:F(1,10)}),
 abstract('Genuine shuffle J (a=6,b=1), impossible Bernoulli cap',
          {j:F(1,7) for j in range(7)},
          {0:F(9,10),6:F(1,10)})]
assert controls[0]['CP_gap']==-F(271,3200)
assert controls[1]['CP_gap']==-F(41,50)
assert controls[1]['C_gap']==-F(1,100)
result={'method':'Fixed cases only; exact rational arithmetic; no random or parameter search',
        'actual_cases':cases,'abstract_nonactual_controls':controls}
(OUT/'verification.json').write_text(json.dumps(val(result),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(val(result),ensure_ascii=False,indent=2))
