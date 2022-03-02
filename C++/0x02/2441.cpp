#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//별찍기4

int main(void){
  int a;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>a;
  for(int i=0;i<a;i++){
    for(int j=0;j<i;j++) cout<<" ";
    for(int k=a-i;k>0;k--) cout<<"*";
    cout<<"\n";
  }
}
