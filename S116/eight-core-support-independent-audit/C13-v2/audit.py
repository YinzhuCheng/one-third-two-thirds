#!/usr/bin/env python3
"""C13 independent audit; all checks remain active under python -O.
No implementation is imported from either author or previous auditor.
"""
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parent

def require(ok, why):
    if not ok: raise RuntimeError(why)
def read(rel):return json.loads((ROOT/rel).read_text())
def digest(rel):return hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
def chain(s,U):return all(b in U[a] or a in U[b] for a,b in combinations(s,2))
def structure(up):
    U=[{j for j in range(8) if mask>>j&1} for mask in up]
    D=[{j for j in range(8) if i in U[j]} for i in range(8)]
    I=[set(range(8))-{i}-U[i]-D[i] for i in range(8)]
    require(all(i not in U[i] for i in range(8)), 'Irreflexivity')
    require(all(U[j]<=U[i] for i in range(8) for j in U[i]),'Transitivity')
    return U,D,I

def port_graph(U,D,I,S):
    # S is the singleton set. Its two ports coalesce.
    def p(i,t):return (i,0 if i in S else t)
    V={p(i,t) for i in range(8) for t in range(2)};E=set()
    for i in range(8):
        if i not in S:E.add((p(i,0),p(i,1)))
        E.update((p(i,1),p(j,0)) for j in U[i])
        for j in I[i]:
            if D[i]<=D[j] and chain(U[j]-U[i],U):E.add((p(i,0),p(j,0)))
            if U[j]<=U[i] and chain(D[i]-D[j],U):E.add((p(i,1),p(j,1)))
    indeg=Counter(b for a,b in E);q=deque(v for v in V if indeg[v]==0);seen=0
    while q:
        a=q.popleft();seen+=1
        for u,v in E:
            if u==a:
                indeg[v]-=1
                if indeg[v]==0:q.append(v)
    return seen!=len(V),E

def explicit_extensions(up,w):
    # Enumerate every labelled extension outright, not a counting DP.
    V=[(i,r) for i in range(8) for r in range(w[i])]
    P=[{k for k,(j,s) in enumerate(V) if (j==i and s<r) or up[j]>>i&1} for i,r in V]
    pairs=list(combinations(range(len(V)),2));counts=[0]*len(pairs);total=0
    def visit(word,remaining,placed):
        nonlocal total
        if not remaining:
            total+=1;rank={v:k for k,v in enumerate(word)}
            for z,(a,b) in enumerate(pairs):counts[z]+=int(rank[a]<rank[b])
            return
        for v in sorted(remaining):
            if P[v]<=placed:visit(word+[v],remaining-{v},placed|{v})
    visit([],set(range(len(V))),set())
    M=[[0]*len(V) for _ in V]
    for (a,b),n in zip(pairs,counts):M[a][b]=n;M[b][a]=total-n
    return V,total,M

def occupancy_count(up,w,edge=None):
    # Second independent representation; impose the selected actual-element
    # precedence by withholding its second member, without altering core order.
    D=[tuple(j for j in range(8) if up[j]>>i&1) for i in range(8)];w=tuple(w)
    @lru_cache(None)
    def f(s):
        if s==w:return 1
        out=0
        for i in range(8):
            if s[i]==w[i] or any(s[j]!=w[j] for j in D[i]):continue
            if edge and (i,s[i])==edge[1] and s[edge[0][0]]<=edge[0][1]:continue
            t=list(s);t[i]+=1;out+=f(tuple(t))
        return out
    return f((0,)*8)

def main():
    require(digest('inputs/author/THEOREM.md')=='899a5bacb83ea3403f69f39dbd37bc8e4f7d9d152eeee8afd4f87015df7b0e78','Theorem pin')
    require(digest('inputs/author/certificate.json')=='aa6c75a0aba79e62602dda5167b571a7ea100a6fa74d8686faa8595c76eaa288','Certificate pin')
    c=read('inputs/author/certificate.json');up=c['strict_up_masks'];require(c['class_id']=='C13','Class label')
    # Check copied prior inputs against the earlier independently frozen manifest.
    pm=read('inputs/prior/MANIFEST.json')['files']
    for rel in ['AUDIT.md','PROVENANCE.json','inputs/input_cores.json','inputs/frozen_singleton_constraints.json','inputs/weight_filter_catalogue.json','inputs/original_orbit_audit.json']:
        require(digest('inputs/prior/'+rel)==pm[rel]['sha256'],'Prior source pin '+rel)
    originals=read('inputs/prior/inputs/frozen_singleton_constraints.json')
    inputs=read('inputs/prior/inputs/input_cores.json')
    frozen=next(q for q in originals if q['class_id']=='C13')
    require(next(q for q in inputs if q['class_id']=='C13')==frozen,'Exact original class record')
    q=next(q for q in read('inputs/prior/inputs/weight_filter_catalogue.json')['cores'] if q['class_id']=='C13')
    require(up==frozen['strict_up_masks']==q['strict_up_masks'],'Frozen core identity')
    orbit=read('inputs/prior/inputs/original_orbit_audit.json')['classes']
    matches=[r for r in orbit if r['n']==8 and r['representative_masks']==up]
    require(len(matches)==1,'Exact orbit representative membership')
    U,D,I=structure(up)
    covers=[[i,j] for i in range(8) for j in sorted(U[i]) if not any(j in U[k] for k in U[i])]
    require(covers==c['cover_edges']==frozen['cover_edges']==q['cover_edges'],'Transitive reduction / covers')
    rules=[]
    for i in range(8):
        low=[j for j in sorted(I[i]) if D[i]==D[j] and chain(U[i]-U[j],U)]
        high=[j for j in sorted(I[i]) if U[i]==U[j] and chain(D[i]-D[j],U)]
        if low or high:rules.append(dict(target=i,incomparable_indices=sorted(I[i]),bottom_witnesses=low,top_witnesses=high,coefficients=[2 if k==i else -int(k in I[i]) for k in range(8)],integer_rhs=-1))
    require(rules==q['rules'],'Every independently reconstructed inequality')
    F=set(c['forced_set']);require(F=={0,3}==set(q['port_forced_nonsingleton_indices']),'Forced set identity')
    cyclic=0
    for bits in range(256):
        S={i for i in range(8) if bits>>i&1};bad,E=port_graph(U,D,I,S)
        require(bad==bool(S&F),'Exact port condition for singleton set '+str(S));cyclic+=bad
    for cert in frozen['minimal_forbidden_singleton_subsets']:
        S=set(cert['singleton_vertices']);bad,E=port_graph(U,D,I,S)
        def coalesce(x):return (x//2,0 if x//2 in S else x%2)
        path=list(map(coalesce,cert['cycle_representative_ports']))
        require(path[0]==path[-1] and all((a,b) in E for a,b in zip(path,path[1:])),'Original cycle certificate')
    # Independently verify all 64 relevant singleton sections, not only minimal clauses.
    rows=[r['coefficients'] for r in rules];base=[2 if i in F else 1 for i in range(8)]
    sections=q['all_sections'];available=sorted(set(range(8))-F)
    expected={tuple(available[j] for j in range(6) if bits>>j&1) for bits in range(64)}
    require(len(sections)==64 and {tuple(s['singleton_indices']) for s in sections}==expected,'Complete section coverage')
    infeasible=[]
    for sec in sections:
        S=set(sec['singleton_indices']);free=sorted(set(range(8))-S)
        require(sec['lower_weights']==base and sec['free_indices']==free,'Section variable coordinates')
        if sec['status']=='feasible_integer_witness':
            w=sec['weights'];require(len(w)==8 and all(type(t) is int for t in w),'Integer witness')
            require(all(w[i]>=base[i] and (i not in S or w[i]==1) for i in range(8)),'Witness domain')
            require(all(sum(a*b for a,b in zip(row,w))<=-1 for row in rows),'Witness inequalities')
        else:
            require(sec['status']=='infeasible_real_relaxation','Section status')
            cert=sec['certificate'];y=cert['row_multipliers']
            require(len(y)==len(rows) and all(type(t) is int and t>=0 for t in y),'Nonnegative exact multipliers')
            coeff=[sum(t*r[i] for t,r in zip(y,rows)) for i in free]
            rhs=sum(t*(-1-sum(a*b for a,b in zip(r,base))) for t,r in zip(y,rows))
            require(all(a>=0 for a in coeff) and rhs<0,'Farkas contradiction')
            require(coeff==cert['combined_free_coefficients'] and rhs==cert['combined_rhs'],'Stored section arithmetic')
            infeasible.append(sec)
    minimal=[s for s in infeasible if not any(set(t['singleton_indices'])<set(s['singleton_indices']) for t in infeasible)]
    clauses=[s['singleton_indices'] for s in minimal]
    require(minimal==q['minimal_additional_forbidden_singleton_sets'],'Minimality of clauses')
    require(clauses==c['additional_nonsingleton_clauses']==[[1,2,4,6],[4,5,6,7]],'Clause identity')
    allowed=[];all_supports=[]
    for k in range(4):
        for tup in combinations(range(8),k):
            S=set(tup);passes=F<=S and all(S&set(C) for C in clauses)
            all_supports.append({'support':list(tup),'passes_ports_and_clauses':passes})
            if passes:allowed.append(list(tup))
    require(len(all_supports)==93 and allowed==[[0,3,4],[0,3,6]],'Exhaustive supports of size <=3')
    require([case['support'] for case in c['cases']]==allowed,'No missing / duplicate author case')
    counts=[]
    for case in c['cases']:
        S=case['support'];chosen=[next(r for r in rules if r['target']==i) for i in S]
        A=[[r['coefficients'][i] for i in S] for r in chosen]
        b=[-1-sum(a for i,a in enumerate(r['coefficients']) if i not in S) for r in chosen]
        require(A==case['matrix'] and b==case['rhs'],'Matrix and strict RHS derived from full inequalities')
        H=[[Fraction(a,4) for a in row] for row in case['inverse_times_four']]
        require(all(a>=0 for row in H for a in row),'Nonnegative inverse')
        for i,j in product(range(3),repeat=2):
            require(sum(H[i][k]*A[k][j] for k in range(3))==int(i==j),'Left inverse')
            require(sum(A[i][k]*H[k][j] for k in range(3))==int(i==j),'Right inverse')
        upper=[sum(H[i][k]*b[k] for k in range(3)) for i in range(3)]
        require(upper==[Fraction(5,2),Fraction(5,2),Fraction(3,1)],'Rational bound')
        bounds=[a.numerator//a.denominator for a in upper];require(bounds==case['integer_upper_bounds'],'Floored integer bound')
        feasible=[list(x) for x in product(*(range(2,t+1) for t in bounds)) if all(sum(a*b for a,b in zip(r,x))<=rhs for r,rhs in zip(A,b))]
        require(feasible==[[2,2,2]],'Whole finite box exhausted')
        w=[2 if i in S else 1 for i in range(8)];require(w==case['weights'],'Only surviving inflation')
        V,Z,M=explicit_extensions(up,w);require(Z==occupancy_count(up,w)==case['denominator'],'Independent total')
        pa,pb=map(tuple,case['pair']);ia=V.index(pa);ib=V.index(pb)
        require(pb[0] in I[pa[0]],'Pair incomparability')
        require(M[ia][ib]==case['numerator'] and Z<=3*M[ia][ib]<=2*Z,'Actual balanced certificate')
        # Recount every ordered orientation by independently imposing precedence.
        for ia0,ib0 in combinations(range(len(V)),2):
            N=occupancy_count(up,w,(V[ia0],V[ib0]));R=occupancy_count(up,w,(V[ib0],V[ia0]))
            require(N==M[ia0][ib0] and R==M[ib0][ia0] and N+R==Z,'All-pair cross-check')
        counts.append(dict(support=S,weights=w,matrix=A,rhs=b,rational_upper=[[a.numerator,a.denominator] for a in upper],integer_upper=bounds,feasible_triples=feasible,vertices=V,extension_count=Z,pair=case['pair'],numerator=M[ia][ib],reverse_numerator=M[ib][ia],all_pair_numerators=M))
    out=dict(verdict='PASS',scope='Every positive-integer C13 chain inflation with at most three nonsingleton chains has a balanced pair',core_up=up,core_cover_edges=covers,independent_rules=rules,port_patterns=256,cyclic_port_patterns=cyclic,singleton_sections=64,infeasible_sections=len(infeasible),minimal_clauses=clauses,supports_tested=93,allowed_supports=allowed,support_ledger=all_supports,counts=counts,all_unordered_pairs_recounted=110,independent_precedence_counts=220)
    (ROOT/'audit_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: C13 all-weight <=3-support exclusion; 93 supports, 64 sections, 256 port patterns, 2 exhaustive extension lists, 220 independent precedence counts.')
    for case in counts:print('support',case['support'],'total',case['extension_count'],'forward',case['numerator'],'reverse',case['reverse_numerator'])

if __name__=='__main__':main()
