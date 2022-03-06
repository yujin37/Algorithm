#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//숫자의개수

int main(void){
  int a,b,c;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>a>>b>>c;
  int multi=a*b*c;
  int num[10]={0,};
  while(multi>0){
    num[multi%10]+=1;
    multi/=10;
  }
  for(int i=0;i<10;i++) cout<<num[i]<<"\n";
}
