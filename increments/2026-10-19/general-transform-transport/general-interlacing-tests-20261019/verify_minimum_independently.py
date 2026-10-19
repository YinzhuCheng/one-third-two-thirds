#!/usr/bin/env python3
"""Generic full labeled actual-poset ideal DP, independent of grouped/subset transfer."""
import sys,json,time
from functools import lru_cache
from test_actual import explicit,ROOT
sys.setrecursionlimit(20000)
cert=json.loads((ROOT/'minimum_gap_certificate.json').read_text()); case=cert['parameters']; rows=[]
def count(m,pair=None):
    labels,edges=explicit(case,m)
    if pair: edges.append(pair)
    idx={x:i for i,x in enumerate(labels)}; n=len(labels); bits=[1<<v for v in range(n)]; pred=[0]*n
    for a,b in edges: pred[idx[b]]|=bits[idx[a]]
    full=(1<<n)-1
    # Only masks of actual ideals are reached. There is no use of the transfer algorithm.
    @lru_cache(None)
    def rec(s):
        if s==full: return 1
        ans=0; remaining=full^s
        while remaining:
            bit=remaining&-remaining; remaining-=bit; v=bit.bit_length()-1
            if pred[v]&s==pred[v]: ans+=rec(s|bit)
        return ans
    st=time.time(); result=rec(0)
    rows.append({'m':m,'added_pair':pair,'count':str(result),'ideal_states':rec.cache_info().currsize,'seconds':time.time()-st})
    return result
m=cert['m']; i=cert['i']; x='x'+str(cert['x'])
assert count(m)==int(cert['total_m'])
assert count(m+1)==int(cert['total_m1'])
assert count(m,(f'c{i}',x))==int(cert['numerator_i_m'])
assert count(m+1,(f'c{i}',x))==int(cert['numerator_i_m1'])
assert count(m+1,(f'c{i+1}',x))==int(cert['numerator_ip1_m1'])
out={'status':'PASS','method':'Full labeled bitmask ideal DP, no compressed transfer recurrence','checks':rows}
(ROOT/'minimum_gap_independent_check.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out),flush=True)
