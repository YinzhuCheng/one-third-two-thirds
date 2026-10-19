# Independent exact six-element calculation underlying the analytic infinite family.
from itertools import combinations
import json
from pathlib import Path
from fractions import Fraction
out=Path(__file__).parent
orders=[]
for Apos in combinations(range(5),3):
    seq=[None]*5
    for k,x in zip(Apos,['a','u','w']):seq[k]=x
    for k,x in zip([i for i in range(5) if seq[i] is None],['b','v']):seq[k]=x
    seq+=['t']
    p={x:i+1 for i,x in enumerate(seq)}
    orders.append(dict(order=seq,E=int(p['u']<p['v']),rank_b=p['b'],E_rank_b=int(p['u']<p['v'])*p['b'],positive_u_difference=max(0,p['u']-p['b']),positive_v_difference=max(0,p['v']-p['b'])))
sums={k:sum(o[k] for o in orders) for k in ['E','rank_b','E_rank_b','positive_u_difference','positive_v_difference']}
assert len(orders)==10
assert sums==dict(E=7,rank_b=20,E_rank_b=16,positive_u_difference=14,positive_v_difference=20)
(out/'family-core-records.json').write_text(json.dumps(dict(orders=orders,sums=sums),indent=2))
print(json.dumps(dict(orders=orders,sums=sums),indent=2))
for o in orders:
    p={x:i+1 for i,x in enumerate(o['order'])}
    o['E_vw']=int(p['v']<p['w'])
    o['E_vw_rank_b']=o['E_vw']*p['b']
assert sum(o['E_vw'] for o in orders)==6
assert sum(o['E_vw_rank_b'] for o in orders)==10
sums.update(E_vw=6,E_vw_rank_b=10)
(out/'family-core-records.json').write_text(json.dumps(dict(orders=orders,sums=sums),indent=2))
print('eligible transferable v/w core moments',6,10)
