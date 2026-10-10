#!/usr/bin/env python3
"""Independent S110 audit: all forward bit matrices, triple transitivity,
direct permutation counts only; no import of the supplied checker."""
import hashlib, itertools, json, math, time
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent
start=time.time()
report={"audit_method":"all forward relation bit matrices; triple transitivity; direct permutation enumeration; no ideal-count DP", "proof_sha256":hashlib.sha256((SOURCE/'bounded_cut_profiles.md').read_bytes()).hexdigest(),"checker_sha256":hashlib.sha256((SOURCE/'check_s110.py').read_bytes()).hexdigest(),"per_n":[],"passed":False}
for n in range(7):
    pairs=tuple(itertools.combinations(range(n),2))
    full=(1<<n)-1
    mask_points={m:tuple(i for i in range(n) if m>>i&1) for m in range(1<<n)}
    perms={m:tuple(itertools.permutations(pts)) for m,pts in mask_points.items()}
    stat=Counter(n=n)
    for bits in range(1<<len(pairs)):
        rel={edge for k,edge in enumerate(pairs) if bits>>k&1}
        if any((i,j) in rel and (j,k) in rel and (i,k) not in rel for i,j,k in itertools.combinations(range(n),3)):
            continue
        stat['posets']+=1
        degree=[sum((min(i,j),max(i,j)) not in rel for j in range(n) if i!=j) for i in range(n)]
        delta=max(degree,default=0)
        def induced_extensions(mask):
            edges=tuple((i,j) for i,j in rel if mask>>i&1 and mask>>j&1)
            result=[]
            for p in perms[mask]:
                position={x:k for k,x in enumerate(p)}
                if all(position[i]<position[j] for i,j in edges): result.append(p)
            return tuple(result)
        exts={m:induced_extensions(m) for m in range(1<<n)}
        ideals=tuple(m for m in range(1<<n) if all(not(m>>j&1) or (m>>i&1) for i,j in rel))
        stat['ideals']+=len(ideals)
        # Verify rank guard directly against EVERY full permutation extension.
        for p in exts[full]:
            assert all(abs(k-i)<=delta for k,i in enumerate(p))
            stat['full_extensions']+=1
        for D in range(delta,n+3):
            C=math.factorial(2*D)//math.factorial(D)
            N=math.comb(2*D,D)
            for r in range(n+1):
                layer=[m for m in ideals if m.bit_count()==r]
                l,u=max(0,r-D),min(n,r+D)
                L=(1<<l)-1; R=full^((1<<u)-1); W=full^L^R
                a,b=r-l,u-r
                tf,tb=min(D,l),min(D,n-u)
                CF=math.factorial(tf+a)//math.factorial(tf)
                CB=math.factorial(tb+b)//math.factorial(tb)
                local={L|S for S in range(1<<n) if not(S&~W) and S.bit_count()==a and all(not(S>>j&1) or not(W>>i&1) or (S>>i&1) for i,j in rel)}
                assert local==set(layer)
                k=len(layer)
                assert 1<=k<=math.comb(a+b,a)<=N
                sf=sum(len(exts[J]) for J in layer); sb=sum(len(exts[full^J]) for J in layer)
                E=len(exts[full])
                assert sum(len(exts[J])*len(exts[full^J]) for J in layer)==E
                for J in layer:
                    F,B=len(exts[J]),len(exts[full^J])
                    assert L&J==L and J&R==0
                    assert len(exts[L])<=F<=CF*len(exts[L])<=C*len(exts[L])
                    assert len(exts[R])<=B<=CB*len(exts[R])<=C*len(exts[R])
                    assert F*(1+(k-1)*CF)>=sf and F*(CF+k-1)<=CF*sf
                    assert B*(1+(k-1)*CB)>=sb and B*(CB+k-1)<=CB*sb
                    assert F*B*(1+(k-1)*CF*CB)>=E and F*B*(CF*CB+k-1)<=CF*CB*E
                    stat['all_D_state_checks']+=1
                    if D==delta:
                        for mask,core,dual in ((J,L,False),(full^J,R,True)):
                            fibers=Counter(tuple(i for i in p if core>>i&1) for p in exts[mask])
                            assert set(fibers)==set(exts[core])
                            aa=(mask^core).bit_count(); t=min(D,core.bit_count())
                            bound=math.factorial(t+aa)//math.factorial(t)
                            assert all(len(exts[mask^core])<=value<=bound for value in fibers.values())
                            for p in exts[mask]:
                                pp=p[::-1] if dual else p
                                base=tuple(i for i in pp if core>>i&1)
                                fixed=core.bit_count()-t
                                assert pp[:fixed]==base[:fixed]
                            stat['cut_fibers']+=len(fibers)
                            if len(set(fibers.values()))>1: stat['nonuniform_directions']+=1
                        if delta==0: assert k==1 and F==B==1
                        if delta==1:
                            assert k<=2
                            assert all(len(exts[K])==F and len(exts[full^K])==B for K in layer)
                            assert F*B*k==E
                            stat['degree_one_states']+=1
                stat['all_D_layer_checks']+=1
        # Audit stronger general insertion lemma with every ideal core K,
        # A=Q\K, and D equal ONLY the cross-incidence degree of A into K.
        for K in ideals:
            A=full^K
            m,a=K.bit_count(),A.bit_count()
            d=max((sum((min(x,y),max(x,y)) not in rel for y in mask_points[K]) for x in mask_points[A]),default=0)
            t=min(d,m)
            bound=math.factorial(t+a)//math.factorial(t)
            fibers=Counter(tuple(x for x in p if K>>x&1) for p in exts[full])
            assert set(fibers)==set(exts[K])
            assert all(len(exts[A])<=v<=bound for v in fibers.values())
            for p in exts[full]:
                base=tuple(x for x in p if K>>x&1)
                assert p[:m-t]==base[:m-t]
            stat['general_lemma_fibers']+=len(fibers)
    report['per_n'].append(dict(stat))
    print(json.dumps(dict(stat),sort_keys=True),flush=True)
report['passed']=True
report['elapsed_seconds']=round(time.time()-start,3)
report['totals']={key:sum(row.get(key,0) for row in report['per_n']) for key in sorted(set().union(*(row.keys() for row in report['per_n']))-{'n'})}
(ROOT/'independent_matrix_audit.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('PASS',report['elapsed_seconds'],json.dumps(report['totals'],sort_keys=True),flush=True)
