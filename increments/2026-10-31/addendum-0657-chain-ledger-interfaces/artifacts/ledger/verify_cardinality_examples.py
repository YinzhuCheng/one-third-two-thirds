import itertools,json
from functools import lru_cache
V=['v','c1','c2','b','d','e']+[f'a{i}'for i in range(1,6)]+['f']
base=[('v','b'),('v','d'),('v','f'),('c1','c2'),('c2','f'),('d','e'),('b','a4')]+[(x,f'a{i}')for x in ['v','c1']for i in range(1,6)]
out=[]
for num,extra in enumerate([list(zip(['e','a1','a2','a3','a4'],['a1','a2','a3','a4','a5'])),[('a1','a2'),('a2','a3'),('a4','a5')]],1):
 D={v:set()for v in V}
 for a,b in base+extra:D[b].add(a)
 for k in V:
  for b in V:
   if k in D[b]:D[b]|=D[k]
 U={a:{b for b in V if a in D[b]}for a in V};A=(U['v']&U['c1'])-U['c2'];F=U['c2'];L=A&U['b'];M=F-U['b'];Q=[v for v in V if v not in {'v','c1','b','c2'}]
 assert A=={f'a{i}'for i in range(1,6)} and L=={'a4','a5'} and M=={'f'}
 assert max(len(V)-1-len(D[x])-len(U[x])for x in V)==9
 assert not D['v'] and set(V)-{'v'}-U['v']=={'c1','c2'} and U['v']-U['c1']=={'b','d','e'}
 pre=[sum(1<<j for j,a in enumerate(Q)if a in D[b])for b in Q];B=Z=N=0
 def rec(w,mask):
  global B,Z,N
  if len(w)==len(Q):
   N+=1;B+=min(w.index(x)+1 for x in M);Z+=min(w.index(x)+1 for x in L);return
  for i,x in enumerate(Q):
   if not mask>>i&1 and pre[i]&mask==pre[i]:rec(w+[x],mask|1<<i)
 rec([],0);assert (B,Z)==[(36,54),(7560,5040)][num-1]
 out.append(dict(example=num,Q_extensions=N,B=B,Z=Z,relations=[a+'<'+b for a,b in base+extra]))
print(json.dumps(out,indent=2))
