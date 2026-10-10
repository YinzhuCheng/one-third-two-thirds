// Independent finite-domain reconstruction. No author code or output is read.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <gmpxx.h>
#include <algorithm>
#include <stdexcept>
int cap(int a) { static int x[]={0,3,9,29}; return x[a]; }
int64_t product(int start,int length) {int64_t ans=1; while(length--)ans*=start++; return ans;}
void need(bool ok,const char *s){if(!ok)throw std::runtime_error(s);}
int main(int argc,char**argv){
 if(argc!=4)return 2;
 std::ofstream survivors(argv[1]), intervals(argv[2]),summary(argv[3]);
 need(bool(survivors)&&bool(intervals)&&bool(summary),"open outputs");
 std::vector<std::vector<mpz_class>> C(349,std::vector<mpz_class>(30));
 C[0][0]=1;for(int n=1;n<=348;n++){C[n][0]=1;for(int k=1;k<=std::min(29,n);k++)C[n][k]=C[n-1][k-1]+C[n-1][k];}
 summary<<"a d rectangle product_pairs nonempty_intervals candidates rank_left rank_right lower_left lower_right max_order eq_rank_left eq_rank_right eq_lower_left eq_lower_right\n";
 intervals<<"u a b c d v candidate_first candidate_last rank_left_first rank_both_first lower_left_first all_first\n";
 for(int a=1;a<=3;a++)for(int d=1;d<=3;d++){
  if(a<3&&d<3)continue;
  long long pairs=0, nonempty=0, counts[5]={}, equality[4]={}; int maxn=0;
  for(int u=2;u<=cap(a);u++)for(int v=2;v<=cap(d);v++)for(int b=1;b<=90;b++)for(int c=1;c<=90;c++){
   if(3*product(b,a+1)>=product(b+u,a+1)||3*product(c,d+1)>=product(c+v,d+1))continue;
   pairs++;
   int first[5]={105,105,105,105,105},last[5]={};
   for(int t=1;t<=104;t++){
    if(2*u>=a+b+t+v||2*v>=u+c+t+d||2*t>=b+c+u||2*t>=b+c+v)continue;
    counts[0]++;first[0]=std::min(first[0],t);last[0]=t;maxn=std::max(maxn,u+a+b+c+t+d+v);
    int64_t left3=3*product(b+t+v+1,a),left2=2*product(b+t+v+u+1,a);
    int64_t right3=3*product(c+t+u+1,d),right2=2*product(c+t+u+v+1,d);
    equality[0]+=left3==left2;equality[1]+=right3==right2;
    if(left3<=left2)continue;
    counts[1]++;first[1]=std::min(first[1],t);last[1]=t;
    if(right3<=right2)continue;
    counts[2]++;first[2]=std::min(first[2],t);last[2]=t;
    const auto &den1=C[u+a+b+t+v][u],&den2=C[v+d+c+t+u][v];
    mpz_class num1=3*C[u+a+b-1][u],num2=3*C[v+d+c-1][v];
    equality[2]+=num1==den1;equality[3]+=num2==den2;
    if(num1>=den1)continue;
    counts[3]++;first[3]=std::min(first[3],t);last[3]=t;
    if(num2>=den2)continue;
    counts[4]++;first[4]=std::min(first[4],t);last[4]=t;
    survivors<<u<<' '<<a<<' '<<b<<' '<<c<<' '<<t<<' '<<d<<' '<<v<<'\n';
   }
   if(first[0]==105)continue;
   nonempty++;
   int lo=std::max({1,2*u-a-b-v+1,2*v-u-c-d+1}),hi=(b+c+std::min(u,v)-1)/2;
   need(first[0]==lo&&last[0]==hi,"candidate interval endpoints");
   for(int j=1;j<5;j++)if(first[j]!=105)need(last[j]==hi,"filter suffix interval");
   intervals<<u<<' '<<a<<' '<<b<<' '<<c<<' '<<d<<' '<<v<<' '<<lo<<' '<<hi;
   for(int j=1;j<5;j++)intervals<<' '<<first[j];intervals<<'\n';
  }
  summary<<a<<' '<<d<<' '<<static_cast<long long>(cap(a)-1)*(cap(d)-1)*90*90*104<<' '<<pairs<<' '<<nonempty;
  for(auto n:counts)summary<<' '<<n;summary<<' '<<maxn;for(auto n:equality)summary<<' '<<n;summary<<'\n';
  std::cerr<<a<<','<<d<<" candidates="<<counts[0]<<" survivors="<<counts[4]<<'\n';
 }
}
