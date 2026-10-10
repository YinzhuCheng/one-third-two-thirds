#!/usr/bin/env python3
"""Count only the reduced four-coordinate envelope, never b,c,t vectors."""
from collections import Counter
import json

V={1:3,2:9,3:29,4:43}
D={1:50,2:92,3:181,4:36}
OTHER_PORT={1:17,2:32,3:63,4:56}

def kind(a,d):
    if max(a,d)<=4:
        return 'both_outer_at_most_four'
    if min(a,d)<=4:
        return 'mixed'
    return 'both_outer_at_least_five'

canonical=set()
for a in range(1,21):
    d_max=D[a] if a<=4 else 41-a
    for d in range(a,d_max+1):
        u_max=V[a] if a<=4 else 108
        v_max=V[d] if d<=4 else OTHER_PORT[a] if a<=4 else 108
        for u in range(2,u_max+1):
            for v in range(2,v_max+1):
                if u+v>110:
                    continue
                if 16*(a*u+d*v)>=60*(u+v)+25*min(u,v)+25*(a+d):
                    continue
                if a<=4 and d>=5 and (16*d-60)*v>=25*d+25*a+(85-16*a)*u:
                    continue
                canonical.add((a,d,u,v))
ordered=canonical | {(d,a,v,u) for a,d,u,v in canonical}
canonical_counts=dict(sorted(Counter(kind(a,d) for a,d,u,v in canonical).items()))
ordered_counts=dict(sorted(Counter(kind(a,d) for a,d,u,v in ordered).items()))
if len(canonical)!=14190 or len(ordered)!=25526:
    raise RuntimeError('four-coordinate domain count mismatch')
print(json.dumps({
    'status':'PASS',
    'scope':'a,d,u,v envelope only; no b,c,t census',
    'requires_fourth_terminal_cap':True,
    'canonical_a_le_d_count':len(canonical),
    'canonical_counts':canonical_counts,
    'ordered_count':len(ordered),
    'ordered_counts':ordered_counts,
},indent=2))
