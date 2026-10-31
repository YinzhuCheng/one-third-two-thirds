from pathlib import Path
from functools import lru_cache
import json,hashlib
p=Path(__file__).resolve().parent;examples={e['id']:e for e in json.loads((p/'examples.json').read_text())['examples']};out={}
for eid in ['E12','E13','E14','E15','E16']:
 e=examples[eid];base=examples[e['extends']] if 'extends'in e else e;vs=base['vertices'];edges=base['relations']+e.get('add_relations',[]) if 'extends'in e else e['relations'];ix={x:i for i,x in enumerate(vs)};pre=[0]*len(vs)
 for rel in edges:
  a,b=rel.split('<');pre[ix[b]]|=1<<ix[a]
 for k in range(len(vs)):
  for j in range(len(vs)):
   if pre[j]>>k&1:pre[j]|=pre[k]
 U=lambda x:{y for y in vs if pre[ix[y]]>>ix[x]&1}
 A=U('v')&U('c1')-U('c2');F=U('c2');S=A-U('d');H=F-U('e');R=A&U('e')
 def count(extra):
  pp=pre.copy()
  for a,b in extra:pp[ix[b]]|=1<<ix[a]
  full=(1<<len(vs))-1
  @lru_cache(None)
  def f(mask):
   if mask==full:return 1
   return sum(f(mask|1<<i) for i in range(len(vs)) if not mask>>i&1 and pp[i]&mask==pp[i])
  return f(0)
 P=[('v','c1')];J=[('v','c1'),('c1','c2'),('c2','d')];avoidS=[('d',s)for s in S];avoidH=[('e',z)for z in H]
 EA=count(P)-count(P+avoidS);EF=count(J)-count(J+avoidH);intersection=count(J)-count(J+avoidS)-count(J+avoidH)+count(J+avoidS+avoidH)
 E=EA+EF-intersection;reverse=[('v','d'),('d','e'),('e','c1')];G=count(reverse)-count(reverse+[('c2',r)for r in R]);K=count([('c1','d')]);N=count([]);R0=count([('c1','v')]);assert 2*K==N+R0+E-G
 out[eid]={'N':N,'K':K,'R0':R0,'E':E,'G':G,'net':E-G}
assert out['E12']['E']==0 and out['E12']['G']==31664
assert out['E13']['E']==52863 and out['E13']['G']==0
assert out['E14']['E']==7149 and out['E14']['G']==51718
assert out['E15']['E']==2852 and out['E15']['G']==7680
assert out['E16']['E']==2110 and out['E16']['G']==14599
(p/'SIGNED_EVENT_VALIDATION.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
manifest={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(p.iterdir()) if x.is_file() and x.name!='MANIFEST.json'};(p/'MANIFEST.json').write_text(json.dumps({'created_utc':'2026-10-31','files':manifest},indent=2))
