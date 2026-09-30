"""Optional exact arithmetic for S74; proofs are in notes/PROOF.md.
Standard library only. No external credentials, no numerical tolerances.
Run: python S74/src/check_s74.py --output S74/evidence
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import argparse, json, random, time


def closure(n, edges):
    up = [0] * n
    for u, v in edges:
        if not (0 <= u < n and 0 <= v < n) or u == v:
            raise ValueError('Invalid edge')
        up[u] |= 1 << v
    for k in range(n):
        for i in range(n):
            if up[i] >> k & 1:
                up[i] |= up[k]
    if any(up[i] >> i & 1 for i in range(n)):
        raise ValueError('Cyclic relations')
    return tuple(up)


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def exact(up):
    """Counts extensions and all directed pair events, visiting ideals only."""
    n = len(up); full = (1 << n) - 1
    down = tuple(sum(1 << j for j in range(n) if up[j] >> i & 1) for i in range(n))
    layers = [{0: 1}]; transitions = {}
    for _ in range(n):
        nxt = {}
        for mask, weight in layers[-1].items():
            moves = []
            for v in bits(full ^ mask):
                if not (down[v] & ~mask):
                    nm = mask | (1 << v)
                    moves.append((v, nm))
                    nxt[nm] = nxt.get(nm, 0) + weight
            transitions[mask] = moves
        layers.append(nxt)
    back = {full: 1}
    for layer in reversed(layers[:-1]):
        for mask in layer:
            back[mask] = sum(back[nm] for _, nm in transitions[mask])
    pair = [[0] * n for _ in range(n)]
    for layer in layers[:-1]:
        for mask, weight in layer.items():
            for v, nm in transitions[mask]:
                ways = weight * back[nm]
                for z in bits(full ^ nm):
                    pair[v][z] += ways
    return down, back[0], pair


def natural_orders(n):
    """Each natural-labelled poset exactly once, by the new maximum's ideal."""
    def rec(down):
        m = len(down)
        if m == n:
            yield tuple(sum(1 << j for j in range(n) if down[j] >> i & 1) for i in range(n))
            return
        for mask in range(1 << m):
            if all(not (down[i] & ~mask) for i in bits(mask)):
                yield from rec(down + (mask,))
    yield from rec(())


def common_prefix(up, ym):
    out = []; remaining = ym
    while remaining:
        roots = [v for v in bits(remaining) if (up[v] & remaining) == (remaining ^ (1 << v))]
        if not roots:
            break
        v = roots[0]; out.append(v); remaining ^= 1 << v
    return out


def maximal_chains(up, ym, y):
    def rec(v, path):
        above = up[v] & ym
        if not above:
            yield tuple(path); return
        covers = [w for w in bits(above)
                  if not any(up[t] >> w & 1 for t in bits(above ^ (1 << w)))]
        for w in covers:
            yield from rec(w, path + [w])
    yield from rec(y, [y])


def autonomous(up, bm):
    for z in range(len(up)):
        if bm >> z & 1:
            continue
        below = up[z] & bm
        above = sum(1 << v for v in bits(bm) if up[v] >> z & 1)
        if below not in (0, bm) or above not in (0, bm):
            return False
    return True


def degree(up, ym):
    inc = {}
    for v in bits(ym):
        inc[v] = sum(1 for w in bits(ym) if w != v and not (up[v] >> w & 1) and not (up[w] >> v & 1))
    return inc, max(inc.values(), default=0)


def eta(b, L, d, k):
    return min(Fraction(comb(b, k), comb(b+L, k)), Fraction(k, 2*k+1),
               Fraction(b, 2*b+d+1), Fraction(b+1, 2*b+2*d+3))


def examine(up, x, y, stats, all_prefixes=True):
    down, E, pair = exact(up)
    if x == y or up[x] >> y & 1 or up[y] >> x & 1 or down[x] & ~down[y]:
        raise ValueError('The structural hypotheses do not hold')
    ym = (1 << y) | (up[y] & ~up[x]); N = ym.bit_count()
    B = common_prefix(up, ym); inc, d = degree(up, ym)
    chains = list(maximal_chains(up, ym, y)); stats['configurations'] += 1
    for C in chains:
        local = max(Fraction(min(pair[x][v], pair[v][x]), E) for v in C)
        for v, w in zip(C, C[1:]):
            ell = 1 + sum(up[t] >> v & 1 for t in bits(ym))
            top = 1 + (up[w] & ym).bit_count()
            window = N - top - ell + 1
            assert window <= inc[v] + inc[w] + 1
            assert ell * (pair[x][w] - pair[x][v]) <= window * pair[x][v]
            stats['cover_windows'] += 1
        if len(B) >= max(1, 2*d) and 2*pair[x][y] <= E:
            assert local >= Fraction(1, 3)
            stats['degree_33_chain_checks'] += 1
            if d:
                stats['genuinely_branched_33_chain_checks'] += 1
            if N-len(C)+1 > len(B):
                stats['beyond_S73_global_deficit_chain_checks'] += 1
        if down[x] == down[y]:
            L = 1 + (up[x] & ~up[y]).bit_count()
            prefix_lengths = range(1, len(B)+1) if all_prefixes else [len(B)]
            for b in prefix_lengths:
                if not autonomous(up, sum(1 << v for v in B[:b])):
                    continue
                for k in range(1, b+1):
                    assert local >= eta(b, L, d, k), (up, x, y, C, b, k)
                    stats['degree_envelopes'] += 1
    return {'n': len(up), 'E': E, 'Y_size': N, 'prefix': len(B), 'degree': d,
            'p_x_y': str(Fraction(pair[x][y], E)), 'chains': len(chains)}


def exhaustive(nmax=6):
    stats = Counter()
    for n in range(2, nmax+1):
        for up in natural_orders(n):
            stats['posets'] += 1
            down, E, pair = exact(up)
            for x in range(n):
                for y in range(n):
                    if x == y or up[x] >> y & 1 or up[y] >> x & 1 or down[x] & ~down[y]:
                        continue
                    examine(up, x, y, stats)
    return dict(stats)


def layered_family(b, block_sizes, L, seed, nonautonomous=False):
    rng = random.Random(seed)
    X = list(range(L)); B = list(range(L, L+b)); off = L+b
    blocks = []
    for k in block_sizes:
        blocks.append(list(range(off, off+k))); off += k
    lower = [off, off+1]; upper = [off+2, off+3, off+4]; n = off+5
    edges = list(zip(X, X[1:])) + list(zip(B, B[1:]))
    groups = [B] + blocks
    for G, H in zip(groups, groups[1:]):
        edges += [(u, v) for u in G for v in H]
    edges += list(zip(lower, lower[1:])) + list(zip(upper, upper[1:]))
    edges += [(X[-1], upper[0]), (B[-1], upper[0])]
    for G in blocks:
        for u in G:
            if rng.random() < .55:
                edges.append((rng.choice(lower), u))
            if rng.random() < .55:
                edges.append((u, rng.choice(upper)))
    if nonautonomous and b >= 2:
        edges.append((lower[-1], B[1]))
    return closure(n, edges), X[0], B[0]


def constructed():
    stats = Counter(); rows=[]
    for d in (1, 2):
        for q in range(1, 7):
            for L in (1, 2, 3):
                for mode in ('33', '40'):
                    b = 2*d if mode == '33' else max(2*L+1, 4*d+1)
                    up, x, y = layered_family(b, [d+1]*q, L, 7400+q*31+L*7+d,
                                             nonautonomous=(mode=='33' and q%2==0))
                    row = examine(up, x, y, stats, all_prefixes=False)
                    row.update(d=d, q=q, L=L, mode=mode); rows.append(row)
    return dict(stats), rows


def tail_poset(upR):
    # labels x,y,t,z,w followed by the arbitrary tail R.
    l = len(upR); edges=[(1,3),(2,3),(1,4)]
    edges += [(i+5, j+5) for i in range(l) for j in bits(upR[i])]
    edges += [(v, j+5) for v in (0,3) for j in range(l)]
    return closure(5+l, edges)


def tail_checks():
    stats=Counter(); examples=[]
    for l in range(6):
        Rorders = [()] if l == 0 else natural_orders(l)
        for R in Rorders:
            up=tail_poset(R); _, E, pair=exact(up)
            eR=1 if l==0 else exact(R)[1]
            assert E == (8*l+25)*eR
            numerators={(0,1):3*l+7,(0,3):6*l+18,(0,4):8*l+16,
                        (3,4):8*l+10,(1,2):4*l+15}
            for (i,j),v in numerators.items():
                assert pair[i][j] == v*eR
                stats['formula_checks'] += 1
            assert Fraction(min(pair[1][2],pair[2][1]),E) >= Fraction(2,5)
            stats['arbitrary_tail_posets'] += 1
            if l==3 and R==closure(3,[(0,1),(1,2)]):
                menu=(0,1,3,4)
                assert max(min(pair[i][j],pair[j][i]) for i,j in combinations(menu,2)) == 16
                assert E==49
                examples.append({'labels':['x','y','t','z','w','r1','r2','r3'],
                                 'strict_successor_masks':list(up),'E':E,'pair_counts':pair,
                                 'local_menu':['x','y','z','w'],'local_balance':'16/49',
                                 'repair_pair':['y','t'],'repair_balance':'22/49'})
    return dict(stats),examples


def artificial_law():
    # This is NOT a uniform-extension law or a conjecture counterexample.
    weighted=[((0,1,2,3),2),((1,0,2,3),2),((1,2,0,3),2),((1,2,3,0),1),
              ((0,1,3,2),1),((1,0,3,2),1),((1,3,0,2),1)]
    pair={(i,j):sum(w for order,w in weighted if order.index(i)<order.index(j))
          for i,j in permutations(range(4),2)}
    assert sum(w for _,w in weighted)==10
    assert max(min(pair[i,j],pair[j,i]) for i,j in combinations(range(4),2))==3
    return {'type':'nonuniform diagnostic, not a poset counterexample',
            'weights_out_of_10': [{'order':list(o),'weight':w} for o,w in weighted],
            'balance':'3/10', 'conditional_rank_masses':[[2,2,2,1],[1,1,1,0]]}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,default=Path('S74/evidence'))
    args=p.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    start=time.time(); out={}
    out['exhaustive_2_to_6']=exhaustive()
    out['constructed'],families=constructed()
    out['tail_checks'],negative=tail_checks()
    out['elapsed_seconds']=round(time.time()-start,3)
    for name,data in [('summary.json',out),('layered_families.json',families),
                      ('width_three_obstruction.json',negative[0]),('artificial_law.json',artificial_law())]:
        (args.output/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
