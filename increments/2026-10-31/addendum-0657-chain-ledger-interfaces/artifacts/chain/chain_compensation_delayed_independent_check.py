#!/usr/bin/env python3
"""Independent closure, old-screen, module and ideal-DP check; no producer imports."""
import json
from fractions import Fraction
from pathlib import Path
import sys

source = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent / 'chain_compensation_witness_delayed_validation.json')
target = Path(sys.argv[2] if len(sys.argv) > 2 else Path(__file__).resolve().parent / 'chain_compensation_delayed_independent_validation.json')
data = json.loads(source.read_text())
V = data['vertices']
ix = {v: i for i, v in enumerate(V)}
n = len(V)
U = [0] * n
for edge in data['hasse_edges']:
    a, b = edge.split('<')
    U[ix[a]] |= 1 << ix[b]
for k in range(n):
    for i in range(n):
        if U[i] >> k & 1:
            U[i] |= U[k]
assert all(not (U[i] >> i & 1) for i in range(n))
D = [sum(1 << j for j in range(n) if U[j] >> i & 1) for i in range(n)]
I = [((1 << n) - 1) & ~(U[i] | D[i] | (1 << i)) for i in range(n)]

def names(mask):
    return [V[i] for i in range(n) if mask >> i & 1]

def chain(mask):
    return all(not (mask & ~(U[i] | D[i] | (1 << i))) for i in range(n) if mask >> i & 1)

vg, dvg, graph = [], [], U.copy()
for i in range(n):
    for j in range(n):
        if not (I[i] >> j & 1):
            continue
        if not (D[i] & ~D[j]) and chain(U[j] & ~U[i]):
            graph[i] |= 1 << j
        if not (U[j] & ~U[i]) and chain(D[i] & ~D[j]):
            graph[i] |= 1 << j
        if i < j and D[i] == D[j] and chain(U[i] & ~U[j]) and chain(U[j] & ~U[i]):
            vg.append([V[i], V[j]])
        if i < j and U[i] == U[j] and chain(D[i] & ~D[j]) and chain(D[j] & ~D[i]):
            dvg.append([V[i], V[j]])
indegree = [sum(bool(graph[j] >> i & 1) for j in range(n)) for i in range(n)]
queue = [i for i in range(n) if not indegree[i]]
topological = []
while queue:
    i = queue.pop(0)
    topological.append(V[i])
    for j in range(n):
        if graph[i] >> j & 1:
            indegree[j] -= 1
            if not indegree[j]:
                queue.append(j)

modules = []
for mask in range(1, (1 << n) - 1):
    if mask.bit_count() < 2:
        continue
    inside = [i for i in range(n) if mask >> i & 1]
    a = inside[0]
    if all(all(bool(U[x] >> y & 1) == bool(U[x] >> a & 1)
               and bool(U[y] >> x & 1) == bool(U[a] >> x & 1)
               for y in inside)
           for x in range(n) if not (mask >> x & 1)):
        modules.append([V[i] for i in inside])

def count(remove=(), extra=()):
    W = [i for i in range(n) if V[i] not in remove]
    wi = {a: j for j, a in enumerate(W)}
    masks = [sum(1 << wi[j] for j in W if D[i] >> j & 1) for i in W]
    for a, b in extra:
        masks[wi[ix[b]]] |= 1 << wi[ix[a]]
    dp = [0] * (1 << len(W))
    dp[0] = 1
    for mask in range(len(dp)):
        if not dp[mask]:
            continue
        for i in range(len(W)):
            if not (mask >> i & 1) and not (masks[i] & ~mask):
                dp[mask | (1 << i)] += dp[mask]
    return dp[-1]

Q = sum(1 << i for i in range(n) if V[i] not in {'v', 'b', 'c1', 'c2'})
F = U[ix['c2']]
A = U[ix['v']] & U[ix['c1']] & ~F
L, M, C = A & U[ix['b']], F & ~U[ix['b']], F & U[ix['b']]
K = sum(1 << ix[x] for x in ['e', 'a8', 'a10'])
external = Q & ~(K | M)
old = [[V[l], V[m]] for l in range(n) if L >> l & 1
       for m in range(n) if M >> m & 1
       and not ((D[m] & Q) & ~D[l]) and not ((U[l] & Q) & ~U[m])]
profiles = {x: {'D_R': names(D[ix[x]] & external), 'U_R': names(U[ix[x]] & external)}
            for x in ['e', 'a8', 'a10', 'f11']}
N, R0, R1 = count(), count(['c1']), count(['v', 'c1'])
B, Z = count(['v', 'b', 'c1']), count(['c1', 'c2'])
candidate = count(extra=[('c1', 'd')])
out = {
    'vertices': V, 'I_v': names(I[ix['v']]), 'T': names(U[ix['v']] & ~U[ix['c1']]),
    'A': names(A), 'F': names(F), 'L': names(L), 'M': names(M), 'C': names(C),
    'K_chain': all(U[ix[a]] >> ix[b] & 1 for a, b in [('e', 'a8'), ('a8', 'a10')]),
    'K_cross_M': all(I[i] >> j & 1 for i in range(n) if K >> i & 1
                     for j in range(n) if M >> j & 1),
    'external_profiles': profiles, 'degrees': dict(zip(V, map(int.bit_count, I))),
    'max_inc': max(x.bit_count() for x in I), 'very_good': vg, 'dual_very_good': dvg,
    'mixed_arcs': sum(x.bit_count() for x in graph), 'topological': topological,
    'modules': modules, 'old_singleton_edges': old,
    'counts': {'N': N, 'R0': R0, 'R1': R1, 'B': B, 'Z': Z, 'K_c1d': candidate},
    'q0': str(Fraction(R0, N)), 'pd': str(Fraction(candidate, N)),
    'q0_lower_slack': 3 * R0 - N, 'B_minus_Z': B - Z,
}
assert len(topological) == n and not vg and not dvg and not modules
assert R0 == R1 + Z and B <= Z
assert out['K_chain'] and out['K_cross_M']
assert not ((D[ix['f11']] & external) & ~D[ix['e']])
assert not ((U[ix['e']] & external) & ~U[ix['f11']])
target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(out, ensure_ascii=False))
