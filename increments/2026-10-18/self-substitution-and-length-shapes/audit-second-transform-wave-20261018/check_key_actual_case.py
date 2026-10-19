"""One fixed actual case, independent permutation count; no batch search."""
from itertools import permutations
from collections import Counter
import json
from pathlib import Path

names = ['d0', 'd1', 'd2', 'd3', 'y', 'z', 'u0']
# Minimal covers of the one certificate case.
covers = [(0,1),(1,3),(0,4),(1,5),(2,5),(4,5),(3,6),(5,6)]
counts = Counter()
events = [Counter(), Counter()]
extensions = []
for word in permutations(range(7)):
    pos = {x:i for i,x in enumerate(word)}
    if any(pos[x] > pos[y] for x,y in covers):
        continue
    last_d = max(pos[x] for x in range(4))
    first_u = pos[6]
    k = sum(last_d < pos[x] < first_u for x in (4,5))
    counts[k] += 1
    if pos[1] < pos[2]: events[0][k] += 1
    if pos[2] < pos[3]: events[1][k] += 1
    extensions.append([names[x] for x in word])

total = [counts[k] for k in range(3)]
event = [[a[k] for k in range(3)] for a in events]
assert total == [8,11,4], total
assert event == [[3,6,2],[8,8,3]], event

def numerator(a, b, c):
    # twice the polynomial in m, coefficients ascending
    return [2*(a+b+c), 2*b+3*c, c]

def derivative_cross(N,T):
    n0,n1,n2=N; t0,t1,t2=T
    return [n1*t0-n0*t1, 2*(n2*t0-n0*t2), n2*t1-n1*t2]

def difference_cross(N,T):
    g0,g1,g2=derivative_cross(N,T)
    return [g0+g1//2, g1+g2, g2]

T=numerator(*total)
D=[derivative_cross(numerator(*v),T) for v in event]
H=[difference_cross(numerator(*v),T) for v in event]
assert D == [[80,8,-4],[-142,-28,2]],D
assert H == [[84,4,-4],[-156,-26,2]],H
out={'scope':'one fixed seven-element actual certificate, direct permutation enumeration',
     'e_R':len(extensions),'total':total,'events':event,
     'derivative_ascending':D,'difference_ascending':H,
     'extensions':extensions}
path=Path(__file__).with_name('key_actual_case_verified.json')
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='extensions'},ensure_ascii=False))
