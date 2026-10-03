#!/usr/bin/env python3
import json
from itertools import permutations
from fractions import Fraction

QPRED=(0,1,0,3,15,3,31)
D={0,1}
F={4,5,6}

def is_linear_extension(order,pred):
    pos={v:i for i,v in enumerate(order)}
    for v,p in enumerate(pred):
        for u in range(len(pred)):
            if (p>>u)&1 and pos[u]>pos[v]:
                return False
    return True

def core_extensions():
    return [p for p in permutations(range(7)) if is_linear_extension(p,QPRED)]

def core_stats():
    les=core_extensions()
    c0=c1=b0=b1=i=h=h_rev=0
    for tau in les:
        pos={v:j for j,v in enumerate(tau)}
        L=max(pos[d] for d in D)
        R=min(pos[f] for f in F)-1
        w=R-L
        x,z=2,3
        if w==0:
            c0+=1
            if pos[x]<=L: b0+=1
        elif w==1:
            c1+=1
            if pos[x]<=L: b1+=1
            elif L<pos[x]<=R: i+=1
        elif w==2:
            assert L<pos[x]<=R and L<pos[z]<=R
            if pos[x]<pos[z]: h+=1
            else: h_rev+=1
        else:
            raise AssertionError(w)
    assert h==h_rev
    return {"extensions":len(les),"c0":c0,"c1":c1,"h":h,
            "b0":b0,"b1":b1,"i":i}

def closure(pred):
    pred=list(pred)
    n=len(pred)
    changed=True
    while changed:
        changed=False
        for v in range(n):
            p=pred[v]
            q=p
            for u in range(n):
                if (p>>u)&1:
                    q |= pred[u]
            if q!=p:
                pred[v]=q
                changed=True
    return tuple(pred)

def build_R(t):
    pred=list(QPRED)+[0]*t
    dmask=sum(1<<d for d in D)
    prev=0
    for g in range(7,7+t):
        pred[g]=dmask|prev
        prev |= 1<<g
    for f in F:
        pred[f] |= prev
    return closure(pred)

def count_extensions(pred):
    n=len(pred)
    dp=[0]*(1<<n)
    dp[0]=1
    for mask in range(1<<n):
        if not dp[mask]:
            continue
        for v in range(n):
            if (mask>>v)&1:
                continue
            if pred[v] & ~mask == 0:
                dp[mask|(1<<v)] += dp[mask]
    return dp[-1]

def add_relation(pred,a,b):
    q=list(pred)
    q[b] |= 1<<a
    q=closure(q)
    if any((q[v]>>v)&1 for v in range(len(q))):
        return None
    return q

def event_count(pred,a,b):
    q=add_relation(pred,a,b)
    return 0 if q is None else count_extensions(q)

def closed_E(t):
    return 3*t*t+17*t+18

def closed_U(t,r):
    return (3*t+7)*r+6*t+8

def main():
    stats=core_stats()
    assert stats=={"extensions":18,"c0":4,"c1":8,"h":3,
                   "b0":2,"b1":6,"i":1}
    rows=[]
    event_checks=0
    for t in range(1,9):
        pred=build_R(t)
        E=count_extensions(pred)
        assert E==closed_E(t)
        vals=[]
        for r in range(1,t+1):
            U=event_count(pred,2,7+r-1)
            assert U==closed_U(t,r)
            event_checks+=1
            vals.append((Fraction(min(U,E-U),E),r,U))
        best=max(vals)
        chosen=1 if t==1 else t//2
        U=closed_U(t,chosen)
        chosen_bal=Fraction(min(U,E-U),E)
        assert chosen==best[1]
        if t>=2:
            assert chosen_bal>=Fraction(7,16)
        rows.append({
            "t":t,"E":E,"chosen_r":chosen,"chosen_U":U,
            "chosen_balance":f"{chosen_bal.numerator}/{chosen_bal.denominator}",
            "best_r":best[1],
            "best_balance":f"{best[0].numerator}/{best[0].denominator}"
        })
    out={
        "status":"ok",
        "core_stats":stats,
        "direct_total_checks":8,
        "direct_event_checks":event_checks,
        "t_range":[1,8],
        "rows":rows,
        "scope":"Finite DP checks only; general formulas and all-t bounds are analytic."
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
