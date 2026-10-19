from itertools import permutations
from fractions import Fraction
from collections import Counter

def check(name, labels, rels):
    le=[]
    for p in permutations(labels):
        ix={x:i for i,x in enumerate(p)}
        if all(ix[a]<ix[b] for a,b in rels): le.append(p)
    prob={}
    for i,a in enumerate(labels):
        for b in labels[i+1:]:
            t=Fraction(sum(p.index(a)<p.index(b) for p in le),len(le))
            if 0<t<1: prob[a+b]=(t,min(t,1-t))
    delta=max((beta for _,beta in prob.values()), default=Fraction(0))
    print(name,'extensions',len(le),'delta',delta,'incomparable',prob)
    return le,prob,delta

P,_,dP=check('Six-point P','zabcdy',[('z','a'),('z','b'),('z','c'),('z','d'),('a','b'),('b','c'),('a','d')])
Q,_,dQ=check('Six-point local dual','zabcdy',[('z','a'),('z','b'),('z','c'),('z','d'),('b','a'),('c','b'),('d','a')])
assert (len(P),len(Q),dP,dQ)==(18,18,Fraction(4,9),Fraction(1,2))
print('Six-point core words for P: z a b c d; z a b d c; z a d b c')
print('Six-point core words for Q: z c b d a; z c d b a; z d c b a')
print('Insert y into each of six gaps of each core word; this gives all 18 extensions.')
R,pR,dR=check('Four-point fixed-label control','zaby',[('z','a'),('z','b'),('a','b')])
S,pS,dS=check('Four-point local dual','zaby',[('z','a'),('z','b'),('b','a')])
assert pR['ay'][0]==Fraction(1,2) and pS['ay'][0]==Fraction(1,4)
assert dR==dS==Fraction(1,2)
