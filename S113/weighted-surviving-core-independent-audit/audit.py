"""Independent standard-library audit. Run: python audit.py

The oracle builds the full quotient transitive closure, then counts actual
chain-label ideals with seven-coordinate states. Pair numerators are obtained
by forward/backward edge counting in that ideal DAG, not by adding pair edges,
not by the author's summation, and not by a uniform quotient-extension law.
Zero blocks are induced deletions from the transitive closure.
"""
from collections import defaultdict, Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import importlib.util
import json
import random
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
FROZEN = HERE / 'frozen'
spec = importlib.util.spec_from_file_location('audited_author', FROZEN / 'weighted_core_formula.py')
author = importlib.util.module_from_spec(spec)
spec.loader.exec_module(author)

# Independent Boolean transitive closure, with all original vertex identities.
rel = [[False] * 7 for _ in range(7)]
for i, j in ((0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5)):
    rel[i][j] = True
for k in range(7):
    for i in range(7):
        for j in range(7):
            rel[i][j] |= rel[i][k] and rel[k][j]
PRED = [tuple(i for i in range(7) if rel[i][j]) for j in range(7)]


def ideal_oracle(w, pairs=()):
    """Return total and requested actual-label pair counts, ranks one-based."""
    w = tuple(w)
    zero = (0,) * 7
    edges = {}

    @lru_cache(None)
    def suffix(s):
        if s == w:
            edges[s] = ()
            return 1
        choices = []
        z = 0
        for j in range(7):
            if s[j] < w[j] and all(s[i] == w[i] for i in PRED[j]):
                q = list(s)
                q[j] += 1
                q = tuple(q)
                choices.append((j, q))
                z += suffix(q)
        edges[s] = choices
        return z

    z = suffix(zero)
    nums = [0] * len(pairs)
    prefix = {zero: 1}
    for s in sorted(edges, key=sum):
        p = prefix[s]
        for j, q in edges[s]:
            prefix[q] = prefix.get(q, 0) + p
            weight = p * suffix(q)
            for k, ((xi, xr), (yi, yr)) in enumerate(pairs):
                if j == yi and q[j] == yr and s[xi] >= xr:
                    nums[k] += weight
    assert prefix[w] == z
    return z, nums


def target_pairs(w):
    return [((1,1),(0,1)), ((6,w[6]),(5,w[5])),
            ((0,w[0]),(2,w[2])), ((3,1),(6,1)),
            ((4,1),(2,1)), ((3,w[3]),(4,w[4]))]


KEYS = ['bottom1_before_bottom0', 'top6_before_top5',
        'top0_before_top2', 'bottom3_before_bottom6']
NAMES = ['singleton_ports','linear_0','linear_6','linear_4',
         'binomial_0','binomial_6','endpoint_first1','endpoint_last5',
         'endpoint_top0_top2','endpoint_bottom3_bottom6']


def tests(w, z, nums):
    u,a,b,c,t,d,v = w
    return [min(u,v) >= 2, 2*u < a+b+t+v, 2*v < u+c+t+d,
            2*t < u+b+c+v,
            3*comb(a+b+u-1,u) < comb(a+b+t+v+u,u),
            3*comb(d+c+v-1,v) < comb(d+c+t+u+v,v),
            3*nums[0] > 2*z, 3*nums[1] > 2*z,
            3*nums[2] < z, 3*nums[3] < z]


def check_positive(w):
    z, nums = ideal_oracle(w, target_pairs(w))
    got = author.endpoint_counts(w)
    assert got['extensions'] == z, (w, 'total')
    assert [got[k] for k in KEYS] == nums[:4], (w, 'endpoints')
    u,a,b,c,t,d,v = w
    assert author.count_formula((v,d,c,b,t,a,u)) == z
    assert (z-nums[0]) * (u+a+b+t+v) >= u*z
    assert (z-nums[1]) * (v+c+d+t+u) >= v*z
    assert nums[4] * (t+u+b+c+v) >= t*z
    assert nums[5] * (t+u+b+c+v) >= t*z
    assert nums[2]*comb(a+b+t+v+u,u) >= z*comb(a+b+u-1,u)
    assert nums[3]*comb(d+c+t+u+v,v) >= z*comb(d+c+v-1,v)
    return z, nums


def enumerate_extensions(w):
    """Tiny explicit actual-label LE oracle, deliberately not memoized."""
    w = tuple(w)
    def walk(s, word):
        if s == w:
            yield tuple(word)
            return
        for j in range(7):
            if s[j] < w[j] and all(s[i] == w[i] for i in PRED[j]):
                q = list(s)
                q[j] += 1
                yield from walk(tuple(q), word + [(j,q[j])])
    yield from walk((0,)*7, [])


def window_audit(w):
    """Check actual fiber multiplicities and conditional numerators at C0."""
    u,a,b,c,t,d,v = w
    fibers = defaultdict(list)
    for word in enumerate_extensions(w):
        outside = tuple(x for x in word if x[0] != 0)
        fibers[outside].append(word)
    hs = Counter()
    totals = [0, 0, 0]
    for outside, words in fibers.items():
        h = outside.index((3,1))
        k = outside.index((2,b)) + 1
        assert a+b <= k <= h <= a+b+t+v
        n = comb(h+u,u)
        first = sum(word[0] == (0,1) for word in words)
        top = sum(word.index((0,u)) < word.index((2,b)) for word in words)
        assert len(words) == n
        assert first*(u+h) == n*u
        assert top == comb(k+u-1,u)
        hs[h] += 1
        totals[0] += n
        totals[1] += first
        totals[2] += top
    return {'weights':list(w), 'outside_extensions':len(fibers),
            'outside_window_histogram':dict(sorted(hs.items())),
            'total_first0_top0_counts':totals,
            'nonuniform_outside_fiber_sizes':len({len(x) for x in fibers.values()}) > 1}


def main():
    standalone = dict.fromkeys(NAMES, 0)
    cumulative = dict.fromkeys(NAMES, 0)
    survivors = []
    equalities = Counter()
    checked = 0
    for w in product(range(1,4), repeat=7):
        z, nums = check_positive(w)
        checks = tests(w,z,nums)
        alive = True
        for name, ok in zip(NAMES,checks):
            standalone[name] += bool(ok)
            alive &= ok
            cumulative[name] += bool(alive)
        if alive:
            survivors.append(list(w))
        u,a,b,c,t,d,v = w
        for name,lhs,rhs in [
            ('linear_0',2*u,a+b+t+v),('linear_6',2*v,u+c+t+d),
            ('linear_4',2*t,u+b+c+v),
            ('binomial_0',3*comb(a+b+u-1,u),comb(a+b+t+v+u,u)),
            ('binomial_6',3*comb(d+c+v-1,v),comb(d+c+t+u+v,v)),
            ('endpoint_first1',3*nums[0],2*z),('endpoint_last5',3*nums[1],2*z),
            ('endpoint_top0_top2',3*nums[2],z),('endpoint_bottom3_bottom6',3*nums[3],z)]:
            if lhs == rhs:
                equalities[name] += 1
                assert not checks[NAMES.index(name)]
        checked += 1
    survivors.sort(key=lambda w:(sum(w),w))
    ref = json.loads((FROZEN/'screen_tested_box.json').read_text())
    assert ref['standalone_surviving_counts'] == standalone
    assert ref['cumulative_surviving_counts'] == cumulative
    assert ref['survivors'] == survivors

    # Zero-block formula extension, including simultaneous deleted end blocks.
    deletion_checked = 0
    for u,a,d,v in product(range(4), repeat=4):
        if min(u,a,d,v) != 0:
            continue
        for b,c,t in product(range(1,4), repeat=3):
            w = (u,a,b,c,t,d,v)
            assert ideal_oracle(w)[0] == author.count_formula(w), ('deletion', w)
            deletion_checked += 1

    rng = random.Random(20261010)
    random_weights = [tuple(rng.randint(1,9) for _ in range(7)) for _ in range(160)]
    for w in random_weights:
        check_positive(w)

    # Unbounded ray theorem is proved in the report; these are boundary checks.
    ray_vectors = 0
    for t in range(1,101):
        expected = {(t+1,t+1),(t,t),(t,t-1),(t-1,t)}
        expected = {(u,v) for u,v in expected if min(u,v)>=2}
        actual = {(u,v) for u in range(2,t+3) for v in range(2,t+3)
                  if 2*u < 2+t+v and 2*v < u+t+2 and 2*t < u+v+2}
        assert actual == expected
        ray_vectors += len(actual)
    assert {(u,v) for u in range(2,20) for v in range(2,20)
            if 2*u < 3+v and 2*v < u+3} == {(2,2)}

    # Recompute all actual unordered pair counts for the smallest menu survivor.
    w = tuple(survivors[0])
    pairs = [((i,r),(j,s)) for i in range(7) for j in range(i+1,7)
             for r in range(1,w[i]+1) for s in range(1,w[j]+1)]
    z, counts = ideal_oracle(w,pairs)
    balanced = [{'x':list(x),'y':list(y),'numerator_x_before_y':n}
                for (x,y),n in zip(pairs,counts) if z <= 3*n <= 2*z]
    delta = max(min(n,z-n) for n in counts)
    maximizers = [{'x':list(x),'y':list(y),'numerator_x_before_y':n}
                  for (x,y),n in zip(pairs,counts) if min(n,z-n)==delta]
    smallest = ref['smallest_menu_survivor']
    assert smallest['balanced_pairs'] == balanced
    assert smallest['maximizing_pairs'] == maximizers
    assert smallest['delta_numerator'] == delta == 454 and z == 1121
    brute = list(enumerate_extensions(w))
    assert len(brute) == z
    assert [sum(word.index(x)<word.index(y) for word in brute) for x,y in pairs] == counts

    window_examples = [window_audit(w) for w in [(1,1,1,1,1,1,1),
                        (2,1,1,1,1,1,2),(2,1,1,1,2,1,2),(2,2,1,1,2,1,2)]]
    # Run both author programs in an isolated copy; preserve frozen inputs.
    with tempfile.TemporaryDirectory(prefix='weighted-core-author-replay-') as tmp:
        tmp = Path(tmp)
        for name in ('weighted_core_formula.py','screen_tested_box.py'):
            shutil.copy2(FROZEN/name,tmp/name)
            subprocess.run([sys.executable,str(tmp/name)],check=True,capture_output=True,text=True)
        for name in ('formula_validation.json','screen_tested_box.json'):
            assert (tmp/name).read_bytes() == (FROZEN/name).read_bytes(), ('author replay',name)
    files = {p.name:sha256(p.read_bytes()).hexdigest() for p in sorted(FROZEN.iterdir()) if p.is_file()}
    output = {
        'status':'PASS', 'frozen_source_sha256':files,
        'author_json_outputs_reproduced_byte_identically':True,
        'positive_box_vectors':checked,
        'independent_pair_numerators_in_box':6*checked,
        'independent_total_counts_in_box':checked,
        'independent_six_bound_checks_in_box':6*checked,
        'auxiliary_zero_block_vectors':deletion_checked,
        'random_vectors_1_to_9':len(random_weights), 'random_seed':20261010,
        'strict_threshold_equality_cases':dict(equalities),
        'four_ray_boundary_t_range':[1,100], 'four_ray_vectors':ray_vectors,
        'standalone_surviving_counts':standalone,
        'cumulative_surviving_counts':cumulative,
        'survivors':survivors,
        'smallest_survivor':{'weights':list(w),'total':z,'delta_numerator':delta,
                             'balanced_pairs':balanced,'maximizing_pairs':maximizers,
                             'explicitly_enumerated_extensions':len(brute)},
        'conditional_window_checks':window_examples,
        'scope':'Finite checks validate implementations only; unrestricted identities, bounds, and two corollaries are audited by proofs in AUDIT.md.'
    }
    (HERE/'results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('survivors','conditional_window_checks')},indent=2))


if __name__ == '__main__':
    main()
