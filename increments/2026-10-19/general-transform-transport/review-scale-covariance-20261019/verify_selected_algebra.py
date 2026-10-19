"""Independent exact audit of one fixed abstract law, without a search."""
from pathlib import Path
import json
import sympy as s

m = s.symbols('m', integer=True, positive=True)
t = s.symbols('t', nonnegative=True)

def choose_poly(z, k):
    if k < 0:
        return s.Integer(0)
    return s.prod(z-i for i in range(k))/s.factorial(k)

law = {
    (0, 0): s.Rational(1, 2),
    (0, 1): s.Rational(1, 4),
    (0, 2): s.Rational(11, 200),
    (0, 3): s.Rational(3, 80),
    (0, 4): s.Rational(23, 400),
    (1, 2): s.Rational(7, 100),
    (1, 3): s.Rational(1, 40),
    (1, 4): s.Rational(1, 200),
}
assert sum(law.values()) == 1
assert all(p > 0 and x <= y for (x, y), p in law.items())

def E(f):
    return s.factor(sum(p*f(x, y) for (x, y), p in law.items()))

def tail(i, j):
    return sum(p for (x, y), p in law.items() if x >= i and y >= j)

def lc_gaps(seq):
    return [s.factor(seq[i]**2-seq[i-1]*seq[i+1])
            for i in range(1, len(seq)-1)]

def shifted_positive(poly):
    coeffs = s.Poly(s.expand(poly.subs(m, t+1)), t).all_coeffs()
    return all(c >= 0 for c in coeffs) and coeffs[-1] > 0

r, ey, c = E(lambda x,y:x), E(lambda x,y:y), E(lambda x,y:x*y)
cov = c-r*ey
assert (r, ey, c, cov, cov-r*(r+1)) == (
    s.Rational(1,10), s.Rational(15,16), s.Rational(47,200),
    s.Rational(113,800), s.Rational(1,32))
assert all(tail(i,j) > 0 for i in range(2) for j in range(i,5))

qx = [tail(i,0) for i in range(2)]
qy = [tail(0,j) for j in range(5)]
mx = [E(lambda x,y,k=k:s.binomial(x,k)) for k in range(2)]
my = [E(lambda x,y,k=k:s.binomial(y,k)) for k in range(5)]
for seq in (qx,qy,mx,my):
    assert all(g >= 0 for g in lc_gaps(seq))

b = [E(lambda x,y,j=j:(min(x,j)+1) if y >= j else 0)
     for j in range(5)]
assert b == [1,s.Rational(3,5),s.Rational(7,20),
             s.Rational(31,200),s.Rational(27,400)]
assert lc_gaps(b) == [s.Rational(1,100),s.Rational(59,2000),
                      s.Rational(1,2500)]

w = E(lambda x,y:sum(y-i+1 for i in range(x+1)))
u = E(lambda x,y:sum(i*(y-i+1) for i in range(x+1)))
d = E(lambda x,y:sum(s.binomial(y-i+1,2) for i in range(x+1)))
v = E(lambda x,y:sum(i*s.binomial(y-i+1,2) for i in range(x+1)))
assert (w,u,d,v,u*d-w*v) == (s.Rational(869,400),s.Rational(47,200),
                            s.Rational(9,5),s.Rational(7,40),
                            s.Rational(137,3200))

A = E(lambda x,y:choose_poly(m+y,y))
B = E(lambda x,y:choose_poly(m+y-1,y-1) if x == 1 else 0)
C = E(lambda x,y:choose_poly(m+y,y-1))
D = E(lambda x,y:choose_poly(m+y-1,y-2) if x == 1 else 0)
F = s.factor(B*C-A*D)
expected = (m**6+45*m**5+739*m**4+5223*m**3+16612*m**2
            +16116*m-19008)/460800
assert s.expand(F-expected) == 0
assert shifted_positive(F)

bm = [E(lambda x,y,j=j:sum(choose_poly(m+j-i-1,j-i)
                           for i in range(min(x,j)+1)) if y >= j else 0)
      for j in range(5)]
rank_gaps = lc_gaps(bm)
expected_rank = [
    (25*m**2-25*m+2)/200,
    m*(125*m**3+370*m**2+349*m-136)/24000,
    m**2*(m+1)*(625*m**3+2750*m**2+1691*m-3914)/5760000,
]
assert all(s.expand(a-b) == 0 for a,b in zip(rank_gaps,expected_rank))
assert all(shifted_positive(g) for g in rank_gaps)

report = {
    'scope': 'One fixed abstract law; exact symbolic identities, no search or actual-poset enumeration.',
    'means': {'r': str(r), 's': str(ey), 'c': str(c),
              'covariance': str(cov), 'T_violation': str(cov-r*(r+1))},
    'joint_tail_positive': True,
    'Y_tail': list(map(str,qy)),
    'Y_binomial_moments': list(map(str,my)),
    'b': list(map(str,b)),
    'b_LC_gaps': list(map(str,lc_gaps(b))),
    'JC_m1_gap': str(u*d-w*v),
    'A_m': str(A), 'B_m': str(B), 'C_m': str(C), 'D_m': str(D),
    'JC_all_m_gap': str(F),
    'last_marker_LC_gaps': list(map(str,rank_gaps)),
    'all_m_positivity_method': 'Substitute m=t+1; expanded polynomial coefficients are nonnegative and constant is positive.',
    'status': 'PASS',
}
Path(__file__).with_name('selected_algebra_verification.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
