from pathlib import Path
from fractions import Fraction
import json,hashlib,itertools
p=Path(__file__).resolve().parent;e=next(e for e in json.loads((p/'examples.json').read_text())['examples']if e['id']=='E16');V=e['vertices'];D={x:set()for x in V}
for rel in e['relations']:
 a,b=rel.split('<');D[b].add(a)
for k in V:
 for j in V:
  if k in D[j]:D[j]|=D[k]
U={x:{y for y in V if x in D[y]}for x in V};incomp=lambda a,b:a!=b and a not in D[b]and b not in D[a]
chain=lambda S:all(not incomp(a,b)for a,b in itertools.combinations(S,2))
assert max(len(V)-1-len(D[x])-len(U[x])for x in V)==9
assert set(V)-{'v'}-U['v']=={'c1','c2'}
A=U['v']&U['c1']-U['c2'];F=U['c2'];assert A=={'s','r','t','u','w'}and F=={'f0','f1','f2','f3'};assert U['v']-U['c1']=={'b','d','e'}
assert A-U['d']=={'s'}and F<=U['e']and A-{'s','w'}<=U['e']and 'b' in D['s']and incomp('e','w')and 'd' in D['w']and 'b' not in D['w']
assert all(F|U['s']<=U[x]for x in ['r','t'])
vg=[]
for a,b in itertools.combinations(V,2):
 if incomp(a,b)and ((D[a]==D[b]and chain(U[a]-U[b])and chain(U[b]-U[a]))or(U[a]==U[b]and chain(D[a]-D[b])and chain(D[b]-D[a]))):vg.append([a,b])
assert not vg
adj={a:set(U[a])for a in V}
for a,b in itertools.permutations(V,2):
 if incomp(a,b)and((D[a]<=D[b]and chain(U[b]-U[a]))or(U[b]<=U[a]and chain(D[a]-D[b]))):adj[a].add(b)
ind={a:sum(a in adj[b]for b in V)for a in V};stack=[a for a in V if not ind[a]];order=[]
while stack:
 a=stack.pop();order.append(a)
 for b in adj[a]:
  ind[b]-=1
  if not ind[b]:stack.append(b)
assert len(order)==len(V)
modules=[]
for mask in range(1,(1<<len(V))-1):
 if mask.bit_count()<2:continue
 M={V[i]for i in range(len(V))if mask>>i&1}
 if all(len({-1 if x in D[y]else 1 if y in D[x]else 0 for y in M})==1 for x in set(V)-M):modules.append(sorted(M))
assert modules==[]
assert Fraction(5,18)<Fraction(38912,136953)<Fraction(1,3)
assert Fraction(2110,136953)<=Fraction(1,3)-Fraction(38912,136953)
result={'example':'E16','C2':True,'max_incomparability_degree':9,'T13_hypotheses':True,'very_good_or_dual_pairs':vg,'mixed_graph_topological_order':order,'all_proper_nontrivial_autonomous_modules':modules,'old_r2_window':True,'old_unsigned_error_budget_covers_this_example':True}
(p/'E16_STRUCTURE_VALIDATION.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
manifest={x.name:hashlib.sha256(x.read_bytes()).hexdigest()for x in sorted(p.iterdir())if x.is_file()and x.name!='MANIFEST.json'};(p/'MANIFEST.json').write_text(json.dumps({'created_utc':'2026-10-31','files':manifest},indent=2))
