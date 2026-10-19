"""One-pass fixed controls only. No poset search and no producer batch rerun."""
from itertools import permutations, combinations
from fractions import Fraction
from math import comb
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).parent
letters = ('d','q','y','z')
words = [p for p in permutations(letters) if p.index('d') < p.index('q')]
pairs = [('d','q'), ('d','y'), ('d','z'), ('y','q'), ('q','z'), ('y','z')]
def K(p):
    return len(p)-1-p.index('q')
def probs(w, s):
    weighted = [(p, n*comb(s+K(p), K(p))) for p,n in w.items()]
    T = sum(n for p,n in weighted)
    return T, {''.join(E): Fraction(sum(n for p,n in weighted if p.index(E[0])<p.index(E[1])), T) for E in pairs}
def safe(v):
    return v < Fraction(1,3) or v > Fraction(2,3)
def jsonable(x):
    if isinstance(x, Fraction): return str(x)
    if isinstance(x, tuple): return list(x)
    raise TypeError(type(x))

# Fixed producer weighted four-word model. Four total-order supports, not actual uniform LE.
w = {('y','z','d','q'):24, ('d','y','q','z'):20, ('d','q','y','z'):1, ('d','q','z','y'):1}
r = {}
for s in (1,2):
    T,p = probs(w,s)
    r[s] = {'T':T,'p':p,'all_external_safe':all(safe(v) for v in p.values())}
assert r[2]['all_external_safe']
assert not r[1]['all_external_safe']
assert r[1]['p']['dy'] == Fraction(23,35)
assert r[2]['p']['dy'] == Fraction(3,4)
assert r[1]['T'] == 70 and r[2]['T'] == 96

# A full-support perturbation of the exact same fixed R. Retain every legal LE with positive integer weight.
wp = {p: 10*w.get(p,0)+1 for p in words}
rp = {}
for s in (1,2):
    T,p = probs(wp,s)
    rp[s] = {'T':T,'p':p,'all_external_safe':all(safe(v) for v in p.values())}
assert len(wp) == 12 and min(wp.values()) == 1
assert rp[2]['all_external_safe'] and not rp[1]['all_external_safe']

# Actual uniform extensions of this same fixed R: independent direct complete-poset counting.
a = Counter(K(p) for p in words)
actual = {'window_coefficients':[a[j] for j in range(3)]}
for m in (1,2):
    chain = ('d','q') + tuple('c'+str(i) for i in range(m))
    labels = chain + ('y','z')
    exts = [p for p in permutations(labels) if all(p.index(chain[i])<p.index(chain[i+1]) for i in range(len(chain)-1))]
    T, p = probs({w:1 for w in words},m)
    direct = {''.join(E):Fraction(sum(s.index(E[0])<s.index(E[1]) for s in exts),len(exts)) for E in pairs}
    assert len(exts)==T and direct==p
    actual[m] = {'T':T,'p':p,'all_external_safe':all(safe(v) for v in p.values())}
assert actual['window_coefficients']==[6,4,2]
assert actual[1]['p']['yz']==actual[2]['p']['yz']==Fraction(1,2)

# Strict endpoint: same permitted K-window support, with (a,b,c)=(3,0,2).
# Event y before d is the entire K0 support. TV=eta gives p1=1/3 exactly.
we = {('y','z','d','q'):3, ('d','q','y','z'):1, ('d','q','z','y'):1}
def mu(w,s):
    z = sum(n*comb(s+K(p),K(p)) for p,n in w.items())
    return {p:Fraction(n*comb(s+K(p),K(p)),z) for p,n in w.items()}
m1,m2 = mu(we,1),mu(we,2)
tv = sum(abs(m1[p]-m2[p]) for p in we)/2
p1 = sum(v for p,v in m1.items() if p.index('y')<p.index('d'))
p2 = sum(v for p,v in m2.items() if p.index('y')<p.index('d'))
assert p1==Fraction(1,3) and p2==Fraction(1,5) and tv==Fraction(2,15)==Fraction(1,3)-p2
endpoint = {'TV':tv,'p_at_k1':p1,'p_at_m2':p2,'eta_for_event':Fraction(1,3)-p2}

# Both branches of t=2 max formula, using fixed positive a_j. Direct full-support and K TVs.
tv_controls=[]
for name,wc,k,m in [('uniform_R', {p:1 for p in words},1,2),('weighted_R',w,1,2),('endpoint',we,1,2),('upper_cut_dominant',{('y','z','d','q'):1,('d','y','q','z'):1,('d','q','y','z'):1,('d','q','z','y'):1},1,2)]:
    mk,mm=mu(wc,k),mu(wc,m)
    qk=[sum(v for p,v in mk.items() if K(p)==j) for j in range(3)]
    qm=[sum(v for p,v in mm.items() if K(p)==j) for j in range(3)]
    tvfull=sum(abs(mk[p]-mm[p]) for p in wc)/2
    tvk=sum(abs(qk[j]-qm[j]) for j in range(3))/2
    cut0=qk[0]-qm[0]; cut1=qm[2]-qk[2]
    assert tvfull==tvk==max(cut0,cut1)
    tv_controls.append({'name':name,'qk':qk,'qm':qm,'TV':tvfull,'cuts':[cut0,cut1]})

out = {'weighted_control':r,'full_support_perturbation':rp,'actual_uniform_control':actual,'strict_endpoint_control':endpoint,'tv_controls':tv_controls,'checks':'PASS'}
(ROOT/'minimal_controls.json').write_text(json.dumps(out,default=jsonable,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,default=jsonable,ensure_ascii=False,indent=2))
