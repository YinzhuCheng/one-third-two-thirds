#!/usr/bin/env python3
"""Independent exact audit. Standard library only; imports no author code.

Core input is pinned to the frozen n<=8 catalogue and original orbit audit.
Extension states are tuples of chain occupancies, not labelled-vertex masks.
All unordered-pair counts are computed by a recursive counting semiring.
For every restricted-family pair a second DP imposes one precedence edge.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json, time

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "inputs"

def read(name):
    return json.loads((INPUT / name).read_text())

def structure(up):
    n = len(up)
    U = [{j for j in range(n) if up[i] & (1 << j)} for i in range(n)]
    D = [{j for j in range(n) if i in U[j]} for i in range(n)]
    I = [set(range(n)) - U[i] - D[i] - {i} for i in range(n)]
    def is_chain(s):
        return all(b in U[a] or a in U[b] for a,b in combinations(s,2))
    return U,D,I,is_chain

def derived_rules(up):
    U,D,I,chain = structure(up)
    rules = []
    for i in range(len(up)):
        bottom = [j for j in sorted(I[i]) if D[j] == D[i] and chain(U[i]-U[j])]
        top = [j for j in sorted(I[i]) if U[j] == U[i] and chain(D[i]-D[j])]
        if bottom or top:
            rules.append(dict(target=i,incomparable_indices=sorted(I[i]),bottom_witnesses=bottom,
                top_witnesses=top,coefficients=[2 if k==i else -int(k in I[i]) for k in range(len(up))],integer_rhs=-1))
    return rules

def port_cyclic(up,singleton):
    U,D,I,chain = structure(up); n=len(up)
    def port(i,side):
        return (i,0 if i in singleton else side)
    vertices = {port(i,s) for i in range(n) for s in (0,1)}
    edges = {(port(i,0),port(i,1)) for i in range(n) if i not in singleton}
    for i in range(n):
        for j in U[i]:
            edges.add((port(i,1),port(j,0)))
        for j in I[i]:
            if D[i] <= D[j] and chain(U[j]-U[i]):
                edges.add((port(i,0),port(j,0)))
            if U[j] <= U[i] and chain(D[i]-D[j]):
                edges.add((port(i,1),port(j,1)))
    # Transitive closure provides an independent cycle detector.
    reach={v:{b for a,b in edges if a==v} for v in vertices}
    for k in sorted(vertices):
        for i in sorted(vertices):
            if k in reach[i]:
                reach[i] |= reach[k]
    return any(v in reach[v] for v in vertices)

def all_pair_counts(up,w):
    """Recursively sum (extension_count, pair_count_vector) over first symbols.

    Vertices have fixed labels (block, zero-based rank). If a is the first
    vertex of a suffix, it precedes every other remaining vertex in that
    suffix. Pairs absent from a suffix contribute zero. No prefix or outside
    distribution is presumed uniform.
    """
    n=len(w); w=tuple(w); U,D,I,chain=structure(up)
    vertices=[(i,r) for i in range(n) for r in range(w[i])]
    idx={v:k for k,v in enumerate(vertices)}
    pairs=list(combinations(range(len(vertices)),2))
    pair_index={p:k for k,p in enumerate(pairs)}
    starts=[sum(w[:i]) for i in range(n)]
    @lru_cache(None)
    def count(s):
        if s==w:
            return (1,(0,)*len(pairs))
        total=0; nums=[0]*len(pairs)
        for i in range(n):
            if s[i]==w[i] or any(s[j]!=w[j] for j in D[i]):
                continue
            t=list(s); t[i]+=1
            z,p=count(tuple(t)); total+=z
            for k,v in enumerate(p):
                nums[k]+=v
            a=starts[i]+s[i]
            # Only pairs in increasing label order are stored.
            for j in range(i,n):
                for r in range(s[j],w[j]):
                    b=starts[j]+r
                    if a<b:
                        nums[pair_index[a,b]]+=z
        return total,tuple(nums)
    z,nums=count((0,)*n)
    result=[[0]*len(vertices) for _ in vertices]
    for (a,b),v in zip(pairs,nums):
        assert 0<=v<=z
        result[a][b]=v; result[b][a]=z-v
        (i,r),(j,s)=vertices[a],vertices[b]
        if j in U[i] or i==j and r<s: assert v==z
        if i in U[j] or i==j and r>s: assert v==0
    return vertices,z,result,count.cache_info().currsize

def edge_count(up,w,a=None,b=None):
    """Independent scalar recurrence: b is blocked until a is placed."""
    U,D,I,chain=structure(up); w=tuple(w)
    @lru_cache(None)
    def f(s):
        if s==w: return 1
        total=0
        for i in range(len(w)):
            if s[i]>=w[i] or any(s[j]<w[j] for j in D[i]): continue
            if a is not None and (i,s[i])==b and s[a[0]]<=a[1]: continue
            t=list(s);t[i]+=1;total+=f(tuple(t))
        return total
    return f((0,)*len(w))

def audit_sections(q,rules,counts):
    F=set(q['port_forced_nonsingleton_indices']); avail=set(range(8))-F
    for mask in range(256):
        S={i for i in range(8) if mask>>i&1}
        assert port_cyclic(q['strict_up_masks'],S)==bool(S&F)
        counts['port_singleton_patterns']+=1
    base=[2 if i in F else 1 for i in range(8)]
    sections=q['all_sections']
    expected={tuple(i for i in sorted(avail) if mask>>i&1) for mask in range(256)}
    assert len(sections)==len(expected)
    assert {tuple(s['singleton_indices']) for s in sections}==expected
    rows=[r['coefficients'] for r in rules]; bad=[];good=[]
    for sec in sections:
        S=set(sec['singleton_indices']);free=[i for i in range(8) if i not in S]
        assert sec['free_indices']==free and sec['lower_weights']==base
        if sec['status']=='feasible_integer_witness':
            w=sec['weights']
            assert len(w)==8 and all(type(x) is int for x in w)
            assert all(w[i]>=base[i] and (i not in S or w[i]==1) for i in range(8))
            assert all(sum(a*x for a,x in zip(row,w))<=-1 for row in rows)
            good.append(sec);counts['integer_section_witnesses']+=1
        else:
            assert sec['status']=='infeasible_real_relaxation'
            c=sec['certificate'];y=c['row_multipliers']
            assert len(y)==len(rows) and all(type(x) is int and x>=0 for x in y)
            B=[-1-sum(a*x for a,x in zip(row,base)) for row in rows]
            coeff=[sum(v*row[i] for v,row in zip(y,rows)) for i in free]
            rhs=sum(v*b for v,b in zip(y,B))
            assert all(x>=0 for x in coeff) and rhs<0
            assert coeff==c['combined_free_coefficients'] and rhs==c['combined_rhs']
            bad.append(sec);counts['exact_infeasibility_certificates']+=1
        counts['sections']+=1
    assert q['section_count']==len(sections) and q['infeasible_sections']==len(bad) and q['feasible_sections']==len(good)
    assert q['minimal_additional_forbidden_singleton_sets']==[s for s in bad if not any(set(t['singleton_indices'])<set(s['singleton_indices']) for t in bad)]
    assert q['maximal_feasible_singleton_sets']==[s for s in good if not any(set(s['singleton_indices'])<set(t['singleton_indices']) for t in good)]
    assert q['global_integer_witness']==[2]*8
    assert all(sum(2*a for a in row)<=-1 for row in rows)

def audit_family(q,c,counts,matrices):
    up=q['strict_up_masks'];U,D,I,chain=structure(up)
    F=q['port_forced_nonsingleton_indices'];m=len(F);S=set(F)
    rules=derived_rules(up);targets={r['target'] for r in rules}
    assert S<=targets and c['variable_indices']==F
    assert c['all_other_weights']==1 and c['variable_lower_bound']==2
    A=[[2 if i==j else -int(j in I[i]) for j in F] for i in F]
    b=[len(I[i]-S)-1 for i in F]
    assert A==c['matrix'] and b==c['rhs']
    H=[[Fraction(*v) for v in row] for row in c['inverse_rational']]
    assert len(H)==m and all(len(row)==m for row in H)
    assert all(x>=0 for row in H for x in row)
    for i,j in product(range(m),repeat=2):
        assert sum(H[i][k]*A[k][j] for k in range(m))==int(i==j)
        assert sum(A[i][k]*H[k][j] for k in range(m))==int(i==j)
    u=[sum(h*v for h,v in zip(row,b)) for row in H]
    bounds=[v.numerator//v.denominator for v in u]
    assert u==[Fraction(*v) for v in c['upper_bounds_rational']]
    assert bounds==c['upper_bounds_integer']
    accepted=[];cartesian=0
    for vals in product(*(range(2,v+1) for v in bounds)):
        cartesian+=1;w=[1]*8
        for i,v in zip(F,vals): w[i]=v
        if all(2*w[r['target']] < sum(w[k] for k in r['incomparable_indices']) for r in rules): accepted.append(w)
    assert cartesian==c['cartesian_vectors']
    assert accepted==[v['weights'] for v in c['balanced_certificates']]
    assert len(accepted)==c['filter_feasible_vectors']
    assert c['additional_nonsingleton_clause']==[i for i in range(8) if i not in S]
    assert c['necessary_nonsingleton_count']==len(S)+1
    cases=[]
    for cert in c['balanced_certificates']:
        w=cert['weights'];V,Z,N,states=all_pair_counts(up,w); idx={v:k for k,v in enumerate(V)}
        assert Z==edge_count(up,w)==cert['extension_count']==cert['denominator']
        pair=[tuple(v) for v in cert['balanced_pair_zero_based_ranks']];a,b=[idx[v] for v in pair]
        assert pair[1][0] in I[pair[0][0]]
        assert Z<=3*N[a][b]<=2*Z and N[a][b]==cert['numerator']
        for a,b in combinations(range(len(V)),2):
            x=edge_count(up,w,V[a],V[b]);y=edge_count(up,w,V[b],V[a])
            assert x==N[a][b] and y==N[b][a] and x+y==Z
            counts['family_all_unordered_pairs']+=1; counts['family_independent_precedence_counts']+=2
        balanced=[(V[a],V[b]) for a,b in combinations(range(len(V)),2) if V[b][0] in I[V[a][0]] and Z<=3*N[a][b]<=2*Z]
        assert balanced
        cases.append(dict(weights=w,order=sum(w),extension_count=Z,balanced_pair_count=len(balanced),author_witness=cert))
        matrices.append(dict(scope='forced_support_family',class_id=q['class_id'],weights=w,vertices=V,extension_count=Z,pair_numerators=N))
        counts['family_vectors']+=1;counts['family_occupancy_states']+=states
    counts['family_classes']+=1
    return dict(class_id=q['class_id'],strict_up_masks=up,original_forced_set=F,certified_bounds=bounds,
        cartesian_vectors=cartesian,filter_feasible_vectors=len(accepted),necessary_nonsingleton_count=len(F)+1,cases=cases)

def audit_small(q,counts,matrices):
    up=q['strict_up_masks'];U,D,I,chain=structure(up);rules=derived_rules(up)
    row=dict(class_id=q['class_id'],linear_pass=0,port_and_linear_pass=0,inflations=0)
    for w in product((1,2),repeat=8):
        V,Z,N,states=all_pair_counts(up,w);index={v:k for k,v in enumerate(V)}
        counts['binary_occupancy_states']+=states
        balanced=[]
        for a,b in combinations(range(len(V)),2):
            counts['binary_all_unordered_pairs']+=1
            if V[b][0] in I[V[a][0]] and Z<=3*N[a][b]<=2*Z:balanced.append((a,b))
        assert balanced
        counts['binary_balanced_inflations']+=1
        for i in range(8):
            denominator=w[i]+sum(w[k] for k in I[i])
            for j in I[i]:
                if D[i]<=D[j]:
                    assert denominator*N[index[i,0]][index[j,0]]>=w[i]*Z
                    counts['bottom_insertion_bounds']+=1
                if U[i]<=U[j]:
                    assert denominator*N[index[j,w[j]-1]][index[i,w[i]-1]]>=w[i]*Z
                    counts['top_insertion_bounds']+=1
        actualU=[{b for b,(j,s) in enumerate(V) if j in U[i] or i==j and r<s} for i,r in V]
        actualD=[{a for a,(j,s) in enumerate(V) if j in D[i] or i==j and s<r} for i,r in V]
        def actual_chain(S):return all(b in actualU[a] or a in actualU[b] for a,b in combinations(S,2))
        for r in rules:
            i=r['target']
            for j in r['bottom_witnesses']:
                a,b=index[j,0],index[i,0]
                assert actualD[a]<=actualD[b] and actual_chain(actualU[b]-actualU[a])
                counts['actual_good_pair_lifts']+=1
            for j in r['top_witnesses']:
                a,b=index[i,w[i]-1],index[j,w[j]-1]
                assert actualU[b]<=actualU[a] and actual_chain(actualD[a]-actualD[b])
                counts['actual_good_pair_lifts']+=1
        linear=all(2*w[r['target']]<sum(w[k] for k in r['incomparable_indices']) for r in rules)
        port=all(w[i]>=2 for i in q['port_forced_nonsingleton_indices'])
        counts['linear_rejections']+=not linear;counts['port_rejections']+=not port
        row['linear_pass']+=linear;row['port_and_linear_pass']+=linear and port;row['inflations']+=1
        counts['binary_inflations']+=1
        matrices.append(dict(scope='binary_weights',class_id=q['class_id'],weights=w,vertices=V,extension_count=Z,pair_numerators=N))
    return row

def main():
    start=time.monotonic();counts=Counter();matrices=[];classes=[];binary=[]
    original=[q for q in read('frozen_singleton_constraints.json') if q['n']==8]
    assert original==read('input_cores.json')
    independent={tuple(q['representative_masks']):q for q in read('original_orbit_audit.json')['classes'] if q['n']==8}
    Q=read('weight_filter_catalogue.json')['cores'];C=read('minimal_support_family_certificates.json')
    assert len(original)==len(Q)==len(C['cores'])==len(independent)==17
    assert [q['class_id'] for q in original]==[f'C{i:02d}' for i in range(2,19)]
    assert len({tuple(q['strict_up_masks']) for q in Q})==17
    for inp,q,c in zip(original,Q,C['cores']):
        assert inp['class_id']==q['class_id']==c['class_id']
        assert inp['strict_up_masks']==q['strict_up_masks'] and inp['cover_edges']==q['cover_edges']
        old=independent[tuple(q['strict_up_masks'])]
        assert old['minimal_forbidden_singleton_sets']==[p['singleton_vertices'] for p in inp['minimal_forbidden_singleton_subsets']]
        assert q['port_certificates']==inp['minimal_forbidden_singleton_subsets']
        F=sorted(s['singleton_vertices'][0] for s in inp['minimal_forbidden_singleton_subsets'])
        assert all(len(s['singleton_vertices'])==1 for s in inp['minimal_forbidden_singleton_subsets'])
        assert q['port_forced_nonsingleton_indices']==F
        rules=derived_rules(q['strict_up_masks']);assert rules==q['rules']
        counts['distinct_inequalities']+=len(rules)
        counts['bottom_witnesses']+=sum(len(r['bottom_witnesses']) for r in rules)
        counts['top_witnesses']+=sum(len(r['top_witnesses']) for r in rules)
        audit_sections(q,rules,counts)
        classes.append(audit_family(q,c,counts,matrices))
        binary.append(audit_small(q,counts,matrices))
        print(q['class_id'],'PASS; original forced set',F,'family vectors',c['filter_feasible_vectors'],flush=True)
    assert counts['family_vectors']==C['total_filter_feasible_vectors']==22
    maxorder=max(r['order'] for q in classes for r in q['cases'])
    assert maxorder==C['maximum_checked_inflation_order']==15
    author=read('inflation_validation.json')
    for a,b in zip(binary,author['by_class']):
        assert all(a[k]==b[k] for k in a)
    for ours,theirs in [('binary_inflations','inflations'),('bottom_insertion_bounds','general_bottom_insertion_bounds'),
        ('top_insertion_bounds','general_top_insertion_bounds'),('actual_good_pair_lifts','actual_good_pair_lifts'),
        ('linear_rejections','linear_rejections'),('port_rejections','port_rejections'),
        ('binary_balanced_inflations','balanced_witnesses'),('binary_occupancy_states','ideal_states')]:
        assert counts[ours]==author['counts'][theirs]
    data=dict(status='PASS',counts=dict(counts),maximum_forced_support_inflation_order=maxorder,
        forced_support_order_histogram=dict(sorted(Counter(r['order'] for q in classes for r in q['cases']).items())),
        family_classes=classes,binary_summary=binary,elapsed_seconds=round(time.monotonic()-start,3))
    (ROOT/'audit_results.json').write_text(json.dumps(data,indent=2)+'\n')
    (ROOT/'all_pair_counts.json').write_text(json.dumps(matrices,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ('family_classes','binary_summary')},indent=2))

if __name__=='__main__':main()
