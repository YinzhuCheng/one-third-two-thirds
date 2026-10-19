#!/usr/bin/env python3
"""Independent labelled brute-force audit; does not import producer code."""
from itertools import permutations, combinations
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent
D = ('u', 'a', 'b', 't', 'v', 'z')
C = ('c1', 'c2')
LABELS = D + C + ('y',)
# Actual Hasse edges. In particular z is incomparable with D minus z.
HASSE = (('u','a'), ('u','b'), ('a','t'), ('b','t'), ('v','t'),
         ('t','c1'), ('z','c1'), ('c1','c2'), ('v','y'))

def relation(labels):
    r = set(HASSE)
    # Compute before restricting, so deletion keeps all induced comparabilities.
    while True:
        rr = r | {(a,d) for a,b in r for c,d in r if b == c}
        if rr == r:
            break
        r = rr
    return {(a,b) for a,b in r if a in labels and b in labels}

def brute(labels):
    rel = relation(labels)
    exts = []
    for perm in permutations(labels):
        pos = {a:i for i,a in enumerate(perm)}
        if all(pos[a] < pos[b] for a,b in rel):
            exts.append(perm)
    nums = {(a,b): sum(e.index(a) < e.index(b) for e in exts)
            for a in labels for b in labels if a != b}
    return rel, exts, nums

def dp_count(labels, extra=()):
    n = len(labels)
    rel = relation(labels) | set(extra)
    pred = [sum(1 << i for i,a in enumerate(labels) if (a,b) in rel) for b in labels]
    @lru_cache(None)
    def f(mask):
        if mask == (1 << n) - 1:
            return 1
        return sum(f(mask | (1 << i)) for i in range(n)
                   if not (mask >> i) & 1 and pred[i] & mask == pred[i])
    return f(0)

def autonomous_chain(subset, labels, rel):
    s = set(subset)
    if not all((a,b) in rel or (b,a) in rel for a,b in combinations(subset,2)):
        return False
    for x in labels:
        if x in s:
            continue
        sigs = {(x,c) in rel and -1 or ((c,x) in rel and 1 or 0) for c in s}
        if len(sigs) != 1:
            return False
    return True

all_data = {}
for name, labels in [('D',D), ('R',D+('y',)), ('P',LABELS), ('Q', tuple(x for x in LABELS if x != 'c1'))]:
    rel, exts, nums = brute(labels)
    den = len(exts)
    assert dp_count(labels) == den
    for a,b in combinations(labels,2):
        assert dp_count(labels, ((a,b),)) == nums[a,b]
        assert dp_count(labels, ((b,a),)) == nums[b,a]
        assert nums[a,b] + nums[b,a] == den
    all_data[name] = {
        'labels': list(labels), 'relation': [list(x) for x in sorted(rel)],
        'linear_extension_count': den,
        'ordered_pair_counts': {f'{a}<{b}': n for (a,b),n in nums.items()},
        'balanced_incomparable_pairs': [
            {'pair':[a,b], 'count':nums[a,b], 'probability':str(Fraction(nums[a,b],den))}
            for a,b in combinations(labels,2)
            if (a,b) not in rel and (b,a) not in rel and den <= 3*nums[a,b] <= 2*den],
    }
    (OUT/f'{name}_linear_extensions.txt').write_text('\n'.join(' '.join(e) for e in exts)+'\n')
    print(name, den, 'balanced:', all_data[name]['balanced_incomparable_pairs'])

rel = relation(LABELS)
autonomous_supersets = []
for k in range(2,len(LABELS)+1):
    for subset in combinations(LABELS,k):
        if set(C) <= set(subset) and autonomous_chain(subset,LABELS,rel):
            autonomous_supersets.append(list(subset))
assert autonomous_supersets == [list(C)]
assert all((d,c) in rel for d in D for c in C)
assert all((c,'y') not in rel and ('y',c) not in rel for c in C)
assert all_data['P']['linear_extension_count'] == 292
assert all_data['Q']['linear_extension_count'] == 244
all_data['structure'] = {
    'hasse_edges': [list(x) for x in HASSE],
    'autonomous_chain_supersets_of_C': autonomous_supersets,
    'C_is_ordinary_maximal_chain': False,
    'ordinary_chain_extension': ['t','c1','c2'],
    'unique_outside_point_incomparable_to_C': 'y',
}
(OUT/'audit.json').write_text(json.dumps(all_data, indent=2)+'\n')
print('Autonomous chain supersets containing C:',autonomous_supersets)
print('Menu P counts:',{p:all_data['P']['ordered_pair_counts'][p] for p in ['u<v','v<u','y<u','u<y','y<v','v<y','c1<y','y<c1','c2<y','y<c2']})
print('Menu Q counts:',{p:all_data['Q']['ordered_pair_counts'][p] for p in ['u<v','v<u','y<u','u<y','y<v','v<y','c2<y','y<c2']})
