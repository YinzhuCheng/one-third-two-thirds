"""Exact finite audit of the S104 joint interface, not a proof."""
import itertools

def run():
    posets=pairs=0
    for n in range(2,6):
        possible=list(itertools.combinations(range(n),2))
        seen=set()
        for bits in range(1<<len(possible)):
            up=[0]*n
            for i,(x,y) in enumerate(possible):
                if bits>>i&1: up[x]|=1<<y
            for x in reversed(range(n)):
                for y in range(x+1,n):
                    if up[x]>>y&1: up[x]|=up[y]
            key=tuple(up)
            if key in seen: continue
            seen.add(key)
            down=[sum(1<<x for x in range(n) if up[x]>>y&1) for y in range(n)]
            les=[]
            for f in itertools.permutations(range(n)):
                order=[0]*n
                for i,x in enumerate(f): order[x]=i
                if all(order[x]<order[y] for x,y in possible if up[x]>>y&1): les.append(order)
            posets+=1
            for a,b in possible:
                if up[a]>>b&1: continue
                neutral=[x for x in range(n) if x not in (a,b) and not ((up[a]|down[a]|up[b]|down[b])>>x&1)]
                if any(not(up[x]>>y&1 or up[y]>>x&1) for x,y in itertools.combinations(neutral,2)):continue
                cells=[[0]*4 for _ in range(2)] # h,r,l,k
                low_count=high_count=0
                for order in les:
                    dr=0 if order[a]<order[b] else 1
                    x,y=(a,b) if dr==0 else (b,a)
                    s=any(up[x]>>z&1 and order[z]<order[y] for z in range(n))
                    t=any(down[y]>>z&1 and order[x]<order[z] for z in range(n))
                    cells[dr][int(s)+2*int(t)]+=1
                    low=all(order[z]<min(order[a],order[b]) for z in range(n) if (down[a]|down[b])>>z&1)
                    high=all(order[z]>max(order[a],order[b]) for z in range(n) if (up[a]|up[b])>>z&1)
                    assert low==(not t)
                    assert high==(not s)
                    low_count+=low; high_count+=high
                h,r,l,k=cells[0]; hh,rr,ll,kk=cells[1]
                assert h==hh and h>0
                assert low_count==2*h+r+rr
                assert high_count==2*h+l+ll
                assert r*rr<=h*h and l*ll<=h*h, (n,key,a,b,cells)
                pairs+=1
        print(f'n={n}: distinct naturally labelled posets={len(seen)}; cumulative checked pairs={pairs}')
    print(f'PASS: {posets} naturally labelled posets; {pairs} eligible incomparable pairs. All complete extension orders enumerated exactly.')
if __name__=='__main__': run()
