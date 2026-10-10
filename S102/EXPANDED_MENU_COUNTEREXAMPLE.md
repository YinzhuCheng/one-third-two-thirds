# Expanded minimum-common-upper-bound menu fails

## Ten-element counterexample

Names in machine order: y,u,s,a,c,d,t,b,e,f.
Cover relations:

y<c; u<s; u<c; u<t; s<a; a<b; c<d; c<b; b<e; e<f.

There are exactly 372 complete linear extensions, all weighted uniformly. This was verified by subset DP, independent recursive enumeration, and direct filtering of all 10!=3,628,800 permutations. Full pair-count matrix and all 372 extensions are in expanded_menu_small_minimal_induced.json. Entry counts[i][j] counts i before j.

### Every hypothesis

- y is minimal.
- Three chains covering the poset: y<c<d; u<s<a<b<e<f; t. The antichain {y,s,t} proves width exactly 3.
- The elements incomparable with y are exactly u,s,a,t. Their counts before y are 252,117,36,45. Thus all are unbalanced and u is the unique majority element, hence in particular a poset-maximal majority element.
- The elements above u but not above y are exactly s,a,t. Their minimal elements are s,t. Thus the private-successor set is exactly {s,t}.
- p=252/372=21/31 satisfies 2/3<p<7/9.
- q_s=117/372=39/124<1/3 and q_t=45/372=15/124<1/3.
- u is minimal, so D(u) is empty and d=1. The required lower bound is 2p-5/9=223/279<1.
- Common upper bounds of u and y are c,d,b,e,f, with unique minimum c. Thus C={c}.

### No balanced pair inside M={y,u,s,t,c}

Balanced integer counts would lie in [124,248]. The six incomparable pairs in this menu have counts:

(y,u):120; (y,s):255; (y,t):327; (s,t):300; (s,c):270; (t,c):118.

Every other menu pair is comparable, with probability zero or one. Hence the expanded menu has no balanced pair even when C is a singleton.

### Complete list of balanced pairs in the whole poset

Orientation is as written:

(a,c):140/372=35/93
(a,t):228/372=19/31
(d,t):127/372
(d,b):138/372=23/62
(d,e):216/372=18/31
(t,b):216/372=18/31

These are all six unordered balanced pairs. Every one uses a point outside the menu. Adding the minimum common upper bound does not force balance: c is itself strongly biased relative to both private successors, whereas balance appears only upon moving farther into the branches (a,d,b,e).

## Eleven-element independent witness retained

Names: y,u,s,a,c,d,t,b,e,f,g.
Covers: y<c,y<f,u<s,u<c,u<t,s<a,a<b,c<d,d<e,b<f,b<g,e<g.
E=1535, width exactly 3. Chain cover: y<c<d<e<g; u<s<a<b<f; t.
The elements incomparable with y are u,s,a,t,b, with respective before-y counts 1040,490,190,177,50. Hence u is again the sole majority point. The private upper set is {s,a,b,t}, with minima {s,t}. Since u is minimal, d=1. Here p=1040/1535=208/307, and 2p-5/9=2209/2763<1.
C={c,f}; the menu incomparable counts are (y,u)495,(y,s)1045,(y,t)1358,(s,t)1249,(s,c)1060,(t,c)463,(t,f)1199,(c,f)1486. None lies in [1535/3,3070/3].
All balanced pairs: (a,c)596/1535,(a,t)963/1535,(d,t)786/1535,(d,b)942/1535,(t,b)858/1535,(f,g)1005/1535.
The full exact matrix and all extensions are in expanded_menu_minimal_induced.json.

## Search and reproducibility

The first randomized search generated width-at-most-three orders using three interleaved chains plus forward edges, also including a two-chain-plus-isolated-point mode. It found a 12-point counterexample at zero-based iteration 42432 among 132 eligible candidates. Exhausting all induced suborders retaining that fork yielded an 11-point witness.
A bounded second independent random search restricted to sizes 7 through 10 found the ten-point witness at zero-based iteration 20898 among 48 eligible candidates. The process stopped at the witness. No global minimality is claimed. Exhaustion of induced suborders only proves induced minimality while retaining the distinguished fork in each particular witness.

Files:
- search_expanded_menu.cpp and search_expanded_menu_small.cpp: exact subset-DP searches, fixed seeds.
- verify_reduce_expanded_menu.py: independent extension enumeration and induced reduction of the 12-point witness.
- verify_expanded_menu_small.py: independent enumeration, induced reduction, and all-permutation verification of the ten-point witness.
- expanded_menu_small_verify.log: verification transcript.
- expanded_menu_small_minimal_induced.json: complete ten-point machine certificate.
- expanded_menu_minimal_induced.json: complete eleven-point machine certificate.

No further menu conjecture or proof claim is proposed.
