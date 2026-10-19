"""Final fixed full-support four-point diagnostic, reconstructed word by word."""
from fractions import Fraction as F
from itertools import permutations,combinations
from math import comb
from pathlib import Path
import json
letters=('d','q','y','z')
words=[w for w in permutations(letters) if w.index('d')<w.index('q')]
base={('y','z','d','q'):24,('d','y','q','z'):20,('d','q','y','z'):1,('d','q','z','y'):1}
weights={w:base.get(w,1) for w in words}
K=lambda w:len(w)-1-w.index('q')
co=lambda event=None:[sum(n for w,n in weights.items() if K(w)==j and (event is None or w.index(event[0])<w.index(event[1]))) for j in range(3)]
T=co();assert T==[29,23,2]
evalpoly=lambda x,s:sum(x[j]*comb(s+j,j) for j in range(3))
rep={'total':T,'support':len(weights),'pairs':{}}
for E in combinations(letters,2):
    v=co(E);q1=F(evalpoly(v,1),evalpoly(T,1));q2=F(evalpoly(v,2),evalpoly(T,2))
    a,b,c=F(v[2],2),F(v[1])+F(3*v[2],2),F(sum(v))
    A,B,C=F(T[2],2),F(T[1])+F(3*T[2],2),F(sum(T))
    h2=a*B-b*A;h1=2*(a*C-c*A);h0=b*C-c*B
    shifted=[h2,h1+2*h2,h0+h1+h2]
    assert all(x>=0 for x in shifted) or all(x<=0 for x in shifted)
    assert q2<F(1,3) or q2>F(2,3)
    rep['pairs'][''.join(E)]={'event':v,'p1':str(q1),'p2':str(q2),'derivative_shift':[str(x) for x in shifted]}
assert rep['pairs']['dy']['p1']=='53/81'
rep['checks']='PASS'
(Path(__file__).parent/'simplified_weight_control.json').write_text(json.dumps(rep,indent=2)+'\n')
print(json.dumps(rep,indent=2))
