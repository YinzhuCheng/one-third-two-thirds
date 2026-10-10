#!/usr/bin/env python3
"""Independent exact audit. Standard library, no assert statements, read-only inputs.
Rebuilds labelled ideals in reversed label order with a forward event DP; checks
unconditional rational Dirichlet integrals and symbolic polynomial identities.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb, factorial
from pathlib import Path
import json, runpy, sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'source_snapshot'
EXPECTED = {
 'FOUR_TAIL_CERTIFICATE.md':'227708fc40a94df919101bcd6815e2191a8e45fd7c9676b222aafa74baa0ab3c',
 'verify_four_tail.py':'96ef9375351cda862f832e102baa577c92778fdc487dbba4ed4e9f45efb407d5',
 'verification.json':'a02196ea9e99e2e547f9ad7be81af20c80c80424699ded4bc985540b3db1ba7c',
}
EDGES = [(0,3),(1,2),(1,4),(2,3),(2,6),(3,5),(4,5)]
def check(condition, label):
    if not condition:
        raise RuntimeError(str(label))

def build(w):
    # Reverse vertex order deliberately; no topologically ordered labels assumed.
    nodes = list(reversed([(b,i) for b,n in enumerate(w) for i in range(n)]))
    ix = {v:i for i,v in enumerate(nodes)}
    reach = [[False]*7 for _ in range(7)]
    for b,c in EDGES: reach[b][c]=True
    for h in range(7):
        for b in range(7):
            for c in range(7): reach[b][c] |= reach[b][h] and reach[h][c]
    pred=[]
    for b,i in nodes:
        pred.append(sum(1<<q for q,(c,j) in enumerate(nodes)
                        if reach[c][b] or (c==b and j<i)))
    x,z=ix[(3,0)],ix[(5,0)]
    fs=[ix[(6,i)] for i in range(4)]
    down=lambda j: {i for i in range(len(nodes)) if pred[j]>>i&1}
    up=lambda j: {i for i in range(len(nodes)) if pred[i]>>j&1}
    C=lambda b:{ix[(b,i)] for i in range(w[b])}
    check(down(fs[0]) == C(1)|C(2),('D(F1)',w))
    check(down(x) == C(0)|C(1)|C(2),('D(x)',w))
    check(up(x)-up(fs[0]) == {z},('U(x)-U(F1)',w))
    check(up(fs[3]) == set() and up(x)=={z},('dual endpoint',w))
    check(down(x)-down(fs[3]) == C(0),('D(x)-D(F4)',w))
    check(up(z)==set() and down(fs[3])-down(z)==set(fs[:3]),('terminal endpoint',w))
    for f in fs:
        check(not(pred[x]>>f&1 or pred[f]>>x&1),('x incomparable F',w))
    check(not(pred[z]>>fs[-1]&1 or pred[fs[-1]]>>z&1),('z incomparable F4',w))
    return nodes,pred,x,z,fs

def independent_dp(w):
    nodes,pred,x,z,fs=build(w); n=len(nodes); fm=sum(1<<f for f in fs)
    # value = number of prefixes, then five rank-event prefix counts, then F4<z.
    layer={0:(1,0,0,0,0,0,0)}; states=1
    for depth in range(n):
        out={}
        for mask,v in layer.items():
            for j,p in enumerate(pred):
                if mask>>j&1 or p&mask!=p:continue
                child=mask|1<<j
                val=list(v)
                if j==x:val[1+(mask&fm).bit_count()]+=v[0]
                if j==z and mask>>fs[-1]&1:val[6]+=v[0]
                if child not in out:out[child]=val
                else:
                    for q in range(7):out[child][q]+=val[q]
        layer=out; states+=len(layer)
    v=layer[(1<<n)-1]
    check(sum(v[1:6])==v[0],('independent rank partition',w))
    return v[0],v[1:6],v[6],states

# Sparse multivariate integer/rational polynomials, independent of source functions.
def add(*polys):
    out=defaultdict(F)
    for p in polys:
        for e,c in p.items():out[e]+=c
    return {e:c for e,c in out.items() if c}
def scale(p,c):return {e:c*v for e,v in p.items() if c*v}
def mul(p,q):
    out=defaultdict(F)
    for e,c in p.items():
        for f,d in q.items():out[tuple(a+b for a,b in zip(e,f))]+=c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out={tuple(0 for _ in next(iter(p))):F(1)}
    for _ in range(n):out=mul(out,p)
    return out
def var(i,n):return {tuple(int(j==i) for j in range(n)):F(1)}
def const(c,n=2):return {(0,)*n:F(c)}
def evaluate(p,values):
    return sum(c*__import__('functools').reduce(lambda a,b:a*b,(v**e for v,e in zip(values,exps)),F(1)) for exps,c in p.items())
def substitute(p,replacements):
    out={}
    for exps,c in p.items():
        term=const(c,len(next(iter(replacements[0]))))
        for e,r in zip(exps,replacements):term=mul(term,power(r,e))
        out=add(out,term)
    return out

@lru_cache(None)
def volume_polynomials(u,t):
    q=[var(i,5) for i in range(5)]
    base=mul(power(add(q[0],q[1],q[2]),u),power(add(q[1],q[2],q[3]),t))
    # Total volume; rank j volume; event F4<z volume.
    result=[mul(base,power(add(q[2],q[3],q[4]),4))]
    result += [mul(mul(base,power(q[2],j)),power(add(q[3],q[4]),4-j)) for j in range(5)]
    result += [mul(base,power(add(q[2],q[3]),4))]
    return result

def volume_counts(w):
    u,a,b,_,t,_,_=w; N=sum(w)
    counts=[]
    denominators=[24]+[factorial(j)*factorial(4-j) for j in range(5)]+[24]
    for polynomial,den in zip(volume_polynomials(u,t),denominators):
        # Integral of q_0^e0 ... q_4^e4 on the unit 4-simplex is
        # product(e_i!)/(sum(e_i)+4)!. Here the final denominator is N!.
        numerator=F(0)
        for e,c in polynomial.items():
            ex=[e[0]+a-1,e[1]+b-1,*e[2:]]
            check(sum(ex)+4==N,('Dirichlet degree',w,e))
            f=1
            for v in ex:f*=factorial(v)
            numerator+=c*f
        fixed=factorial(a-1)*factorial(b-1)*factorial(u)*factorial(t)*den
        volume=numerator/F(fixed*factorial(N))
        count=volume*factorial(N)
        check(count.denominator==1,('volume count integral',w,count))
        counts.append(count.numerator)
    return counts[0],counts[1:6],counts[6]

def symbolic_checks():
    k,n=var(0,2),var(1,2)
    plus=lambda x,c:add(x,const(c))
    D=scale(mul(mul(plus(k,4),plus(k,5)),mul(plus(n,5),plus(n,6))),3)
    # D*(11/3 -48 M3 +51 M4 -(n+2)/(n+6)), cancelling denominators.
    raw=add(scale(D,F(11,3)),
            scale(mul(mul(plus(k,1),plus(n,2)),mul(plus(k,5),plus(n,6))),-144),
            scale(mul(mul(plus(k,1),plus(n,2)),mul(plus(k,4),plus(n,5))),153),
            scale(mul(mul(plus(k,4),plus(k,5)),mul(plus(n,5),plus(n,2))),-3))
    expected={(2,2):17,(2,1):19,(2,0):102,(1,2):-27,(1,1):-657,(1,0):-18,(0,2):52,(0,1):524,(0,0):3480}
    check(raw==expected,'symbolic denominator-clearing identity')
    # n=k+l; both variables remain formal.
    kl=substitute(raw,[k,add(k,n)])
    small=[{(0,2):52,(0,1):524,(0,0):3480},
           {(0,2):42,(0,1):-30,(0,0):3492},
           {(0,2):66,(0,1):-450,(0,0):2688},
           {(0,2):124,(0,1):-532,(0,0):1632},
           {(0,2):216,(0,1):-72,(0,0):1296}]
    for j,p in enumerate(small):
        check(substitute(kl,[const(j),n])==p,('symbolic small-k',j))
        aa,bb,cc=p[(0,2)],p[(0,1)],p[(0,0)]
        if j:check(aa>0 and bb*bb-4*aa*cc<0,('quadratic strictly positive',j))
        else:check(all(v>0 for v in p.values()),'k=0 positivity')
    shifted=substitute(kl,[plus(k,5),n])
    expected_shift={(4,0):17,(3,1):34,(3,0):332,(2,2):17,(2,1):475,(2,0):1927,(1,2):143,(1,1):1647,(1,0):3376,(0,2):342,(0,1):1134,(0,0):3060}
    check(shifted==expected_shift and all(v>0 for v in shifted.values()),'symbolic nonnegative shifted polynomial')
    # The ratio numerator minus denominator is (j-4)m+3j-4, formally.
    m,j=k,n
    diff=add(mul(add(m,j,const(1)),plus(m,3)),scale(mul(plus(m,1),plus(m,7)),-1))
    check(diff=={(1,1):1,(1,0):-4,(0,1):3,(0,0):-4},'symbolic atom ratio')
    return {'polynomial_identity':'formal sparse polynomial equality',
            'small_k_cases':5,'positive_shift_terms':len(shifted),
            'discriminants_reduced':[-16271,-14087,-32903,-215]}

def triangle_checks():
    cases=0; mixtures=0; atoms=0
    for k,l in product(range(31),repeat=2):
        n=k+l
        Z=F(1,(k+1)*(n+2))
        # Integrate h^(k+j)y^l over 0<h<y<1 directly, then normalize.
        mom=lambda j:F(1,(k+j+1)*(n+j+2))/Z
        for j in range(9):
            check(mom(j)==F(k+1,k+j+1)*F(n+2,n+j+2),('triangle moment',k,l,j));cases+=1
        cy=F(1,(k+1)*(n+6))/Z
        check(cy==F(n+2,n+6),('y4 integral',k,l))
        rank=[]
        for j in range(5):
            value=comb(4,j)*sum((-1)**i*comb(4-j,i)*mom(j+i) for i in range(5-j))
            rank.append(value)
        check(sum(rank)==1 and min(rank)>0,('rank partition via integrals',k,l))
        # Explicit positive mixture weights of Beta(m+1,2).
        weights=[F(1,(l+1)*(m+1)*(m+2))/Z for m in range(k,k+l+1)]
        check(sum(weights)==1 and min(weights)>0,('beta mixing normalization',k,l))
        for j in range(5):
            mixed=sum(v*F((5-j)*comb(m+j,j),comb(m+6,4)) for m,v in zip(range(k,k+l+1),weights))
            check(mixed==rank[j],('beta mixture equals triangle rank law',k,l,j));mixtures+=1
        A=sum(rank[3:]);B=sum(rank[:4])
        check(12*A+15*B+cy<F(56,3),('triangle certificate',k,l))
    for m in range(1001):
        for j in range(5):
            # Independent beta integral evaluation using factorials.
            direct=F(comb(4,j)*(m+1)*(m+2)*factorial(m+j)*factorial(5-j),factorial(m+6))
            advertised=F((5-j)*comb(m+j,j),comb(m+6,4))
            check(direct==advertised,('beta-binomial factorial identity',m,j))
            ratio=F((m+j+1)*(m+3),(m+1)*(m+7))
            following=F((5-j)*comb(m+1+j,j),comb(m+7,4))
            check(following==advertised*ratio,('ratio',m,j))
            if j==1:check(advertised<=F(4,15),('rank1 bound',m))
            if j==2:check(advertised<=F(9,35),('rank2 bound',m))
            atoms+=1
    check(F(2*comb(8,3),comb(11,4))==F(56,165)>F(1,3),'rank3 bound genuinely fails for Beta(6,2)')
    check(F(4,15)<F(1,3) and F(9,35)<F(1,3),'strict rank gap thresholds')
    return {'exact_triangle_moments':cases,'explicit_beta_mixture_atom_equalities':mixtures,'beta_factorial_and_ratio_equalities':atoms}

def conditional_mixture_checks():
    # Exact rational conditioning examples include endpoints-near and asymmetric r,s.
    tests=0
    for r,s in [(F(1,5),F(2,5)),(F(1,100),F(99,100)),(F(49,100),F(1,2)),(F(1,1000),F(1,500))]:
        for u,t in product([1,2,5,8],repeat=2):
            coeff={(k,l):comb(u,k)*s**(u-k)*(1-s)**k*comb(t,l)*(s-r)**(t-l)*(1-s)**l for k in range(u+1) for l in range(t+1)}
            masses={kl:c*F(1,(kl[0]+1)*(sum(kl)+2)) for kl,c in coeff.items()}
            Z=sum(masses.values());check(Z>0 and min(masses.values())>0,('positive triangle mixture',r,s,u,t))
            lhs=F(0)
            for (k,l),mass in masses.items():
                n=k+l;M3=F(k+1,k+4)*F(n+2,n+5);M4=F(k+1,k+5)*F(n+2,n+6)
                lhs+=mass*(12*(4*M3-3*M4)+15*(1-M4)+F(n+2,n+6))/Z
            check(lhs<F(56,3),('conditioned certificate',r,s,u,t));tests+=1
    return tests

def main():
    source_hashes={name:sha256((SOURCE/name).read_bytes()).hexdigest() for name in EXPECTED}
    check(source_hashes==EXPECTED,'frozen source hashes')
    original=runpy.run_path(str(SOURCE/'verify_four_tail.py'))
    symbolic=symbolic_checks();triangles=triangle_checks();conditioned=conditional_mixture_checks()
    records=[];totalstates=0;maxrank3=F(0);minmargin=None;crossings=0
    # Full source box plus 15 all-positive asymmetric/out-of-box stress vectors.
    weights=[(u,a,b,1,t,1,4) for u,a,b,t in product(range(1,6),repeat=4)]
    extras=[(9,1,1,1),(1,9,1,1),(1,1,9,1),(1,1,1,9),(9,2,3,7),(7,9,2,3),(3,7,9,2),(2,3,7,9),(12,1,2,5),(1,12,5,2),(2,5,12,1),(5,2,1,12),(10,10,1,1),(1,1,10,10),(8,8,8,8)]
    weights += [(u,a,b,1,t,1,4) for u,a,b,t in extras]
    for index,w in enumerate(weights):
        E,h,C,states=independent_dp(w);totalstates+=states
        check((E,h,C)==original['count_and_hist'](w),('source versus independent DP',w))
        check((E,h,C)==volume_counts(w),('DP versus unconditional rational integrals',w))
        check(15*h[1]<=4*E and 35*h[2]<=9*E,('actual rank atom bounds',w))
        margin=F(56,3)-F(12*sum(h[3:])+15*sum(h[:4])+C,E)
        check(margin>0,('actual strict certificate',w))
        if index<625:
            maxrank3=max(maxrank3,F(h[3],E));minmargin=margin if minmargin is None else min(minmargin,margin)
            if 3*(E-h[0])>2*E and 3*(E-h[4])>2*E and 3*C>2*E:
                crossings+=1
                check(any(E<=3*sum(h[i:])<=2*E for i in range(1,5)),('forced crossing',w))
        records.append({'weights':w,'extensions':E,'rank_histogram':h,'F4_before_z':C,'certificate_margin':str(margin),'independent_ideals':states})
    expected_summary=json.loads((SOURCE/'verification.json').read_text())
    check(str(maxrank3)==expected_summary['largest_rank3_atom_in_box'],'rank3 summary reproduced')
    check(str(minmargin)==expected_summary['smallest_certificate_margin_in_box'],'margin summary reproduced')
    check(crossings==expected_summary['forced_endpoint_crossing_vectors'],'crossing summary reproduced')
    output={'status':'PASS','source_sha256':source_hashes,'independent_labelled_DP_vectors':len(weights),
            'source_box_vectors':625,'asymmetric_larger_vectors':len(extras),'independent_ideals_processed':totalstates,
            'unconditional_exact_rational_volume_crosschecks':7*len(weights),
            'largest_rank3_atom_in_source_box':str(maxrank3),'minimum_certificate_margin_in_source_box':str(minmargin),
            'forced_endpoint_crossing_vectors':crossings,'symbolic':symbolic,'triangle':triangles,
            'positive_conditional_mixture_examples':conditioned,
            'scope':'Unbounded proof validated symbolically; finite DP/integrals are independent implementation crosschecks.'}
    outpath=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'audit_results.json'
    outpath.write_text(json.dumps(output,indent=2)+'\n')
    outpath.with_name(outpath.stem+'_vectors.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
