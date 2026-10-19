from itertools import permutations
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path

# Only these named, explicitly chosen objects are checked. No poset sweep.
OBJECTS = {
 'matching_Q': (['a','b','c','d'], [('a','c'),('b','d')]),
 'cross_matching_Qp': (['a','b','c','d'], [('a','d'),('b','c')]),
 'mean_swap_Q': (['a','x','c','z'], [('a','x'),('x','c')]),
 'mean_swap_Qp': (['a','x','c','z'], [('a','z'),('z','c')]),
 'mean_swap_singleton_Q': (['a','x','c','z','w'], [('a','x'),('x','c')]),
 'mean_swap_singleton_Qp': (['a','x','c','z','w'], [('a','z'),('z','c')]),
 'mean_swap_chain2_Q': (['a','x','c','z','w1','w2'], [('a','x'),('x','c'),('w1','w2')]),
 'mean_swap_chain2_Qp': (['a','x','c','z','w1','w2'], [('a','z'),('z','c'),('w1','w2')]),
 # Unequal block context: p || r, p < t, sizes (4,2,1).
 'context_Q': (['a','b','c','d','r1','r2','t'], [('a','c'),('b','d'),('r1','r2')]+[(x,'t') for x in 'abcd']),
 'context_Qp': (['a','b','c','d','r1','r2','t'], [('a','d'),('b','c'),('r1','r2')]+[(x,'t') for x in 'abcd']),
 'boundary_joint_Q': (['a','b','c','d','z'], [('a','c'),('b','d')]),
 'boundary_joint_Qp': (['a','b','c','d','z'], [('a','d'),('b','c')]),
}

def les(data):
    names, edges = data
    return [p for p in permutations(names) if all(p.index(a)<p.index(b) for a,b in edges)]

def rank_rows(names, ls):
    return {x: [F(sum(p[i]==x for p in ls),len(ls)) for i in range(len(names))] for x in names}

def pair(a,b,ls):
    return F(sum(p.index(a)<p.index(b) for p in ls),len(ls))

L={key:les(data) for key,data in OBJECTS.items()}
mu={key:rank_rows(OBJECTS[key][0],ls) for key,ls in L.items()}
assert mu['matching_Q']==mu['cross_matching_Qp']
assert pair('a','c',L['matching_Q'])==1
assert pair('a','c',L['cross_matching_Qp'])==F(5,6)
# One singleton context sees only mean ranks, and is strictly weaker.
for x in ['a','x','c','z']:
    avgs=[sum((i+1)*q for i,q in enumerate(mu[key][x])) for key in ('mean_swap_Q','mean_swap_Qp')]
    assert avgs[0]==avgs[1]
    assert pair('w',x,L['mean_swap_singleton_Q'])==pair('w',x,L['mean_swap_singleton_Qp'])
assert mu['mean_swap_Q']['x'] != mu['mean_swap_Qp']['x']
assert pair('w2','x',L['mean_swap_chain2_Q'])==F(3,10)
assert pair('w2','x',L['mean_swap_chain2_Qp'])==F(1,3)
# Check all pairs with at least one outside endpoint, not internal pairs.
context_pairs={}
for a in OBJECTS['context_Q'][0]:
    for b in OBJECTS['context_Q'][0]:
        if a==b or (a in 'abcd' and b in 'abcd'):
            continue
        v=pair(a,b,L['context_Q'])
        assert v==pair(a,b,L['context_Qp'])
        context_pairs[f'{a}<{b}']=str(v)
assert len(L['context_Q'])==len(L['context_Qp'])==126
joint={}
for key in ('boundary_joint_Q','boundary_joint_Qp'):
    ls=L[key]
    joint[key]=F(sum(p.index('a')<p.index('z')<p.index('c') for p in ls),len(ls))
assert joint['boundary_joint_Q']==F(1,3)
assert joint['boundary_joint_Qp']==F(11,30)
for x in 'abcd':
    assert pair(x,'z',L['boundary_joint_Q'])==pair(x,'z',L['boundary_joint_Qp'])

# Analytic chain probe matrix checks. These are kernels, not more poset objects.
def rising(i,r):
    out=1
    for j in range(r):out*=i+j
    return out

def conditional_J(m,k,i,t):
    return F(comb(i+t-1,t)*comb(m-i+k-t,k-t),comb(m+k,k))

matrix_checks=[]
for m,k in [(1,0),(2,1),(3,2),(4,3),(4,1),(4,2)]:
    for i in range(1,m+1):
        probs=[conditional_J(m,k,i,t) for t in range(k+1)]
        assert sum(probs)==1
        for r in range(k+1):
            lhs=sum(comb(t,r)*probs[t] for t in range(r,k+1))
            rhs=F(comb(k,r)*rising(i,r),rising(m+1,r))
            assert lhs==rhs
        endpoint=probs[k]
        assert endpoint==F(comb(i+k-1,k),comb(m+k,k))
    matrix_checks.append({'m':m,'k':k,'all_conditional_moments_verified':True})

# Two explicitly chosen ten-point controls, counted by ideal DP rather than permutations.
def dp_stats(names,edges,pair=None):
    n=len(names); full=(1<<n)-1
    pred=[0]*n
    for a,b in edges:pred[names.index(b)] |= 1<<names.index(a)
    from functools import lru_cache
    @lru_cache(None)
    def suffix(mask):
        if mask==full:return 1
        return sum(suffix(mask|(1<<i)) for i in range(n) if not mask>>i&1 and pred[i]&mask==pred[i])
    prefix=[0]*(1<<n);prefix[0]=1
    ranks=[[0]*n for _ in range(n)]
    pair_count=0
    for mask in range(1<<n):
        if not prefix[mask]:continue
        for i in range(n):
            if not mask>>i&1 and pred[i]&mask==pred[i]:
                nxt=mask|1<<i
                prefix[nxt]+=prefix[mask]
                ranks[i][mask.bit_count()]+=prefix[mask]*suffix(nxt)
                if pair is not None and names[i]==pair[0] and not mask>>names.index(pair[1])&1:
                    pair_count+=prefix[mask]*suffix(nxt)
    total=suffix(0)
    return total,[[F(c,total) for c in row] for row in ranks],pair_count

cycle_names=[f'a{i}' for i in range(5)]+[f'b{i}' for i in range(5)]
cycle_edges=[(f'a{i}',f'b{j}') for i in range(5) for j in (i,(i+1)%5)]
swap=lambda x: {'a1':'a2','a2':'a1'}.get(x,x)
cycle_edges_p=[(swap(a),swap(b)) for a,b in cycle_edges]
cycle_e,cycle_mu,cycle_pair_count=dp_stats(cycle_names,cycle_edges,pair=('a1','b0'))
cycle_ep,cycle_mup,cycle_pair_count_p=dp_stats(cycle_names,cycle_edges_p,pair=('a1','b0'))
assert cycle_e==cycle_ep==39680
assert cycle_mu==cycle_mup
cycle_pair=F(cycle_pair_count,cycle_e)
cycle_pair_p=F(cycle_pair_count_p,cycle_ep)
assert cycle_pair==F(113,124)
assert cycle_pair_p==F(281,310)
assert ('a1','b0') not in cycle_edges and ('a1','b0') not in cycle_edges_p

out={
 'named_poset_count':len(OBJECTS)+2,
 'extension_counts':{key:len(ls) for key,ls in L.items()},
 'rank_rows_Q':{x:list(map(str,v)) for x,v in mu['matching_Q'].items()},
 'internal_pair_a_c':{'Q':str(pair('a','c',L['matching_Q'])),'Qp':str(pair('a','c',L['cross_matching_Qp']))},
 'mean_swap_chain2_last_before_x':{key:str(pair('w2','x',L[key])) for key in ('mean_swap_chain2_Q','mean_swap_chain2_Qp')},
 'boundary_joint_a_z_c':{k:str(v) for k,v in joint.items()},
 'unequal_context_external_and_cross_pairs':context_pairs,
 'cycle_control':{'e_Q':cycle_e,'e_Qp':cycle_ep,'all_rank_rows_equal':True,'incomparable_pair_a1_b0_Q':str(cycle_pair),'incomparable_pair_a1_b0_Qp':str(cycle_pair_p)},
 'chain_probe_checks':matrix_checks,
}
Path(__file__).with_name('controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
