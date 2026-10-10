#include <gmpxx.h>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
using Z=mpz_class;
int main(int argc,char**argv){
 if(argc!=3){std::cerr<<"usage: count_exact INTERVALS COUNTS\n";return 2;}
 const int cap=1665;
 std::vector<std::vector<Z>> C(cap+1);
 for(int n=0;n<=cap;++n){C[n].resize(n+1);C[n][0]=C[n][n]=1;for(int k=1;k<n;++k)C[n][k]=C[n-1][k-1]+C[n-1][k];}
 std::ifstream in(argv[1]);std::ofstream out(argv[2]);if(!in||!out)return 3;
 int u,a,b,c,d,v,low,high;long count=0,passed=0;int maxn=0;
 while(in>>u>>a>>b>>c>>d>>v>>low>>high){
  if(u+a+b+c+high+d+v>cap||std::min({u,a,b,c,low,d,v})<1)return 4;
  for(int t=low;t<=high;++t){
   Z z=0,n02=0;
   for(int i=0;i<=u;++i)for(int j=0;j<=t;++j){
    Z term=C[b+j-1][j]*C[a+b+i+j-1][i]*C[u-i+c+t-j][t-j]*C[u-i+c+t-j+d+v][v];
    z+=term;if(i==u)n02+=term;
   }
   out<<u<<' '<<a<<' '<<b<<' '<<c<<' '<<t<<' '<<d<<' '<<v<<' '<<z<<' '<<n02<<'\n';
   ++count;if(3*n02<z)++passed;maxn=std::max(maxn,u+a+b+c+t+d+v);
  }
 }
 std::cout<<"vectors "<<count<<" survivors "<<passed<<" maxn "<<maxn<<'\n';
 return 0;
}
