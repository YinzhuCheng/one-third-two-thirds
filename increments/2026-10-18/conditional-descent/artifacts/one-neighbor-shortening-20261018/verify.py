"""Exact local verification of the t=1 shortening countercontrol family.
No global no-balanced-poset search is performed.
"""
from fractions import Fraction
import json
from pathlib import Path


def linear_extensions(labels, relations):
    labels=tuple(labels)
    pred={x:set() for x in labels}
    for a,b in relations:
        pred[b].add(a)
    def visit(prefix, remaining):
        if not remaining:
            yield tuple(prefix)
            return
        done=set(prefix)
        for x in labels:
            if x in remaining and pred[x] <= done:
                yield from visit(prefix+[x],remaining-{x})
    yield from visit([],set(labels))


def family(m, chain_length):
    aa=[f'a{i}' for i in range(1,2*m+1)]
    cc=[f'c{i}' for i in range(1,chain_length+1)]
    labels=aa+['z']+cc+['y']
    rel={(aa[i],aa[j]) for i in range(len(aa)) for j in range(i+1,len(aa))}
    rel|={(cc[i],cc[j]) for i in range(len(cc)) for j in range(i+1,len(cc))}
    rel|={(d,c) for d in aa+['z'] for c in cc}
    return labels,rel,aa,cc


def check(m):
    labels,rel,aa,cc=family(m,m)
    les=list(linear_extensions(labels,rel))
    external=aa+['z','y']
    rel_r={(a,b) for a,b in rel if a in external and b in external}
    external_les=list(linear_extensions(external,rel_r))
    classes={'A':[],'B':[],'C0':[]}
    for le in external_les:
        # U is empty. Window means y follows every D element.
        key='C0' if le[-1]=='y' else 'A'
        classes[key].append(le)
    A=len(classes['A']);B=len(classes['B']);c=len(classes['C0'])
    expected_A=(2*m+1)**2
    expected_c=2*m+1
    assert (A,B,c)==(expected_A,0,expected_c)
    E=lambda le:le.index('y')<le.index(f'a{m}')
    counts={k:sum(E(le) for le in v) for k,v in classes.items()}
    assert counts=={'A':2*m*(m+1),'B':0,'C0':0}
    N=sum(E(le) for le in les)
    T=len(les)
    assert T==(2*m+1)*(3*m+2)
    assert N==2*m*(m+1)
    qs=[Fraction(sum(le.index(ci)<le.index('y') for le in les),T) for ci in cc]
    assert qs==[Fraction(m+1-i,3*m+2) for i in range(1,m+1)]
    assert max(qs)<Fraction(1,3)
    labels2,rel2,aa2,cc2=family(m,m-1)
    les2=list(linear_extensions(labels2,rel2))
    N2=sum(E(le) for le in les2);T2=len(les2)
    assert T2==(2*m+1)*(3*m+1)
    assert N2==N
    p=Fraction(N,T);p2=Fraction(N2,T2)
    assert p<Fraction(1,3)<p2<Fraction(2,3)
    qs2=[Fraction(sum(le.index(ci)<le.index('y') for le in les2),T2) for ci in cc2]
    assert max(qs2)<Fraction(1,3)
    invariant=lambda le:le.index('z')<le.index('a1')
    r1=Fraction(sum(invariant(le) for le in les),T)
    r2=Fraction(sum(invariant(le) for le in les2),T2)
    assert r1==r2==Fraction(1,2*m+1)
    existing_balanced=Fraction(sum(le.index('y')<le.index('z') for le in les),T)
    assert existing_balanced==Fraction(m+1,3*m+2)
    assert Fraction(1,3)<existing_balanced<Fraction(2,3)
    # Check autonomy and inclusion-maximality directly over all subsets
    # that could enlarge C as a chain. For this family, a larger chain
    # cannot contain both z and any a_i, so checking all subsets is tiny.
    def cmp(a,b):
        return -1 if (a,b) in rel else (1 if (b,a) in rel else 0)
    def autonomous(S):
        return all(len({cmp(x,s) for s in S})==1 for x in labels if x not in S)
    assert autonomous(set(cc))
    candidates=[]
    for mask in range(1,1<<len(aa)):
        candidates.append(set(cc)|{a for i,a in enumerate(aa) if mask>>i&1})
    candidates.append(set(cc)|{'z'})
    assert not any(autonomous(S) for S in candidates)
    return {'m':m,'A':A,'B':B,'C0':c,'event_counts':counts,'e_original':T,
            'e_shortened':T2,'event_numerator':N,'p_original':str(p),
            'p_shortened':str(p2),'C_y_original':[str(q) for q in qs],
            'C_y_shortened':[str(q) for q in qs2],
            'unchanged_external_pair':str(r1),
            'already_balanced_y_z':str(existing_balanced),
            'C_inclusion_maximal_autonomous_chain':True}

if __name__=='__main__':
    # m up to 5 is enough for direct exhaustive subset maximality checks;
    # all statements for arbitrary m are proved in RESULT.md.
    data=[check(m) for m in range(2,6)]
    output=Path(__file__).with_name('verification.json')
    output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(data,ensure_ascii=False,indent=2))
