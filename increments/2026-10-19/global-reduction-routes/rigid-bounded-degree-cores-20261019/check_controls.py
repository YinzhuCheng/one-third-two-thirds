from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def fibonacci(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def path_poset(n):
    return {(i,j) for i in range(n) for j in range(i+2,n)}

def generic_dp(n,rel):
    pred=[sum(1<<i for i,j in rel if j==v) for v in range(n)]
    succ=[sum(1<<j for i,j in rel if i==v) for v in range(n)]
    full=(1<<n)-1
    @lru_cache(None)
    def enabled(mask):
        return tuple(x for x in range(n) if not(mask>>x&1) and pred[x]&mask==pred[x])
    levels=[[] for _ in range(n+1)]
    alpha={0:1}; levels[0]=[0]
    for t in range(n):
        nex=set()
        for mask in levels[t]:
            for x in enabled(mask):
                m2=mask|1<<x
                alpha[m2]=alpha.get(m2,0)+alpha[mask]
                nex.add(m2)
        levels[t+1]=sorted(nex)
    beta={full:1}
    for t in range(n-1,-1,-1):
        for mask in levels[t]: beta[mask]=sum(beta[mask|1<<x] for x in enabled(mask))
    return levels,alpha,beta,enabled,pred,succ

def module(n,rel,M):
    M=set(M)
    for z in range(n):
        if z in M: continue
        typ={(1 if (z,x) in rel else -1 if (x,z) in rel else 0) for x in M}
        if len(typ)>1: return False
    return True

def trace_signature(n,rel,D=2):
    L=tuple(range(2*D)); R=tuple(range(n-2*D,n)); K=set(range(2*D,n-2*D))
    B=set(L+R)
    pred={x:{y for y,z in rel if z==x} for x in range(n)}
    full=set(range(n))
    def ideal(S): return all(pred[x]<=S for x in S)
    def les(S):
        S=frozenset(S)
        if not S:
            yield ()
            return
        for x in sorted(S):
            if not(pred[x]&S):
                for tail in les(S-{x}): yield (x,)+tail
    def name(x):
        return f'L{x}' if x in L else f'R{x-(n-2*D)}'
    H={}
    for s in combinations(L,D):
        Is=set(s)
        if not ideal(Is): continue
        for t in combinations(R,D):
            Jt=set(L)|K|set(t)
            if not ideal(Jt): continue
            counts=defaultdict(int)
            for word in les(Jt-Is):
                tau=tuple(name(x) for x in word if x in B)
                assert len(tau)==2*D
                counts[tau]+=1
            for tau,count in counts.items():
                key=(tuple(name(x) for x in s),tuple(name(x) for x in t),tau)
                H[key]=count
    return H

def projective_equal(H,G):
    keys=set(H)|set(G)
    ratios=[]
    for key in keys:
        a,b=H.get(key,0),G.get(key,0)
        if bool(a)!=bool(b): return False,None
        if b: ratios.append(Fraction(a,b))
    return len(set(ratios))==1, ratios[0] if ratios else None

results={'path_dp':[],'small_prime_checks':[]}
for n in range(4,21):
    rel=path_poset(n)
    levels,alpha,beta,enabled,pred,succ=generic_dp(n,rel)
    Z=beta[0]
    N=sum(alpha[m]*beta[m|2] for level in levels for m in level if 1 in enabled(m) and not(m&1))
    assert Z==fibonacci(n+1)
    assert N==fibonacci(n-1)
    p=Fraction(N,Z)
    assert Fraction(1,3)<=p<=Fraction(2,5)
    assert p.denominator==Z
    D=2
    for t,level in enumerate(levels):
        assert len(level)<=6
        fixed=(1<<max(0,t-D))-1
        allowed=(1<<min(n,t+D))-1
        for m in level:
            assert m&fixed==fixed and m&~allowed==0
    ideals=sum(map(len,levels))
    assert ideals<=1+n*(2**D)
    # Formula (2.1) on all actual incomparable pairs.
    all_pair=[]
    for x in range(n-1):
        y=x+1
        numerator=sum(alpha[m]*beta[m|1<<x] for level in levels for m in level
                      if x in enabled(m) and not(m>>y&1))
        reverse=fibonacci(x+1)*fibonacci(n-x-1)
        assert Z-numerator==reverse
        all_pair.append([x+1,y+1,str(Fraction(numerator,Z))])
    results['path_dp'].append({'n':n,'Z':Z,'N_2_before_1':N,'p':str(p),
                               'ideal_count':ideals,'max_layer':max(map(len,levels)),
                               'all_adjacent_pairs':all_pair})
for n in range(4,9):
    rel=path_poset(n)
    found=[]
    for mask in range(1,(1<<n)-1):
        M=[i for i in range(n) if mask>>i&1]
        if len(M)>1 and module(n,rel,M): found.append(M)
    assert not found
    results['small_prime_checks'].append({'n':n,'nontrivial_modules':found})

rays=[(1,1),(2,1)]
images=[(u+v,u) for u,v in rays]
assert images==[(2,1),(3,2)]
assert images[1]==tuple(rays[0][i]+rays[1][i] for i in range(2))
for u,v in rays:
    assert 3*u-(2*u+v)>=0
    assert 2*(2*u+v)-5*u>=0
results['cone']={'rays':rays,'images':images,'second_image_coefficients':[1,1],
                 'probability_bounds':['1/3','2/5']}

H9=trace_signature(9,path_poset(9))
H10=trace_signature(10,path_poset(10))
same,c=projective_equal(H9,H10)
assert not same
# The retained induced order is identical after naming L/R ports.
def exterior_relation(n,rel):
    E=list(range(4))+list(range(n-4,n))
    pos={x:i for i,x in enumerate(E)}
    return {(pos[x],pos[y]) for x,y in rel if x in pos and y in pos}
assert exterior_relation(9,path_poset(9))==exterior_relation(10,path_poset(10))
results['trace_nonprojective']={'n_values':[9,10],'common_exterior':True,
                              'positive_coordinate_counts':[len(H9),len(H10)],
                              'projectively_equal':same}

# Positive interface control: chain L_4 + antichain core of size 2 + chain R_4
# versus chain L_4 + singleton core + chain R_4. All exterior labels have same order.
def ordinal_core(core_size,antichain):
    n=8+core_size
    rel=set()
    for i in range(n):
        for j in range(i+1,n):
            if antichain and 4<=i<4+core_size and 4<=j<4+core_size: continue
            rel.add((i,j))
    return n,rel
na,ra=ordinal_core(2,True)
nb,rb=ordinal_core(1,False)
Ha=trace_signature(na,ra); Hb=trace_signature(nb,rb)
same,c=projective_equal(Ha,Hb)
assert same and c==2
assert generic_dp(na,ra)[2][0]==2 and generic_dp(nb,rb)[2][0]==1
results['trace_positive']={'core_sizes':[2,1],'projectively_equal':same,
                          'ratio':str(c),'external_law':'deterministic chain',
                          'internal_balance_not_preserved':True}
(HERE/'controls.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print('PASS: prescribed path DP, prime, cone, and trace controls')
