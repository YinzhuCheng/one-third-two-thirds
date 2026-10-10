#!/usr/bin/env python3
"""Independent structural + exact-probability tests of finite-window compression."""
import collections, fractions, hashlib, json, math, random
from pathlib import Path
OUT=Path(__file__).parent
SEED=948013
rng=random.Random(SEED)

def valid(inc,D):
 n=len(inc)
 assert all(i not in inc[i] and len(inc[i])<=D for i in range(n))
 assert all(i in inc[j] for i in range(n) for j in inc[i])
 R=2*D-1
 for i in range(n):
  for k in inc[i]:
   if i<k:
    assert k-i<=R
    assert all(j in inc[i] or k in inc[j] for j in range(i+1,k))
 return True

def word(inc,D):
 R=2*D-1
 return tuple(sum((1<<(d-1)) for d in range(1,R+1) if i-d>=0 and i-d in inc[i]) for i in range(len(inc)))

def decode(w,D):
 n=len(w); R=2*D-1; inc=[set() for _ in w]
 for j,z in enumerate(w):
  for d in range(1,R+1):
   if z&(1<<(d-1)):
    assert j-d>=0, ('invalid leading bit',j,d)
    inc[j].add(j-d); inc[j-d].add(j)
 valid(inc,D)
 return inc

def bfs(g,start,end):
 if start==end:return []
 prev={start:None}; qq=collections.deque([start])
 while qq:
  u=qq.popleft()
  for v,last in g[u]:
   if v not in prev:
    prev[v]=(u,last);qq.append(v)
    if v==end:
     edges=[];cur=end
     while cur!=start:
      par,last=prev[cur];edges.append(last);cur=par
     return edges[::-1]
 raise AssertionError('unreachable')

def q_start(n,q,a,b):
 assert b-a+1<=q
 # Zero-based inclusive interval. Choose a q-gram covering it.
 t=max(0,b-q+1)
 assert t<=a and t+q<=n
 return t

def compress(w,D,B,marked_pair):
 q=2*B+3*(2*D-1)+6;n=len(w)
 if n<=q:return w,dict(q=q,unchanged=True,pair=marked_pair,kind='short')
 g=collections.defaultdict(set)
 for k in range(n-q+1):
  g[w[k:k+q-1]].add((w[k+1:k+q],w[k+q-1]));g[w[k+1:k+q]]
 s=w[:q-1];t=w[-q+1:];x,y=marked_pair
 left=(x<=B);right=(y>=n-B-1)
 assert not(left and right)
 if left or right:
  # Author may retain an arbitrary marked edge too; retaining one only increases length.
  mark=0 if left else n-q
 else:mark=q_start(n,q,x-B-1,y+B+1)
 u=w[mark:mark+q-1];v=w[mark+1:mark+q]
 first=bfs(g,s,u);last=bfs(g,v,t)
 out=s+tuple(first)+(w[mark+q-1],)+tuple(last)
 assert len(out)<=q+2*len(g)-2
 assert len(out)<=n
 if left:mp=(x,y);kind='left'
 elif right:mp=(x+len(out)-n,y+len(out)-n);kind='right'
 else:mp=(q-1+len(first)-q+1+x-mark,q-1+len(first)-q+1+y-mark);kind='interior'
 # Marked edge starts at len(first) in reconstructed word.
 if not left and not right:assert mp==(len(first)+x-mark,len(first)+y-mark)
 assert out[:q-1]==w[:q-1] and out[-q+1:]==w[-q+1:]
 originals={w[k:k+q] for k in range(n-q+1)}
 assert all(out[k:k+q] in originals for k in range(len(out)-q+1))
 return out,dict(q=q,unchanged=False,pair=mp,kind=kind,vertices=len(g),mark=mark,first_edges=len(first),last_edges=len(last))

def signature(inc,pair,B):
 n=len(inc);x,y=pair;a=max(0,x-B);b=min(n-1,y+B)
 return (x-a,y-a,a==0,b==n-1,tuple(tuple(j-i for j in sorted(inc[i]) if i<j<=b) for i in range(a,b+1)))

def witness(w,out,i,j,B,q):
 n=len(w);nn=len(out)
 if i<=B:return (i,j),'left'
 if j>=nn-B-1:return (i+n-nn,j+n-nn),'right'
 a=i-B-1;b=j+B+1;k=q_start(nn,q,a,b)
 block=out[k:k+q]
 for l in range(n-q+1):
  if w[l:l+q]==block:return (i+l-k,j+l-k),'interior'
 raise AssertionError('no q-gram witness')

def probabilities(inc,D):
 n=len(inc);pred=[((1<<j)-1)^sum(1<<i for i in inc[j] if i<j) for j in range(n)]
 F=[{0:1}]; T=[]
 for r in range(n):
  new={};ed={}
  for J,f in F[-1].items():
   row=[]
   for j in range(max(0,r-D),min(n,r+D+1)):
    if (J>>j)&1 or pred[j]&~J:continue
    K=J|(1<<j);row.append((j,K));new[K]=new.get(K,0)+f
   assert row
   ed[J]=row
  F.append(new);T.append(ed)
 assert len(F[-1])==1
 B=[None]*(n+1);B[n]={(1<<n)-1:1}
 for r in range(n-1,-1,-1):B[r]={J:sum(B[r+1][K] for j,K in row) for J,row in T[r].items()}
 total=B[0][0]; counts={(x,y):0 for y in range(n) for x in inc[y] if x<y}
 for r in range(n):
  for J,row in T[r].items():
   for y,K in row:
    for x in inc[y]:
     if x<y and ((J>>x)&1):counts[x,y]+=F[r][J]*B[r+1][K]
 return {pair:fractions.Fraction(c,total) for pair,c in counts.items()},total

def adjacent(pattern,repeats):
 bits=(pattern*repeats);n=len(bits)+1;inc=[set() for _ in range(n)]
 for i,z in enumerate(bits):
  if z:inc[i].add(i+1);inc[i+1].add(i)
 return inc

def interval_family(gaps,repeats,width):
 gs=gaps*repeats; xs=[0]
 for d in gs:xs.append(xs[-1]+d)
 inc=[set() for _ in xs]
 for i in range(len(xs)):
  for j in range(i+1,len(xs)):
   if xs[j]-xs[i]>=width:break
   inc[i].add(j);inc[j].add(i)
 return inc

def permutation_family(n,D):
 perm=list(range(n));deg=[0]*n
 for _ in range(8*n):
  p=rng.randrange(n-1); a,b=perm[p:p+2]
  change=1 if a<b else -1
  if deg[a]+change<=D and deg[b]+change<=D:
   perm[p:p+2]=[b,a];deg[a]+=change;deg[b]+=change
 pos=[0]*n
 for j,i in enumerate(perm):pos[i]=j
 inc=[set() for _ in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   if pos[j]<pos[i]:inc[i].add(j);inc[j].add(i)
 return inc

cases=[]
for B in [0,1,4,8]:
 for pattern in [[1],[1,0],[1,1,0],[0,1,1,1,0,0,1]]:
  cases.append((f'adjacent_{pattern}_B{B}',adjacent(pattern,80),2,B))
for B in [0,2,8]:
 for gaps,width in [([1],3),([1,1,2,1,2],3),([1,2,1,3,1],4)]:
  inc=interval_family(gaps,30,width);D=max(map(len,inc));cases.append((f'interval_{gaps}_w{width}_B{B}',inc,D,B))
for k in range(12):
 D=2+(k%3);cases.append((f'permutation_{k}',permutation_family(90,D),D,k%3))
results=[];kinds=collections.Counter();pairs_checked=0;changed=0
for name,inc,D,B in cases:
 valid(inc,D);w=word(inc,D);probs,total=probabilities(inc,D)
 # Test true maximizer and both endpoint-adjacent incomparable choices where available.
 mx=max(probs,key=lambda k:min(probs[k],1-probs[k])); marks=[mx]
 marks+=sorted(probs,key=lambda p:p[0])[:1]+sorted(probs,key=lambda p:p[1])[-1:]
 for mp in dict.fromkeys(marks):
  out,meta=compress(w,D,B,mp);other=decode(out,D);other_probs,other_total=probabilities(other,D)
  assert other_probs
  assert signature(inc,mp,B)==signature(other,meta['pair'],B)
  maxerr=fractions.Fraction(0)
  for pair,p in other_probs.items():
   old,kind=witness(w,out,*pair,B,meta['q']) if not meta['unchanged'] else (pair,'short')
   assert old in probs
   assert signature(other,pair,B)==signature(inc,old,B)
   maxerr=max(maxerr,abs(p-probs[old]));kinds[kind]+=1;pairs_checked+=1
  delta=max(min(p,1-p) for p in probs.values());delta_new=max(min(p,1-p) for p in other_probs.values())
  # Choosing the true maximizer makes the bidirectional max argument fully testable.
  reverse_error=abs(probs[mp]-other_probs[meta['pair']])
  if mp==mx:assert abs(delta-delta_new)<=max(maxerr,reverse_error)
  changed+=len(out)<len(w)
  results.append(dict(name=name,D=D,B=B,n=len(w),new_n=len(out),q=meta['q'],mark=list(mp),mark_kind=meta['kind'],true_maximizer=mp==mx,delta=str(delta),delta_new=str(delta_new),max_witness_probability_error=str(maxerr),reverse_probability_error=str(reverse_error)))
# Explicit unmarked zero-edge tests, where there is no output q-gram.
zero_edge=[]
for D in [2,3,4]:
 for B in [0,1,4]:
  R=2*D-1;q=2*B+3*R+6
  z=tuple([0]+[int(k%4!=0) for k in range(1,q-1)])
  w=z*5;inc=decode(w,D);out=z;other=decode(out,D)
  assert w[:q-1]==w[-q+1:]==out and len(out)==q-1
  probs,total=probabilities(inc,D);other_probs,other_total=probabilities(other,D)
  for pair in other_probs:
   i,j=pair
   if i<=B:old=pair;kind='zero_left'
   elif j>=len(out)-B-1:old=(i+len(w)-len(out),j+len(w)-len(out));kind='zero_right'
   else:old=pair;kind='zero_interior'
   assert old in probs and signature(other,pair,B)==signature(inc,old,B)
   pairs_checked+=1;kinds[kind]+=1
  zero_edge.append(dict(D=D,B=B,q=q,n=len(w),new_n=len(out),pairs=len(other_probs)))
summary=dict(seed=SEED,families=len(cases),compressions=len(results),strict_shortenings=changed,all_final_incomparable_pair_witnesses_checked=pairs_checked,witness_kinds=dict(kinds),minimum_output_size=min(r['new_n'] for r in results),maximum_input_size=max(r['n'] for r in results),status='PASS',unmarked_zero_edge_cases=zero_edge,results=results)
(OUT/'compression_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='results'},indent=2))
