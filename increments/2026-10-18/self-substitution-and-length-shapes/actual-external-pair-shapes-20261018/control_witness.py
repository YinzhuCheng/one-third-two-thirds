"""Direct LE controls of the single already-budgeted witness, no new typed R."""
import json
from pathlib import Path
from fractions import Fraction
P=Path(__file__).resolve().parent
R=json.loads((P/'all_counts.json').read_text())[65]
assert R['case_index']==66

def le_count(m,event=None):
    """Prefix DP with explicit chain progress; no binomial window formula."""
    n=R['n']; Dmask=(1<<R['d'])-1; U=set(range(R['d']+2,n))
    pred=R['pred']; final=(1<<n)-1
    # Event tuple is ((kind,index),(kind,index)); kind is 'R' or 'C'.
    def placed(token,mask,h):
        return (bool(mask>>token[1]&1) if token[0]=='R' else h>=token[1])
    dp={(0,0):1}
    for size in range(n+m):
        nxt={}
        for (mask,h),count in dp.items():
            if h<m and mask&Dmask==Dmask:
                x=('C',h+1)
                if event is None or x!=event[1] or placed(event[0],mask,h):
                    nxt[mask,h+1]=nxt.get((mask,h+1),0)+count
            for x in range(n):
                if mask>>x&1 or pred[x]&~mask or (x in U and h<m):continue
                token=('R',x)
                if event is not None and token==event[1] and not placed(event[0],mask,h):continue
                key=(mask|1<<x,h);nxt[key]=nxt.get(key,0)+count
        dp=nxt
    return dp.get((final,m),0)

out=[]
for m in [0,1,6,18]:
    T=le_count(m)
    expected=8+11*(m+1)+4*(m+1)*(m+2)//2
    assert T==expected
    pairrows=[]
    for event,coeff in [((1,2),(3,6,2)),((2,3),(8,8,3))]:
        count=le_count(m,(('R',event[0]),('R',event[1])))
        a,b,c=coeff
        assert count==a+b*(m+1)+c*(m+1)*(m+2)//2
        pairrows.append(dict(pair=[R['names'][event[0]],R['names'][event[1]]],count=count,probability=str(Fraction(count,T))))
    chainrows=[]
    for j in range(1,m+1):
        for x in [R['d'],R['d']+1]:
            count=le_count(m,(('C',j),('R',x)))
            chainrows.append(dict(pair=[f'c{j}',R['names'][x]],count=count,probability=str(Fraction(count,T)),balanced=(T<=3*count<=2*T)))
    out.append(dict(m=m,total=T,external=pairrows,chain_columns=chainrows,chain_columns_have_balanced_pair=any(r['balanced'] for r in chainrows)))
(P/'direct_LE_controls.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([dict(m=r['m'],total=r['total'],external=r['external'],balanced_chain_pairs=[p for p in r['chain_columns'] if p['balanced']][:5],chain_columns_have_balanced_pair=r['chain_columns_have_balanced_pair']) for r in out],ensure_ascii=False,indent=2))
