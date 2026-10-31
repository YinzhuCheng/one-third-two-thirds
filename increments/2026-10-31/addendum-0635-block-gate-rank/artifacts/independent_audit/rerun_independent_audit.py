import json,itertools,functools,hashlib
from fractions import Fraction
from pathlib import Path
path=(Path(__file__).resolve().parent / 'free_residual_hits.json'); raw=path.read_bytes(); source=json.loads(raw)
p=next(x for x in source if x.get('N')==201453)
V=p['V'];n=len(V);ix={x:i for i,x in enumerate(V)};full=(1<<n)-1
assert n==15 and len(set(V))==n
# Independent reachability: traverse the input edges from each vertex.
adj={x:set() for x in V}
for rel in p['relations']:
 a,b=rel.split('<');assert a in ix and b in ix and a!=b;adj[a].add(b)
U={}
for a in V:
 stack=list(adj[a]);seen=set()
 while stack:
  x=stack.pop()
  if x not in seen:seen.add(x);stack.extend(adj[x])
 assert a not in seen
 U[a]=seen
D={a:{b for b in V if a in U[b]} for a in V}
I={a:set(V)-{a}-U[a]-D[a] for a in V}
chain=lambda X:all(b in U[a] or a in U[b] for a,b in itertools.combinations(X,2))
A=(U['v']&U['c1'])-U['c2'];F=U['c2'];T=U['v']-U['c1'];S=A-U['d']
H=(A&U['d'])-U['e'];R=(A-{'s'})&U['e'];anchors={a for a in R if F|U['s'] <= U[a]}
assert D['v']==set() and I['v']=={'c1','c2'} and 'c2' in U['c1']
assert T=={'b','d','e'} and 'e' in U['d'] and {'d','e'}<=I['b']
assert A=={'s','a1','a2','a3','a4'} and F=={'f0','f1','f2','f3'}
assert S=={'s'} and 's' in I['b'] and F<=U['e']
assert H=={'a1'} and 'a1' in I['e'] and R=={'a2','a3','a4'} and len(anchors)<2
assert set(V)=={'v','c1','c2'}|T|A|F
assert max(map(len,I.values()))==9
# Full P (not induced subposets): primal, dual very-good pair criteria.
vgp=[];vgd=[]
for a,b in itertools.combinations(V,2):
 if b not in I[a]:continue
 if D[a]==D[b] and chain(U[a]-U[b]) and chain(U[b]-U[a]):vgp.append([a,b])
 if U[a]==U[b] and chain(D[a]-D[b]) and chain(D[b]-D[a]):vgd.append([a,b])
# S112 mixed graph: retain all strict order arcs and add both forcing rules.
G={a:set(U[a]) for a in V};primal=[];dual=[]
for a,b in itertools.permutations(V,2):
 if b not in I[a]:continue
 if D[a]<=D[b] and chain(U[b]-U[a]):G[a].add(b);primal.append([a,b])
 if U[b]<=U[a] and chain(D[a]-D[b]):G[a].add(b);dual.append([a,b])
remaining=set(V);topo=[]
while remaining:
 zero=sorted(a for a in remaining if not any(a in G[b] for b in remaining))
 if not zero:break
 a=zero[0];topo.append(a);remaining.remove(a)
assert len(topo)==n
assert all(topo.index(a)<topo.index(b) for a in V for b in G[a])
# Exhaust all proper subsets of size >=2, using the outside-point uniformity definition.
modules=[];checks=0
for mask in range(1,full):
 if mask.bit_count()<2:continue
 checks+=1;M={V[j] for j in range(n) if mask>>j&1}
 if all(len({-1 if y in U[x] else 1 if y in D[x] else 0 for y in M})==1 for x in set(V)-M):modules.append(sorted(M))
assert checks==32751
pred=[sum(1<<ix[a] for a in D[b]) for b in V]
# Two-sided ideal DP counts each occurrence of i being inserted before j.
fw=[0]*(full+1);fw[0]=1;available={}
for m in range(full+1):
 if not fw[m]:continue
 av=[j for j in range(n) if not m>>j&1 and pred[j]&m==pred[j]];available[m]=av
 for j in av:fw[m|1<<j]+=fw[m]
bw=[0]*(full+1);bw[full]=1
for m in sorted(available,reverse=True):
 if m!=full:bw[m]=sum(bw[m|1<<j] for j in available[m])
N=fw[full];assert N==bw[0]
before=[[0]*n for _ in V]
for m,av in available.items():
 for a in av:
  w=fw[m]*bw[m|1<<a]
  for b in range(n):
   if b!=a and not m>>b&1:before[a][b]+=w
assert all(before[a][b]+before[b][a]==N for a,b in itertools.combinations(range(n),2))
R0=before[ix['c1']][ix['v']];K=before[ix['c1']][ix['d']]
assert(N,R0,K)==(201453,66867,137524)
# Independent direct enumeration of all linear extensions, without the DP counts.
# Track positions of just c1,v,d, and count each leaf exactly once.
leaf=cnt0=cntd=0
prefix=[]
def visit(mask):
 global leaf,cnt0,cntd
 if mask==full:
  leaf+=1
  cnt0+=prefix.index(ix['c1'])<prefix.index(ix['v'])
  cntd+=prefix.index(ix['c1'])<prefix.index(ix['d'])
  return
 for j in range(n):
  if not mask>>j&1 and pred[j]&mask==pred[j]:
   prefix.append(j);visit(mask|1<<j);prefix.pop()
visit(0)
assert (leaf,cnt0,cntd)==(N,R0,K)
balanced=[]
for a,b in itertools.combinations(V,2):
 if b in I[a] and N<=3*before[ix[a]][ix[b]]<=2*N:
  k=before[ix[a]][ix[b]];balanced.append({'pair':[a,b],'count':k,'fraction':str(Fraction(k,N))})
force_pairs=sorted(set(map(tuple,primal))|set(map(tuple,dual)))
actual_good=[{'pair':[a,b],'count':before[ix[a]][ix[b]]} for a,b in force_pairs if 2*before[ix[a]][ix[b]]<=N]
min_force=min((before[ix[a]][ix[b]],a,b) for a,b in force_pairs)
cover=[[a,b] for a in V for b in U[a] if not U[a]&D[b]]
out={'source':str(path),'source_sha256':hashlib.sha256(raw).hexdigest(),'V':V,'input_generating_relations':p['relations'],'transitive_reduction':sorted(cover),'D':{a:sorted(D[a])for a in V},'U':{a:sorted(U[a])for a in V},'I':{a:sorted(I[a])for a in V},'complete_C2':True,'T':sorted(T),'A':sorted(A),'F':sorted(F),'S':sorted(S),'d_only_H':sorted(H),'R':sorted(R),'anchors_below_every_F_and_U_s':sorted(anchors),'anchor_deficits':{a:sorted((F|U['s'])-U[a])for a in R},'b_incomparable_s':True,'e_below_all_F':True,'incomparability_degrees':{a:len(I[a])for a in V},'max_incomparability_degree':9,'positive_very_good_pairs':vgp,'dual_very_good_pairs':vgd,'S112_primal_arcs':primal,'S112_dual_arcs':dual,'S112_mixed_topological_order':topo,'S112_mixed_cycle':bool(remaining),'module_subsets_checked':checks,'proper_nontrivial_autonomous_modules':modules,'reachable_ideals':len(available),'N':N,'R0':R0,'K':K,'q0':str(Fraction(R0,N)),'p_c1_before_d':str(Fraction(K,N)),'q0_minus_one_third':str(Fraction(R0,N)-Fraction(1,3)),'p_c1_before_d_minus_two_thirds':str(Fraction(K,N)-Fraction(2,3)),'strong_bound_excess_numerator':2*K-N-R0,'fixed_menu_pairs_both_unbalanced':3*R0<N and 3*K>2*N,'direct_enumeration_totals':[leaf,cnt0,cntd],'balanced_pair_count':len(balanced),'balanced_pairs':balanced,'structural_good_direction_count':len(force_pairs),'actual_good_directions':actual_good,'min_structural_good_direction_count_and_pair':list(min_force),'all_pair_order_counts':{a:{b:before[ix[a]][ix[b]]for b in V if a!=b}for a in V}}
(Path(__file__).resolve().parent / 'audit_free_residual_independent_result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ['V','input_generating_relations','transitive_reduction','D','U','I','S112_primal_arcs','S112_dual_arcs','all_pair_order_counts','balanced_pairs']},ensure_ascii=False,indent=2))
print('Balanced pairs:',balanced[:12])
