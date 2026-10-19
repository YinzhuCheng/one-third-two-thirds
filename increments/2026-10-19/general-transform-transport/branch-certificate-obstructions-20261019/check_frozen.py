from fractions import Fraction
from itertools import permutations
import json

def check(names, edges):
    n=len(names); idx={v:i for i,v in enumerate(names)}
    rel={(idx[a],idx[b]) for a,b in edges}
    changed=True
    while changed:
        old=len(rel)
        rel|={(a,d) for a,b in rel for c,d in rel if b==c}
        changed=len(rel)!=old
    assert all(a!=b for a,b in rel)
    le=[]
    for perm in permutations(range(n)):
        at=[0]*n
        for i,a in enumerate(perm):at[a]=i
        if all(at[a]<at[b] for a,b in rel):le.append(at)
    x,y=idx['x'],idx['y']
    branches={'+':[at for at in le if at[x]<at[y]],'-':[at for at in le if at[y]<at[x]]}
    def probs(arr):return {(a,b):Fraction(sum(at[a]<at[b] for at in arr),len(arr)) for a in range(n) for b in range(a+1,n)}
    qp=probs(le); qs={k:probs(arr) for k,arr in branches.items()}
    def get(q,a,b):return q[a,b] if a<b else 1-q[b,a]
    def bal(q,a,b):return Fraction(1,3)<=get(q,a,b)<=Fraction(2,3)
    menus={}
    for typ,br,v in [('A','+',x),('B','-',x),('C','+',y),('D','-',y)]:
        menus[typ]=[a for a in range(n) if a not in (x,y) and bal(qs[br],v,a)]
    rects={}
    for l,r in [('B','A'),('C','D'),('B','D')]:
        rects[l+r]=[(names[a],names[b]) for a in menus[l] for b in menus[r] if a==b or (a,b) in rel]
    graph=set(rel)|{(y,x)}
    graph|={(a,x) for a in menus['A']}|{(x,b) for b in menus['B']}|{(y,c) for c in menus['C']}|{(d,y) for d in menus['D']}
    reach=set(graph)
    changed=True
    while changed:
        old=len(reach);reach|={(a,d) for a,b in reach for c,d in reach if b==c};changed=len(reach)!=old
    cyclic=any(a==b for a,b in reach)
    assert cyclic==any(rects.values())
    down=lambda S:{a for a in range(n) if any(a==b or (a,b) in rel for b in S)}
    I=down(set(menus['D'])|{y})
    J=I|down(set(menus['A'])|{x})
    sep=(x not in I and not (set(menus['C'])&I) and not (set(menus['B'])&J))
    assert sep==not_cyclic(cyclic)
    return dict(n=n,eP=len(le),p=str(Fraction(len(branches['+']),len(le))),menus={k:[names[a] for a in arr] for k,arr in menus.items()},rectangles=rects,cyclic=cyclic,canonical_ideals={'I':[names[a] for a in sorted(I)],'J':[names[a] for a in sorted(J)]},branch_balanced={k:[(names[a],names[b],str(q)) for (a,b),q in val.items() if Fraction(1,3)<=q<=Fraction(2,3)] for k,val in qs.items()},parent_balanced=[(names[a],names[b],str(q)) for (a,b),q in qp.items() if Fraction(1,3)<=q<=Fraction(2,3)])
def not_cyclic(cyclic):return not cyclic

cases=[]
for m,k in [(3,2),(5,4)]:
    names=['x','y']+[f'z{i}' for i in range(1,m+1)]
    edges=[(f'z{i}',f'z{i+1}') for i in range(1,m)]+[(f'z{k}','x')]
    cases.append((names,edges))
cases.append((['x','y','z1','z2','z3'],[('z1','z2'),('z2','z3')]))
cases.append((['x','y','a2','a3','b1','b2','z'],[('y','a2'),('a2','a3'),('b1','b2'),('b2','x')]))
out=[check(*case) for case in cases]
print(json.dumps(out,ensure_ascii=False,indent=2))
with open('/workspace/shared/branch-certificate-obstructions-20261019/verification.json','w') as f:json.dump(out,f,ensure_ascii=False,indent=2)
