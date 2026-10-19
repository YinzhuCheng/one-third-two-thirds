from fractions import Fraction as F
from itertools import permutations
import json

def le(n,edges):
    return [p for p in permutations(range(n)) if all(p.index(x)<p.index(y) for x,y in edges)]
def moments(rows,S,T):
    pairs=[(min(p.index(x) for x in S), min(p.index(x) for x in T)) for p in rows]
    av=lambda vals: sum(vals,F(0))/len(pairs)
    r=av(x for x,y in pairs);s=av(y for x,y in pairs)
    prod=av(x*y for x,y in pairs); mn=av(min(x,y) for x,y in pairs)
    return r,s,prod,mn,prod-r*s

def check(a,b,wedges,vedges,Sz):
    edges=wedges+[(a+x,a+y) for x,y in vedges]
    rows=le(a+b,edges); vrows=le(b,vedges)
    h=sum((F(min(p.index(x) for x in Sz)) for p in vrows),F(0))/len(vrows)
    r,s,prod,mn,cov=moments(rows,set(range(a,a+b)),set(a+x for x in Sz))
    expected_r=F(a,b+1)
    expected_s=h+F(a,b+1)*(h+1)
    expected_cov=F(a*(a+b+1), (b+1)**2*(b+2))*(b-h)
    gap=F(a*(a+b+1), (b+1)**2*(b+2))*(h+2)
    assert (r,s,cov,mn)==(expected_r,expected_s,expected_cov,r)
    assert r*s+r*r+2*r-(prod+mn)==gap==r*r+r-cov
    return {'a':a,'b':b,'W_edges':wedges,'V_edges':vedges,'Sz':sorted(Sz),'extensions':len(rows),'h':str(h),'r':str(r),'s':str(s),'cov':str(cov),'Tgap=Cgap':str(gap)}

cases=[
check(1,3,[],[(0,2),(1,2)],{2}),
check(2,3,[(0,1)],[(0,2),(1,2)],{2}),
check(2,4,[],[(0,2),(1,3)],{2,3}),
check(3,2,[(0,1),(1,2)],[],{0,1})]
print(json.dumps(cases,indent=2))
open('/workspace/shared/audit-slot-shortening-extensions-20261018/verification.json','w').write(json.dumps(cases,indent=2)+'\n')

def mixture(n,edges,A,B):
    rows=le(n,edges)
    r,s,prod,mn,cov=moments(rows,A,B)
    R=[min(p.index(x) for x in A) for p in rows]
    var=sum((F(x*x) for x in R),F(0))/len(R)-r*r
    groups=[]
    for i in sorted(A):
        group=[p for p in rows if min(A,key=p.index)==i]
        if not group: continue
        newrows=le(n,edges+[(i,j) for j in A if i!=j])
        assert set(group)==set(newrows)
        ri,si,pi,mi,ci=moments(group,A,B)
        ri2=sum((F(min(p.index(x) for x in A)**2) for p in group),F(0))/len(group)
        vi=ri2-ri*ri;eps=vi+ri-(pi+mi-ri*si)
        assert eps>=0
        groups.append((F(len(group),len(rows)),ri,si,vi,eps))
    delta=sum((w*ri*(si-ri) for w,ri,si,vi,eps in groups),F(0))-r*(s-r)
    epsbar=sum((w*eps for w,ri,si,vi,eps in groups),F(0))
    assert prod+mn-r*s==var+r+delta-epsbar
    return {'extensions':len(rows),'r':str(r),'s':str(s),'var':str(var),'N':str(prod+mn),'Delta':str(delta),'epsilon_bar':str(epsbar),'groups':[[str(x) for x in g] for g in groups]}

mixtures=[mixture(6,[(0,1),(2,3),(3,4)],{1,5},{4,5}),mixture(7,[(0,1),(2,3),(4,5),(5,6)],{1,3},{1,6})]
assert mixtures[0]['Delta']=='161/720' and mixtures[0]['epsilon_bar']=='63/80'
assert mixtures[0]['r']=='23/12' and mixtures[0]['s']=='43/20' and mixtures[0]['N']=='427/60'
assert mixtures[1]['Delta']=='0' and mixtures[1]['r']=='49/15' and mixtures[1]['s']=='11/3'
open('/workspace/shared/audit-slot-shortening-extensions-20261018/verification.json','w').write(json.dumps({'independent_block_cases':cases,'mixture_cases':mixtures},indent=2)+'\n')
print('Mixture exact controls:',json.dumps(mixtures,indent=2))
