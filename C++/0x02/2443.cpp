#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//별찍기6

int main(void){
  int a;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>a;
  for(int i=a;i>0;i--){
    for(int j=a-i;j>0;j--) cout<<" ";
    for(int k=1;k<=2*i-1;k++) cout<<"*";
    cout<<"\n";
  }
}
