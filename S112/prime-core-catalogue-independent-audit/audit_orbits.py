#!/usr/bin/env python3
"""Independent isomorphism and singleton audit. No catalogue imports.
Canonical form is minimum relabelled strict order over ALL linear extensions,
not over permutations within degree colour classes.
"""
import itertools,json,collections,argparse
from pathlib import Path
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--reference',type=Path,action='append',default=[],help='Optional JSON survivor source; repeat for exact comparisons')
args=parser.parse_args()

def from_masks(p):
 return tuple(frozenset(j for j in range(len(p)) if m>>j&1) for m in p)
def pred(U):return tuple(frozenset(a for a in range(len(U)) if b in U[a]) for b in range(len(U)))
def relabel(U,order):
 inverse={a:i for i,a in enumerate(order)}
 return tuple(sum(1<<inverse[b] for b in U[a]) for a in order)
def extension_orbit(U):
 D=pred(U);remaining=set(range(len(U)));order=[];forms=[]
 def rec():
  if not remaining:forms.append(relabel(U,order));return
  for a in sorted(remaining):
   if not (D[a]&remaining):
    remaining.remove(a);order.append(a);rec();order.pop();remaining.add(a)
 rec();return len(forms),set(forms)
def chain(U,S):return all(b in U[a] or a in U[b] for a,b in itertools.combinations(S,2))
def graph(U):
 n=len(U);D=pred(U);g={a:set() for a in range(2*n)}
 for a in range(n):
  g[2*a].add(2*a+1)
  for b in range(n):
   if b in U[a]:g[2*a+1].add(2*b)
   elif a!=b and a not in U[b]:
    if D[a]<=D[b] and chain(U,U[b]-U[a]):g[2*a].add(2*b)
    if U[b]<=U[a] and chain(U,D[a]-D[b]):g[2*a+1].add(2*b+1)
 return g
def contract(g,S):
 def f(a):return a-1 if a%2 and a//2 in S else a
 h={f(a):set() for a in g}
 for a,bs in g.items():
  for b in bs:
   if f(a)!=f(b):h[f(a)].add(f(b))
 return h
def cyclic(g):
 degree=collections.Counter(b for bs in g.values() for b in bs)
 todo=[a for a in g if not degree[a]];seen=0
 while todo:
  a=todo.pop();seen+=1
  for b in g[a]:
   degree[b]-=1
   if not degree[b]:todo.append(b)
 return seen!=len(g)
def subsets(n):
 for k in range(n+1):yield from itertools.combinations(range(n),k)
def actual_graph(U,w):
 blocks=[];a=0
 for x in w:blocks.append(list(range(a,a+x)));a+=x
 R=[set() for _ in range(a)]
 for i,B in enumerate(blocks):
  for k,x in enumerate(B):
   R[x].update(B[k+1:])
   for j in U[i]:R[x].update(blocks[j])
 D=pred(R);g={x:set(R[x]) for x in range(a)}
 for x in range(a):
  for y in range(a):
   if x!=y and y not in R[x] and x not in R[y]:
    if (D[x]<=D[y] and chain(R,R[y]-R[x])) or (R[y]<=R[x] and chain(R,D[x]-D[y])):g[x].add(y)
 return g

def geometry(U):
 n=len(U);D=pred(U)
 width=max(len(S) for S in subsets(n) if all(not(U[a]&set(S)) for a in S))
 heights=[]
 for a in range(n):heights.append(1+max((heights[b] for b in D[a]),default=0))
 return width,max(heights)

data=json.loads((HERE/'enumeration.json').read_text())
ours={tuple(p) for p in data['survivor_masks']}
assert len(ours)==len(data['survivor_masks'])
comparison=[]
for reference in args.reference:
 author=json.loads(reference.read_text())
 masks=([r['strict_up_masks'] for r in author] if isinstance(author,list) else author['survivor_masks'])
 assert ours=={tuple(p) for p in masks}
 comparison.append({'reference_name':reference.name,'status':'PASS: identical complete survivor sets through n8'})
# Whole-orbit peeling avoids repeating equivalent canonicalization work.
left=set(ours);classes=[]
while left:
 p=min(left,key=lambda p:(len(p),p));e,orbit=extension_orbit(from_masks(p))
 assert orbit<=ours, 'An isomorphism orbit is incomplete in the natural catalogue.'
 assert orbit<=left, 'Previously removed isomorphism orbit overlaps.'
 left-=orbit
 assert e%len(orbit)==0
 width,height=geometry(from_masks(p))
 entry={'n':len(p),'canonical_natural_masks':list(min(orbit)),
 'representative_masks':list(p),'natural_multiplicity':len(orbit),
 'extension_count':e,'automorphism_order':e//len(orbit),'width':width,'height':height}
 g=graph(from_masks(p));forbidden=[];cyclic_count=0
 for S in subsets(len(p)):
  if cyclic(contract(g,set(S))):
   cyclic_count+=1
   if not any(set(T)<=set(S) for T in forbidden):forbidden.append(list(S))
 entry['minimal_forbidden_singleton_sets']=forbidden
 entry['cyclic_singleton_patterns']=cyclic_count
 classes.append(entry)
classes.sort(key=lambda x:(x['n'],x['canonical_natural_masks']))
# Audit every survivor-class singleton pattern against an ACTUAL inflated-poset forced graph.
all_actual_checks=0
for entry in classes:
 U=from_masks(entry['representative_masks']);g=graph(U);n=len(U)
 for S in subsets(n):
  w=[1 if i in S else 2 for i in range(n)]
  assert cyclic(contract(g,set(S)))==cyclic(actual_graph(U,w))
  all_actual_checks+=1
# Check the stated n7 characterization and explicit witness edges separately.
p=(40,124,104,32,32,0,0);U=from_masks(p);g=graph(U);checks=0
for S in subsets(7):
 w=[1 if i in S else 2 for i in range(7)]
 assert cyclic(contract(g,set(S)))==cyclic(actual_graph(U,w))
 assert cyclic(contract(g,set(S)))==(0 in S or 6 in S)
 checks+=1
# Human-readable witness edges are checked directly, including both hypotheses.
D=pred(U)
witnesses=[]
for label,a,b,kind in [('B0 to B2',0,2,'lower'),('T2 to T0',2,0,'upper'),('T3 to T6',3,6,'upper'),('B6 to B3',6,3,'lower')]:
 if kind=='lower':
  assert D[a]<=D[b] and chain(U,U[b]-U[a])
  witnesses.append({'edge':label,'rule':kind,'down_source':sorted(D[a]),'down_target':sorted(D[b]),'upper_difference':sorted(U[b]-U[a])})
 else:
  assert U[b]<=U[a] and chain(U,D[a]-D[b])
  witnesses.append({'edge':label,'rule':kind,'upper_target':sorted(U[b]),'upper_source':sorted(U[a]),'down_difference':sorted(D[a]-D[b])})
result={'status':'PASS','catalogue_comparison':comparison,
'classes_by_n':dict(collections.Counter(x['n'] for x in classes)),
'all_class_actual_endpoint_equivalence_checks':all_actual_checks,'n7_actual_endpoint_equivalence_checks':checks,'n7_cycle_witness_edges':witnesses,'classes':classes}
(HERE/'orbit_and_singleton_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='classes'},indent=2))
print('n8 width/height/multiplicity:',[(x['width'],x['height'],x['natural_multiplicity']) for x in classes if x['n']==8])
