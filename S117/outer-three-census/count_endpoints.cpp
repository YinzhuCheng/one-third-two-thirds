#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <vector>
#include <chrono>
using cpp_int = mpz_class;
int main(int argc,char**argv){
 if(argc!=3){std::cerr<<"usage: count_endpoints INPUT OUTPUT\n";return 2;}
 std::vector<std::vector<cpp_int>> C(349,std::vector<cpp_int>(349));
 for(int n=0;n<=348;++n){C[n][0]=1;C[n][n]=1;for(int k=1;k<n;++k)C[n][k]=C[n-1][k-1]+C[n-1][k];}
 std::ifstream in(argv[1]);std::ofstream out(argv[2]);
 if(!in||!out)return 3;
 int u,a,b,c,t,d,v;long count=0;auto start=std::chrono::steady_clock::now();
 while(in>>u>>a>>b>>c>>t>>d>>v){
  if(u+a+b+c+t+d+v>348||std::min({u,a,b,c,t,d,v})<1){std::cerr<<"bad input\n";return 4;}
  cpp_int z=0,n10=0,n65=0,n02=0,n24=0;
  for(int i=0;i<=u;++i)for(int j=0;j<=t;++j){
   const auto &tail=C[u-i+c+t-j][t-j];
   cpp_int common=tail*C[u-i+c+t-j+d+v][v];
   cpp_int left=C[b+j-1][j]*C[a+b+i+j-1][i];
   cpp_int term=left*common;
   z+=term;
   n10+=C[b+j-1][j]*C[a+b+i+j-2][i]*common;
   n65+=left*tail*C[u-i+c+t-j+d+v-1][v];
   if(i==u)n02+=term;
   if(j==0)n24+=C[a+b+i+j-1][i]*common;
   else if(b>=2)n24+=C[b+j-2][j]*C[a+b+i+j-1][i]*common;
  }
  out<<u<<' '<<a<<' '<<b<<' '<<c<<' '<<t<<' '<<d<<' '<<v<<' '<<z<<' '<<n10<<' '<<n65<<' '<<n02<<' '<<n24<<'\n';
  ++count;if(count%2000==0)std::cerr<<count<<" elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<'\n';
 }
 std::cerr<<"COMPLETE "<<count<<" elapsed "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<'\n';
 return 0;
}
