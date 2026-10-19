from fractions import Fraction as F
from functools import lru_cache
from math import comb
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def compute(name, labels, edges, allowed):
    labels=tuple(labels); n=len(labels); ix={v:i for i,v in enumerate(labels)}
    pred=[0]*n
    for a,b in edges: pred[ix[b]]|=1<<ix[a]
    change=True
    while change:
        change=False
        for x in range(n):
            old=pred[x]
            for y in range(n):
                if pred[x]>>y&1: pred[x]|=pred[y]
            change |= old!=pred[x]
    assert all(not(pred[x]>>x&1) for x in range(n))
    mask=sum(1<<ix[x] for x in allowed); full=(1<<n)-1
    @lru_cache(None)
    def suffix(s):
        if s==full:return 1
        return sum(suffix(s|1<<x) for x in range(n) if not(s>>x&1) and pred[x]&s==pred[x])
    pref={0:1}
    qcount=[0]*(n+1); qcount[0]=suffix(0)
    for k in range(n):
        nxt={}
        for s,c in pref.items():
            for x in range(n):
                if not(s>>x&1) and pred[x]&s==pred[x]:
                    ns=s|1<<x
                    if not(ns&~mask):nxt[ns]=nxt.get(ns,0)+c
        pref=nxt
        qcount[k+1]=sum(c*suffix(s) for s,c in pref.items())
    e=suffix(0);q=[F(c,e) for c in qcount]
    pmf=[q[k]-(q[k+1] if k<n else 0) for k in range(n+1)]
    M=[sum(pmf[k]*comb(k,r) for k in range(r,n+1)) for r in range(n+1)]
    assert all(q[k]**2>=q[k-1]*q[k+1] for k in range(1,n))
    assert all(M[r]**2>=M[r-1]*M[r+1] for r in range(1,n))
    return dict(name=name,n=n,e=e,q=q,M=M,labels=labels,edges=edges,allowed=sorted(allowed))

controls=[]
def add(*args):
    z=compute(*args);controls.append(z);return z

# 11 explicitly named actual-poset controls; no family search.
q2=add('antichain2_internal', ['a','b'],[],{'a'})
s2=add('autonomous_successor_shell2', ['s1','s2','z','w'],[('s1','s2'),('s2','z')],{'s1','s2'})
g2=add('autonomous_gluing2', ['a','b','z','w'],[('a','z'),('b','z')],{'a'})
q4=add('two_chains2_internal',list('abcd'),[('a','b'),('c','d')],{'a','c'})
s4=add('autonomous_successor_shell4',['s1','s2','s3','s4','z','w'],[('s1','s2'),('s2','s3'),('s3','s4'),('s4','z')],{'s1','s2','s3','s4'})
g4=add('autonomous_gluing4',list('abcdzw'),[('a','b'),('c','d')]+[(x,'z') for x in 'abcd'],{'a','c'})
bad=add('nonautonomous_three_point',list('abz'),[('a','z')],{'a'})
high=add('two_chains3_high_moments',list('abcdef'),[('a','b'),('b','c'),('d','e'),('e','f')],set('abcde'))
nonideal=add('nonideal_allowed_subset',list('abc'),[('a','b')],{'b','c'})
refa=add('high_moment_refinement_a_before_d',list('abcdef'),[('a','b'),('b','c'),('d','e'),('e','f'),('a','d')],set('abcde'))
refd=add('high_moment_refinement_d_before_a',list('abcdef'),[('a','b'),('b','c'),('d','e'),('e','f'),('d','a')],set('abcde'))
for inner,shell,glob in [(q2,s2,g2),(q4,s4,g4)]:
    for i in range(len(glob['q'])):
        a=inner['q'][i] if i<len(inner['q']) else 0
        b=shell['q'][i] if i<len(shell['q']) else 0
        assert glob['q'][i]==a*b
assert q2['q'][1]==F(1,2) and bad['q'][1]==F(2,3)
assert g2['e']==8 and g2['q'][1]==F(3,8)
assert g4['e']==36 and g4['q'][1:3]==[F(5,6),F(4,9)]
# One explicitly formal distribution, proving new adjacent-moment constraints
# are stronger than all old individual geometric bounds. Not a poset model.
formal_pmf=[F(9,20),F(1,2),F(0),F(1,20)]
M=[sum(formal_pmf[k]*comb(k,r) for k in range(r,4)) for r in range(4)]
assert all(M[r]<=M[1]**r for r in range(4))
assert M[2]**2<M[1]*M[3]

# Actual disjoint refinement partition, with forced counting weights.
assert refa['e']==refd['e']==10 and high['e']==20
weights=[F(refa['e'],high['e']),F(refd['e'],high['e'])]
budgets={}
for key in ['q','M']:
    profiles=[refa[key],refd[key]]
    mix=high[key]
    assert all(mix[i]==sum(p*x[i] for p,x in zip(weights,profiles)) for i in range(len(mix)))
    records=[]
    for j in range(1,len(mix)-1):
        if mix[j-1]==0:continue
        terms=[]
        for p,x in zip(weights,profiles):
            if x[j-1]==0:continue
            nu=p*x[j-1]/mix[j-1]
            u=x[j]/x[j-1]
            v=x[j+1]/x[j] if x[j]>0 else 0
            terms.append((nu,u,v))
        mu=sum(nu*u for nu,u,v in terms)
        variance=sum(nu*(u-mu)**2 for nu,u,v in terms)
        curvature=sum(nu*u*(u-v) for nu,u,v in terms)
        normalized_gap=(mix[j]**2-mix[j-1]*mix[j+1])/mix[j-1]**2
        assert normalized_gap==curvature-variance>=0
        records.append(dict(j=j,variance=variance,curvature=curvature,normalized_gap=normalized_gap))
    budgets[key]=records
assert budgets['q'][2]==dict(j=3,variance=F(1,400),curvature=F(21,200),normalized_gap=F(41,400))

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x
out={'actual_control_count':len(controls),'actual_controls':controls,'actual_refinement_budgets':budgets,'formal_strength_separation':{'pmf':formal_pmf,'M':M},'all_assertions_passed':True}
(HERE/'controls.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(serial(out),indent=2))
