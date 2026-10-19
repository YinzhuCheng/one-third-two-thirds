# Frozen targeted actual-poset budget

The test is Q_i(m+1) > Q_i(m) > Q_{i+1}(m+1), with D < C_m < U and every I point incomparable to every chain point. I itself may have relations. All counts are uniform counts of labeled actual linear extensions.

Budget frozen before testing: 28 outer families = 7 multigate side schemas × 4 I-order templates. For each family test t in {3,4,5,6}, three gate aspect ratios, and m in {1,3,11,47,191,767}. This is at most 336 actual outside posets and 2016 adjacent-length comparisons. Every x and every eligible i is checked. Stop enlarging the pool immediately on any failure; minimize its actual relation certificate instead.

I templates: antichain; full chain; alternating fence; two disjoint chains.
Side schemas: two independent chains with staggered cuts; two ordinally joined antichain blocks; two independent antichain clone gates; chain with incomparable antichain gate; three ordinal gate blocks; crossed two-chain cuts; asymmetric opposite-marker gates. Aspect ratios: balanced (3,3), left-heavy (23,1), right-heavy (1,23). Side assignments and closures must be explicit in the executable manifest. No arbitrary polynomial-coefficient relaxation is admitted.

Method: exact grouped ideal DP on D∪I and I∪U, then exact central-chain subset transfer. Antichain clone multiplicities count labeled elements. Independent full bitmask ideal DP verifies tiny controls. Complete relations and the two chain-length total/numerator counts are saved for any failure.
