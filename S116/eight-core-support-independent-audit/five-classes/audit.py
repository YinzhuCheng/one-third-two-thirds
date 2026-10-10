#!/usr/bin/env python3
"""Independent symbolic outside-fiber reconstruction and occupancy recount.
Every check is explicit and remains active with python -O. Standard library.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb,factorial
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
CLASSES=['C08','C09','C11','C14','C15']

def require(ok,s):
    if not ok:raise RuntimeError(s)
def read(s):return json.loads((R/s).read_text())
def sha(s):return hashlib.sha256((R/s).read_bytes()).hexdigest()
def structure(up):
    U=[{j for j in range(8) if up[i]>>j&1} for i in range(8)]
    D=[{j for j in range(8) if i in U[j]} for i in range(8)]
    I=[set(range(8))-{i}-U[i]-D[i] for i in range(8)]
    require(all(i not in U[i] for i in range(8)) and all(U[j]<=U[i] for i in range(8) for j in U[i]),'Strict partial order')
    return U,D,I

def occupancy_count(up,w,edge=None):
    D=[tuple(j for j in range(8) if up[j]>>i&1) for i in range(8)];w=tuple(w)
    @lru_cache(None)
    def f(s):
        if s==w:return 1
        out=0
        for i in range(8):
            if s[i]==w[i] or any(s[j]!=w[j] for j in D[i]):continue
            if edge and (i,s[i])==edge[1] and s[edge[0][0]]<=edge[0][1]:continue
            t=list(s);t[i]+=1;out+=f(tuple(t))
        return out
    return f((0,)*8)

def outside_extensions(up,i):
    V=set(range(8))-{i};D={j:{k for k in V if up[k]>>j&1} for j in V};words=[]
    def visit(word,remaining,placed):
        if not remaining:words.append(word);return
        for j in sorted(remaining):
            if D[j]<=placed:visit(word+[j],remaining-{j},placed|{j})
    visit([],V,set());return words

def fibers(up,i):
    U,D,I=structure(up);result=[]
    for word in outside_extensions(up,i):
        positions={v:j for j,v in enumerate(word)}
        L=max((positions[j] for j in D[i]),default=-1)
        Q=min((positions[j] for j in U[i]),default=7)
        require(L<Q,'Legal window boundaries')
        inside=word[L+1:Q];require(set(inside)<=I[i],'Only incomparable vertices in legal window')
        result.append((word,positions,L,Q,Q-L-1))
    return result

def symbolic_fibers(up,i,pair,F):
    a,sa,b,sb=pair;require(a!=b and sa in (0,1) and sb in (0,1),'Endpoint description')
    U,D,I=structure(up);require(b in I[a],'Incomparable polynomial pair')
    Z=[0]*8;N=[0]*8
    for word,pos,L,Q,h in F:
        Z[h]+=1
        if i not in (a,b):
            if pos[a]<pos[b]:N[h]+=1
            continue
        # Cumulative favorable chain-before-singleton vector in this fiber.
        x=b if a==i else a;side=sa if a==i else sb;v=[0]*8
        if pos[x]>=Q:v[h]+=1
        elif pos[x]>L:
            rr=pos[x]-L
            if side==0:v[h]+=1;v[h-rr]-=1
            else:v[rr-1]+=1
        if b==i:
            v=[-z for z in v];v[h]+=1
        N=[x+y for x,y in zip(N,v)]
    return Z,N

def ev(a,t):return sum(c*comb(t+h,h) for h,c in enumerate(a))
def differences(a,K):
    v=[ev(a,K+j) for j in range(8)];r=[]
    while v:r.append(v[0]);v=[y-x for x,y in zip(v,v[1:])]
    return r

def linear_product(constants,denom=1):
    p=[Fraction(1)]
    for c in constants:
        q=[Fraction(0)]*(len(p)+1)
        for j,a in enumerate(p):q[j]+=a*c;q[j+1]+=a
        p=q
    return [v/denom for v in p]+[Fraction(0)]*(8-len(p))
def monomials(a):
    p=[Fraction(0)]*8
    for h,v in enumerate(a):
        f=linear_product(range(1,h+1),factorial(h));p=[x+v*y for x,y in zip(p,f)]
    return p

def newton_check(a,K,expected):
    require(type(K) is int and K>=2,'Tail integer domain')
    d=differences(a,K);require(d==expected and all(x>=0 for x in d),'Nonnegative exact Newton coefficients')
    p=[Fraction(0)]*8
    for k,v in enumerate(d):
        f=linear_product([-K-j for j in range(k)],factorial(k));p=[x+v*y for x,y in zip(p,f)]
    require(p==monomials(a),'Symbolic Newton polynomial identity')
    return d

def actual_pair(desc,w):
    a,sa,b,sb=desc;return (a,w[a]-1 if sa else 0),(b,w[b]-1 if sb else 0)

def main():
    require(sha('inputs/author/THEOREM.md')=='1480dcbeab1bf5f6eb80989a13e7aaea1482f64a76460ab65b1b70b35e4209b8','Theorem pin')
    require(sha('inputs/author/certificate.json')=='e07d48091d22ad661cfaa7292a6d9a96fec9840deae9be2ef9b3cd7056a50997','Certificate pin')
    pm=read('inputs/prior/MANIFEST.json')['files']
    for rel in ['AUDIT.md','inputs/frozen_singleton_constraints.json','inputs/weight_filter_catalogue.json','inputs/original_orbit_audit.json']:
        require(sha('inputs/prior/'+rel)==pm[rel]['sha256'],'Prior source pin '+rel)
    c=read('inputs/author/certificate.json');require([q['class_id'] for q in c['cores']]==CLASSES,'Exact class list')
    old={q['class_id']:q for q in read('inputs/prior/inputs/frozen_singleton_constraints.json')}
    prior={q['class_id']:q for q in read('inputs/prior/inputs/weight_filter_catalogue.json')['cores']}
    orbit=read('inputs/prior/inputs/original_orbit_audit.json')['classes']
    cores={q['class_id']:q['strict_up_masks'] for q in c['cores']}
    for q in c['cores']:
        cls=q['class_id'];up=q['strict_up_masks'];U,D,I=structure(up)
        require(up==old[cls]['strict_up_masks']==prior[cls]['strict_up_masks'],'Frozen labelled representative '+cls)
        require(len([r for r in orbit if r['n']==8 and r['representative_masks']==up])==1,'Original orbit membership '+cls)
        cover=[[i,j] for i in range(8) for j in sorted(U[i]) if not any(j in U[k] for k in U[i])]
        require(cover==q['cover_edges']==old[cls]['cover_edges'],'Reconstructed cover edges '+cls)
    covered=set();records=[];witnesses=[];evals=0;orientation_counts=0
    def witness(x,scope):
        nonlocal orientation_counts
        up=cores[x['class_id']];w=x['weights'];a,b=map(tuple,x['pair']);U,D,I=structure(up)
        require(len(w)==8 and all(type(t) is int and t>=1 for t in w),'Witness positive weights')
        require(all(0<=v[0]<8 and 0<=v[1]<w[v[0]] for v in (a,b)) and b[0] in I[a[0]],'Witness incomparable actual elements')
        Z=occupancy_count(up,w);N=occupancy_count(up,w,(a,b));Q=occupancy_count(up,w,(b,a));orientation_counts+=2
        require(Z==x['denominator'] and N==x['numerator'] and N+Q==Z and Z<=3*N<=2*Z,'Actual balanced witness '+scope)
        witnesses.append(dict(scope=scope,class_id=x['class_id'],weights=w,pair=x['pair'],denominator=Z,numerator=N,reverse_numerator=Q))
    def family(cls,i):
        require(cls in CLASSES and type(i) is int and 0<=i<8 and (cls,i) not in covered,'Exact support coverage')
        covered.add((cls,i));return fibers(cores[cls],i)
    def check_polynomial(cls,i,Z,checks,F):
        nonlocal evals,orientation_counts
        require(len(Z)==8 and all(type(x) is int for x in Z),'Denominator basis')
        for pair,N in checks:
            z,n=symbolic_fibers(cores[cls],i,pair,F)
            require(z==Z and n==N,'Exact outside-fiber coefficient reconstruction '+str((cls,i,pair)))
        for t in range(1,9):
            w=[1]*8;w[i]=t;z=occupancy_count(cores[cls],w);require(z==ev(Z,t),'Independent denominator grid')
            for pair,N in checks:
                a,b=actual_pair(pair,w);n=occupancy_count(cores[cls],w,(a,b));q=occupancy_count(cores[cls],w,(b,a));orientation_counts+=2
                require(n==ev(N,t) and n+q==z,'Independent two-orientation polynomial grid')
            evals+=1
    require(len(c['polynomial_certificates'])==36,'36 fixed families')
    tail_hist=Counter()
    for x in c['polynomial_certificates']:
        cls=x['class_id'];i=x['variable'];F=family(cls,i);Z=x['denominator_coefficients'];N=x['numerator_coefficients'];K=x['tail_start']
        require(x['all_other_weights']==1 and x['domain_lower']==2,'Exact one-block domain')
        require(len(F)==x['outside_extension_count'],'Outside extension cardinality')
        check_polynomial(cls,i,Z,[(x['pair'],N)],F)
        low=newton_check([3*n-z for n,z in zip(N,Z)],K,x['lower_balance_newton_coefficients'])
        high=newton_check([2*z-3*n for n,z in zip(N,Z)],K,x['upper_balance_newton_coefficients'])
        require([s['weight'] for s in x['finite_prefix']]==list(range(2,K)),'Complete finite prefix')
        for s in x['finite_prefix']:
            w=[1]*8;w[i]=s['weight'];a,b=actual_pair(s['pair'],w)
            witness(dict(class_id=cls,weights=w,pair=[a,b],numerator=s['numerator'],denominator=s['denominator']),'fixed-pair finite prefix')
        tail_hist[K]+=1;records.append(dict(class_id=cls,variable=i,method='fixed-pair polynomial',outside_fibers=len(F),tail_start=K,pair=x['pair'],denominator_coefficients=Z,numerator_coefficients=N,lower_newton=low,upper_newton=high))
    require(dict(tail_hist)=={2:34,3:2},'Tail partition')
    require(len(c['bounded_certificates'])==3,'Three bounded families')
    for x in c['bounded_certificates']:
        cls=x['class_id'];i=x['variable'];F=family(cls,i);U,D,I=structure(cores[cls]);require(cls in ('C09','C14','C15') and i==6,'Bounded exact family')
        require(sorted(I[i])==x['incomparable_indices'] and len(I[i])==5,'Outside incomparable mass five')
        def chain(S):return all(b in U[a] or a in U[b] for a,b in combinations(S,2))
        low=[j for j in sorted(I[i]) if D[i]==D[j] and chain(U[i]-U[j])]
        high=[j for j in sorted(I[i]) if U[i]==U[j] and chain(D[i]-D[j])]
        rule=dict(target=i,incomparable_indices=sorted(I[i]),bottom_witnesses=low,top_witnesses=high,coefficients=[2 if k==i else -int(k in I[i]) for k in range(8)],integer_rhs=-1)
        require((low or high) and rule in prior[cls]['rules'],'Exact audited structural inequality')
        bound=(len(I[i])-1)//2;require(bound==x['integer_upper_bound']==2,'Strict integer finite bound')
        require(x['case']['class_id']==cls and x['case']['weights']==[2 if j==i else 1 for j in range(8)],'Unique bounded candidate')
        witness(x['case'],'inequality-bounded family');records.append(dict(class_id=cls,variable=i,method='strict inequality',integer_upper_bound=bound,reconstructed_rule=rule))
    x=c['long_chain_certificate'];cls=x['class_id'];i=x['variable'];F=family(cls,i);j=x['comparison_vertex']
    require((cls,i,j)==('C09',1,3),'Rank-crossing exact family')
    U,D,I=structure(cores[cls]);M=len(I[i]);K=x['tail_start'];require(sorted(I[i])==x['incomparable_indices'] and j in I[i] and M==x['incomparable_outside_mass']==5 and K==10 and K>=2*M,'Rank lemma domain')
    Z=x['denominator_coefficients'];N=x['bottom_numerator_coefficients'];T=x['top_numerator_coefficients']
    check_polynomial(cls,i,Z,[([i,0,j,0],N),([i,1,j,0],T)],F)
    low=newton_check([3*n-2*z for n,z in zip(N,Z)],K,x['bottom_minus_two_thirds_newton'])
    high=newton_check([z-3*t for z,t in zip(Z,T)],K,x['one_third_minus_top_newton'])
    require([p['weights'][i] for p in x['finite_prefix']]==list(range(2,K)),'Complete rank-crossing finite prefix')
    for p in x['finite_prefix']:
        require(p['class_id']==cls and all(w==1 for k,w in enumerate(p['weights']) if k!=i),'Rank-crossing prefix support')
        witness(p,'rank-crossing finite prefix')
    # Exact finite validations of the universal shuffle proof, not its source.
    shuffle_tests=0
    for t in range(2,25):
        for h in range(1,8):
            Zs=comb(t+h,h)
            for rr in range(1,h+1):
                for k in range(1,t):
                    gap=comb(k+rr-1,k)*comb(t-k+h-rr,t-k)
                    require(gap*(t+h)<=h*Zs,'Adjacent-rank shuffle subset bound');shuffle_tests+=1
    # Direct actual-rank checks at the entire tail start and several later lengths.
    rank_checks=[]
    for t in [10,11,12,20,40,100]:
        w=[1]*8;w[i]=t;z=occupancy_count(cores[cls],w);nums=[occupancy_count(cores[cls],w,((i,k),(j,0))) for k in range(t)]
        require(z==ev(Z,t) and nums[0]==ev(N,t) and nums[-1]==ev(T,t),'Rank-tail actual counts')
        require(3*nums[0]>=2*z and 3*nums[-1]<=z,'Rank-tail endpoint thresholds')
        require(all(0<=a-b and (a-b)*(t+M)<=M*z for a,b in zip(nums,nums[1:])),'Actual adjacent-rank gap')
        balanced=[k for k,n in enumerate(nums) if z<=3*n<=2*z];require(balanced,'Actual rank crossing')
        rank_checks.append(dict(t=t,denominator=z,numerators=nums,balanced_zero_based_ranks=balanced))
    records.append(dict(class_id=cls,variable=i,method='rank crossing',outside_fibers=len(F),incomparable_mass=M,tail_start=K,denominator_coefficients=Z,bottom_coefficients=N,top_coefficients=T,bottom_newton=low,top_newton=high))
    require(covered=={(cls,i) for cls in CLASSES for i in range(8)},'All 40 exact supports')
    require(len(c['zero_support_certificates'])==5 and sorted(p['class_id'] for p in c['zero_support_certificates'])==CLASSES,'Exactly five zero-support cases')
    for p in c['zero_support_certificates']:
        require(p['weights']==[1]*8,'Zero support');witness(p,'zero support')
    out=dict(verdict='PASS',scope='C08,C09,C11,C14,C15: every positive-integer inflation with support cardinality <=1 has a balanced pair',classes=CLASSES,exact_support_families=len(covered),polynomial_families=36,inequality_families=3,rank_crossing_families=1,polynomial_grid_instances=evals,polynomial_and_witness_orientation_counts=orientation_counts,newton_symbolic_identities=74,finite_and_zero_witnesses=len(witnesses),shuffle_gap_tests=shuffle_tests,records=records,witnesses=witnesses,rank_tail_validation=rank_checks)
    (R/'audit_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: 40 infinite exact-support families and five zero-support cases; 37 direct outside-fiber reconstructions; 74 symbolic Newton identities; normal/-O-safe checks.')
    print('Polynomial grid instances:',evals,'separate precedence counts:',orientation_counts,'finite/zero witnesses:',len(witnesses),'shuffle gap checks:',shuffle_tests)

if __name__=='__main__':main()
