from itertools import permutations
from fractions import Fraction
from collections import Counter
import json

def les(n,edges):
    return [p for p in permutations(range(n)) if all(p.index(a)<p.index(b) for a,b in edges)]
def prob(ls,a,b):
    return Fraction(sum(p.index(a)<p.index(b) for p in ls),len(ls))
def tc(n,edges):
    r=set(edges)
    for k in range(n):
        r|={(a,b) for a in range(n) for b in range(n) if (a,k) in r and (k,b) in r}
    return r
def delta(n,edges):
    l=les(n,edges); r=tc(n,edges)
    vals=[(min(prob(l,a,b),1-prob(l,a,b)),a,b) for a in range(n) for b in range(a+1,n) if (a,b) not in r and (b,a) not in r]
    return (max(vals,default=(Fraction(0),None,None)),len(l))
# One targeted relation-edit control: A={0<1}, B={2}.
p=les(3,[(0,1)]); q=les(3,[(0,1),(0,2)])
# One module-replacement boundary control: two disjoint 2-chains,
# fixed label matching, external isolated y=4.
e=[(0,2),(1,3)]; f=[(0,3),(1,2)]
pe=les(5,e); pf=les(5,f)
# One partial-duality control: M={a,b,c,d}={0,1,2,3}; z=4,y=5.
g=[(4,0),(0,1),(1,2),(0,3)]
h=[(4,i) for i in range(4)]+[(2,1),(1,0),(3,0)]
pg=les(6,g); ph=les(6,h)
res={
 'relation_edit':{'eP':len(p),'eQ':len(q),'p_a2_before_b_before':str(prob(p,1,2)),'p_a2_before_b_after':str(prob(q,1,2)), 'delta_before':str(delta(3,[(0,1)])[0][0]),'delta_after':str(delta(3,[(0,1),(0,2)])[0][0])},
 'module_replacement':{'eP':len(pe),'eQ':len(pf),'boundary_before':[str(prob(pe,x,4)) for x in range(4)],'boundary_after':[str(prob(pf,x,4)) for x in range(4)],'internal_a_c_before':str(prob(pe,0,2)),'internal_a_c_after':str(prob(pf,0,2))},
 'partial_duality':{'eP':len(pg),'eQ':len(ph),'delta_before':str(delta(6,g)[0][0]),'delta_after':str(delta(6,h)[0][0]),'p_d_before_y_before':str(prob(pg,3,5)),'p_d_before_y_after':str(prob(ph,3,5)),'cross_before':[str(prob(pg,x,5)) for x in range(4)],'cross_after':[str(prob(ph,x,5)) for x in range(4)]}}
print(json.dumps(res,indent=2))
with open('/workspace/shared/audit-new-transform-routes-20261019/CONTROL.json','w') as out: json.dump(res,out,indent=2)
