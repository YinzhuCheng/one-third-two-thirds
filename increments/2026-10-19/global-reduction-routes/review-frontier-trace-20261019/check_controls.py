from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def les(labels, rel):
    labels=tuple(labels); S=frozenset(labels)
    pred={x:{u for u,v in rel if v==x}&S for x in labels}
    def rec(rem, word):
        if not rem:
            yield word; return
        for x in labels:
            if x in rem and not (pred[x]&rem):
                yield from rec(rem-{x},word+(x,))
    return list(rec(S,()))

def path(labels):
    return {(labels[i],labels[j]) for i in range(len(labels)) for j in range(i+2,len(labels))}

def chain(labels):
    return {(labels[i],labels[j]) for i in range(len(labels)) for j in range(i+1,len(labels))}

def ordinal(parts):
    labels=[]; rel=set()
    for ls,rs in parts:
        rel |= rs
        rel |= {(x,y) for x in labels for y in ls}
        labels+=list(ls)
    return labels,rel

def incomparability_degree(labels,rel):
    return max((sum(y!=x and (x,y) not in rel and (y,x) not in rel for y in labels) for x in labels),default=0)

def interface(U,L,K,R,V,rel,D,marked=()):
    labels=U+L+K+R+V; allset=set(labels)
    pred={x:{u for u,v in rel if v==x} for x in labels}
    def ideal(S): return all(pred[x]<=S for x in S)
    H=Counter()
    trace_set=set(L+R+list(marked))
    for ss in combinations(L,D):
        s=set(ss); I=set(U)|s
        if not ideal(I): continue
        for tt in combinations(R,D):
            t=set(tt); J=set(U+L+K)|t
            if not ideal(J): continue
            for w in les([x for x in labels if x in J-I],rel):
                trace=tuple(x for x in w if x in trace_set)
                H[(tuple(sorted(s)),tuple(sorted(t)),trace)]+=1
    return H

def ratio(H,G):
    cs=[]
    for k in set(H)|set(G):
        if not H[k] or not G[k]: return None
        cs.append(Fraction(H[k],G[k]))
    return cs[0] if cs and len(set(cs))==1 else None

def marginalize(H,keep):
    out=Counter()
    for (s,t,tau),c in H.items():
        out[(s,t,tuple(x for x in tau if x in keep))]+=c
    return out

out={}
# Control 1: nonautonomous path block, with both remote U,V present.
D=2; U=['u'];L=['l0','l1','l2','l3'];K=['k0','k1'];R=['r0','r1','r2','r3'];V=['v']
labels=U+L+K+R+V; rel=path(labels); E=U+L+R+V
words=les(labels,rel); external=les(E,rel)
H=interface(U,L,K,R,V,rel,D)
fib=Counter(tuple(x for x in w if x not in K) for w in words)
for eta in external:
    pre=eta[:len(U)+D]; tau=eta[len(U)+D:len(U)+3*D]
    s=set(pre)-set(U); t=set(tau)&set(R)
    shape=(set(U)<=set(pre) and s<=set(L) and len(s)==D and len(t)==D and set(tau)==(set(L)-s)|t)
    prediction=H[(tuple(sorted(s)),tuple(sorted(t)),tau)] if shape else 0
    assert prediction==fib[eta],(eta,prediction,fib[eta])
assert len(words)==233 and len(external)==64
assert incomparability_degree(labels,rel)==2
assert len(set(fib.values()))>1
# Remote points can permute with boundary ports, but only in the prefix/suffix.
assert any(w.index('l0')<w.index('u') for w in words)
assert any(w.index('v')<w.index('r3') for w in words)
out['nonautonomous_fiber_factorization']={'n':len(labels),'extensions':len(words),'external_extensions':len(external),'fiber_sizes':sorted(set(fib.values())),'all_external_fibers_equal_H':True,'remote_U_V_permute_with_boundary_ports':True}

# Control 2: nontrivial exterior, different core sizes, full marked law proportional.
left=U+L;right=R+V;K=['m','z']
labels,rel=ordinal([(left,path(left)),(K,set()),(right,path(right))])
labels2=[x for x in labels if x!='z']; rel2={(x,y) for x,y in rel if x!='z' and y!='z'}
H=interface(U,L,K,R,V,rel,D,marked=['m'])
G=interface(U,L,['m'],R,V,rel2,D,marked=['m'])
assert ratio(H,G)==2
words=les(labels,rel); words2=les(labels2,rel2)
fib=Counter(tuple(x for x in w if x!='z') for w in words)
assert len(words)==128 and len(words2)==64 and set(fib.values())=={2} and set(fib)==set(words2)
assert incomparability_degree(labels,rel)<=2
out['different_sizes_joint_marked_positive']={'sizes':[len(labels),len(labels2)],'extensions':[len(words),len(words2)],'common_ratio':'2','retained_full_law_support':len(words2),'each_fiber':2}

# Control 3: individual marked marginals, even with one common ratio, do not suffice.
U=[];V=[];L=['l0','l1','l2','l3'];R=['r0','r1','r2','r3'];K=['a','b','c']
labels,rel=ordinal([(L,chain(L)),(K,{('a','c')}),(R,chain(R))])
M=['a','b']; labels2=[x for x in labels if x!='c']; rel2={(x,y) for x,y in rel if x!='c' and y!='c'}
H=interface(U,L,K,R,V,rel,D,marked=M); G=interface(U,L,M,R,V,rel2,D,marked=M)
B=set(L+R)
assert ratio(marginalize(H,B|{'a'}),marginalize(G,B|{'a'}))==Fraction(3,2)
assert ratio(marginalize(H,B|{'b'}),marginalize(G,B|{'b'}))==Fraction(3,2)
assert ratio(H,G) is None
words=les(labels,rel);words2=les(labels2,rel2)
p=Fraction(sum(w.index('a')<w.index('b') for w in words),len(words))
q=Fraction(sum(w.index('a')<w.index('b') for w in words2),len(words2))
assert p==Fraction(2,3) and q==Fraction(1,2)
assert incomparability_degree(labels,rel)==2
out['single_marker_marginals_counterexample']={'sizes':[len(labels),len(labels2)],'extensions':[len(words),len(words2)],'common_single_marker_ratio':'3/2','joint_projective_equal':False,'P_a_before_b':str(p),'Pprime_a_before_b':str(q),'core_relations':['a<c'],'retained':['a','b']}
(HERE/'controls.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
