#!/usr/bin/env python3
"""Independent exact audit: one fixed example, direct topological-word enumeration."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).parent
D=('a','d0','b','c'); U=('u','v'); I=('y','z')
base=[(a,b) for a in ('a','d0') for b in ('b','c')]
base += [(d,u) for d in D for u in U]
base += [('a','y'),('a','z'),('d0','z'),('b','z'),('y','v'),('z','u')]

def enumerate_words(nodes, edges):
    predecessors={x:set() for x in nodes}
    for a,b in edges: predecessors[b].add(a)
    result=[]
    def visit(prefix, seen):
        if len(prefix)==len(nodes):
            result.append(tuple(prefix)); return
        for x in nodes:
            if x not in seen and predecessors[x] <= seen:
                visit(prefix+[x], seen|{x})
    visit([],set())
    return result

records=[]
for m in (0,1,2):
    C=tuple('k'+str(i) for i in range(m))
    nodes=D+I+U+C
    edges=base+[(d,k) for d in D for k in C]+[(k,u) for k in C for u in U]+list(zip(C,C[1:]))
    words=enumerate_words(nodes,edges)
    event=sum(w.index('d0')<w.index('y') for w in words)
    t=m+1
    total_formula=8*(Q(t*t)+5*t+Q(13,4))
    failure_formula=8*(Q(t,2)+Q(1,2))
    assert len(words)==total_formula
    assert len(words)-event==failure_formula
    records.append({'m':m,'t':t,'direct_total':len(words),'direct_event':event,
                    'direct_failure':len(words)-event,'probability':str(Q(event,len(words)))})

t,p,r,q,s,beta,F,M,N=sp.symbols('t p r q s beta F M N')
B=p+r+q+s; A=M+N+p*s+r*q; T=t*t+(B+1)*t+A
G=sp.expand((beta*t+F)*sp.diff(T,t)-beta*T)
assert sp.simplify(G-(beta*t*t+2*F*t+F*(B+1)-beta*A))==0
low=sp.expand(G.subs(F,beta*(r+s)).subs({M:p*r+r,N:q*s+s*s+2*s}))
assert sp.simplify(low-beta*((t+r)**2+s*(2*t+2*r-1)))==0
fixed_p=1-(t+1)/(2*(t*t+5*t+sp.Rational(13,4)))
fixed_derivative=sp.factor(sp.diff(fixed_p,t))
assert sp.simplify(fixed_derivative - 2*(4*t*t+8*t+7)/(4*t*t+20*t+13)**2)==0
out={'method':'Direct topological-word recursion, distinct from producer ideal DP; one fixed object only.',
     'checks':records,'symbolic_identities':'PASS', 'fixed_derivative':str(fixed_derivative)}
(OUT/'exact_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
