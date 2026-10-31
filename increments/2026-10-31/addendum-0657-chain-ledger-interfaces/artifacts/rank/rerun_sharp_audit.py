import json,itertools
from pathlib import Path
root=Path(__file__).resolve().parent;data=json.loads((root/'sharp_rank_witness.json').read_text());V=data['vertices'];n=len(V);ix={x:i for i,x in enumerate(V)}
rel=[[False]*n for _ in V]
for edge in data['relations']:
 a,b=edge.split('<');rel[ix[a]][ix[b]]=True
for k in range(n):
 for i in range(n):
  for j in range(n):rel[i][j]=rel[i][j] or(rel[i][k] and rel[k][j])
assert not any(rel[i][i] for i in range(n))
D={x:{y for y in V if rel[ix[y]][ix[x]]} for x in V};U={x:{y for y in V if rel[ix[x]][ix[y]]} for x in V}
inc=lambda x,y:x!=y and y not in U[x] and x not in U[y]
chain=lambda X:all(not inc(x,y) for x,y in itertools.combinations(X,2))
A=U['v']&U['c1']-U['c2'];F=U['c2'];R=A&U['e'];K=A-{'s'}-R
assert not D['v'] and {x for x in V if inc('v',x)}=={'c1','c2'} and 'c2' in U['c1']
assert U['v']-U['c1']=={'b','d','e'} and 'e' in U['d'] and inc('b','d') and inc('b','e')
assert A-U['d']=={'s'} and 's' in U['b'] and F<=U['e']
vg=[(x,y) for x,y in itertools.combinations(V,2) if inc(x,y) and ((D[x]==D[y] and chain(U[x]-U[y]) and chain(U[y]-U[x])) or (U[x]==U[y] and chain(D[x]-D[y]) and chain(D[y]-D[x])))]
graph={x:set(U[x]) for x in V}
for x,y in itertools.permutations(V,2):
 if inc(x,y) and ((D[x]<=D[y] and chain(U[y]-U[x])) or (U[y]<=U[x] and chain(D[x]-D[y]))):graph[x].add(y)
remaining=set(V);top=[]
while remaining:
 sources=[x for x in V if x in remaining and all(x not in graph[y] for y in remaining)]
 if not sources:break
 top+=sources;remaining-=set(sources)
mods=[]
for mask in range(1,(1<<n)-1):
 if mask.bit_count()<2:continue
 inside=[i for i in range(n) if mask>>i&1];outside=[i for i in range(n) if not mask>>i&1]
 if all(len({(rel[x][y],rel[y][x]) for y in inside})==1 for x in outside):mods.append([V[i] for i in inside])
# Enumerate every linear extension directly; no memoized event counting, no check.py import.
pre=[sum(1<<ix[y] for y in D[x]) for x in V];counts=dict(N=0,R0=0,K=0,E=0,G=0);pos=[0]*n;full=(1<<n)-1
v,a,d,e,s,x=[ix[z] for z in ['v','c1','d','e','s','c2']];rids=[ix[z] for z in R]
def dfs(mask,depth):
 if mask==full:
  counts['N']+=1;counts['R0']+=pos[a]<pos[v];counts['K']+=pos[a]<pos[d]
  counts['E']+=(pos[v]<pos[a] and pos[s]<pos[d])
  counts['G']+=(pos[e]<pos[a] and any(pos[r]<pos[x] for r in rids))
  return
 for i in range(n):
  if not mask>>i&1 and pre[i]&mask==pre[i]:pos[i]=depth;dfs(mask|1<<i,depth+1)
dfs(0,0)
result={'C2':True,'A':sorted(A),'F':sorted(F),'R':sorted(R),'K':sorted(K),'profiles_F':{f:sorted(D[f]&R) for f in sorted(F)},'profiles_Us':{u:sorted(D[u]&R) for u in sorted(U['s'])},'alpha':min([len(R)]+[len(D[f]&R) for f in F]),'beta':min([len(R)]+[len(D[u]&R) for u in U['s']]),'common_anchors':sorted(r for r in R if F|U['s']<=U[r]),'max_inc':max(sum(inc(x,y) for y in V) for x in V),'very_good_pairs':vg,'mixed_topological_order':top,'mixed_remaining':sorted(remaining),'proper_nontrivial_modules':mods,'counts':counts}
print(json.dumps(result,indent=2));(root/'sharp_witness_independent_result.json').write_text(json.dumps(result,indent=2))
assert counts==dict(N=168366,R0=49873,K=104621,E=2690,G=11687)
assert not vg and not mods and not remaining and result['max_inc']==9
