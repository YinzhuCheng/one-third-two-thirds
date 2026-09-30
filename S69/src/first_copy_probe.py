"""One targeted counterexample to a first-copy 2/5 menu, not to the conjecture.
Reuses the existing S68 exact order-ideal recurrence; separate from the pure
proofs of S69-CONE and S69-DIAGONAL. Emits JSON without changing any files.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "S68" / "src"))
from skeletons import expanded_counts

PRED = (0, 1, 67, 71, 79, 479, 0, 1, 193, 207)
NAMES = ["c1", "c2", "c3", "c4", "c5", "c6", "u1", "v1", "w", "z"]
lengths = (1, 1, 1, 1, 1, 1, 3, 50, 1, 1)
row = expanded_counts(PRED, lengths)
E = row[0]
comparisons = [
    {"x": NAMES[i], "y": NAMES[j], "x_before_y": v,
     "smaller_direction": min(v, E-v)}
    for (i, j), v in zip(combinations(range(10), 2), row[1:])
]
best = max(comparisons, key=lambda v: v["smaller_direction"])
print(json.dumps({
    "a": 3, "b": 50, "extensions": E, "scope": "45 first-copy/original-label pairs only",
    "best_pair": [best["x"], best["y"]],
    "maximum_smaller_direction_count": best["smaller_direction"],
    "maximum_smaller_direction_probability": str(Fraction(best["smaller_direction"], E)),
    "not_a_counterexample_to": ["Q68-TEN", "1/3-2/3 conjecture"],
    "comparisons": comparisons,
}, ensure_ascii=False, indent=2))
