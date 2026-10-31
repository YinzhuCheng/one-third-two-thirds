# Independent wordwise verification, not the ideal-DP event count.
import json
from collections import Counter
from pathlib import Path
p=Path(__file__).resolve().parent;E=json.loads((p/'candidate.json').read_text());V=E['vertices'];n=len(V);ix={v:i for i,v in enumerate(V)}
D={v:set()for v in V}
for relation in E['relations']:
 a,b=relation.split('<');D[b].add(a)
for k in V:
 for v in V:
  if k in D[v]:D[v]|=D[k]
U={v:{u for u in V if v in D[u]}for v in V};A=U['v']&U['c1']-U['c2'];R=A&U['e'];assert A-U['d']=={'s'} and U['s']<=U['e']
pre=[sum(1<<ix[d]for d in D[v])for v in V];full=(1<<n)-1
sw={'c1':'d','d':'c1','s':'e','e':'s'}
source=set();target=set();images=set();c=Counter()
def visit(word,mask):
 if mask!=full:
  for j,v in enumerate(V):
   if not mask>>j&1 and pre[j]&mask==pre[j]:visit(word+(v,),mask|1<<j)
  return
 c['N']+=1;t={v:i for i,v in enumerate(word)}
 late=any(t[r]<t['c2']for r in R)
 isE=t['v']<t['c1']<t['s']<t['d'] and late
 isG=t['v']<t['d']<t['e']<t['c1'] and late
 isGA=isG and t['c1']<t['s'] and all(t['s']<t[u]for u in U['e']) and ('b'not in D['s'] or t['b']<t['e'])
 if isE:
  source.add(word);out=tuple(sw.get(v,v)for v in word);tt={v:i for i,v in enumerate(out)}
  assert all(tt[d]<tt[v]for v in V for d in D[v]);assert tt['v']<tt['d']<tt['e']<tt['c1'];assert any(tt[r]<tt['c2']for r in R)
  images.add(out)
 if isGA:target.add(word)
visit((),0)
assert images==target and len(source)==len(images)
res={'N':c['N'],'source_count':len(source),'image_count':len(images),'exact_target_count':len(target),'every_image_legal':True,'image_equals_characterized_target':True}
print(json.dumps(res,indent=2));(p/'INJECTION_WORDWISE_VALIDATION.json').write_text(json.dumps(res,indent=2))
