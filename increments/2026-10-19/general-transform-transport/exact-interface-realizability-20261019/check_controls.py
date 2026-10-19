#!/usr/bin/env python3
"""Eleven directed exact controls; fourteen named true posets, no poset sweep."""
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def extensions(labels, edges):
    labels = tuple(labels)
    pred = {x: {a for a, b in edges if b == x} for x in labels}
    ans = []
    def rec(order, rest):
        if not rest:
            ans.append(tuple(order))
            return
        used = set(order)
        for x in sorted(rest):
            if pred[x] <= used:
                rec(order + [x], rest - {x})
    rec([], set(labels))
    return ans


def family(m, ell):
    C = [f'c{j}' for j in range(1, ell + 1)]
    Z = [f'z{j}' for j in range(1, m - ell + 1)]
    return C + Z, list(zip(C, C[1:]))


def law(words, x):
    m = len(words[0])
    return {i: F(sum(w.index(x) + 1 == i for w in words), len(words))
            for i in range(1, m + 1)}


def moments(mu):
    assert sum(mu.values()) == 1 and all(w >= 0 for w in mu.values())
    M = sum(i*w for i,w in mu.items())
    R = sum(i*(i+1)*w for i,w in mu.items())
    return M, R - M - M*M, R


def delta(labels, edges, words):
    less = set(edges)
    for z in labels:
        for x in labels:
            for y in labels:
                if (x,z) in less and (z,y) in less:
                    less.add((x,y))
    vals = []
    for a,x in enumerate(labels):
        for y in labels[a+1:]:
            if (x,y) not in less and (y,x) not in less:
                p = F(sum(w.index(x) < w.index(y) for w in words),len(words))
                vals.append(min(p,1-p))
    return max(vals, default=F(0))


def model(m, ell, j):
    t, s = m + 1, ell + 1
    M = F(j*t,s)
    V = F(j*(s-j)*t*(t-s),s*s*(s+1))
    return M,V,M*M+M+V


def h1_realize(m, M):
    r = M / (m+1)
    p,q = r.numerator,r.denominator
    if 0 < p < q <= m+1:
        return q-1,p
    return None


def h2_inverse(m, M, V):
    t = m+1
    A = M*(t-M)
    if A <= 0 or V < 0:
        return None,None,None
    s = t*(A-V)/(A+t*V)
    j = M*s/t
    valid = s.denominator == 1 and 2 <= s <= t and j.denominator == 1 and 1 <= j <= s-1
    return (int(s)-1,int(j)) if valid else None,s,j


def full_realize(m, rows, second=False):
    t = m+1
    center = F(t,2)
    means = [row[0] for row in rows]
    if len(rows) != m:
        return None
    if all(M == center for M in means):
        ell = 1
    else:
        minimum = min(means)
        if minimum <= 0:
            return None
        s = t/minimum
        if s.denominator != 1 or not 3 <= s <= t:
            return None
        ell = int(s)-1
    U = F(m*m-1,12)
    target = [model(m,ell,j)[:2] for j in range(1,ell+1)] + [(center,U)]*(m-ell)
    if second:
        ok = Counter(rows) == Counter(target)
    else:
        ok = Counter(means) == Counter(M for M,V in target)
    return ell if ok else None


def kernel(m,h,j,i):
    return sum(F(comb(i+r-1,r)*comb(m-i+h-r,h-r),comb(m+h,h)) for r in range(j,h+1))


def boundary(mu,m,h):
    return [sum(w*kernel(m,h,j,i) for i,w in mu.items()) for j in range(1,h+1)]


instances = {}
def load(name, labels, edges):
    assert name not in instances
    words = extensions(labels,edges)
    data = {'labels':labels,'edges':edges,'extensions':len(words),
            'moments':{x:moments(law(words,x)) for x in labels},
            'delta':delta(labels,edges,words)}
    instances[name] = data
    return words,data


controls = []
# 1. Positive full interface, with an odd-length central-chain ambiguity at h=1.
labels,edges = family(6,3)
W,D = load('chain3_parallel_antichain3',labels,edges)
for j in range(1,4):
    assert D['moments'][f'c{j}'] == model(6,3,j)
    expected = {i:F(comb(i-1,j-1)*comb(6-i,3-j),comb(6,3))
                for i in range(j,6-3+j+1)}
    assert all(law(W,f'c{j}')[i] == expected.get(i,0) for i in range(1,7))
assert all(D['moments'][f'z{j}'][:2] == (F(7,2),F(35,12)) for j in range(1,4))
rows = [v[:2] for v in D['moments'].values()]
assert full_realize(6,rows) == full_realize(6,rows,True) == 3
assert D['delta'] == F(1,2)
controls.append({'name':'full_positive_m6_ell3','moment_rows':D['moments'],'delta':D['delta']})

# 2. Noncentral order statistic, a second size, with inverse certificate.
labels,edges = family(7,4)
W,D = load('chain4_parallel_antichain3',labels,edges)
M,V,R = D['moments']['c3']
assert (M,V,R) == model(7,4,3)
assert (M,V) == (F(24,5),F(24,25))
answer,s,j = h2_inverse(7,M,V)
assert answer == (4,3)
controls.append({'name':'order_statistic_m7_ell4_j3','M':M,'V':V,'s':s,'j':j})

# Shared true realization for controls 3 and 4; this is one named true poset.
labels,edges = family(6,4)
W,D = load('chain4_parallel_antichain2',labels,edges)
true_mu = law(W,'c2')
assert {i:w for i,w in true_mu.items() if w} == {2:F(2,5),3:F(2,5),4:F(1,5)}

# 3. A two-atom mean interface realizes at h=1, and demonstrably fails at h=2.
nu = {2:F(1,5),3:F(4,5)}
M,V,R = moments(nu)
assert h1_realize(6,M) == (4,2)
assert boundary(nu,6,1) == boundary(true_mu,6,1)
assert boundary(nu,6,2) != boundary(true_mu,6,2)
controls.append({'name':'two_atom_h1_only','nu':nu,'M':M,'source_V':V,
                 'target_V':moments(true_mu)[1],'h1_boundary':boundary(nu,6,1),
                 'h2_source':boundary(nu,6,2),'h2_target':boundary(true_mu,6,2)})

# 4. A different three-atom law exactly realizes at h=2, but not h=3.
nu = {1:F(2,15),3:F(4,5),4:F(1,15)}
M,V,R = moments(nu)
assert (M,V,R) == moments(true_mu)
assert h2_inverse(6,M,V)[0] == (4,2)
assert boundary(nu,6,2) == boundary(true_mu,6,2)
assert boundary(true_mu,6,3)[2] - boundary(nu,6,3)[2] == F(1,630)
controls.append({'name':'three_atom_h2_exact_not_full_rank','nu':nu,'true_mu':true_mu,
                 'M':M,'V':V,'R2':R,'h2_boundary':boundary(nu,6,2),'h3_tail_gap':F(1,630)})

# 5. A true sparse rank law is admissible at h=1, but impossible in the family at h=2.
labels = ['a','x','y','z','b']
edges = [( 'a',u) for u in ['x','y','z']] + [(u,'b') for u in ['x','y','z']]
W,D = load('ordinal_singleton_antichain3_singleton',labels,edges)
mu = law(W,'x'); M,V,R = moments(mu)
assert (M,V) == (F(3),F(2,3)) and h1_realize(5,M) == (1,1)
answer,s,j = h2_inverse(5,M,V)
assert answer is None and s == F(50,13)
controls.append({'name':'genuine_h2_family_nonrealizability','mu':mu,'M':M,'V':V,'inverse_s':s})

# 6. All-marked h=1 collision: precisely the center-chain/isolate exchange.
labels = ['a','x','c','z']
W,D = load('chain3_plus_singleton_center_x',labels,[('a','x'),('x','c')])
W2,D2 = load('chain3_plus_singleton_center_z',labels,[('a','z'),('z','c')])
rows,rows2 = [D['moments'][x][:2] for x in labels],[D2['moments'][x][:2] for x in labels]
assert [a for a,b in rows] == [a for a,b in rows2]
assert rows != rows2 and full_realize(4,rows) == full_realize(4,rows2) == 3
assert full_realize(4,rows,True) == full_realize(4,rows2,True) == 3
assert all(boundary(law(W,x),4,1) == boundary(law(W2,x),4,1) for x in labels)
assert boundary(law(W,'x'),4,2) != boundary(law(W2,'x'),4,2)
assert D['delta'] == D2['delta'] == F(1,2)
controls.append({'name':'all_marked_h1_center_exchange','rows_Q':D['moments'],'rows_Qprime':D2['moments'],
                 'delta_Q':D['delta'],'delta_Qprime':D2['delta']})

# 7. Genuine whole-module obstruction, despite legal individual means and correct total.
labels = ['a','b','c','d','z']
W,D = load('two_chains2_plus_singleton',labels,[('a','b'),('c','d')])
rows = [v[:2] for v in D['moments'].values()]
assert sorted(M for M,V in rows) == list(map(F,[2,2,3,4,4]))
assert sum(M for M,V in rows) == 15
assert all(h1_realize(5,M) is not None for M,V in rows)
assert full_realize(5,rows) is None
controls.append({'name':'genuine_joint_obstruction_individually_realizable','means':{x:v[0] for x,v in D['moments'].items()},
                 'individual_parameters':{x:h1_realize(5,v[0]) for x,v in D['moments'].items()},'full_family_realization':None})

# 8. True single-marker boundary equality, all ranks matched, with unequal internal delta.
labels = ['x','a','b','c']
W,D = load('chain4_mark_first',labels,[('x','a'),('a','b'),('b','c')])
W2,D2 = load('diamond4_mark_bottom',labels,[('x','a'),('x','b'),('a','c'),('b','c')])
assert law(W,'x') == law(W2,'x')
assert (D['delta'],D2['delta']) == (F(0),F(1,2))
controls.append({'name':'single_marker_does_not_preserve_internal_delta','mu_x':law(W,'x'),
                 'delta_chain':D['delta'],'delta_diamond':D2['delta']})

# 9. The non-half-balanced one-isolate case of the independent delta formula.
labels,edges = family(5,4)
W,D = load('chain4_plus_singleton',labels,edges)
rows = [v[:2] for v in D['moments'].values()]
assert full_realize(5,rows) == full_realize(5,rows,True) == 4
assert D['delta'] == F(2,5)
controls.append({'name':'delta_one_isolate_even_chain','delta':D['delta'],'moments':D['moments']})

# 10. The m=2 collapsed second coordinate; m=1 is checked algebraically only.
W,D = load('antichain2',['a','b'],[])
W2,D2 = load('chain2',['a','b'],[('a','b')])
for poset in [D,D2]:
    for M,V,R in poset['moments'].values():
        assert R == 4*M-2
        assert h2_inverse(2,M,V)[0] is not None
assert model(1,1,1) == (F(1),F(0),F(2))
controls.append({'name':'small_m_degenerate_second_coordinate','m2_A':D['moments'],'m2_C':D2['moments'],
                 'm1_algebraic_moments':model(1,1,1)})

# 11. All marked chain ranks agree for an arbitrary complement, yet delta differs.
labels = ['c1','c2','c3','r1','r2']
chain_edges = [('c1','c2'),('c2','c3')]
W,D = load('chain3_parallel_chain2',labels,chain_edges+[('r1','r2')])
W2,D2 = load('chain3_parallel_antichain2',labels,chain_edges)
assert all(law(W,x) == law(W2,x) for x in ['c1','c2','c3'])
assert (D['delta'],D2['delta']) == (F(2,5),F(1,2))
K = [[F(sum(w.index(x)<w.index(y) for w in W),len(W))
      for y in ['r1','r2']] for x in ['c1','c2','c3']]
controls.append({'name':'all_chain_rank_interfaces_do_not_preserve_internal_delta',
                 'chain_rank_marginals':{x:law(W,x) for x in ['c1','c2','c3']},
                 'cross_matrix_chain3_before_chain2':K,
                 'delta_chain_complement':D['delta'],'delta_antichain_complement':D2['delta']})

assert len(controls) == 11 and len(instances) == 14

def serial(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [serial(v) for v in x]
    return x

out = {'status':'all 11 directed controls passed; 14 named true posets; no poset-family sweep',
       'instances':instances,'controls':controls}
Path(__file__).with_name('controls.json').write_text(json.dumps(serial(out),ensure_ascii=False,indent=2)+'\n')
print(out['status'])
