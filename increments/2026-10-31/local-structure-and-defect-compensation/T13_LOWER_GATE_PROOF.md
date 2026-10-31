# T13：A侧下门一般参数定理（两次独审通过）

任意有限 C2，S=A\U(d)={s}，b<s，e<F。令 R=A∩U(e)，其中有 m 个不同锚，每个都严格低于 F∪U(s) 的每个点；令 k=|A\({s}∪U(e))|，这些是 d-only A 点。若
- m≥2 且 k≤2m−3；或
- m=1 且 k=0，
则 **p(c1<d)<(1+q0)/2**，固定菜单 {(c1,v),(c1,d)} 至少一对闭平衡。无需度数界。单 h 双锚是 m=2,k=1 的特例，不重复作为主定理。

## 一般证明增量
沿用后文的真实外词、核心和插槽定义；空目标仍用末槽哨兵。
b 非首时原封闭式 `D=W(C,H)−W(C,I)≤0` 不变，不限制该分支的 H。
b 首时，删 b 后 e 截止 H≤k+1，两个自由截止 I,J≥H+m。原逐前缀恒等式仍是
`D=4W(J,H)+2W(I,H)+5H−4W(I,J)`，
化为 `4HJ+2HI+11H−4IJ−4min(I,J)`，分别随 I,J 严格递减，因此
`D≤f_m(H)=2H²+(7−2m)H−4m²−4m`。
m≥2、k≤2m−3 给 1≤H≤2m−2；凸函数 f_m 在此区间的最大值取端点，其值分别为
`f_m(1)=9−6m−4m²<0`，`f_m(2m−2)=−2m−6<0`。
m=1,k=0 时 H=1，同式给 f_1(1)=−1<0。
因为 b 在外部诱导偏序中极小，存在 b 首的合法外词且对应纤维非空，求和严格为负，故最终得到严格上界。有限小核计算不承担一般证明。

参数版由本轮研究汇总记录确认已两次独审；后附旧单h正文用于保存完整前缀推导，不再把“仅单h/推广待审”的历史文字当当前状态。历史/文献优先权仍未全排重。

## E16 的准确覆盖声明
15点E16满足m=2,k=1，已审无VG/混合环/真非平凡模块，q0处于旧r2门槛未覆盖窗口。但精确E预算本身可对本例计算闭合；因此只声称超出已查静态/匹配门槛，不能说旧误差预算不适用或超出全部工具。

---
## 历史单h证明细节（作为一般参数证明的共同前缀计数，不另立定理）

# A-side lower-gate anchor-budget lemma (general extension under independent audit)

## Statement
Use the complete finite C2 setting from the checkpoint, with uniform measure on all linear extensions of the original P. Write q0=Pr(c1<v), p_d=Pr(c1<d).
Assume:
1. A\U(d)={s};
2. Set R=A intersect U(e), and H_A=A\({s} union R), with k=|H_A|. Assume e<F. Every point of H_A is above d and incomparable with e.
3. b<s. **No relation between b and H_A is assumed or needed.**
4. There are m>=2 distinct anchors in R, each strictly below every member of F union U(s), where U(s) is the full strict upper set in P, and k<=2m-3.

Then p_d < (1+q0)/2 (in particular the weak inequality needed for the menu). Hence the existing C2 fixed menu {(c1,v),(c1,d)} contains a balanced pair. No bound on |A|, |F| or incomparability degree is used.
The relevant |A|=5 special case is m=2,k<=1. The statement does not claim general C2 closure. The m=1,k=0 case also follows from the same formula, but is not needed here.

## Reduction preserving the original measure
On the event v<c1, v is necessarily first. Delete it and put a=c1, x=c2, y=e. The five core labels K={a,d,x,y,s} satisfy exactly a<x,s and d<y. The external set is O={b} union H_A union R union F. Here b<s is the sole external-to-core predecessor relation. Indeed every A point other than s is above d, so none can be below s; b is the only possible remaining predecessor of s besides a after deleting v.
The external successors of a and d are all of O\{b}; those of y are R union F; those of x are F; those of s are U(s). All other restrictions are encoded by the fixed real external linear extension w of P[O]. We prove a nonpositive signed count (#a<d)-(#d<a) in each fiber; fibers are summed with their actual cardinalities, never reweighted uniformly.

For a fixed external word, use gap index j for the gap before its j-th label, with final gap m+1. A label with its first required external successor at position j can occupy gaps 1,...,j. An empty successor set uses the sentinel m+1.
For two independent core labels with allowed initial gap sets [1,i],[1,j], the insertion count is
    W(i,j)=ij+min(i,j).
The product counts different gap choices once; a common gap permits two relative orders and adds min(i,j).

## Case 1: b is not the first external label
Let b be at position B>=2. Let H,I,J be the external deadlines of y,x,s, respectively. Both a,d must precede the first external label. The anchors lie before every F point, and y is below both anchors, so I>=H. The b<s relation forces s to use only gaps in C={B+1,...,J}. (The external word already respects b<U(s), so J>B whenever this fiber is nonempty.)
Pair words whose core prefix is a,d with those whose prefix is d,a; swap these two labels. The remainder and all insertion restrictions are identical. Because s cannot precede the first external label, the only uncancelled positive prefix is a,x,d; the only uncancelled negative prefix is d,y,a.
After deleting those prefixes, the positive remainder consists of s in C and y before deadline H. The negative remainder consists of s in C and x before deadline I. For an arbitrary interval C define
    W(C,k)=k|C|+|C intersect {1,...,k}|.
Thus the signed count is exactly W(C,H)-W(C,I)<=0, since I>=H. This is the step that removes the unnecessary b<H_A assumption: an H_A point is allowed to be the first external label, and y need not be before it.

## Case 2: b is the first external label
Delete b from the external word, leaving w'. Both a,d must be before the first label of w'. Let H,I,J now mean y,x,s deadlines measured in w'. Only H_A points fail to be above y, so 1<=H<=k+1. The m distinct anchors precede every x- and s-successor; therefore
    I,J >= H+m.
Inserting b back requires b to precede the first w' label and also to precede s. Any relation of b to other external labels is already respected because b is first among all external labels.

Again cancel the adjacent starting prefixes a,d and d,a. The remaining prefixes and their b-weighted contributions are:
    a x d:   3W(J,H)+B(J,H)
    a s d:   2W(I,H)
    a x s d: 3H
    a s x d: 2H
    d y a:   3W(I,J)+B(J,I)  [negative]
Here B(J,k) counts insertion of b,s,z after the displayed prefix, with b before the first external label, b<s, and deadlines J,k for s,z. Its initial labels must be either b, or z,b; hence
    B(J,k)=W(J,k)+J.
The extra J cancels between the positive and negative terms, giving the exact signed difference
    D=4W(J,H)+2W(I,H)+5H-4W(I,J).
Since H<=I,J this equals
    D=4HJ+2HI+11H-4IJ-4min(I,J).
For I,J>=H+m it is strictly decreasing separately in each variable (the discrete increments are at most 2H-4J and 4H-4I). Thus its maximum is at I=J=H+m, namely
    D <= f_m(H)=2H^2+(7-2m)H-4m^2-4m.
Since k<=2m-3, we have 1<=H<=2m-2. The function f_m is convex, so its maximum on this interval is attained at an endpoint:
    f_m(1)=9-6m-4m^2<0,
    f_m(2m-2)=-2m-6<0.
Consequently D<0 throughout. For m=2,k<=1 this gives the original H=1 bound -19 and H=2 bound -10.

## Return to P
Every real external-word fiber has signed count <=0. Moreover b is minimal in the external induced poset, so a real external word beginning with b exists and its signed count is strictly negative. Hence
    Pr(c1<d | v<c1)<1/2.
On c1<v, the relation v<d forces c1<d. Total probability gives
    p_d<q0+(1-q0)/2=(1+q0)/2.
All counts and probabilities refer to the unmodified original P. No added-edge measure is substituted.

## Targeted nonredundancy witness (two implementations; second audit in progress)
Witness E16 (the original temporary input path is omitted; generating relations are also preserved in examples.json). Vertices are
    v,b,d,e,c1,c2,s,r,t,u,w,f0,f1,f2,f3.
Here h=w; R={r,t,u}; F={f0,f1,f2,f3}; anchors r<t.
Generated relations (take transitive closure):
    v<b,d,s; c1<c2,s,r,w; c2<f0,f1,f3;
    b<t,s; d<e,w; e<r; s<f1,f2;
    r<t,u; t<f0,f1,f3; u<f2; w<f1,f3;
    f0<f2; f3<f1.
(The redundancies in the listed generating relations are harmless.)
Exact DP results:
    N=136953, R0=38912, K=#(c1<d)=81688, E_A=2110,
    2K-N-R0=-12489.
Independent audit additionally obtains G=14599 and B=8147>Z=4283. Full structural checks report Delta=9; no primal/dual very-good pair; mixed directed graph acyclic; no proper nontrivial autonomous module. These are finite witness checks, not the proof of the lemma. Historical/literature priority remains unchecked. Here L={s,t}, M=empty, so partial matching has r=2 and q0 is in its unresolved window (5/18,1/3). The old unsigned-error budget DOES hold numerically: E_A=2110 < N/3-R0=6739. Thus this is a new enumeration-free structural sufficient domain beyond the checked VG/mixed/module/full-jump/partial-matching/zero-defect filters, not a witness that every prior numerical-error criterion fails. The original temporary audit script and full receipt are not included. The separately reconstructed checks in verify_e16_structure.py and E16_STRUCTURE_VALIDATION.json verify the corresponding instance without purporting to recover that original receipt.


## Boundary of this uniform fiber estimate
For m>=2 the count threshold k<=2m-3 is exact for this worst-fiber argument: at H=2m-1 and I=J=H+m, f_m(H)=4m-5>0. Such an external word can occur with k=2m-2 d-only points first, then the m anchors, and F empty (both x/s deadlines are the final sentinel). This only blocks the claim that every fiber is nonpositive beyond the threshold; it is not a counterexample to the global inequality or to the balanced-pair conjecture.


### T13 的下门假设不可省：E17
10 点，A={s,h,r,t}，F=∅，生成关系 v<b,d,s；c1<c2,s,h；d<e,h；b<h；h<r；e<r；r<t（取闭包）。
它满足 m=2,k=1 的上锚条件，却有 b∥s，不满足 T13 的 b<s。
N=1015，R0=315，K=679，q0=9/29<1/3，p_d=97/145>2/3，因此 **固定菜单两对都不平衡**。
这是下门假设不可删除的反例，比仅使原上界失效更强。但 |A|=4、Δ8，且含 very-good/模块结构；不属于原 |A|=5 筛后残余，不是一般猜想反例。

## 方法边界另见主账本
自由门b∥s版本的充分域k0,m≥2或k≥1,m≥k+3，以及m=k+2的正纤维障碍，已归档于THEOREMS.md。前者不是A5新覆盖，后者仅限制逐纤维非正证明，不能升级成全局必要性反例。
