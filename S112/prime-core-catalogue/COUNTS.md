# Exact catalogue counts

All enumeration columns below count naturally labelled relations, not unlabelled posets.

| n | Natural posets | Prime | Prime, width ≥3 | No very-good pair either side | Separate cycles passed | Generic two-port passed | Survivor isomorphism classes |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 3 | 7 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 40 | 5 | 0 | 0 | 0 | 0 | 0 |
| 5 | 357 | 35 | 27 | 0 | 0 | 0 | 0 |
| 6 | 4824 | 744 | 696 | 0 | 0 | 0 | 0 |
| 7 | 96428 | 19256 | 19097 | 44 | 44 | 44 | 1 |
| 8 | 2800472 | 720147 | 719417 | 2552 | 2552 | 2552 | 17 |

The last column alone is an exact isomorphism-class count, obtained by canonicalizing survivors. Duals are not automatically identified.

No cycle filter adds a uniform exclusion beyond very-good pairs through n=8. There are no recorded cycle-beyond-very-good examples in this range.

At n=8, survivors by width: 2,087 natural copies at width 3 and 465 at width 4; by height: 783 at height 3, 1,687 at height 4, and 82 at height 5.

## Exact survivor-class inventory

Representative upper masks are the lexicographically least natural presentation. Every class has Aut=1. The displayed forced nonsingletons are complete minimal singleton-pattern clauses in this finite catalogue; all clauses happen to be singletons. A blank clause list means this structural test supplies no weight restriction.

| ID | n | width | height | Natural copies = e(Q) | Must have weight ≥2 | Local minimum total size from these clauses |
|---|---:|---:|---:|---:|---|---:|
| C01 | 7 | 3 | 4 | 44 | 0, 6 | 9 |
| C02 | 8 | 3 | 4 | 194 | 7 | 9 |
| C03 | 8 | 3 | 4 | 102 | 0, 5 | 10 |
| C04 | 8 | 3 | 4 | 194 | 0 | 9 |
| C05 | 8 | 3 | 4 | 102 | 5, 7 | 10 |
| C06 | 8 | 3 | 4 | 107 | 0 | 9 |
| C07 | 8 | 3 | 5 | 82 | 0, 3, 6 | 11 |
| C08 | 8 | 3 | 4 | 107 | none | 8 |
| C09 | 8 | 3 | 4 | 132 | none | 8 |
| C10 | 8 | 3 | 4 | 107 | 5 | 9 |
| C11 | 8 | 3 | 3 | 318 | none | 8 |
| C12 | 8 | 3 | 4 | 96 | 0, 6 | 10 |
| C13 | 8 | 3 | 4 | 98 | 0, 3 | 10 |
| C14 | 8 | 3 | 4 | 121 | none | 8 |
| C15 | 8 | 3 | 4 | 121 | none | 8 |
| C16 | 8 | 3 | 4 | 96 | 5, 6 | 10 |
| C17 | 8 | 3 | 4 | 110 | 6 | 9 |
| C18 | 8 | 4 | 3 | 465 | 0, 7 | 10 |

These are necessary lower bounds from port constraints only, not existence results or sharp bounds for counterexamples.

## Representatives

### C01
Upper masks: `(40, 124, 104, 32, 32, 0, 0)`.
Cover edges: `[[0, 3], [1, 2], [1, 4], [2, 3], [2, 6], [3, 5], [4, 5]]`.

### C02
Upper masks: `(68, 236, 64, 96, 224, 64, 0, 0)`.
Cover edges: `[[0, 2], [1, 2], [1, 3], [1, 7], [2, 6], [3, 5], [4, 5], [4, 7], [5, 6]]`.

### C03
Upper masks: `(72, 252, 216, 64, 192, 64, 0, 0)`.
Cover edges: `[[0, 3], [1, 2], [1, 5], [2, 3], [2, 4], [3, 6], [4, 6], [4, 7], [5, 6]]`.

### C04
Upper masks: `(72, 252, 88, 0, 64, 192, 0, 0)`.
Cover edges: `[[0, 3], [0, 6], [1, 2], [1, 5], [2, 3], [2, 4], [4, 6], [5, 6], [5, 7]]`.

### C05
Upper masks: `(84, 252, 80, 208, 64, 64, 0, 0)`.
Cover edges: `[[0, 2], [1, 2], [1, 3], [1, 5], [2, 4], [3, 4], [3, 7], [4, 6], [5, 6]]`.

### C06
Upper masks: `(168, 252, 184, 128, 32, 0, 128, 0)`.
Cover edges: `[[0, 3], [0, 5], [1, 2], [1, 6], [2, 3], [2, 4], [3, 7], [4, 5], [6, 7]]`.

### C07
Upper masks: `(168, 252, 184, 0, 160, 128, 128, 0)`.
Cover edges: `[[0, 3], [0, 5], [1, 2], [1, 6], [2, 3], [2, 4], [4, 5], [5, 7], [6, 7]]`.

### C08
Upper masks: `(168, 252, 136, 128, 224, 0, 128, 0)`.
Cover edges: `[[0, 3], [0, 5], [1, 2], [1, 4], [2, 3], [3, 7], [4, 5], [4, 6], [6, 7]]`.

### C09
Upper masks: `(178, 16, 248, 176, 0, 128, 128, 0)`.
Cover edges: `[[0, 1], [0, 5], [1, 4], [2, 3], [2, 6], [3, 4], [3, 5], [5, 7], [6, 7]]`.

### C10
Upper masks: `(178, 144, 248, 176, 128, 0, 128, 0)`.
Cover edges: `[[0, 1], [0, 5], [1, 4], [2, 3], [2, 6], [3, 4], [3, 5], [4, 7], [6, 7]]`.

### C11
Upper masks: `(68, 236, 0, 192, 224, 64, 0, 0)`.
Cover edges: `[[0, 2], [0, 6], [1, 2], [1, 3], [1, 5], [3, 6], [3, 7], [4, 5], [4, 7], [5, 6]]`.

### C12
Upper masks: `(168, 252, 184, 128, 160, 0, 128, 0)`.
Cover edges: `[[0, 3], [0, 5], [1, 2], [1, 6], [2, 3], [2, 4], [3, 7], [4, 5], [4, 7], [6, 7]]`.

### C13
Upper masks: `(168, 252, 232, 0, 160, 128, 128, 0)`.
Cover edges: `[[0, 3], [0, 5], [1, 2], [1, 4], [2, 3], [2, 5], [2, 6], [4, 5], [5, 7], [6, 7]]`.

### C14
Upper masks: `(178, 144, 248, 176, 0, 128, 128, 0)`.
Cover edges: `[[0, 1], [0, 5], [1, 4], [1, 7], [2, 3], [2, 6], [3, 4], [3, 5], [5, 7], [6, 7]]`.

### C15
Upper masks: `(180, 252, 16, 176, 0, 128, 128, 0)`.
Cover edges: `[[0, 2], [0, 5], [1, 2], [1, 3], [1, 6], [2, 4], [3, 4], [3, 5], [5, 7], [6, 7]]`.

### C16
Upper masks: `(180, 252, 144, 176, 128, 0, 128, 0)`.
Cover edges: `[[0, 2], [0, 5], [1, 2], [1, 3], [1, 6], [2, 4], [3, 4], [3, 5], [4, 7], [6, 7]]`.

### C17
Upper masks: `(180, 252, 144, 176, 0, 128, 128, 0)`.
Cover edges: `[[0, 2], [0, 5], [1, 2], [1, 3], [1, 6], [2, 4], [2, 7], [3, 4], [3, 5], [5, 7], [6, 7]]`.

### C18
Upper masks: `(32, 104, 248, 32, 96, 0, 0, 0)`.
Cover edges: `[[0, 5], [1, 3], [1, 6], [2, 3], [2, 4], [2, 7], [3, 5], [4, 5], [4, 6]]`.

