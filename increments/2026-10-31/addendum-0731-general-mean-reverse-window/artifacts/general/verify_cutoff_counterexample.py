from itertools import permutations
import json
W=[p for p in permutations(['h','l1','l2','m'])if p.index('h')<p.index('l1')<p.index('l2')]
B=sum(p.index('m')+1 for p in W);Z=sum(min(p.index('l1'),p.index('l2'))+1 for p in W)
a=sum('m'not in p[:3]for p in W);b=sum(not(set(p[:3])&{'l1','l2'})for p in W)
assert(len(W),B,Z,a,b)==(4,10,10,1,0)
print(json.dumps(dict(N=4,B=B,Z=Z,cutoff=3,avoid_M=a,avoid_L=b),indent=2))
