#!/usr/bin/env python3
"""Independent audit: construct the poset, then count ideals via deletion.
No imports or code from the discovering search or its family formula.
The supplied JSON is consulted only after all counts have been computed.
"""
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
labels = ['a', 'b', 'x', 'y'] + [f'z{i}' for i in range(1,16)] + [f'c{i}' for i in range(1,55)]
index = {v:i for i,v in enumerate(labels)}
n = len(labels)
chains = [['a','b']+[f'c{i}' for i in range(1,55)], ['y']+[f'z{i}' for i in range(1,16)], ['x']]
edges = [(u,v) for chain in chains for u,v in zip(chain,chain[1:])] + [('a','z1'),('x','z2'),('x','c1')]
pred = [0]*n
for u,v in edges: pred[index[v]] |= 1 << index[u]
full = (1<<n)-1

# Transitive closure, performed independently of ideal counting.
anc = pred[:]
for k in range(n):
    for v in range(n):
        if anc[v] >> k & 1: anc[v] |= anc[k]
assert all(not (anc[v] >> v & 1) for v in range(n))
minima = [labels[v] for v in range(n) if anc[v] == 0]
assert set(minima) == {'a','x','y'}
assert anc[index['b']] == 1 << index['a']
assert all(anc[index[v]] >> index[u] & 1 for chain in chains for u,v in zip(chain,chain[1:]))
assert len({v for chain in chains for v in chain}) == n
# These three chains cover P, so width <= 3; {a,x,y} is an antichain.
assert all(not (anc[index[v]] >> index[u] & 1) for u in minima for v in minima if u != v)
up_xy = {v for v in labels if v in ('x','y') or (anc[index[v]] & ((1<<index['x']) | (1<<index['y'])))}
avoidance = [v for v in labels if v not in up_xy]
assert avoidance == ['a','b']

# A completely general recurrence on ideal bitmasks. To count u<v,
# add u as a prerequisite of v; no family-specific counting formula is used.
def extensions(extra_edge=None):
    req = pred[:]
    if extra_edge:
        u,v=extra_edge
        req[index[v]] |= 1<<index[u]
    @lru_cache(None)
    def dp(ideal):
        if ideal == full: return 1
        rest = full ^ ideal
        total = 0
        while rest:
            bit = rest & -rest
            rest -= bit
            v = bit.bit_length()-1
            if req[v] & ideal == req[v]: total += dp(ideal | bit)
        return total
    count = dp(0)
    return count, dp.cache_info().currsize

pairs = [('a','x'),('a','y'),('b','x'),('b','y'),('x','y')]
E, states = extensions()
K, pair_states = [], []
for pair in pairs:
    k, s = extensions(pair)
    K.append(k); pair_states.append(s)
# Independently verify complements exactly, to expose edge-orientation errors.
reverse_K = [extensions((v,u))[0] for u,v in pairs]
assert all(k + j == E for k,j in zip(K,reverse_K))

# A second method: count all events together in one chain-prefix DAG.
# Prefixes determine an ideal uniquely. At an edge that inserts the right
# endpoint, count F(prefix)*B(next_prefix) if the left endpoint is present.
lengths = tuple(len(chain) for chain in chains)
prefix_masks = []
for chain in chains:
    masks=[0]
    for v in chain: masks.append(masks[-1] | (1<<index[v]))
    prefix_masks.append(masks)

def transitions(state):
    ideal = prefix_masks[0][state[0]] | prefix_masks[1][state[1]] | prefix_masks[2][state[2]]
    for c in range(3):
        if state[c] == lengths[c]: continue
        v=index[chains[c][state[c]]]
        if pred[v] & ideal != pred[v]: continue
        next_state=list(state); next_state[c]+=1
        yield tuple(next_state),v,ideal

@lru_cache(None)
def backward(state):
    if state == lengths: return 1
    return sum(backward(next_state) for next_state,_,_ in transitions(state))

origin=(0,0,0)
assert backward(origin)==E
front={origin:1}
event_K=[0]*5
for rank in range(n):
    next_front={}
    for state,f in front.items():
        for next_state,v,ideal in transitions(state):
            next_front[next_state]=next_front.get(next_state,0)+f
            suffix=backward(next_state)
            for p,(left,right) in enumerate(pairs):
                if v==index[right] and ideal>>index[left]&1:
                    event_K[p]+=f*suffix
    front=next_front
assert front == {lengths:E}
assert event_K==K

# Check supplied claims only now, after deriving every number.
certificate=json.loads((HERE/'L_family_counterexample.json').read_text())
assert certificate['n']==n and certificate['E']==E and certificate['K']==K
margins=[{'pair':'<'.join(pair), 'K':k, 'fraction':str(Fraction(k,E)),
          'decimal':format(float(Fraction(k,E)), '.15f'),
          '3K_minus_2E':3*k-2*E, '3K_minus_E':3*k-E}
         for pair,k in zip(pairs,K)]
assert all(3*K[i]>2*E for i in (0,1,4))
assert 3*K[2]<E
assert E<3*K[3]<2*E
result={'status':'VERIFIED: L REFUTED; MC3 NOT REFUTED', 'n':n,
        'width':3,'minima':minima,'avoidance_B':avoidance,
        'chain_cover':chains,'generating_edges':edges,
        'E':E,'K':K,'reverse_K':reverse_K,'margins':margins,
        'ideal_states':states,'pair_ideal_states':pair_states,
        'chain_prefix_states':backward.cache_info().currsize,
        'independent_methods_agree':True,
        'source_certificate_matches':True}
(HERE/'L_counterexample_independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','n','width','minima','avoidance_B','E','K','margins','ideal_states','pair_ideal_states','chain_prefix_states','independent_methods_agree','source_certificate_matches')},indent=2))
