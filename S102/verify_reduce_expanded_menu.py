import json,itertools,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).parent
orig=json.loads((ROOT/'expanded_menu_witness.json').read_text())
def enumerate_le(pre):
 n=len(pre); ext=[]
 def rec(seq,mask):
  if len(seq)==n:ext.append(seq);return
  for v in range(n):
   if not mask>>v&1 and pre[v]&mask==pre[v]:rec(seq+(v,),mask|1<<v)
 rec((),0);return ext

def check(pre,y,u,s,t,details=False):
 n=len(pre);ext=enumerate_le(pre);E=len(ext);M=[[0]*n for _ in pre];d=0
 for perm in ext:
  rank={v:i for i,v in enumerate(perm)}
  for i in range(n):
   for j in range(n):M[i][j]+=rank[i]<rank[j]
  d+=all(rank[v]<rank[y] for v in range(n) if pre[u]>>v&1)
 inc=[v for v in range(n) if v!=y and not pre[v]>>y&1 and not pre[y]>>v&1]
 if pre[y] or not all(3*M[v][y]<E or 3*M[v][y]>2*E for v in inc):return
 if not 3*M[u][y]>2*E:return
 if any(pre[v]>>u&1 and 3*M[v][y]>2*E for v in range(n)):return
 cov=[v for v in range(n) if pre[v]>>u&1 and not pre[v]>>y&1 and not any(pre[v]>>w&1 and pre[w]>>u&1 for w in range(n))]
 if set(cov)!={s,t}:return
 common=[v for v in range(n) if pre[v]>>u&1 and pre[v]>>y&1]
 C=[v for v in common if not any(pre[v]>>w&1 for w in common)]
 menu=[y,u,s,t]+C
 if any(E<=3*M[i][j]<=2*E for i,j in itertools.combinations(menu,2)):return

 width=max(len(a) for r in range(n+1) for a in itertools.combinations(range(n),r) if all(not pre[i]>>j&1 and not pre[j]>>i&1 for i,j in itertools.combinations(a,2)))
 assert width<=3 and 9*M[u][y]<7*E and 3*M[s][y]<E and 3*M[t][y]<E and 9*d>18*M[u][y]-5*E
 return dict(n=n,y=y,u=u,s=s,t=t,E=E,d_count=d,pre=pre,counts=M,width=width,C=C,menu=menu,inc_y=inc,extensions=ext)

original=check(orig['pre'],orig['y'],orig['u'],orig['s'],orig['t']);assert original and original['counts']==orig['counts'] and original['E']==orig['E']
fixed={orig[k] for k in ('y','u','s','t')};others=sorted(set(range(orig['n']))-fixed)
found=[]
for size in range(4,orig['n']+1):
 for extra in itertools.combinations(others,size-4):
  labels=sorted(fixed|set(extra));mp={v:i for i,v in enumerate(labels)}
  pre=[sum(1<<mp[v] for v in labels if orig['pre'][w]>>v&1) for w in labels]
  ans=check(pre,*(mp[orig[k]] for k in ('y','u','s','t')))
  if ans:ans['original_labels']=labels;found.append(ans)
 if found:break
res=found[0];(ROOT/'expanded_menu_minimal_induced.json').write_text(json.dumps(res,indent=2))
print('Original independently verified',orig['n'],orig['E'])
print('Smallest induced witness retaining fork:',res['n'],'labels',res['original_labels'],'E',res['E'],'pre',res['pre'])
print('Witnesses at smallest size:',len(found))
for a,b in [(res['u'],res['y']),(res['s'],res['y']),(res['t'],res['y']),(res['s'],res['t'])]:print(a,b,Fraction(res['counts'][a][b],res['E']))
print('width',res['width'],'y incomparables',res['inc_y'],'C',res['C'],'Menu',res['menu']); print('pre',res['pre']); print('matrix',res['counts'])
# Independently filter all permutations when reasonably small.
if res['n']<=10:
 edges=[(i,j) for j,p in enumerate(res['pre']) for i in range(res['n']) if p>>i&1]
 perms=[]
 for perm in itertools.permutations(range(res['n'])):
  rank=[0]*res['n']
  for k,v in enumerate(perm):rank[v]=k
  if all(rank[a]<rank[b] for a,b in edges):perms.append(perm)
 assert sorted(perms)==sorted(res['extensions'])
 print('ALL PERMUTATIONS check passed:',math.factorial(res['n']),'permutations,',len(perms),'linear extensions')
else:print('Original independent backtracking verified; factorial filter omitted n>10')
