# Q8: retaining the true z-insertion mixture is necessary for the source bank

2026-11-10. Author exact control; independent review requested.

The source terminal bank on Q8=(0,0,1,1,7,7,7,23), reference01234567, is

    15A+3B+2C+2D+E >=23/3,
    A={2<1}, B={3<2}, C={5<4}, D={6<5}, E={7<6}.

Take this actual eight-label ideal and an actual exterior six-chain O1<...<O6. Impose x<Oj iff h_x<j for

    h_Q8=(0,0,0,0,0,0,5,6),

and take transitive closure. The resulting original fourteen-point P has Delta9. Its full counts are

    N2087; (KA,KB,KC,KD,KE)=(740,532,961,426,755);
    3(15KA+3KB+2KC+2KD+KE)-23N=674>0.

Thus the actual source bank succeeds, as expected.

Now condition on the finer projected exterior word O1 O2 ... O6 z, where z=label7 has been moved into the exterior of Q7. This is a nonempty legitimate event in the same original P. Its Q7 deadlines are(0,0,0,0,0,0,5). The exact fibre counts are

    N242; (KA,KB,KC,KD,KE)=(86,64,121,51,0);
    3(15KA+3KB+2KC+2KD+KE)-23N=-88.

The fibre is independently counted by imposing only O6<z on the full original poset, together with each queried event. Q8_PROJECTED_WORD_CONTROL.py reconstructs both original and fibre counts by full ideal-subset recursion, as recorded in its JSON.

Therefore the source five-event bank is NOT valid on every projected Q7 exterior word. This is not an ordinary bank counterexample: the bank was meant to be averaged over all legal insertions of z after fixing only the ORIGINAL O word, and indeed that real mixture pays. It prevents replacing this mixture by an arbitrary per-projected-word assertion or a profile-independent argument that forgets z's insertion correlations. The projected h_v=0 fibre still satisfies the OLD six-weight four-event bank, but that does not automatically pay the different source five-event bank with its larger coefficient sum. No NB assumption, new coverage or source error is asserted.

## Useful direct-Q8 reduction, not yet a complete proof

Stay on the full original Q8 and condition only on its original exterior O word. Its tail H consists of the chain4<7 and the two isolated labels5,6. Let B=h_b,U=h_u and m=min(h4,h5,h6). Since h5,h6<=5, m<=5. For shifted tail deadlines after exterior gap j, let F_j be the tail placement count and W_j the weighted tail count2K_(5<4)+2K_(6<5)+K_(7<6). Let G and W_G be the corresponding gap-zero counts with an extra independent v of deadline0 inserted beside the tail.

The same root-gap decomposition as THREE_TAIL gives source margin multiplied by3:

    11F_0-24G+15W_0+9W_G
      +sum_j[(45a_j+9d_j-23c_j)F_j+3c_jW_j],

with c_j,a_j,d_j as in that theorem. Increasing B from k-1 to k<=U changes it by

    (39+31k)F_k+3(k+3)W_k
      +sum_(j=k+1..U)(3W_j-14F_j)
    >=(39+45k-14U)F_k>0,

because F_j decreases, W_j>=0, U<=5. For k>U the newly added term is positive. Hence B=0 is worst.

Every tail word has weighted score at most4: all three charged tail inversions cannot occur simultaneously because4<7. Therefore W_j<=4F_j, and at B=0 each added U term is3(3W_j-14F_j)<0. Thus U=m is worst. This analytically eliminates BOTH root deadline axes without enumerating profiles. The remaining four-tail inequality in h4,h5,h6,h7 is not proved here; the projection control above explains why its z correlations must be retained.
