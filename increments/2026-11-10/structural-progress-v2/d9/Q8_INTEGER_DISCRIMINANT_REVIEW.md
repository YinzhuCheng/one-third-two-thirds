# Independent audit: two Q8 discriminants at integer minimum deadlines

2026-11-10. PASS for integer t in {0,1,2,3,4}, real p in [0,6-t]. This is not a positivity proof for continuous t. It removes the 81 Bernstein-coefficient dependency for this integer subproblem only; unresolved boundary faces and the full ledger are unaffected.

The review reconstructed the chamber polynomials from the formal Q8_SOURCE_BERNSTEIN_CERTIFICATE.json, substituted r=6-t-p-q, extracted A,B,C as q coefficients, and recomputed H=4AC-B^2 independently. Both resulting H expressions agree identically with the temporary author expressions. The specializations are:

    H0(0,p)=20196p^3+(41943/4)p^2+5424p+74816;
    H0(1,p)=75240p^3+43604p^2+522828p+1385343;
    H0(2,p)=186624p^3-135756p^2+855036p+5404887;
    H0(3,p)=372060p^3-(2541201/4)p^2-1053129p+12007775;
    H0(4,p)=643860p^3-(4873609/4)p^2-7607763p+17207559.

The first two have all coefficients positive. For t=2, p^2<=4p gives a lower bound 186624p^3+312012p+5404887>0. For t=3, discard the positive cubic and use p^2<=9,p<=3 to obtain H>=12522743/4>0. For t=4, H'=1931580p^2-(4873609/2)p-7607763 is convex; its endpoint values on [0,2] are -7607763 and -4755052. Convexity puts it below its negative endpoint chord, hence H is decreasing and H(p)>=H(2)=2269304>0.

The second discriminant specializes to:

    H6(0,p)=-598p^4+9162p^3-(101233/4)p^2+339240p+74816;
    H6(1,p)=-1357p^4+7100p^3+33986p^2+1615572p+1385343;
    H6(2,p)=-(2673/4)p^4-(66825/2)p^3+(435699/4)p^2+4551309p+5404887;
    H6(3,p)=(11507/4)p^4-110055p^3-78547p^2+8630556p+12007775;
    H6(4,p)=10511p^4-198619p^3-(3125233/4)p^2+12033927p+17207559.

For t=0, p<=6 gives H>=5574p^3+(374781/2)p+74816>0. For t=1, p<=5 gives H>=315p^3+33986p^2+1615572p+1385343>0. For t=2, p^4<=64p and p^3<=16p, discarding the positive quadratic, give H>=3973941p+5404887>0. For t=3, discard the positive quartic and use p^3<=9p,p^2<=3p, giving H>=7404420p+12007775>0. For t=4, discard the positive quartic and use p^3<=4p,p^2<=2p, giving H>=(19353669/2)p+17207559>0.

In both chambers A is strictly positive, so H>0 proves Aq^2+Bq+C>0 on the entire real q-axis for these five integer t values. Actual original-poset deadlines make t an integer, so this is sufficient for that portion of the application. Larger t are handled separately by the audited direction-of-derivative reduction, not by the present specialization argument. No claim that integer checks imply continuous-t positivity is made.

These are explicit polynomial inequalities using the threshold intervals, not a new coefficient-table certificate. They do not independently settle the r=0 face or the q=0 saturated-face boundaries. Retain the existing 400 pure-analytic plus 2 finite-symbolic source classification until those obligations are closed and independently audited.
