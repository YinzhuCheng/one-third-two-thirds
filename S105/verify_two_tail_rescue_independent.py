#!/usr/bin/env python3
"""Independent diagnostics for the self-contained two-tail rescue proof.
Counts actual linear extensions from predecessor masks; no closed-form count is
used by the generic DP. Integer comparisons only, including strict endpoints.
The finite tests supplement, and do not replace, the proof in the audit.
"""
from pathlib import Path
from math import comb
from functools import lru_cache
from collections import Counter
import hashlib, json

HERE = Path(__file__).resolve().parent
DOCUMENT = HERE / 'two_tail_mc3_rescue.txt'


def poset(m, r, s):
    assert m >= 1 and r >= 1 and 1 <= s <= r
    labels = ['a', 'b'] + [f'c{i}' for i in range(1,m+1)] + ['y'] + [f'z{i}' for i in range(1,r+1)] + ['x']
    index = {v:i for i,v in enumerate(labels)}
    edges = []
    for chain in [['a','b']+[f'c{i}' for i in range(1,m+1)], ['y']+[f'z{i}' for i in range(1,r+1)]]:
        edges += list(zip(chain,chain[1:]))
    edges += [('a','z1'),('x',f'z{s}'),('x','c1')]
    pred = [0]*len(labels)
    for u,v in edges:
        pred[index[v]] |= 1 << index[u]
    # Closure is used only to independently verify the structural claims.
    closure=pred.copy()
    changed=True
    while changed:
        changed=False
        for v in range(len(labels)):
            extra=closure[v]
            for u in range(len(labels)):
                if closure[v] >> u & 1:
                    extra |= closure[u]
            if extra != closure[v]:
                closure[v]=extra; changed=True
    assert [labels[v] for v,p in enumerate(closure) if p==0] == ['a','y','x']
    assert closure[index['b']] == 1 << index['a']
    roots = (1 << index['x']) | (1 << index['y'])
    outside=[labels[v] for v,p in enumerate(closure) if not ((p | (1 << v)) & roots)]
    assert outside == ['a','b']
    return labels,index,pred


def count_extensions(pred):
    n=len(pred); full=(1<<n)-1
    @lru_cache(None)
    def visit(used):
        if used==full:
            return 1
        answer=0
        for v in range(n):
            bit=1<<v
            if not (used & bit) and not (pred[v] & ~used):
                answer += visit(used|bit)
        return answer
    return visit(0)


def actual_counts(m,r,s):
    labels,index,pred=poset(m,r,s)
    out={'E':count_extensions(tuple(pred))}
    for u,v,key in [('a','x','K_ax'),('a','y','K_ay'),('b','x','K_bx'),('b','y','K_by'),('x','y','K_xy')]:
        added=pred.copy(); added[index[v]] |= 1<<index[u]
        out[key]=count_extensions(tuple(added))
    return out


def claimed_counts(m,r,s):
    M=m+2; R=r+1; N=M+R
    U=[comb(N-1-j,M-1) for j in range(s+2)]
    V=[comb(N-2-j,M-2) for j in range(s+1)]
    assert all(v>0 for v in U+V)
    assert all(V[j]==U[j]-U[j+1] for j in range(s+1))
    assert all(U[j]>U[j+1] for j in range(s+1))
    # Correct inverse-ratio direction, with no floating-point division.
    assert all(U[j]*U[j+2] < U[j+1]**2 for j in range(s))
    C=U[0]+2*U[1]; I=U[0]+2*sum(U[1:s+1]); u=U[s+1]; T=(2*s+1)*u
    result={'E':C+2*I-T,'K_ax':2*I-T,'K_ay':2*U[0]+I-(s+1)*u,
            'K_bx':I-T,'K_by':3*U[0]-2*U[1]-u,'K_xy':3*U[0]}
    return result,U,V


def check_formulas_and_implication(m,r,s):
    actual=actual_counts(m,r,s)
    claim,U,V=claimed_counts(m,r,s)
    assert actual==claim,(m,r,s,actual,claim)
    E=actual['E']; ax=actual['K_ax']; ay=actual['K_ay']; bx=actual['K_bx']; by=actual['K_by']
    u=U[-1]; T=(2*s+1)*u; S=sum(U[2:s+1])
    assert 2*bx-ax==-T
    assert by==2*ay-E
    assert 3*ax-2*E==4*S-T
    assert 3*bx-E==2*(S-T)
    assert 2*E-3*by==-3*U[0]+18*U[1]+8*S+(1-4*s)*u
    assert 2*bx<E
    if s==1:
        assert 3*ax<2*E
    event='no_dual_majority'
    if 3*ax>2*E and 3*ay>2*E:
        if 3*bx>=E:
            assert 3*bx<=2*E
            event='bx_balanced'
        else:
            assert s>=2 and T<4*S and S<T
            assert S>=(s-1)*U[s]
            assert U[s]*U[1]>=U[0]*u
            assert (s-1)*U[0]<(2*s+1)*U[1]
            assert U[0]<5*U[1]
            assert 2*E-3*by>3*(U[1]+u)>0
            assert E<3*by<2*E
            event='strict_by_rescue'
    return event,actual


def enumerated_cells(m,r,s):
    """Literal complete-extension enumeration for small instances, cell by cell."""
    labels,index,pred=poset(m,r,s); n=len(labels); full=(1<<n)-1
    a_chain={'a','b'}|{f'c{i}' for i in range(1,m+1)}
    y_chain={'y'}|{f'z{i}' for i in range(1,r+1)}
    cells={}
    def visit(order,used):
        if used==full:
            names=[labels[v] for v in order]; at=names.index('x'); before=names[:at]
            cell=(sum(v in a_chain for v in before),sum(v in y_chain for v in before))
            values=cells.setdefault(cell,[0,0,0]); values[0]+=1
            values[1]+=names.index('a')<names.index('y')
            values[2]+=names.index('b')<names.index('y')
            return
        for v in range(n):
            if not used>>v&1 and not pred[v]&~used:
                visit(order+[v],used|(1<<v))
    visit([],0)
    _,U,V=claimed_counts(m,r,s)
    expected={(0,0):[U[0]+U[1],U[0],V[0]], (0,1):[U[1],0,0],
              (1,0):[U[0],U[0],V[0]], (2,0):[V[0],V[0],V[0]]}
    for j in range(1,s+1):
        expected[1,j]=[2*U[j],U[j],0]
        expected[2,j]=[(2*j+1)*V[j],(j+1)*V[j],V[j]]
    assert cells==expected,(m,r,s,cells,expected)
    assert len(cells)==2*s+4
    return sum(v[0] for v in cells.values())


def main():
    events=Counter(); number=0
    for m in range(1,13):
        for r in range(1,13):
            for s in range(1,r+1):
                outcome,_=check_formulas_and_implication(m,r,s)
                events[outcome]+=1; number+=1
    literal_cases=0; literal_extensions=0
    for m in range(1,4):
        for r in range(1,5):
            for s in range(1,r+1):
                literal_extensions += enumerated_cells(m,r,s)
                literal_cases+=1
    special=[]
    for m,r,s in [(13,3,2),(54,15,2),(74,20,2),(1,1,1),(1,12,12),(12,12,12)]:
        event,actual=check_formulas_and_implication(m,r,s)
        special.append({'m':m,'r':r,'s':s,'n':m+r+4,'outcome':event,**actual})
    # Grid large enough to include multiple strict opposite-marginal rescues,
    # checked by exact binomial arithmetic after the formula has been derived.
    broad_events=Counter()
    for m in range(1,101):
        for r in range(1,51):
            for s in range(1,r+1):
                d,_,_=claimed_counts(m,r,s); E=d['E']
                if 3*d['K_ax']>2*E and 3*d['K_ay']>2*E:
                    assert E<=3*d['K_bx']<=2*E or E<=3*d['K_by']<=2*E
                    broad_events['dual_majority']+=1
                    broad_events['strict_by_rescue']+=3*d['K_bx']<E
    result={'status':'PASS','reviewed_document_sha256':hashlib.sha256(DOCUMENT.read_bytes()).hexdigest(),
            'generic_predecessor_mask_DP_cases':number,'DP_case_outcomes':dict(events),
            'literal_extension_enumeration_cases':literal_cases,'literal_extensions_counted':literal_extensions,
            'binomial_grid_bounds':{'m':[1,100],'r':[1,50],'s':'1..r'},
            'binomial_grid_case_count':127500,'binomial_grid_outcomes':dict(broad_events),
            'special_cases':special,
            'scope':'Finite diagnostic confirmation only; the audit supplies the all-parameter self-contained proof.'}
    (HERE/'two_tail_mc3_rescue_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
