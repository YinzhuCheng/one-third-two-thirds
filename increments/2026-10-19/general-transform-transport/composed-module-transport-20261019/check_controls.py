from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

OUT=Path(__file__).parent

def closure(n,edges):
    reach=[[False]*n for _ in range(n)]
    for x,y in edges: reach[x][y]=True
    for k in range(n):
        for i in range(n):
            for j in range(n): reach[i][j] |= reach[i][k] and reach[k][j]
    if any(reach[i][i] for i in range(n)): raise ValueError('cycle')
    return {(i,j) for i in range(n) for j in range(n) if reach[i][j]}

def les(n,edges):
    edges=closure(n,edges); pred=[0]*n
    for x,y in edges: pred[y]|=1<<x
    @lru_cache(None)
    def rec(mask):
        if mask==(1<<n)-1: return ((),)
        ans=[]
        for x in range(n):
            if not(mask>>x&1) and pred[x]&mask==pred[x]:
                ans.extend((x,)+v for v in rec(mask|1<<x))
        return tuple(ans)
    return rec(0)

def prob(n,edges,x,y):
    L=les(n,tuple(edges)); return F(sum(t.index(x)<t.index(y) for t in L),len(L))

def ranklaw(n,edges,x):
    L=les(n,tuple(edges)); return [F(sum(t.index(x)==i for t in L),len(L)) for i in range(n)]

def beta(p): return min(p,1-p)

def delta(n,edges):
    E=closure(n,edges)
    return max([beta(prob(n,edges,x,y)) for x in range(n) for y in range(x+1,n) if (x,y) not in E and (y,x) not in E],default=F(0))

def kernel(m,n):
    L=les(m+n,tuple((i,i+1) for i in range(m-1))+tuple((m+j,m+j+1) for j in range(n-1)))
    return [[F(sum(t.index(i)<t.index(m+j) for t in L),len(L)) for j in range(n)] for i in range(m)]

def bil(mu,K,nu): return sum(mu[i]*K[i][j]*nu[j] for i in range(len(mu)) for j in range(len(nu)))

def cdf(mu):
    s=F(0); a=[]
    for x in mu: s+=x;a.append(s)
    return a

def envelope(mu,e,sign):
    a=cdf(mu); a=[max(F(0),min(F(1),v+sign*e)) for v in a[:-1]]+[F(1)]
    return [a[i]-(a[i-1] if i else 0) for i in range(len(a))]

def reverse_subset(order,S):
    values=iter([x for x in order if x in S][::-1])
    return [next(values) if x in S else x for x in order]

controls={}
# 1: all four dual masks, two 2-chains and an unchanged isolated point.
e0=((0,1),(2,3)); ps=[]
for a,b in ((0,0),(1,0),(0,1),(1,1)):
    ed=((1,0) if a else (0,1),(3,2) if b else (2,3))
    p=prob(5,ed,0,2); ps.append(p)
assert ps==[F(1,2),F(1,6),F(5,6),F(1,2)]
controls['C1_double_dual_cancellation']={'p_a1_b1_masks_00_10_01_11':ps,'balances':[beta(p) for p in ps]}
# 2: uniform 3x3 shuffle, actual CDF-envelope extremes.
K=kernel(3,3); u=[F(1,3)]*3
lo=envelope(u,F(1,3),-1); hi=envelope(u,F(1,3),1)
L=bil(lo,K,hi); U=bil(hi,K,lo)
p=bil(u,K,u)
assert hi==[F(2,3),F(1,3),0] and lo==[0,F(1,3),F(2,3)]
# Realize the upper endpoint by target 0 minimal in 0<1 and target 4 maximal in 3<4.
p_actual=prob(6,((0,1),(3,4)),0,4)
assert p_actual==U and bil(hi,K,u)==prob(6,((0,1),),0,3)
controls['C2_sharp_CDF_endpoint']={'K':K,'original':p,'epsilon_each':F(1,3),'lower':L,'upper':U,'actual_upper':p_actual,'one_endpoint_shift':bil(hi,K,u)-p,'two_endpoint_shift':U-p}
# 3: fixed skeleton outside modifications genuinely irrelevant.
# Quotient s<t, r isolated, sizes s=2,r=2,t=1. Change t impossible; add fourth block u of size2 above t.
# Core: all s below t below u; r independent. Vary only u's internal chain orientation.
ed=[(0,1),(2,3),(0,4),(1,4),(4,5),(4,6),(5,6)]
ed2=[e for e in ed if e!=(5,6)]+[(6,5)]
p1=prob(7,ed,0,2);p2=prob(7,ed2,0,2)
assert p1==p2
controls['C3_nonendpoint_module_zero_effect']={'p_before':p1,'p_after':p2}
# 4: internal delta changes while every cross-block pair stays comparable.
# Fixed quotient is 1<2, both blocks size 2. Replace the first chain by an antichain.
a=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
b=((0,2),(0,3),(1,2),(1,3),(2,3))
assert delta(4,a)==0 and delta(4,b)==F(1,2)
assert all(prob(4,a,x,y)==prob(4,b,x,y)==1 for x in (0,1) for y in (2,3))
controls['C4_internal_delta_independent_term']={'old_delta':delta(4,a),'new_delta':delta(4,b),'all_cross_probabilities':F(1)}
# 5: three nested prefix modules each affect one external pair's balance.
# Full chain has seven elements z,a,b,c,d,e,f; y isolated. Prefixes on six-element a..f core have sizes 2,4,6.
base=list(range(6)); sets=[set(range(k)) for k in (2,4,6)]
rows=[]
for omit in (None,0,1,2):
    order=base[:]
    for j,S in enumerate(sets):
        if j!=omit: order=reverse_subset(order,S)
    r=order.index(0)+1
    # z is label6, y label7.
    chain=[6]+order; ed=[(chain[i],chain[i+1]) for i in range(6)]
    px=prob(8,ed,0,7)
    assert px==F(7-r,8)
    rows.append({'omit':omit,'core_order':order,'rank_a':r,'prob':px,'balance':beta(px)})
assert [v['balance'] for v in rows]==[F(3,8),F(1,2),F(1,4),F(1,2)]
controls['C5_nested_depth_three'] = rows
# 6: crossing original modules in a 3-chain create cycle under naive simultaneous reversal.
static={(0,1),(1,2),(0,2)}
for S in ({0,1},{1,2}):
    static={(y,x) if x in S and y in S else (x,y) for x,y in static}
try: closure(3,static); raise AssertionError('expected cycle')
except ValueError: pass
controls['C6_overlap_chain_cycle']={'directed_edges':sorted(static),'cycle':[0,2,1,0]}
# 7: safe crossing over anticomplete pieces = disjoint parity replacement.
# A=X union Y, B=Y union Z, each piece a two-chain. Overlap Y flipped twice.
old=[(0,1),(2,3),(4,5)];new=[(1,0),(2,3),(5,4)]
# A,B are autonomous and remain so; only X,Z flip, Y returns.
controls['C7_overlap_parallel_parity']={'p_Xfirst_Yfirst_old':prob(6,old,0,2),'new':prob(6,new,0,2),'p_Yfirst_Zfirst_old':prob(6,old,2,4),'new2':prob(6,new,2,4)}
# 8: CDF exact mixed difference identity for an asymmetric 2x3 rank pair.
K23=kernel(2,3);mu=[F(1,2),F(1,2)];nu=[F(1,3)]*3
mu2=[F(1),F(0)];nu2=[F(1),F(0),F(0)]
h=[a-b for a,b in zip(cdf(mu2)[:-1],cdf(mu)[:-1])]
g=[a-b for a,b in zip(cdf(nu2)[:-1],cdf(nu)[:-1])]
term1=sum(h[i]*sum((K23[i][j]-K23[i+1][j])*nu[j] for j in range(3)) for i in range(1))
term2=sum(g[j]*sum(mu[i]*(K23[i][j]-K23[i][j+1]) for i in range(2)) for j in range(2))
term12=sum(h[i]*g[j]*(K23[i][j]-K23[i+1][j]-K23[i][j+1]+K23[i+1][j+1]) for i in range(1) for j in range(2))
change=bil(mu2,K23,nu2)-bil(mu,K23,nu)
assert change==term1+term2+term12 and term12!=0
assert bil(mu2,K23,nu2)==prob(5,((0,1),(2,3),(3,4)),0,2)
controls['C8_mixed_CDF_interaction']={'K':K23,'first':term1,'second':term2,'mixed':term12,'total':change}

def stringify(obj):
    if isinstance(obj,F):return str(obj)
    if isinstance(obj,dict):return {str(k):stringify(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [stringify(v) for v in obj]
    return obj
(OUT/'controls.json').write_text(json.dumps(stringify(controls),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(stringify(controls),ensure_ascii=False,indent=2))
