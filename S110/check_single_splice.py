#!/usr/bin/env python3
"""Independent exact-rational one-splice check on a genuine connected D=2 family.
No randomized tests, floats used only in human-readable secondary displays.
"""
from fractions import Fraction
import json
from pathlib import Path

OUT = Path(__file__).parent

def path_poset(n):
    # i <_P j iff j-i >= 2, using zero-based indices internally.
    return [((1 << max(0, j-1)) - 1) for j in range(n)]

def count_dp(pred, D):
    n=len(pred); F=[{0:1}]; T=[]
    for r in range(n):
        nextF={}; edges={}
        for J,w in F[-1].items():
            row=[]
            for j in range(max(0,r-D),min(n,r+D+1)):
                bj=1<<j
                if J&bj or pred[j]&~J: continue
                JJ=J|bj
                # Rank-drift constraints for the new ideal.
                low=max(0,r+1-D); high=min(n,r+1+D)
                if ((1<<low)-1)&~JJ or JJ>>high: continue
                row.append((j,JJ)); nextF[JJ]=nextF.get(JJ,0)+w
            edges[J]=row
        assert nextF
        F.append(nextF); T.append(edges)
    full=(1<<n)-1
    assert set(F[-1])=={full}
    B=[None]*(n+1); B[n]={full:1}
    for r in range(n-1,-1,-1):
        B[r]={J:sum(B[r+1].get(JJ,0) for _,JJ in row) for J,row in T[r].items()}
        assert all(w>0 for w in B[r].values())
    E=F[n][full]
    assert E==B[0][0]
    for r in range(n+1): assert sum(F[r][J]*B[r][J] for J in F[r])==E
    return F,B,T,E

def profile(V,r,D):
    out={}
    for J,w in V[r].items():
        key=tuple(i-r for i in range(r-D+1,r+D+1) if J&(1<<(i-1)))
        assert len(key)==D
        out[key]=w
    return out

def norm(v):
    s=sum(v.values()); return {k:Fraction(x,s) for k,x in v.items()}

def relerr(v,w):
    assert set(v)==set(w)
    return max(abs(w[k]/v[k]-1) for k in v)

def reverse_probs(F,B,T,E,n):
    out={}
    for x in range(n-1):
        y=x+1; total=0
        for r in range(n):
            for J,row in T[r].items():
                if J&(1<<x): continue
                for j,JJ in row:
                    if j==y: total+=F[r][J]*B[r+1][JJ]
        out[x+1]=Fraction(total,E)
    return out

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def fmt(x): return str(x)
def fp(v): return {str(k):fmt(w) for k,w in sorted(v.items())}

D=2; R=2*D-1; h=R+D; K=h+D
n=40; a=9; b=26; L=b-a; nn=n-L
assert a>=K and b+K<=n and L>=2*K+1
P=path_poset(n); PP=path_poset(nn)
# Explicitly verify splice of R-local relation symbols gives PP.
def code(pred):
    return [tuple(bool(pred[j]&(1<<(j-t))) if j>=t else None for t in range(1,R+1)) for j in range(len(pred))]
word=code(P); spliced=word[:a]+word[b:]
assert spliced==code(PP)
# Full buffer relations agree, including comparability beyond the coding range.
for i in range(a-K,a+K):
    for j in range(a-K,a+K):
        assert bool(P[j]&(1<<i))==bool(P[j+L]&(1<<(i+L)))

F,B,T,E=count_dp(P,D); FF,BB,TT,EE=count_dp(PP,D)
assert E==fib(n+1) and EE==fib(nn+1)
c=a-h; d=a+h
f1=norm(profile(F,c,D)); f2=norm(profile(F,c+L,D))
g1=norm(profile(B,d,D)); g2=norm(profile(B,d+L,D))
ef=relerr(f1,f2); eb=relerr(g1,g2); eta=max(ef,eb)
assert ef>0 and eb>0 and eta<=Fraction(1,2)
assert profile(FF,d,D)==profile(F,d,D)
assert profile(BB,d,D)==profile(B,d+L,D)
assert profile(FF,c,D)==profile(F,c,D)
assert profile(BB,c,D)==profile(B,c+L,D)
old=reverse_probs(F,B,T,E,n); new=reverse_probs(FF,BB,TT,EE,nn)
for i,p in old.items(): assert p==Fraction(fib(i)*fib(n-i),fib(n+1))
for i,p in new.items(): assert p==Fraction(fib(i)*fib(nn-i),fib(nn+1))
rows=[]
for i,p in new.items():
    if i<a: kind='surviving-left'; witness=i
    elif i>a: kind='surviving-right'; witness=i+L
    else: kind='new-cross-seam'; witness=i
    q=old[witness]; error=abs(p-q)
    assert error<=eta
    if kind=='surviving-left': assert error<=eb
    if kind=='surviving-right': assert error<=ef
    if kind=='new-cross-seam':
        # Actual original endpoints a,b+1 were comparable, yet the transplanted witness a,a+1 was incomparable.
        assert P[b]&(1<<(a-1))
        assert not(P[a]&(1<<(a-1)))
        assert error<=eb
    rows.append({'kind':kind,'new_pair':[i,i+1],
                 'actual_original_pair':[i if i<=a else i+L,(i+1) if i+1<=a else i+1+L],
                 'old_witness_pair':[witness,witness+1],
                 'old_reverse_probability':fmt(q),'new_reverse_probability':fmt(p),
                 'absolute_error':fmt(error),'error_float':float(error)})
maxrow=max(rows,key=lambda row:Fraction(row['absolute_error']))
result={'family':'P_n: i<j iff j-i>=2; incomparability graph is a path',
        'parameters':dict(D=D,R=R,h=h,K=K,n=n,a=a,b=b,L=L,new_n=nn),
        'extension_counts':{'old':E,'new':EE},
        'profiles':{'F_left':fp(f1),'F_right':fp(f2),'B_left':fp(g1),'B_right':fp(g2)},
        'relative_errors':{'F':fmt(ef),'B':fmt(eb),'eta':fmt(eta),'eta_float':float(eta)},
        'verified_new_incomparable_pairs':len(rows),
        'max_probability_error':maxrow,
        'new_cross_seam_pair':next(row for row in rows if row['kind']=='new-cross-seam'),
        'all_pairs':rows,
        'checks':['original and spliced words are valid actual posets', 'matched complete relation buffers',
                  'nonidentical normalized forward and backward profiles','exact DP extension counts',
                  'exact DP profiles at both protected cuts','all pair probabilities independently checked against Fibonacci formulas',
                  'all retained same-side pair bounds','new cross-seam actual identity and original witness distinction']}
(OUT/'single_splice_exact_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='all_pairs'},indent=2))
