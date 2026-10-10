#!/usr/bin/env python3
"""Independent local-only exact audit. Does not modify audited source files."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
from hashlib import sha256
import json, math, subprocess, sys
import sympy as S
OUT=Path(__file__).resolve().parent
BASE=OUT/'source_snapshot'
expected={}
for line in (BASE/'PROOF_ROUTE_SHA256SUMS').read_text().splitlines():
    h,name=line.split(None,1); expected[name]=h
actual={name:sha256((BASE/name).read_bytes()).hexdigest() for name in expected}
assert actual==expected
rerun=subprocess.run([sys.executable,str(BASE/'verify_realizability_barrier.py')],capture_output=True,text=True,check=True)
assert rerun.stdout==(BASE/'verify_realizability_barrier.log').read_text()

# Integrate independently in outer-s first order, plus direct diagonal integration.
s,t=S.symbols('s t',real=True)
g=(1-s)*(6-5*s)*(1-t)**3/6
F=S.integrate(S.integrate(g,(t,s,1)),(s,0,1))
G=S.integrate(S.integrate(g,(t,0,s)),(s,0,1))
H=S.integrate(s*g.subs(t,s),(s,0,1))
vals=dict(E=F+G,F=F,G=G,H=H)
assert vals==dict(E=S.Rational(13,144),F=S.Rational(37,1008),G=S.Rational(3,56),H=S.Rational(8,315))
counts={k:int(v*math.factorial(7)) for k,v in vals.items()}
assert counts==dict(E=455,F=185,G=270,H=128)
assert 6*counts['E']*counts['H']-7*counts['F']*counts['G']==-210
assert counts['H']**2-(counts['F']-counts['H'])*(counts['G']-counts['H'])==8290
assert S.expand(g*S.diff(g,s,t)-S.diff(g,s)*S.diff(g,t))==0
assert S.total_degree(g)==5
assert g.subs(s,1)==g.subs(t,1)==0
assert g.subs({s:0,t:0})==1
assert g.subs({s:S.Rational(1,2),t:0})==S.Rational(7,24)
assert S.diff(g,s).subs({s:0,t:0})==-S.Rational(11,6)

# Check normalized Hessian of fifth root without numerical radical evaluation.
x,y,a=S.symbols('x y a',positive=True)
R=x*(x+a)
h=R**S.Rational(1,5)*y**S.Rational(3,5)
hxx=S.simplify(S.diff(h,x,2)/h)
hyy=S.simplify(S.diff(h,y,2)/h)
hxy=S.simplify(S.diff(h,x,y)/h)
assert S.simplify(hxx-(-6*R-4*a*a)/(25*R*R))==0
assert S.simplify(hyy+6/(25*y*y))==0
assert S.simplify(hxx*hyy-hxy*hxy-3*a*a/(125*R*R*y*y))==0

# Homogeneous sector polynomials: every degree-five monomial coefficient nonnegative.
x,y,z=S.symbols('x y z',nonnegative=True)
left=(y+z)*(x+6*y+6*z)*z**3/6
right=z*(x+y+6*z)*(y+z)**3/6
for poly,sub in [(left,{x:s,y:t-s,z:1-t}),(right,{x:t,y:s-t,z:1-s})]:
    assert all(coef>=0 and sum(mon)==5 for mon,coef in S.Poly(poly,x,y,z).terms())
    assert S.expand(poly.subs(sub)-g)==0

# Count original seven-point linear extensions and literal label swaps.
def valid(word,pred):
    seen=0
    for v in word:
        if pred[v]&~seen:return False
        seen|=1<<v
    return True

def extensions(pred):
    n=len(pred); full=(1<<n)-1
    def rec(seen,word):
        if seen==full:
            yield tuple(word);return
        for v in range(n):
            b=1<<v
            if not seen&b and not pred[v]&~seen:
                word.append(v);yield from rec(seen|b,word);word.pop()
    yield from rec(0,[])

def direct_counts(pred,u,v,words=None):
    E=F=H=adj=0
    for word in extensions(pred) if words is None else words:
        E+=1
        p,q=word.index(u),word.index(v)
        if p<q:
            F+=1; adj+=q==p+1
            w=list(word);w[p],w[q]=w[q],w[p]
            H+=valid(w,pred)
    return dict(E=E,F=F,G=E-F,H=H,Aadj=adj)
p1=(0,0,1,1,2,2,2)
p2=(0,0,1,0,2,2,2)
c1=direct_counts(p1,0,1);c2=direct_counts(p2,0,1)
assert {k:c1[k] for k in vals}==dict(E=420,F=180,G=240,H=120)
assert {k:c2[k] for k in vals}==dict(E=630,F=210,G=420,H=168)
assert {k:Q(5*c1[k]+c2[k],6) for k in vals}==counts

# Independent rank histograms in the deletion-antichain chambers.
def hist(U,V):
    c=Counter()
    for w in permutations(range(5)):
        pos={v:k+1 for k,v in enumerate(w)}
        c[min(pos[u] for u in U),min(pos[v] for v in V)]+=1
    return c
h1,h2=hist({0,1},{2,3,4}),hist({0},{2,3,4})
hmix={k:Q(5*h1[k]+h2[k],6) for k in h1.keys()|h2.keys()}
assert all(v.denominator==1 for v in hmix.values())
assert sum(hmix.values())==120
assert hmix=={(1,2):33,(1,3):11,(2,1):33,(2,3):1,(3,1):23,(3,2):1,(4,1):13,(4,2):1,(5,1):3,(5,2):1}

# All 1055 possible labeled shared-downset posets whose five-point deletion
# poset is an antichain. D empty allows arbitrary successor subsets; D nonempty
# forbids both successor sets. Every boundary value f(1/2,0) is dyadic.
boundary_values=Counter()
for states in product(range(4),repeat=5):
    U={i for i,q in enumerate(states) if q&1}
    V={i for i,q in enumerate(states) if q&2}
    boundary_values[Q(1,2)**len(U)]+=1
for D in range(1,1<<5):
    boundary_values[Q(1,2)**D.bit_count()]+=1
assert sum(boundary_values.values())==1055
assert Q(7,24) not in boundary_values
# Added ray lemma at n=7: if f=lambda*g is genuine, integer F,H give
# lambda=9*F-13*H; f(0,0)=lambda is a deletion-polytope volume in (0,1].
assert 9*185-13*128==1
possible_scales=[]
for deletion_extensions in range(1,121):
    lam=Q(deletion_extensions,120)
    if (185*lam).denominator==(128*lam).denominator==1:
        possible_scales.append(lam)
assert possible_scales==[Q(1)]

# Exhaustive naturally labeled posets through n=6, generated by adding an ideal
# as the predecessor set of each new last vertex. Independent literal-swap H.
def all_natural_posets(n):
    if not n:
        yield ();return
    for p in all_natural_posets(n-1):
        for ideal in range(1<<(n-1)):
            if all(not(ideal&(1<<i)) or not(p[i]&~ideal) for i in range(n-1)):
                yield p+(ideal,)
finite=[]
for n in range(2,7):
    stats=dict(n=n,posets=0,shared_pairs=0,one_wing_pairs=0,one_wing_equalities=0,nested_pairs=0)
    for pred in all_natural_posets(n):
        stats['posets']+=1
        pairs=[(u,v) for u in range(n) for v in range(u+1,n) if pred[u]==pred[v]]
        if not pairs:continue
        words=list(extensions(pred))
        succ=[sum(1<<j for j in range(n) if pred[j]&(1<<i)) for i in range(n)]
        for u,v in pairs:
            stats['shared_pairs']+=1
            c=direct_counts(pred,u,v,words)
            E,F,G,H,A=[c[k] for k in ('E','F','G','H','Aadj')]
            assert G<=(n-1)*A<=(n-1)*F
            B=sum(w.index(u)==w.index(v)+1 for w in words)
            assert F<=(n-1)*B<=(n-1)*G
            nested=not(succ[u]&~succ[v]) or not(succ[v]&~succ[u])
            if nested:
                stats['nested_pairs']+=1
                assert F==H or G==H
            if F==H or G==H:
                stats['one_wing_pairs']+=1
                delta=(n-1)*E*H-n*F*G
                assert delta>=0
                mins={j for j in range(n) if pred[j]==0}
                iso_u=pred[u]==0 and succ[u]==0
                iso_v=pred[v]==0 and succ[v]==0
                expected_equality=(F==H and iso_u and mins-{u}=={v}) or (G==H and iso_v and mins-{v}=={u})
                assert (delta==0)==expected_equality
                if delta==0:stats['one_wing_equalities']+=1
    finite.append(stats)
assert [x['posets'] for x in finite]==[2,7,40,357,4824]

# Independent check of the ancillary genuine eight-point MTP2 counterexample.
p8=(0,0,3,3,1,2,23,43)
c8=direct_counts(p8,2,3)
assert {k:c8[k] for k in vals}==dict(E=200,F=100,G=100,H=74)
assert 7*c8['E']*c8['H']-8*c8['F']*c8['G']==23600
phi=(t-1)**3*(25*s*s*t+15*s*s-8*s*t*t+6*s*t+2*s-3*t**3-15*t*t-16*t-6)/240
phi00=phi.subs({s:0,t:0})
eps=S.Rational(1,100)
mtp8=S.factor(phi00*phi.subs({s:eps,t:eps})-phi.subs({s:0,t:eps})**2)
assert phi00==S.Rational(1,40)
assert [S.diff(phi,v).subs({s:0,t:0}) for v in (s,t)]==[-S.Rational(1,120)]*2
assert S.diff(phi,s,t).subs({s:0,t:0})==0
assert mtp8==-S.Rational(24895078440973240401,6400000000000000000000000000)
assert S.integrate(S.integrate(phi,(s,0,t)),(t,0,1))*math.factorial(8)==100
assert S.integrate(t*phi.subs(s,t),(t,0,1))*math.factorial(8)==74
# The earlier square-support analytic example, independently reintegrated.
q=(S.Rational(6,5)-s)*(1-t)**2
qF=S.integrate(S.integrate(q,(s,0,t)),(t,0,1))
qG=S.integrate(S.integrate(q,(t,0,s)),(s,0,1))
qH=S.integrate(t*q.subs(s,t),(t,0,1))
assert (qF,qG,qH)==(S.Rational(1,12),S.Rational(3,20),S.Rational(1,15))
assert 4*(qF+qG)*qH-5*qF*qG==-S.Rational(1,3600)

result={
 'verdict':'PASS: exact mixture barrier, exact and ray nonrealizability at n=7, restricted one-wing theorem; general target not proved or refuted',
 'source_sha256':actual,
 'source_log_reproduced_byte_for_byte':True,
 'mixture_integrals':{k:str(v) for k,v in vals.items()},
 'mixture_counts':counts,'dimension_sharp_defect':-210,'ordinary_square_defect':8290,
 'literal_swap_counts_P1':c1,'literal_swap_counts_P2':c2,
 'rank_histogram':[{ 'p':p,'q':q,'multiplicity':int(c)} for (p,q),c in sorted(hmix.items())],
 'deletion_antichain_realizations_checked':1055,
 'possible_boundary_values':{str(k):v for k,v in sorted(boundary_values.items())},
 'excluded_mixture_boundary_value':'7/24',
 'ray_certificate':'9*185-13*128=1; 0<lambda=f(0,0)<=1; integer F,H force lambda=1',
 'admissible_scales_from_120_deletion_extension_counts':[str(v) for v in possible_scales],
 'fifth_root_normalized_hessian':{'xx':str(hxx),'yy':str(hyy),'det':'3*a^2/(125*x^2*(x+a)^2*y^2)>0 for a=1/5'},
 'left_homogeneous_polynomial':str(S.expand(left)),
 'right_homogeneous_polynomial':str(S.expand(right)),
 'restricted_theorem_finite_checks':finite,
 'ancillary_actual_eight_point_counts':c8,
 'ancillary_actual_mtp2_defect':str(mtp8),
 'ancillary_square_analytic_defect':'-1/3600',
 'scope':'Finite tests are supporting checks only. The source proof supplies the all-n one-wing theorem. No claim that the general dimension-sharp swap conjecture is settled.'
}
(OUT/'audit_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
