from itertools import combinations
from fractions import Fraction as F
from math import comb

def stats(n,edges,name):
 pred=[0]*n
 for a,b in edges:pred[b]|=1<<a
 for k in range(n):
  for i in range(n):
   if pred[i]>>k&1:pred[i]|=pred[k]
 ideals=[m for m in range(1<<n) if all(not(m>>i&1) or pred[i]&m==pred[i] for i in range(n))]
 runs={i:[] for i in ideals}
 le=[]
 def rec(pref,used):
  if len(pref)==n:
   le.append(tuple(pref));return
  for i in range(n):
   if not(used>>i&1) and pred[i]&used==pred[i]:rec(pref+[i],used|1<<i)
 rec([],0)
 for w in le:
  for i in ideals:
   r=0
   for x in w:
    if i>>x&1:r+=1
    else:break
   runs[i].append(r)
 e=len(le); found=[]; mn=(None,None); mx=(None,None)
 for k in ideals:
  for l in ideals:
   if k&l!=k or k==l or not k or l==(1<<n)-1:continue
   X,Y=runs[k],runs[l];r=F(sum(X),e);s=F(sum(Y),e)
   var=F(sum(x*x for x in X),e)-r*r
   cov=F(sum(x*y for x,y in zip(X,Y)),e)-r*s
   gap=cov-var
   if gap>0:found.append((gap,k,l,r,s,var,cov,[(x,y) for x,y in zip(X,Y)]))
   if mn[0] is None or gap<mn[0]:mn=(gap,(k,l))
   if mx[0] is None or gap>mx[0]:mx=(gap,(k,l))
 print(name,n,e,'ideals',len(ideals),'range',mn,mx)
 if found:
  v=max(found);print(' POSITIVE',v[:-1]);from collections import Counter;print(Counter(v[-1]))
 return found

def chainunion(lengths):
 n=sum(lengths);edges=[];p=0
 for m in lengths:
  edges +=[(i,i+1) for i in range(p,p+m-1)];p+=m
 return n,edges
models=[]
for lengths in [(1,1,1),(2,1),(2,2),(2,3),(2,2,1),(3,3),(2,3,1),(2,2,2),(3,2,2),(1,1,1,1)]:
 n,edges=chainunion(lengths);models.append((n,edges,'C'+'+'.join(map(str,lengths))))
models +=[(5,[(0,2),(1,2),(2,3)],'fork-tail+isolate'),(6,[(0,3),(1,3),(1,4),(2,4),(3,5),(4,5)],'asymmetric-twofork')]
if __name__=='__main__':
 for n,e,name in models:stats(n,e,name)
