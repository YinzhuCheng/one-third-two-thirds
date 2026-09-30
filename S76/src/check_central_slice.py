"""Complete finite remainder t=1..23 for the S76 mixed central slice.
Infinite t>=24 is handled by the written bounded-defect proof.
Run with Python 3 from any directory; outputs go to S76/evidence.
Both encodings share the template and finite domain, not independent review.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
import csv
import json
import time
from ten_chain_counts import distribution

PRED = (0, 1, 67, 71, 79, 479, 0, 1, 193, 207)


def direct(t, witness=None):
    if not isinstance(t, int) or t < 1:
        raise ValueError('t must be a positive integer')
    sizes = (1, 1, t, t, 1, 1, 1, 2*t, 1, 1)
    pred = [[a for a in range(10) if PRED[b] >> a & 1] for b in range(10)]
    if witness:
        i, j = witness
        xi = 2 if i <= t else 3
        rank = i if i <= t else i-t

    @lru_cache(None)
    def count(state):
        if state == sizes:
            return 1
        out = 0
        for b in range(10):
            if state[b] == sizes[b] or any(state[a] < sizes[a] for a in pred[b]):
                continue
            # Exclude V_j until the specified C3+C4 label has occurred.
            if witness and b == 7 and state[7] == j-1 and state[xi] < rank:
                continue
            nxt = list(state)
            nxt[b] += 1
            out += count(tuple(nxt))
        return out

    result = count((0,)*10)
    count.cache_clear()
    return result


def run():
    root = Path(__file__).resolve().parents[1] / 'evidence'
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    started = time.time()
    for t in range(1, 24):
        stats, hist = distribution((1,1,t,t,1,1), (1,2*t,1,1))
        total = stats['total']
        best = None
        for i in range(1, 2*t+1):
            event = 0
            for j in range(1, 2*t+1):
                # C3+C4 starts after the first two singleton main-chain points.
                event += hist[0,2][i+1][j-1]
                candidate = (min(event,total-event), -i, -j, event)
                if best is None or candidate > best:
                    best = candidate
        balanced, ii, jj, event = best
        i, j = -ii, -jj
        if not (5*event >= 2*total and 5*event <= 3*total):
            raise ArithmeticError(f'No recorded 2/5 witness at t={t}')
        if direct(t) != total or direct(t,(i,j)) != event:
            raise ArithmeticError(f'Coordinate recurrences disagree at t={t}')
        rows.append(dict(t=t, i=i, j=j, E=str(total), N=str(event),
                         probability=str(Fraction(event,total)),
                         balance=str(Fraction(balanced,total)),
                         left_margin=str(5*event-2*total),
                         right_margin=str(3*total-5*event), states=stats['states']))
        print(t, i, j, str(Fraction(balanced,total)), flush=True)
    with (root/'central_slice_1_23.csv').open('w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    low = min(rows,key=lambda r: Fraction(r['balance']))
    summary = dict(cases=23, all_pass=True,
                   domain='main=(1,1,t,t,1,1), outer=(1,2t,1,1), t=1..23',
                   minimum_selected_balance=low['balance'], minimum_selected_at=low['t'],
                   seconds=time.time()-started,
                   shared_inputs='same template and domain; three-chain edge flow vs ten-module direct event recurrence')
    (root/'central_summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))


if __name__ == '__main__':
    run()
