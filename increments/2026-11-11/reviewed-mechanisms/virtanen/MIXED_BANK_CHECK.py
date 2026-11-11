from itertools import permutations
from fractions import Fraction
import json
words=[w for w in permutations('ubv') if w.index('b')<w.index('v')]
out=[]
for k in (1,2,3):
 ws=[w for w in words if w.index('u')+1==k]
 val=Fraction(sum(2*(w.index('u')<w.index('b'))+(w.index('v')<w.index('u')) for w in ws),len(ws))
 out.append({'rank_u':k,'words':[''.join(w) for w in ws],'E[2[u<b]+[v<u]]':str(val)})
assert [v['E[2[u<b]+[v<u]]'] for v in out]==['2','0','1']
print(json.dumps(out,indent=2))
