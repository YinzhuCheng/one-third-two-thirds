from functools import lru_cache

def counts(r,t):
    # a0 b1 x2 y3, v labels4..3+r, z labels4+r..3+r+t
    n=4+r+t; pred=[0]*n
    edges=[(0,1),(0,4),(3,4),(2,5),(1,4+r),(2,4+r)]
    edges +=[(i,i+1) for i in range(4,3+r)]+[(i,i+1) for i in range(4+r,3+r+t)]
    for a,b in edges:pred[b]|=1<<a
    def e(pair=None):
        p=pred.copy()
        if pair:p[pair[1]]|=1<<pair[0]
        full=(1<<n)-1
        @lru_cache(None)
        def f(mask):
            if mask==full:return 1
            return sum(f(mask|1<<i) for i in range(n) if not(mask>>i&1) and p[i]&mask==p[i])
        return f(0)
    return [e()]+[e(ab) for ab in [(0,2),(0,3),(1,2),(1,3),(2,3)]]
if __name__=='__main__':
    E,ax,ay,bx,by,xy=counts(15,54)
    assert [E,ax,ay,bx,by,xy]==[14395164266463908,9750632308747096,11262772937084132,4796894339975628,8130381607704356,9604711718385252]
    print('PASS',E,ax,ay,bx,by,xy)
    print('Hypothesis margins',[3*k-2*E for k in [ax,ay,xy]])
    print('L margin',3*bx-E)
    print('Rescue pair margins',3*by-E,2*E-3*by)
