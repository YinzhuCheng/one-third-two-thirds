from explore import models
from fractions import Fraction as F
from collections import Counter

def inspect(n,edges,name):
 pred=[0]*n
 for a,b in edges:pred[b]|=1<<a
 for k in range(n):
  for i in range(n):
   if pred[i]>>k&1:pred[i]|=pred[k]
 ideals=[m for m in range(1<<n) if all(not(m>>i&1) or pred[i]&m==pred[i] for i in range(n))]
 le=[]
 def rec(pref,used):
  if len(pref)==n:le.append(tuple(pref));return
  for i in range(n):
   if not(used>>i&1) and pred[i]&used==pred[i]:rec(pref+[i],used|1<<i)
 rec([],0)
 runs={m:[] for m in ideals}
 for w in le:
  for m in ideals:
   r=0
   for x in w:
    if m>>x&1:r+=1
    else:break
   runs[m].append(r)
 for k in ideals:
  for l in ideals:
   if k&l!=k or not k or k==l or l==(1<<n)-1:continue
   X,Y=runs[k],runs[l];h=k.bit_count();g=l.bit_count();e=len(le)
   q=[[F(sum(x>=i and y>=j for x,y in zip(X,Y)),e) for j in range(g+1)]for i in range(h+1)]
   tests=[]
   for j in range(g+1):
    for i in range(1,h):
     if q[i][j]**2<q[i-1][j]*q[i+1][j]:tests.append(('i_slice',i,j,q[i][j]**2-q[i-1][j]*q[i+1][j]))
   for i in range(h+1):
    for j in range(1,g):
     if q[i][j]**2<q[i][j-1]*q[i][j+1]:tests.append(('j_slice',i,j,q[i][j]**2-q[i][j-1]*q[i][j+1]))
   if tests:
    print(name,n,'K,L',k,l,'nLE',e,tests,'joint',Counter(zip(X,Y)));return
 print(name,'all slices pass')
for model in models:inspect(*model)
