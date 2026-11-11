"""Independent direct-permutation check. Does not import search code."""
from itertools import permutations,combinations
from collections import Counter,defaultdict
from fractions import Fraction
import json

def verify(labels,edges,J):
  words=[w for w in permutations(labels) if all(w.index(a)<w.index(b) for a,b in edges)]
  pred={a:set() for a in labels}
  for a,b in edges:pred[b].add(a)
  changed=True
  while changed:
    changed=False
    for b in labels:
      p=set().union(*(pred[a] for a in list(pred[b]))) if pred[b] else set()
      if not p<=pred[b]:pred[b]|=p;changed=True
  assert all(pred[j]<=J for j in J)
  degree={a:sum(a!=b and a not in pred[b] and b not in pred[a] for b in labels) for a in labels}
  out={'labels':labels,'generating_edges':edges,'ideal':sorted(J),'LE':len(words),'minima':[a for a in labels if not pred[a]],'incomparable_degree':degree,'layers':{}}
  by=defaultdict(list)
  for w in words:by[1+max(w.index(j) for j in J)].append(w)
  for k,ws in sorted(by.items()):
    out['layers'][k]={'count':len(ws),'words':[''.join(w) for w in ws],'before':dict(Counter(''.join(sorted(w[:k-1])) for w in ws)),'through':dict(Counter(''.join(sorted(w[:k])) for w in ws)),'last_label':dict(Counter(w[k-1] for w in ws))}
  return out

three=verify('abc',[('a','b')],{'a','c'})
assert three['LE']==3
assert three['layers'][2]['before']=={'a':1,'c':1}
assert three['layers'][3]['before']=={'ab':1}
five=verify('abcde',[('a','d'),('a','e'),('b','c')],{'a','b'})
assert five['LE']==20
assert five['layers'][3]['through']=={'abc':2,'abd':2,'abe':2}
assert five['layers'][4]['through']=={'abde':2}
assert max(five['incomparable_degree'].values())==3
# Every included prefix atom containing c at rank3 has positive supply but no rank4 inclusion-neighbor.
assert Fraction(five['layers'][3]['through']['abc'],five['layers'][3]['count'])==Fraction(1,3)
# Same fixed x in an antichain: nonpivot pair conditional expectation is not monotone.
anti=[]
for pref in ['a','b','ab']:
  ws=[w for w in permutations('xab') if set(w[:w.index('x')])==set(pref)]
  p=Fraction(sum(w.index('a')<w.index('b') for w in ws),len(ws))
  anti.append({'prefix':pref,'count':len(ws),'Pr(a<b)':str(p)})
assert [x['Pr(a<b)'] for x in anti]==['1','0','1/2']
result={'status':'all exact direct-permutation assertions passed','three_point_before':three,'five_point_through':five,'nonpivot_pair_nonmonotonicity':anti}
print(json.dumps(result,indent=2))
