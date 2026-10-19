from fractions import Fraction as Q
import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
CONTROLS=[((3,3,1),(2,0)),((4,4,1),(3,0)),((6,6,1),(5,0)),((3,6,1),(2,1)),((6,3,1),(4,0)),((4,4,2),(2,1)),((5,5,2),(3,1)),((3,5,3),(2,1))]
def close_pred(n,edges):
    pred=[0]*n
    for a,b in edges: pred[b]|=1<<a
    for k in range(n):
        for j in range(n):
            if pred[j]>>k&1: pred[j]|=pred[k]
    return pred

def calc(n,edges):
    pred=close_pred(n,edges); full=(1<<n)-1
    pref={0:1}; levels=[[0]]
    for size in range(n):
        nxt=set()
        for mask in levels[-1]:
            for a in range(n):
                if not mask>>a&1 and pred[a]&mask==pred[a]:
                    m=mask|1<<a; pref[m]=pref.get(m,0)+pref[mask];nxt.add(m)
        levels.append(sorted(nxt))
    if full not in pref:return 0,{},0
    suff={full:1}
    counts={(a,b):0 for a in range(n) for b in range(n) if a!=b}
    for lev in reversed(levels[:-1]):
        for mask in lev:
            s=0
            for a in range(n):
                if not mask>>a&1 and pred[a]&mask==pred[a]:
                    m=mask|1<<a; s+=suff[m]; v=pref[mask]*suff[m]
                    for b in range(n):
                        if b!=a and not mask>>b&1: counts[a,b]+=v
            suff[mask]=s
    assert pref[full]==suff[0]
    return pref[full],{k:Q(v,pref[full]) for k,v in counts.items()},sum(map(len,levels))

def bal(v):return Q(1,3)<=v<=Q(2,3)
results=[]
for idx,(lens,(ia,jb)) in enumerate(CONTROLS,1):
    names=[]; edges=[];start=0; chains=[]
    for letter,l in zip('ABC',lens):
        ids=list(range(start,start+l));chains.append(ids)
        names.extend(f'{letter}{k+1}' for k in range(l))
        edges.extend(zip(ids,ids[1:]));start+=l
    n=start;x=chains[0][ia];y=chains[1][jb]
    t,q,states=calc(n,edges);tp,qp,sp=calc(n,edges+[(x,y)]);tm,qm,sm=calc(n,edges+[(y,x)])
    p=Q(tp,t);assert tp+tm==t
    for uv in q:assert q[uv]==p*qp[uv]+(1-p)*qm[uv]
    ext=[(a,b) for a in range(n) for b in range(a+1,n) if a not in (x,y) and b not in (x,y)]
    wp=[uv for uv in ext if bal(qp[uv])];wm=[uv for uv in ext if bal(qm[uv])]
    lostp=[uv for uv in wp if not bal(q[uv])];lostm=[uv for uv in wm if not bal(q[uv])]
    def desc(uv):
        a,b=uv;return {'pair':[names[a],names[b]],'q':str(q[uv]),'plus':str(qp[uv]),'minus':str(qm[uv]),'delta':str(qp[uv]-qm[uv])}
    r={'control':idx,'lengths':lens,'edit':[names[x],names[y]],'extensions':t,'plus_extensions':tp,'minus_extensions':tm,'p':str(p),'ideal_states':[states,sp,sm],'external_plus_witnesses':[desc(uv) for uv in wp],'external_minus_witnesses':[desc(uv) for uv in wm],'external_lost_plus':[desc(uv) for uv in lostp],'external_lost_minus':[desc(uv) for uv in lostm]}
    results.append(r)
    print(idx,lens,r['edit'],'p',p,'e',t,'ext witnesses',len(wp),len(wm),'lost',len(lostp),len(lostm))
    if lostp:print(' LOST PLUS',*[desc(uv) for uv in lostp],sep='\n')
    if lostm:print(' LOST MINUS',*[desc(uv) for uv in lostm],sep='\n')
(OUT/'verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
