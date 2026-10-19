"""Fixed exact checks for winner-mixture identities; no poset search."""
from itertools import permutations
from fractions import Fraction as F
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent

def mean(xs):
    return sum(xs,F(0))/len(xs)

def covariance(p,x,y):
    return sum((q*a*b for q,a,b in zip(p,x,y)),F(0))-sum((q*a for q,a in zip(p,x)),F(0))*sum((q*b for q,b in zip(p,y)),F(0))

def closure(names,edges):
    rel=set(edges)
    while True:
        old=len(rel)
        rel|={(a,d) for a,b in rel for c,d in rel if b==c}
        if old==len(rel):break
    assert all(a!=b for a,b in rel)
    return rel

def run(name,names,edges,A,B,keep_rows=False):
    rel=closure(names,edges)
    assert all(v in A for u,v in rel if u in A)
    assert all(v in B for u,v in rel if u in B)
    C=[a for a in names if a in A and not any(b in A and (b,a) in rel for b in names)]
    ex=[seq for seq in permutations(names) if all(seq.index(a)<seq.index(b) for a,b in rel)]
    rows=[]
    for seq in ex:
        at={a:i for i,a in enumerate(seq)}
        winner=min(C,key=lambda a:at[a]);R=min(at[a] for a in A);T=min(at[b] for b in B)
        assert R==at[winner]
        rows.append(dict(extension=''.join(seq),winner=winner,R=R,T=T))
    groups=[]
    for winner in C:
        group=[row for row in rows if row['winner']==winner]
        assert group
        new_rel=closure(names,edges+[(winner,c) for c in C if c!=winner])
        cond_ex=[seq for seq in permutations(names) if all(seq.index(a)<seq.index(b) for a,b in new_rel)]
        assert set(cond_ex)=={tuple(row['extension']) for row in group}
        assert {winner}|{v for u,v in new_rel if u==winner}==set(A)
        ri=mean([F(q['R']) for q in group]);si=mean([F(q['T']) for q in group])
        vi=mean([F(q['R']**2) for q in group])-ri*ri
        Ni=mean([F(q['R']*q['T']+min(q['R'],q['T'])) for q in group])
        epsilon=vi+ri-(Ni-ri*si)
        eta=ri*(ri+1)-vi
        assert epsilon>=0 and eta>=0
        groups.append(dict(winner=winner,count=len(group),p=F(len(group),len(rows)),r=ri,s=si,d=si-ri,var_R=vi,N=Ni,epsilon=epsilon,eta=eta))
    r=mean([F(q['R']) for q in rows]);s=mean([F(q['T']) for q in rows])
    var=mean([F(q['R']**2) for q in rows])-r*r
    N=mean([F(q['R']*q['T']+min(q['R'],q['T'])) for q in rows])
    p=[q['p'] for q in groups];ris=[q['r'] for q in groups];ds=[q['d'] for q in groups]
    delta=covariance(p,ris,ds);epsbar=sum((q['p']*q['epsilon'] for q in groups),F(0))
    marginal_slack=r*(r+1)-var
    identity_rhs=var+r+delta-epsbar
    assert N-r*s==identity_rhs
    assert marginal_slack>=0
    D=len(names)+1
    # Continuous exact conversion, including the n+1/n+2 correction.
    a=(r+1)/D;b=(s+1)/D
    EW2=mean([F((q['R']+1)*(q['R']+2),D*(D+1)) for q in rows])
    EWV=mean([F(q['R']*q['T']+min(q['R'],q['T'])+q['R']+q['T']+2,D*(D+1)) for q in rows])
    h=EW2-a*a-(EWV-a*b)-a*(b-a)/(D+1)
    assert D*(D+1)*h==epsbar-delta
    return dict(name=name,n=len(names),edges=edges,A=A,B=B,min_A=C,extension_count=len(rows),groups=groups,r=r,s=s,var_R=var,N=N,delta=delta,epsilon_bar=epsbar,marginal_slack=marginal_slack,one_sided_target_slack=r*r+2*r-(N-r*s),target_slack=r*s+min(r*r+2*r,s*s+2*s)-N,continuous_h=h,rows=rows if keep_rows else None)

results=[]
for m in (1,2,3):
    chain=[chr(ord('c')+j) for j in range(m)]
    names=['a','b','x']+chain
    edges=[('a','b')]+list(zip(chain,chain[1:]))
    result=run(f'C2 plus C{m} plus isolated x',names,edges,['b','x'],['x',chain[-1]],keep_rows=(m==3))
    gs={q['winner']:q for q in result['groups']}
    assert gs['b']['p']==F(1,3) and gs['x']['p']==F(2,3)
    assert gs['b']['r']==F(m+2,2)
    assert gs['x']['r']==F(3*m+4,8)
    assert gs['b']['s']==F(3*m+8,4)-F(3,m+1)
    assert gs['x']['s']==F(3*m+4,8)-F(3,(m+1)*(m+2))
    assert result['delta']==F((m+4)*(m*m+6*m-4),144*(m+2))
    assert result['r']==F(5*m+8,12)
    assert result['s']==F(m+2,2)-F(m+4,(m+1)*(m+2))
    results.append(result)

symmetric=run('C2 plus C2 plus C3; B is not A-symmetry invariant',list('abcdefg'),[('a','b'),('c','d'),('e','f'),('f','g')],['b','d'],['b','g'])
assert symmetric['groups'][0]['r']==symmetric['groups'][1]['r']
assert symmetric['delta']==0
assert symmetric['r']<symmetric['s']
results.append(symmetric)

def serialize(x):
    if isinstance(x,F):return str(x)
    raise TypeError(type(x))
(OUT/'verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2,default=serialize)+'\n')
for q in results:
    print(q['name'], 'LE=',q['extension_count'],'r=',q['r'],'s=',q['s'],'Delta=',q['delta'],'T slack=',q['target_slack'])
    print('  groups:',[{k:str(v) for k,v in row.items()} for row in q['groups']])
print('All conditional-poset identities, continuous/discrete identities, and fixed-example checks passed.')
