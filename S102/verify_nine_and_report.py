exec(open('verify_reduce_fork.py').read().split('original=check')[0])
names=['a','u','s','t','y','v','x1','x2','x3'];edges=[('a','s'),('a','t'),('u','s'),('u','t'),('s','v'),('t','v'),('s','x1'),('y','x1'),('x1','x2'),('x2','x3')]
p=[0]*9
for a,b in edges:p[names.index(b)]|=1<<names.index(a)
for k in range(9):
 for j in range(9):
  if p[j]>>k&1:p[j]|=p[k]
r=check(p,4,1,2,3);assert r and r['E']==132
perms=[]
for perm in itertools.permutations(range(9)):
 rank=[0]*9
 for k,v in enumerate(perm):rank[v]=k
 if all(rank[names.index(a)]<rank[names.index(b)] for a,b in edges):perms.append(perm)
assert sorted(perms)==sorted(r['extensions'])
(ROOT/'nine_point_verified.json').write_text(json.dumps(r,indent=2))
print('Nine-point all 362880 permutations verified; E=',r['E'],'matrix=',r['counts'],'width=',r['width'])
res=json.loads((ROOT/'terminal_fork_minimal_induced.json').read_text());ns=['u','s','t','y','a','b','c'];E=res['E'];M=res['counts'];pre=res['pre']
covers=[(ns[i],ns[j]) for j,p in enumerate(pre) for i in range(7) if p>>i&1 and not any(p>>k&1 and pre[k]>>i&1 for k in range(7))]
lines=['# Exact seven-point terminal-fork counterexample','','This falsifies the proposed stronger sibling-balance statement, not the 1/3–2/3 conjecture or S99 Theorem D.1.','','Labels: '+', '.join(ns)+'.','Hasse relations: '+', '.join(a+'<'+b for a,b in covers)+'.','No other relations except transitivity.','','## Exact checks','','- E=62 linear extensions, counted by order-ideal DP and independently by filtering all 7!=5040 permutations.','- y is minimal; its incomparable elements are exactly u,s,t.','- P(u<y)=42/62=21/31 >2/3, and <7/9.','- P(s<y)=10/62=5/31 <1/3; P(t<y)=18/62=9/31 <1/3.','- a,b,c are above y, so their before-y probabilities are all zero.','- u is the only y-incomparable majority point, hence poset-maximal in that set.','- Its private Hasse covers are exactly s,t; a is another cover of u but lies above y.','- D(u) is empty, hence d=1 >2p−5/9 =223/279.','- The chain partition (u,s), (y,a), (t,b,c) proves width≤3. The antichain {s,t,y} proves width=3.','- P(s<t)=17/62 <1/3 (3×17=51<62); equivalently P(t<s)=45/62 >2/3.','','## Full original-law probability matrix','','Every entry is numerator/62; row label precedes column label. Diagonal entries are zero.','','| |'+'|'.join(ns)+'|','|'+'---|'*8]
for i,name in enumerate(ns):lines.append('|'+name+'|'+'|'.join(map(str,M[i]))+'|')
lines += ['','## Scope','','The search was seeded random sampling of n=5–12 posets with explicit two- or three-chain decompositions and extra forward relations; it stopped at its first counterexample (iteration 35, counting from zero). This was not exhaustive and not canonical unlabeled enumeration. The 11-point witness was exhaustively reduced over all induced subposets retaining its designated y,u,s,t: seven is the smallest size within that reduction, not a claim of global minimality. All 62 extensions of the seven-point witness are supplied in terminal_fork_minimal_induced.json.','','Nine-point candidate supplied independently was also verified by all 9!=362880 permutations: E=132, p_u=p_a=90/132, q_s=40/132, q_t=28/132, P(s<t)=90/132. Its full matrix is in nine_point_verified.json.']
(ROOT/'COUNTEREXAMPLE_REPORT.md').write_text('\n'.join(lines)+'\n')
print('7point covers',covers,'matrix',M)
