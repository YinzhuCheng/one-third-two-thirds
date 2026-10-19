#include <algorithm>
#include <array>
#include <chrono>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <string>
#include <tuple>
#include <vector>
#include <gmpxx.h>
using namespace std;
using Big=mpz_class;
struct Cross { int a,p,b,q; };
struct Pair {int a,b; string cls;};
static bool leq(const array<int,3>&a,const array<int,3>&b,int k){for(int c=0;c<k;c++)if(a[c]>b[c])return false;return true;}
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage stress input.txt output.jsonl\n";return 1;}
 ifstream in(argv[1]);ofstream out(argv[2]);
 mt19937_64 rng(2026101802ULL); auto start=chrono::steady_clock::now();
 long long budget=30000000,used=0,totalpairs=0;int nc;in>>nc;
 for(int ci=0;ci<nc;ci++){
  string name;int k;array<int,3>L{0,0,0};int m,q;in>>name>>k;for(int c=0;c<k;c++)in>>L[c];in>>m;
  vector<Cross>cross(m);for(auto&e:cross)in>>e.a>>e.p>>e.b>>e.q;
  in>>q;vector<array<int,3>>filters(q);for(auto&t:filters){t={0,0,0};for(int c=0;c<k;c++)in>>t[c];}
  array<int,3>stride{1,1,1};for(int c=1;c<3;c++)stride[c]=stride[c-1]*(L[c-1]+1);
  int grid=(L[0]+1)*(L[1]+1)*(L[2]+1);vector<int>index(grid,-1);vector<array<int,3>>states;states.reserve(grid);
  for(int id=0;id<grid;id++){
   array<int,3>x{0,0,0};for(int c=0;c<k;c++)x[c]=(id/stride[c])%(L[c]+1);
   bool ok=true;for(auto&e:cross)if(x[e.b]>e.q && x[e.a]<=e.p){ok=false;break;}
   if(ok){index[id]=states.size();states.push_back(x);}
  }
  int ns=states.size();vector<array<int,3>>next(ns);long long ne=0;
  for(int i=0;i<ns;i++){
   auto x=states[i];int id=0;for(int c=0;c<k;c++)id+=x[c]*stride[c];next[i]={-1,-1,-1};
   for(int c=0;c<k;c++)if(x[c]<L[c] && index[id+stride[c]]>=0){next[i][c]=index[id+stride[c]];ne++;}
  }
  vector<Big>F(ns),G(ns);F[0]=1;
  for(int i=0;i<ns;i++)for(int c=0;c<k;c++)if(next[i][c]>=0)F[next[i][c]]+=F[i];
  G[ns-1]=1;for(int i=ns-2;i>=0;i--)for(int c=0;c<k;c++)if(next[i][c]>=0)G[i]+=G[next[i][c]];
  Big K=F.back();if(K!=G[0]||K==0){cerr<<"DAG count error\n";return 3;}
  vector<Big>means(q);for(int i=1;i<ns;i++){Big w=F[i]*G[i];for(int j=0;j<q;j++)if(leq(states[i],filters[j],k))means[j]+=w;}
  vector<Pair>pairs;for(int a=0;a<q;a++)for(int b=a;b<q;b++){
   string cl;bool empty=filters[a]==L||filters[b]==L;
   bool full=accumulate(filters[a].begin(),filters[a].end(),0)==0||accumulate(filters[b].begin(),filters[b].end(),0)==0;
   bool nested=leq(filters[a],filters[b],k)||leq(filters[b],filters[a],k);
   bool disjoint=true;for(int c=0;c<k;c++)if(max(filters[a][c],filters[b][c])<L[c])disjoint=false;
   cl=empty?"empty_filter":full?"zero_mean":a==b?"same":nested?"nested":disjoint?"disjoint":"overlap_nonnested";
   pairs.push_back({a,b,cl});
  }
  int cap=ns<=1000?240:ns<=15000?160:ns<=100000?64:16;
  cap=min(cap,(int)pairs.size());vector<int>chosen;set<int>seen;
  auto add=[&](int i){if((int)chosen.size()<cap && seen.insert(i).second)chosen.push_back(i);};
  auto good=[&](const Pair&p){return means[p.a]>0&&means[p.b]>0&&p.cls!="empty_filter";};
  auto ratio_less=[&](int x,int y){auto&p=pairs[x];auto&t=pairs[y];Big pa=min(means[p.a],means[p.b]),pb=max(means[p.a],means[p.b]);Big ta=min(means[t.a],means[t.b]),tb=max(means[t.a],means[t.b]);Big left=pb*ta,right=tb*pa;return left!=right?left>right:x<y;};
  vector<int>rank;for(int i=0;i<(int)pairs.size();i++)if(good(pairs[i])&&pairs[i].a!=pairs[i].b)rank.push_back(i);
  sort(rank.begin(),rank.end(),ratio_less);
  // Exact-mean asymmetry gets the largest single quota, with no empty filter.
  for(int i:rank){if((int)chosen.size()>=max(1,cap/3))break;add(i);}
  for(string cl:{"nested","overlap_nonnested","disjoint"}){
   int quota=max(1,cap/10),added=0;
   // Mix the highest ratios with nearby, small-positive-mean filters.
   for(int i:rank)if(pairs[i].cls==cl && !seen.count(i)){add(i);if(++added>=quota/2)break;}
   vector<int>small;for(int i:rank)if(pairs[i].cls==cl)small.push_back(i);
   sort(small.begin(),small.end(),[&](int x,int y){auto&p=pairs[x];auto&t=pairs[y];Big pa=min(means[p.a],means[p.b]),ta=min(means[t.a],means[t.b]);if(pa!=ta)return pa<ta;int d1=0,d2=0;for(int c=0;c<k;c++){d1+=abs(filters[p.a][c]-filters[p.b][c]);d2+=abs(filters[t.a][c]-filters[t.b][c]);}return d1!=d2?d1<d2:x<y;});
   for(int i:small)if(!seen.count(i)){add(i);if(++added>=quota)break;}
  }
  vector<int>diags;for(int i=0;i<(int)pairs.size();i++)if(pairs[i].a==pairs[i].b&&good(pairs[i]))diags.push_back(i);
  sort(diags.begin(),diags.end(),[&](int x,int y){return means[pairs[x].a]<means[pairs[y].a];});
  int dc=0;for(int i:diags){add(i);if(++dc>=max(2,cap/12))break;}
  // Two explicit degeneracy controls, then fixed-seed residual pair sampling.
  for(string cl:{"empty_filter","zero_mean"})for(int i=0;i<(int)pairs.size();i++)if(pairs[i].cls==cl){add(i);break;}
  vector<int>rest(pairs.size());iota(rest.begin(),rest.end(),0);shuffle(rest.begin(),rest.end(),rng);for(int i:rest)add(i);
  out<<"{\"type\":\"case\",\"name\":\""<<name<<"\",\"n\":"<<accumulate(L.begin(),L.end(),0)<<",\"states\":"<<ns<<",\"edges\":"<<ne<<",\"le\":\""<<K<<"\",\"filter_count\":"<<q<<",\"planned_pairs\":"<<chosen.size()<<",\"filters\":[";
  for(int i=0;i<q;i++){if(i)out<<",";out<<"{\"threshold\":[";for(int c=0;c<k;c++){if(c)out<<",";out<<filters[i][c];}out<<"],\"sum_R\":\""<<means[i]<<"\"}";}out<<"]}\n";out.flush();
  int completed=0;vector<Big>Y(ns),Z(ns),P(ns),M(ns),YY(ns),ZZ(ns);
  for(int pi:chosen){
   if(used+ns>budget || chrono::duration<double>(chrono::steady_clock::now()-start).count()>720){out<<"{\"type\":\"stop\",\"reason\":\"budget\",\"state_pair_passes\":"<<used<<",\"pairs\":"<<totalpairs<<"}\n";out.flush();return 0;}
   fill(Y.begin(),Y.end(),0);fill(Z.begin(),Z.end(),0);fill(P.begin(),P.end(),0);fill(M.begin(),M.end(),0);fill(YY.begin(),YY.end(),0);fill(ZZ.begin(),ZZ.end(),0);
   auto&p=pairs[pi];auto&sy=filters[p.a];auto&sz=filters[p.b];
   for(int i=0;i<ns;i++)for(int c=0;c<k;c++)if(next[i][c]>=0){int j=next[i][c];bool a=leq(states[j],sy,k),b=leq(states[j],sz,k);
    Y[j]+=Y[i];Z[j]+=Z[i];P[j]+=P[i];M[j]+=M[i];YY[j]+=YY[i];ZZ[j]+=ZZ[i];
    if(a){Y[j]+=F[i];P[j]+=Z[i];YY[j]+=(Y[i]<<1)+F[i];}
    if(b){Z[j]+=F[i];P[j]+=Y[i];ZZ[j]+=(Z[i]<<1)+F[i];}
    if(a&&b){P[j]+=F[i];M[j]+=F[i];}
   }
   Big A=Y.back(),B=Z.back(),C=P.back(),D=M.back(),lo=min(A,B);
   if(A!=means[p.a]||B!=means[p.b]){cerr<<"mean mismatch\n";return 4;}
   Big tn=A*B+lo*lo+2*lo*K-(C+D)*K,cn=A*B+lo*lo+lo*K-C*K;
   out<<"{\"type\":\"pair\",\"case\":\""<<name<<"\",\"i\":"<<p.a<<",\"j\":"<<p.b<<",\"class\":\""<<p.cls<<"\",\"sum_Ry\":\""<<A<<"\",\"sum_Rz\":\""<<B<<"\",\"sum_product\":\""<<C<<"\",\"sum_min\":\""<<D<<"\",\"sum_Ry2\":\""<<YY.back()<<"\",\"sum_Rz2\":\""<<ZZ.back()<<"\",\"target_gap_num\":\""<<tn<<"\",\"covariance_gap_num\":\""<<cn<<"\"}\n";
   used+=ns;totalpairs++;completed++;
   if(tn<0||cn<0){out<<"{\"type\":\"stop\",\"reason\":\"counterexample\",\"state_pair_passes\":"<<used<<",\"pairs\":"<<totalpairs<<"}\n";out.flush();return 2;}
  }
  out.flush();double secs=chrono::duration<double>(chrono::steady_clock::now()-start).count();cerr<<name<<" states="<<ns<<" pairs="<<completed<<" cumulative="<<totalpairs<<" passes="<<used<<" seconds="<<secs<<"\n";
 }
 out<<"{\"type\":\"stop\",\"reason\":\"fixed_batch_complete\",\"state_pair_passes\":"<<used<<",\"pairs\":"<<totalpairs<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
}
