import json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parent
from collections import Counter
j=json.load(open(ROOT/'EXAMPLE.json'));V=j['V'];edges={tuple(e.split('<')) for e in j['relations']}
while True:
 new=edges|{(a,d) for a,b in edges for c,d in edges if b==c}
 if new==edges:break
 edges=new
U=lambda a:{b for x,b in edges if x==a}
A=U('v')&U('c1')-U('c2');F=U('c2');L=A&U('b');C=F&U('b');Q=set(V)-{'v','c1','b','c2'};pre={a:{b for b,x in edges if x==a}&Q for a in Q};words=[]
def rec(w,left):
 if not left:words.append(tuple(w));return
 for a in sorted(left):
  if not(pre[a]&left):rec(w+[a],left-{a})
rec([],Q);valid=set(words);n=len(Q);result={'Q_extensions':len(words),'choices':{}}
for l in ['a2','a4']:
 out=Counter()
 for k in range(n+1):
  S={w for w in words if not(set(w[:k])&F)}
  T={w for w in words if not(set(w[:k])&({l}|C))}
  T0={w for w in words if not(set(w[:k])&(L|C))}
  image=set()
  for w in S:
   z=list(w)
   if l in w[:k]:
    p,q=w.index(l),w.index('f0');z[p],z[q]=z[q],z[p]
   z=tuple(z);assert z in T and z in valid;image.add(z)
  assert len(image)==len(S)
  out['B']+=len(S);out['Z']+=len(T0);out['Z1']+=len(T);out['Hplus']+=len(T-T0);out['Hminus']+=len(T0-T);out['G']+=len(T-image)
  for w in T-image:
   # Check missing-image characterization directly, not only its aggregate weight.
   p,q=w.index('f0'),w.index(l);assert p<k<=q
   z=list(w);z[p],z[q]=z[q],z[p];assert tuple(z) not in valid
   lower=any(p<w.index(x)<q for x in (pre[l]-pre['f0']))
   upper=any(p<w.index(x)<q for x in (U('f0')-U(l))&Q)
   assert lower or upper
   out['G_lower']+=lower;out['G_upper']+=upper;out['G_both']+=lower and upper;out['G_upper_only']+=upper and not lower
 result['choices'][l]=dict(out)
print(json.dumps(result,indent=2));json.dump(result,open(ROOT/'block_defect_15_independent_validation.json','w'),indent=2)
