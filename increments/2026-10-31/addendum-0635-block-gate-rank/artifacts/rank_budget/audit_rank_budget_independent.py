from functools import lru_cache

def count(n,H,I,J,B):
 names=['a','d','x','y','s']+list(range(1,n+1)); idx={x:i for i,x in enumerate(names)}; N=len(names);preds=[0]*N
 edges=[('a','x'),('a','s'),('d','y'),(B,'s')]+[(i,i+1) for i in range(1,n)]
 edges += [(p,j) for p in ['a','d'] for j in range(1,n+1) if j!=B]
 edges += [(p,q) for p,q in [('x',I),('y',H),('s',J)] if q<=n]
 for p,q in edges:preds[idx[q]]|=1<<idx[p]
 @lru_cache(None)
 def rec(mask,sign):
  if mask==(1<<N)-1:return sign
  ans=0
  for i in range(N):
   if not mask>>i&1 and preds[i]&mask==preds[i]:
    s=sign
    if sign==0 and names[i] in ['a','d']:s=1 if names[i]=='a' else -1
    ans+=rec(mask|1<<i,s)
  return ans
 return rec(0,0)
checks=0
for n in range(1,8):
 for h in range(1,n+1):
  for i in range(h+1,n+1):
   for j in range(h+1,n+1):
    # h,i,j are positions in the word after deleting its first letter b.
    got=count(n,h+1,i+1,j+1,1)
    want=4*h*j+2*h*i+11*h-4*i*j-4*min(i,j)
    assert got==want,(n,h,i,j,got,want)
    checks+=1
print('b-first independent ideal-DP cases:',checks)
checks=0
for n in range(2,8):
 for b in range(2,n+1):
  for h in range(1,n+2):
   if h==b:continue
   for i in range(h,n+2):
    if i==b:continue
    for j in range(b+1,n+2):
     got=count(n,h,i,j,b)
     C=range(b+1,j+1)
     W=lambda t: t*len(C)+sum(c<=t for c in C)
     want=W(h)-W(i)
     assert got==want,(n,h,i,j,b,got,want)
     checks+=1
print('b-not-first independent ideal-DP cases:',checks)
