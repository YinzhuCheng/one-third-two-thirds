from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
OUT=Path(__file__).parent
names=['a','b','z','u','v','w','t','c1','c2','y']
edges=[('a','u'),('u','w'),('w','t'),('t','c1'),('c1','c2'),('b','v'),('v','t'),('z','c1'),('b','y')]

def build(labels, edges):
    idx={x:i for i,x in enumerate(labels)}
    rel=[[False]*len(labels) for _ in labels]
    for a,b in edges:rel[idx[a]][idx[b]]=True
    for k in range(len(labels)):
        for i in range(len(labels)):
            for j in range(len(labels)):
                rel[i][j] |= rel[i][k] and rel[k][j]
    assert not any(rel[i][i] for i in range(len(labels)))
    pred=[sum(1<<j for j in range(len(labels)) if rel[j][i]) for i in range(len(labels))]
    total=0; counts=[[0]*len(labels) for _ in labels]; orders=[];calls=0
    def dfs(mask,order):
        nonlocal total,calls
        calls+=1
        if len(order)==len(labels):
            total+=1
            orders.append(tuple(labels[i] for i in order))
            for k,i in enumerate(order):
                for j in order[k+1:]:counts[i][j]+=1
            return
        for i in range(len(labels)):
            if not (mask>>i)&1 and pred[i]&mask==pred[i]:dfs(mask|(1<<i),order+[i])
    dfs(0,[])
    @lru_cache(None)
    def dp(mask):
        if mask==(1<<len(labels))-1:return 1
        return sum(dp(mask|1<<i) for i in range(len(labels)) if not mask>>i&1 and pred[i]&mask==pred[i])
    assert dp(0)==total
    rows=[]
    for i,j in combinations(range(len(labels)),2):
        assert counts[i][j]+counts[j][i]==total
        relation='<' if rel[i][j] else '>' if rel[j][i] else '||'
        rows.append(dict(pair=[labels[i],labels[j]],relation=relation,count=counts[i][j],total=total,fraction=str(Fraction(counts[i][j],total)),balanced=(total<=3*counts[i][j]<=2*total),lower_gap=3*counts[i][j]-total,upper_gap=2*total-3*counts[i][j]))
    covers=[(labels[i],labels[j]) for i in range(len(labels)) for j in range(len(labels)) if rel[i][j] and not any(rel[i][k] and rel[k][j] for k in range(len(labels)))]
    return dict(names=labels,total=total,dfs_calls=calls,rows=rows,covers=covers,relation=rel,counts=counts),orders
P,Porders=build(names,edges)
qnames=[x for x in names if x!='c1']
qedges=[(names[i],names[j]) for i in range(len(names)) for j in range(len(names)) if P['relation'][i][j] and names[i]!='c1' and names[j]!='c1']
Q,Qorders=build(qnames,qedges)
# Independent module check of every strict superset of C, using only the relation matrix.
def is_chain(ids):return all(P['relation'][i][j] or P['relation'][j][i] for i,j in combinations(ids,2))
def profile(x,s):return -1 if P['relation'][x][s] else 1 if P['relation'][s][x] else 0
def autonomous(ids):
    return all(len({profile(x,s) for s in ids})==1 for x in range(len(names)) if x not in ids)
C={names.index('c1'),names.index('c2')}
supersets=[]
for mask in range(1<<len(names)):
    ids={i for i in range(len(names)) if mask>>i&1}
    if C<ids and is_chain(ids) and autonomous(ids):supersets.append([names[i] for i in ids])
assert autonomous(C) and is_chain(C) and not supersets
# D orders and y-insertion windows; no formula from producer used.
Dnames=[x for x in names if x not in ['c1','c2','y']]
Dedges=[(names[i],names[j]) for i in range(len(names)) for j in range(len(names)) if P['relation'][i][j] and names[i] in Dnames and names[j] in Dnames]
D,Dorders=build(Dnames,Dedges)
window=[]
for o in Dorders:
    pos={x:i+1 for i,x in enumerate(o)}
    # Insertion after gap k (0<=k<=7), with b strictly before y, means k>=pos(b).
    admissible=list(range(pos['b'],len(o)+1))
    window.append(dict(order=o,h=len(admissible),u_before_v=pos['u']<pos['v'],y_before_u=sum(k<pos['u'] for k in admissible),y_before_v=sum(k<pos['v'] for k in admissible)))
h=sum(w['h'] for w in window)
e=sum(w['u_before_v'] for w in window)
he=sum(w['h']*w['u_before_v'] for w in window)
result=dict(P=P,Q=Q,D=D,C_autonomous=True,C_maximal=True,strict_autonomous_chain_supersets=supersets,window=dict(count=len(window),h_sum=h,event_count=e,h_event_sum=he,covariance=str(Fraction(he,len(window))-Fraction(h,len(window))*Fraction(e,len(window))),y_before_u=sum(w['y_before_u'] for w in window),y_before_v=sum(w['y_before_v'] for w in window)))
(OUT/'audit-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
(OUT/'P-linear-extensions.tsv').write_text('\n'.join('\t'.join(o) for o in Porders)+'\n')
(OUT/'Q-linear-extensions.tsv').write_text('\n'.join('\t'.join(o) for o in Qorders)+'\n')
(OUT/'D-window-records.json').write_text(json.dumps(window,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ['P','Q','D']},ensure_ascii=False,indent=2))
for k in ['P','Q','D']:print(k, 'LE=',result[k]['total'],'DFS_calls=',result[k]['dfs_calls'],'covers=',result[k]['covers'])
for p in [('u','v'),('c1','y'),('c2','y')]:
    print(p,next(r for r in P['rows'] if r['pair']==list(p)))
print('BALANCED P:',[r for r in P['rows'] if r['balanced']])
print('BALANCED Q:',[r for r in Q['rows'] if r['balanced']])
# Exact deletion-fiber/window verification: erase c1 in every P extension.
from collections import Counter
fibers=Counter(tuple(x for x in o if x!='c1') for o in Porders)
assert set(fibers)==set(Qorders)
E=lambda o:o.index('u')<o.index('v')
window_special=lambda o:max(o.index(d) for d in Dnames)<o.index('y')<o.index('c2')
assert all(fibers[o]==1+int(window_special(o)) for o in Qorders)
T=len(Qorders); SX=sum(E(o) for o in Qorders); SW=sum(fibers.values()); SWX=sum(fibers[o]*E(o) for o in Qorders)
cov=Fraction(SWX,T)-Fraction(SW,T)*Fraction(SX,T)
result['deletion_window']=dict(Q_count=T,window_special_count=sum(window_special(o) for o in Qorders),window_special_and_event_count=sum(window_special(o) and E(o) for o in Qorders),sum_W=SW,sum_X=SX,sum_WX=SWX,window_size_distribution=dict(Counter(fibers.values())),cov_W_X=str(cov),probability_shift=str(cov/Fraction(SW,T)))
(OUT/'audit-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('DELETION WINDOW',result['deletion_window'])
