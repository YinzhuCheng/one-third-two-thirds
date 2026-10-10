#!/usr/bin/env python3
"""Independent exact audit. Does not import the author's checking programs."""
import collections, itertools, json, math
from pathlib import Path
import sympy as S
BASE=Path(__file__).resolve().parent
pred=(0,0,3,3,1,2,23,43); u,y=2,3; n=len(pred); m=n-2

def linear_extensions(pred):
    def gen(done,seq):
        if len(seq)==len(pred):
            yield seq
        else:
            for v,ps in enumerate(pred):
                if not done>>v&1 and ps&~done==0:
                    yield from gen(done|1<<v,seq+(v,))
    return list(gen(0,()))

def is_extension(seq,pred):
    pos={v:i for i,v in enumerate(seq)}
    return all(pos[w]<pos[v] for v,ps in enumerate(pred) for w in range(len(pred)) if ps>>w&1)

assert pred[u]==pred[y] and not (pred[u]>>y&1 or pred[y]>>u&1)
D={v for v in range(n) if pred[u]>>v&1}
U={v for v in range(n) if pred[v]>>u&1}
V={v for v in range(n) if pred[v]>>y&1}
remain=tuple(v for v in range(n) if v not in (u,y))
delete=tuple(sum(1<<i for i,w in enumerate(remain) if pred[v]>>w&1) for v in remain)
C=collections.Counter()
for ee in linear_extensions(delete):
    e=tuple(remain[v] for v in ee); ranks={v:i+1 for i,v in enumerate(e)}
    a=max([ranks[v] for v in D],default=0)
    b=min([ranks[v] for v in U],default=m+1)
    c=min([ranks[v] for v in V],default=m+1)
    assert a<b and a<c
    C[b-a,c-a]+=1
s,t=S.symbols('s t',real=True)

def kernel(p,q):
    # On s<=t. Distinct order-statistic ranks p<q, otherwise only q matters.
    if p>=q:
        return sum(S.binomial(m,k)*t**k*(1-t)**(m-k) for k in range(q))
    return sum(S.factorial(m)/(S.factorial(a)*S.factorial(b)*S.factorial(m-a-b)) * s**a*(t-s)**b*(1-t)**(m-a-b)
               for a in range(p) for b in range(q-a) if a+b<=m)
f=S.factor(sum(v*kernel(p,q) for (p,q),v in C.items())/S.factorial(m))
l=S.symbols('l',real=True); x=1-l
ks=(x*x-s*s)/2;kt=(x*x-t*t)/2
direct=S.integrate(2*l*ks*kt+l*l/2*(ks*(x-t)+kt*(x-s)),(l,0,1-t))
assert S.expand(f-direct)==0
assert C==collections.Counter({(1,3):1,(2,3):2,(2,4):2,(3,1):1,(3,2):2,(3,4):4,(4,2):2,(4,3):4})
assert all(C[p,q]==C[q,p] for p,q in C)
e=S.Rational(1,100); d=S.Rational(1,10000)
evaluate=lambda a,b:f.subs({s:min(a,b),t:max(a,b)})
boundary=[evaluate(0,0),evaluate(0,e),evaluate(e,0),evaluate(e,e)]
minor=lambda a:a[0]*a[3]-a[1]*a[2]
interior=[evaluate(d,d),evaluate(d,e),evaluate(e,d),evaluate(e,e)]
assert minor(boundary)<0 and minor(interior)<0
full=linear_extensions(pred); counts=collections.Counter()
for ext in full:
    posu=ext.index(u);posy=ext.index(y); swapped=list(ext);swapped[posu],swapped[posy]=swapped[posy],swapped[posu]
    counts[('forward' if posu<posy else 'reverse')+('_legal' if is_extension(swapped,pred) else '_illegal')]+=1
assert counts=={'forward_legal':74,'reverse_legal':74,'forward_illegal':26,'reverse_illegal':26}
F=S.integrate(S.integrate(f,(s,0,t)),(t,0,1));G=F
H=S.integrate(t*f.subs(s,t),(t,0,1));E=F+G
assert [v*S.factorial(n) for v in (E,F,G,H)]==[200,100,100,74]
origin={name:str(expr.subs({s:0,t:0})) for name,expr in [('f',f),('f_s',S.diff(f,s)),('f_t',S.diff(f,t)),('f_st',S.diff(f,s,t))]}
result={'status':'PASS','source_poset_predecessors':pred,'pair':[u,y],'D':sorted(D),'U':sorted(U),'V':sorted(V),'deletion_labels':remain,'deletion_predecessors':delete,'deletion_extension_count':sum(C.values()),'rank_histogram':[[p,q,k] for (p,q),k in sorted(C.items())], 'f_on_s_le_t':str(f),'independent_direct_integral_matches':True,'origin_derivatives':origin,'boundary_rectangle':['0','1/100'],'boundary_fiber_values':list(map(str,boundary)),'boundary_minor':str(S.factor(minor(boundary))),'strictly_interior_rectangle':['1/10000','1/100'],'interior_fiber_values':list(map(str,interior)),'interior_minor':str(S.factor(minor(interior))),'full_extension_count':len(full),'full_extension_swap_counts':dict(counts),'integrals':dict(zip(['E','F','G','H'],map(str,[E,F,G,H]))),'integrals_times_n_factorial':[200,100,100,74],'ordinary_square_slack':74**2-26**2,'dimension_sharp_slack':7*200*74-8*100*100}
(BASE/'actual_fiber_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
