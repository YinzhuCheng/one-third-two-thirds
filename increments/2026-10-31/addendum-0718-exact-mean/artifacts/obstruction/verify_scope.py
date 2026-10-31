import json
from pathlib import Path
p=Path(__file__).resolve().parent
j=json.loads((p/'EXAMPLE.json').read_text());V=j['V'];D={x:set() for x in V}
for edge in j['relations']:a,b=edge.split('<');D[b].add(a)
for k in V:
 for b in V:
  if k in D[b]:D[b]|=D[k]
U={a:{b for b in V if a in D[b]}for a in V};Q=set(V)-{'v','c1','b','c2'}
A=(U['v']&U['c1'])-U['c2'];F=U['c2'];L=A&U['b'];M=F-U['b']
assert L=={'a1','a2','a4'} and M=={'f0'} and 'e'in Q
assert 'e'in D['f0'] and 'e'not in D['a1'] and 'a1'not in D['e']
lower=set.union(*(D[x]&Q for x in M))-M;common=set.intersection(*(D[x]&Q for x in L));upper=set.union(*(U[x]&Q for x in L))-L;common_u=set.intersection(*(U[x]&Q for x in M))
assert 'e'in lower-common and upper<=common_u
print(json.dumps({'L':sorted(L),'M':sorted(M),'e_precedes_f0':True,'e_incomparable_a1':True,'lower_obstructions':sorted(lower-common),'upper_outside_L':sorted(upper),'upper_test':True},indent=2))
