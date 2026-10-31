import json, functools, hashlib
from pathlib import Path
p=Path(__file__).resolve().parent; data=json.loads((p/'examples.json').read_text()); by={e['id']:e for e in data['examples']}; out=[]
for e in data['examples']:
 base=by[e['extends']] if 'extends' in e else e
 vs=base['vertices']; edges=base['relations']+e.get('add_relations',[]) if 'extends' in e else e['relations']; index={x:i for i,x in enumerate(vs)}; pre=[0]*len(vs)
 for s in edges:
  a,b=s.split('<');pre[index[b]]|=1<<index[a]
 for k in range(len(vs)):
  for j in range(len(vs)):
   if pre[j]>>k&1:pre[j]|=pre[k]
 assert all(not (pre[j]>>j&1) for j in range(len(vs)))
 def count(extra=None, deleted=()):
  pp=pre.copy()
  if extra:
   a,b=map(index.get,extra.split('<'));pp[b]|=1<<a
  full=(1<<len(vs))-1
  @functools.lru_cache(None)
  def go(s):
   if s==full:return 1
   return sum(go(s|1<<i) for i in range(len(vs)) if not s>>i&1 and pp[i]&s==pp[i])
  return go(sum(1<<index[x] for x in deleted))
 den=count();assert den==e['linear_extensions'],(e['id'],den)
 if 'deletion_counts' in e:
  deletions={'R0':['c1'],'R1':['v','c1'],'B':['v','b','c1'],'Z':['c1','c2']}
  for key, deleted in deletions.items(): assert count(deleted=deleted)==e['deletion_counts'][key]
 from fractions import Fraction
 for pair,val in e['probabilities'].items():assert Fraction(count(pair),den)==Fraction(val),(e['id'],pair)
 if 'q_distribution' in e:
  cur={0:1}; nums=[]; Y=sum(1<<index[x] for x in ['v','b','d','e'])
  for k in range(5):
   nxt={}; num=0
   for mask, ways in cur.items():
    deleted=[vs[j] for j in range(len(vs)) if mask>>j&1]+['c1']
    num+=ways*count(deleted=deleted)
    for j in range(len(vs)):
     if Y>>j&1 and not mask>>j&1 and pre[j]&mask==pre[j]: nxt[mask|1<<j]=nxt.get(mask|1<<j,0)+ways
   nums.append(num);cur=nxt
  assert [Fraction(n,den) for n in nums]==[Fraction(q) for q in e['q_distribution']]
 out.append(f"{e['id']}: e(P)={den}; all stored pair probabilities match exact ideal-DP recomputation")
print('\n'.join(out))
(p/'VALIDATION.txt').write_text('2026-10-31 independent packaging-stage exact recomputation\n'+'\n'.join(out)+'\nOnly the stored extension totals and pair probabilities were recomputed. No general theorem, bad-fiber mass, graph audit, or priority verification is implied.\n')
manifest={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(p.iterdir()) if x.is_file() and x.name!='MANIFEST.json'}
(p/'MANIFEST.json').write_text(json.dumps({'created_utc':'2026-10-31','files':manifest},indent=2))
