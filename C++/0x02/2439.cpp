#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//별찍기2

int main(void){
  int a;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>a;
  for(int i=1;i<=a;i++){
    for(int j=a-1;j>=i;j--) cout<<" ";
    for(int k=1;k<=i;k++) cout<<"*";
    cout<<"\n";
  }
}
