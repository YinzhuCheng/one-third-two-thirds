// Independent endpoint counts by two integer word-count recurrences.
// No binomial closed count formula and no author implementation is used.
#include <gmpxx.h>
#include <array>
#include <fstream>
#include <iostream>
#include <vector>
#include <stdexcept>
#include <algorithm>
#include <chrono>
using Z=mpz_class;
constexpr int I=30,K=90,J=105,P=120,V=30;
size_t leftindex(int i,int k,int j){return (i*K+k)*J+j;}
size_t rightindex(int p,int q,int v){return (p*J+q)*V+v;}
void need(bool ok,const char *msg){if(!ok)throw std::runtime_error(msg);}
int main(int argc,char **argv){
 if(argc!=3)return 2;
 std::ifstream input(argv[1]);std::ofstream output(argv[2]);need(bool(input)&&bool(output),"input/output");
 // L_a(i,k,j): i independent C0, a C1 before fork k C2 / j C4.
 // A_a is the same recurrence with first C2 < first C4.
 std::array<std::vector<Z>,4> L,A,F;
 for(int a=1;a<=3;a++){
  L[a].resize(I*K*J);A[a].resize(I*K*J);std::vector<std::vector<Z>> base(a+1,std::vector<Z>(I));
  for(int x=0;x<=a;x++)for(int i=0;i<I;i++)base[x][i]=(x==0||i==0)?Z(1):base[x-1][i]+base[x][i-1];
  for(int i=0;i<I;i++)for(int k=0;k<K;k++)for(int j=0;j<J;j++){
   auto h=leftindex(i,k,j);
   if(k==0&&j==0){L[a][h]=A[a][h]=base[a][i];continue;}
   if(i)L[a][h]+=L[a][leftindex(i-1,k,j)];
   if(k)L[a][h]+=L[a][leftindex(i,k-1,j)];
   if(j)L[a][h]+=L[a][leftindex(i,k,j-1)];
   if(k==0)continue;
   if(i)A[a][h]+=A[a][leftindex(i-1,k,j)];
   A[a][h]+=A[a][leftindex(i,k-1,j)];
   if(j)A[a][h]+=A[a][leftindex(i,k,j-1)];
  }
 }
 // F_d(p,q,v): p chain elements and q chain elements precede d terminal
 // elements; v independent elements. Count by the first letter.
 for(int d=1;d<=3;d++){
  F[d].resize(P*J*V);std::vector<std::vector<Z>> base(d+1,std::vector<Z>(V));
  for(int x=0;x<=d;x++)for(int v=0;v<V;v++)base[x][v]=(x==0||v==0)?Z(1):base[x-1][v]+base[x][v-1];
  for(int p=0;p<P;p++)for(int q=0;q<J;q++)for(int v=0;v<V;v++){
   auto h=rightindex(p,q,v);if(p==0&&q==0){F[d][h]=base[d][v];continue;}
   if(p)F[d][h]+=F[d][rightindex(p-1,q,v)];
   if(q)F[d][h]+=F[d][rightindex(p,q-1,v)];
   if(v)F[d][h]+=F[d][rightindex(p,q,v-1)];
  }
 }
 int u,a,b,c,t,d,v;long count=0;auto start=std::chrono::steady_clock::now();
 while(input>>u>>a>>b>>c>>t>>d>>v){
  need(a>=2&&a<=3&&d>=2&&d<=3&&u<I&&v<V&&b<=K&&c+u<P&&t<J,"survivor limits");
  Z total=0,first1=0,last5=0,top0_before_top2=0,first2_before_first4=0;
  for(int i=0;i<=u;i++)for(int j=0;j<=t;j++){
   auto h=leftindex(i,b-1,j),r=rightindex(u-i+c,t-j,v);
   Z term=L[a][h]*F[d][r];total+=term;
   first1+=L[a-1][h]*F[d][r];last5+=L[a][h]*F[d-1][r];
   if(i==u)top0_before_top2+=term;
   first2_before_first4+=A[a][h]*F[d][r];
  }
  output<<u<<' '<<a<<' '<<b<<' '<<c<<' '<<t<<' '<<d<<' '<<v<<' '<<total<<' '<<first1<<' '<<last5<<' '<<top0_before_top2<<' '<<first2_before_first4<<'\n';
  need(3*top0_before_top2>=total,"unrejected T2<T0");
  if(++count%10000==0)std::cerr<<count<<" elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<'\n';
 }
 std::cerr<<"COMPLETE "<<count<<'\n';
}
