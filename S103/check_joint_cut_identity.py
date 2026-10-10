"""Exact bounded sanity check, not a proof or counterexample search."""
import itertools, math
checked=0
for n in range(2,6):
 pairs=list(itertools.combinations(range(n),2))
 for mask in range(1<<len(pairs)):
  up=[0]*n
  for k,(i,j) in enumerate(pairs):
   if mask>>k&1: up[i]|=1<<j
  if any(up[i]>>j&1 and up[j]&~up[i] for i,j in pairs):continue
  if any(all(not(up[i]>>j&1) for i,j in itertools.combinations(A,2)) for A in itertools.combinations(range(n),4)):continue
  perms=[p for p in itertools.permutations(range(n)) if all(p.index(i)<p.index(j) for i,j in pairs if up[i]>>j&1)]
  E=len(perms)
  cuts=[{k for k,p in enumerate(perms) if p[x]==x and set(p[:x])==set(range(x))} for x in range(n)]
  for a,b in pairs:
   if up[a]>>b&1:continue
   if any((up[a]>>c&1) or (up[c]>>b&1) for c in range(a+1,b)):continue
   if any(not(up[c]>>d&1) for c,d in itertools.combinations(range(a+1,b),2)):continue
   js=[{k for k,p in enumerate(perms) if set(p[:i+1])==set(range(i+1))} for i in range(a,b)]
   z=len(cuts[a]&cuts[b])
   assert z*math.prod(map(len,js))==math.prod(len(cuts[x]) for x in range(a,b+1))
   if b>a+1:
    R=set(range(b+1,n)); S=set(range(a,b+1)); ct=b-1
    mr={r for r in R if not any(up[s]>>r&1 for s in R)}
    active=set()
    for k in cuts[a]:
     p=perms[k]
     if R and min(p.index(r) for r in R)<max(p.index(s) for s in S):
      r=min(R,key=p.index); s=max(S,key=p.index)
      assert r in mr and s in (b,ct) and p.index(r)<p.index(s)
      assert not(up[s]>>r&1)
      active.add((r,s))
      if p.index(r)<min(p.index(b),p.index(ct)):
       assert up[a]>>r&1
    assert len(active)<=4
   checked+=1
print(f'PASS: {checked} width-at-most-3 interval instances, natural posets n=2..5; exact integer identity and external-label partition checks.')
