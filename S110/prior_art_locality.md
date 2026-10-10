# Prior-art review: bounded-incomparability locality and finite additive representatives

Checked 2026-10-10. This is a limited, source-grounded overlap review, not a novelty certification. Here D always means maximum degree of the incomparability graph. It does not mean width, comparability degree, or cover-graph degree.

## Bottom line

There is substantial direct prior art for random linear extensions of bounded-incomparability-degree posets, dating to Brightwell (1988), and exact classical antecedents for the positive-matrix contraction, projective-to-total-variation estimate, and finite-word overlap graph used in the present argument. The accessible sources checked do not state the present finite two-environment theorem with its explicit constants, endpoint-aware induced-window approximation, or marked finite representative bound N(D,epsilon). That is a retrieval-limited finding, not evidence of novelty. In particular, the original 1988 proof has not been inspected in full; it may contain a quantitative lemma that subsumes the locality statement.

The appropriate description is a self-contained quantitative application of classical methods, with its precise overlap with the earlier thin-poset literature still unresolved.

## 1. Direct poset antecedent: Brightwell (1988)

Graham R. Brightwell, *Linear extensions of infinite posets*, Discrete Mathematics 70(2) (1988), 113–136. DOI: https://doi.org/10.1016/0012-365X(88)90087-8 . Publisher: https://www.sciencedirect.com/science/article/pii/0012365X88900878 .

The publisher abstract establishes that the paper extends finite uniform-extension probabilities to an infinite-poset class, carries correlation inequalities to that setting, and exhibits failure of the infinite analogue of the 1/3–2/3 conjecture. The author's own 2007 DIMACS abstract explicitly identifies the bounded-incomparability hypothesis and uniqueness of a sensible random-extension law: https://archive.dimacs.rutgers.edu/Workshops/Trotter/abstracts.html .

Full-text status: publisher metadata/abstract retrieved, but the original article PDF was not retrieved. Official article/PDF endpoints were unavailable in this session. The theorem-level hypotheses below are verified through subsequent primary papers involving the same author, not guessed from the abstract.

## 2. Two-sided thin posets: BFT (1995), Section 7

G. R. Brightwell, S. Felsner, W. T. Trotter, *Balancing pairs and the cross product conjecture*, Order 12 (1995), 327–349. DOI: https://doi.org/10.1007/BF01110378 . Author-hosted full text: https://trotter.math.gatech.edu/papers/97.pdf .

Section 7, printed page 346 (PDF page 20), treats an infinite, thin, locally finite poset: a uniform finite bound on the number incomparable to each point, and finite order intervals. For nested finite order-convex subsets exhausting the poset, probabilities of every event depending on finitely many comparison events converge. This result is attributed to Brightwell (1988). This setting allows two-sided orders; it is not limited to past-finite causal sets.

The introduction, printed pages 329–330, uses Q={x_i:i in Z}, with x_i<x_j exactly when j>i+1. The finite central exhaustion has the direction probability Pr(x_0>x_1) tending to (5−sqrt(5))/10. Theorem 1.4 identifies the infinite thin-poset optimal balance bound with this value.

Scope comparison: this checked passage states convergence, not a uniform effective exponential modulus across all finite environments. The infinite example makes endpoint loss a substantive issue; it does not refute finite endpoint-aware approximation or compression.

## 3. Past-finite special setting: Brightwell–Łuczak (2012)

G. Brightwell, M. Łuczak, *Order-invariant measures on fixed causal sets*, Combinatorics, Probability and Computing 21(3) (2012), 330–357. DOI: https://doi.org/10.1017/S0963548311000721 . Full text: https://arxiv.org/pdf/0901.0242 (v2, 29 January 2012; first submitted 2 January 2009).

Theorem 8.1 (PDF page 17) assumes a causal set, meaning a countably infinite poset in which each point has finitely many predecessors, and a uniform bound |I(x)|≤k. It concludes uniqueness of the order-invariant measure on natural extensions. The proof attributes exhaustion-independent limits of finite Boolean comparison events to Brightwell (1988). The introduction (page 3) already interprets order-invariant measures as one-dimensional spin systems; page 18 relates the bounded-incomparability condition to Dobrushin uniqueness.

Theorem 8.1 is not directly a theorem about the two-sided Z-indexed Fibonacci poset: that poset is not past-finite. Section 7 of BFT supplies the relevant broader setting. Neither this theorem nor its short proof displays the explicit finite-window rate or the finite representative construction at issue here.

## 4. Exact analytic mechanism: Birkhoff–Hopf and base norms

D. Reeb, M. J. Kastoryano, M. M. Wolf, *Hilbert's projective metric in quantum information theory*, Journal of Mathematical Physics 52 (2011), 082201. DOI: https://doi.org/10.1063/1.3615729 . Full text: https://arxiv.org/pdf/1102.5170 (v2, 15 August 2011).

Theorem 4 states the Birkhoff–Hopf contraction theorem for a positive linear map between two proper cones, with coefficient tanh(Delta/4). Different source/target dimensions are allowed. Proposition 7 gives one half of the base-norm distance at most tanh(h/4). On the nonnegative orthant with the probability-simplex base, this is exactly TV(p,q)≤tanh(h(p,q)/4).

Application to the present proof: entries of a rectangular block in [1,M] give projective diameter at most 2 log M, hence contraction at most (M−1)/(M+1). Positive reweighting factors in [l,u] give projective distance at most log(u/l), hence the bounded-reweighting lemma. Thus both analytic lemmas are known specializations, even when independently proved elementarily.

Historical origin: G. Birkhoff, *Extensions of Jentzsch's theorem*, Transactions of the American Mathematical Society 85 (1957), 219–227, DOI https://doi.org/10.1090/S0002-9947-1957-0087058-6 . The original PDF was unavailable in this session; the exact general-cone formulations above were checked in Reeb–Kastoryano–Wolf.

## 5. Inhomogeneous positive-block forgetting

J. E. Cohen, *Contractive inhomogeneous products of non-negative matrices*, Mathematical Proceedings of the Cambridge Philosophical Society 86 (1979), 351–364. Author-hosted full text: https://lab.rockefeller.edu/cohenje/PDFs/077ContractiveInhomogenProductsNonnegMatricesMathProcCombPhilSoc1979.pdf .

Section 2, Theorem A (printed page 354), gives explicit exponential contraction for an ergodic set of square matrices: all matrices are allowable, every g-fold product is positive, and positive entries have a uniform min-positive/max ratio bound. It restates and corrects a quantitative constant in Hajnal (1976). Thus exponential forgetting for nonstationary positive-block products was already standard by the 1970s. Cohen's square, fixed-dimension statement should not be cited as directly checking changing legal supports; the general-cone contraction above covers each rectangular positive block.

The application-specific work here is establishing genuine local ideal supports, proving positivity of every 2D-step block, bounding true boundary profiles, and comparing the actual uniformly weighted central path laws. A generic one-dimensional Gibbs uniqueness slogan is not a substitute for these checks: hard constraints and legal supports must be handled explicitly.

## 6. Restricted de Bruijn graph mechanism

E. Moreno, *De Bruijn sequences and De Bruijn graphs for a general language*, Information Processing Letters 96(6) (2005), 214–219. DOI: https://doi.org/10.1016/j.ipl.2005.05.028 . Author manuscript dated 9 May 2005: https://www.dim.uchile.cl/~emoreno/publicaciones/PREPRINTS/preprint-IPL-De_Bruijn_sequences_and_De_Bruijn_graphs_for_a_general_language.pdf .

Section 2 (manuscript pages 2–3) defines the overlap graph of an arbitrary dictionary D of equal-length words: vertices are their length-one-shorter prefixes/suffixes, edges are the dictionary words, and walks spell words whose local factors remain in D. This is exactly the graph mechanism needed for the finite representative argument; no new graph construction is involved.

Our comparison: shortening paths on the two sides of a marked edge is an elementary finite-graph step. The poset-specific layer is the finite-range encoding, finite-witness legality, matching physical endpoints, preservation of a maximizing incomparable pair, and transfer of actual probability estimates. Moreno does not state the poset balance representative theorem. Classical de Bruijn graph origin is N. G. de Bruijn (1946), *A combinatorial problem*, Proc. KNAW 49(7), 758–764; this historical citation is not itself a claim that its main cyclic-enumeration theorem proves the marked-path bound.

## 7. Bounded-degree balance and Kahn–Saks comparisons

M. Peczarski, *The Gold Partition Conjecture for 6-Thin Posets*, Order 25 (2008), 91–103, published online 25 June 2008. https://doi.org/10.1007/s11083-008-9081-9 . The publisher abstract expressly proves GPC when each element is incomparable with at most six others, using substantial computer assistance. It therefore proves the stronger exact balance assertion for D≤6, but the abstract does not establish all-D locality or compression. Full text was not obtained; no assertion is made that its intermediate lemmas lack overlap.

G. Brightwell and C. D. Wright, *The 1/3–2/3 conjecture for 5-thin posets*, SIAM Journal on Discrete Mathematics 5 (1992), 467–474. https://doi.org/10.1137/0405037 . Publisher abstract verifies the D≤5 hypothesis and computer-assisted case elimination.

J. Kahn and M. Saks, *Balancing poset extensions*, Order 1(2) (1984), 113–126. https://doi.org/10.1007/BF00565647 . Author-university record: https://www.researchwithrutgers.org/en/publications/balancing-poset-extensions/ . Its verified headline theorem gives a 3/11-balanced pair in every finite nonchain. This is a balance-existence theorem, not the finite-window probability comparison stated here. No inspected primary Stanley theorem was identified that directly subsumes the locality/representative claim; generic transfer-matrix enumeration alone does not imply uniform forgetting.

## Safe use and unresolved scope

1. Cite Brightwell's thin-poset convergence before presenting the finite-window result.
2. Attribute the analytic and finite-word mechanisms as classical, even when providing self-contained proofs.
3. Say that the present package supplies an explicit checked finite formulation and application, without asserting that it improves the literature.
4. Do not infer a uniform exact 1/3 decision procedure from additive approximation.
5. Novelty of either quantitative locality or the finite representative/computability corollary remains unestablished until the original Brightwell and relevant thin-poset proofs are compared directly.

No external messages or remote edits were made. Locally downloaded source PDFs are research aids, not part of the proposed original-work publication.
