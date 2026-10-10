// Independent word-recurrence oracle. No binomial formula or author code.
#include <gmpxx.h>
#include <array>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
using Z=mpz_class;
struct Row {int u,a,b,c,t,d,v;Z expected_z,expected_n,z,n;};
int main(int argc,char**argv){
 if(argc!=3) throw std::runtime_error("usage: recurrence source_counts output_counts");
 std::ifstream input(argv[1]);if(!input)throw std::runtime_error("input missing");
 std::vector<Row> rows; Row r;
 while(input>>r.u>>r.a>>r.b>>r.c>>r.t>>r.d>>r.v>>r.expected_z>>r.expected_n) rows.push_back(r);
 if(!input.eof()||rows.empty())throw std::runtime_error("malformed counts");
 for(int d=4;d<=6;++d){
  int P=0,Q=0,R=0;
  for(auto &x:rows)if(x.d==d){P=std::max(P,x.u+x.c);Q=std::max(Q,x.t);R=std::max(R,x.v);}
  if(P==0)continue;
  auto at=[&](int p,int q,int r)->size_t{return ((size_t)p*(Q+1)+q)*(R+1)+r;};
  std::vector<Z> tail((size_t)(P+1)*(Q+1)*(R+1));
  // Boundary: number of shuffles of independent chains d and r, by Pascal.
  std::vector<Z> boundary(R+1,1);
  for(int k=1;k<=d;++k)for(int rr=1;rr<=R;++rr)boundary[rr]+=boundary[rr-1];
  for(int p=0;p<=P;++p)for(int q=0;q<=Q;++q)for(int rr=0;rr<=R;++rr){
   Z &z=tail[at(p,q,rr)];
   if(p==0&&q==0){z=boundary[rr];continue;}
   if(p)z+=tail[at(p-1,q,rr)];
   if(q)z+=tail[at(p,q-1,rr)];
   if(rr)z+=tail[at(p,q,rr-1)];
  }
  for(int a=2;a<=4;++a){
   int I=0,J=0,K=0;
   for(auto &x:rows)if(x.d==d&&x.a==a){I=std::max(I,x.u);J=std::max(J,x.t);K=std::max(K,x.b-1);}
   if(I==0)continue;
   auto pos=[&](int i,int j)->size_t{return (size_t)i*(J+1)+j;};
   std::vector<Z> previous((I+1)*(J+1)),current(previous.size()),base(I+1,1);
   for(int k=1;k<=a;++k)for(int i=1;i<=I;++i)base[i]+=base[i-1];
   for(int k=0;k<=K;++k){
    std::fill(current.begin(),current.end(),Z(0));
    for(int i=0;i<=I;++i)for(int j=0;j<=J;++j){
     Z &z=current[pos(i,j)];
     if(k==0&&j==0){z=base[i];continue;}
     if(i)z+=current[pos(i-1,j)];
     if(j)z+=current[pos(i,j-1)];
     if(k)z+=previous[pos(i,j)];
    }
    for(auto &x:rows)if(x.d==d&&x.a==a&&x.b-1==k){
     x.z=0;x.n=0;
     for(int j=x.t;j>=0;--j)for(int i=x.u;i>=0;--i){
      Z contribution=current[pos(i,j)]*tail[at(x.u-i+x.c,x.t-j,x.v)];
      x.z+=contribution;if(i==x.u)x.n+=contribution;
     }
     if(x.z!=x.expected_z||x.n!=x.expected_n)throw std::runtime_error("author count mismatch");
     if(3*x.n<x.z)throw std::runtime_error("unexcluded vector");
    }
    previous.swap(current);
   }
  }
  std::cout<<"recurrence d="<<d<<" done; tail states="<<tail.size()<<std::endl;
 }
 std::ofstream output(argv[2]);if(!output)throw std::runtime_error("output missing");
 int stronger=0;for(auto &x:rows){
  if(x.z==0)throw std::runtime_error("unprocessed vector");
  if(2*x.n>x.z)++stronger;
  output<<x.u<<' '<<x.a<<' '<<x.b<<' '<<x.c<<' '<<x.t<<' '<<x.d<<' '<<x.v<<' '<<x.z<<' '<<x.n<<'\n';
 }
 std::cout<<"all "<<rows.size()<<" exact denominator/numerator pairs match; "<<stronger<<" strictly above 1/2"<<std::endl;
}
