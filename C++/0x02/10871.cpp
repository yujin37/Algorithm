#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용

int n,x,a[10005];
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>n>>x;
  for(int i=0;i<n;i++) cin>>a[i];
  for(int i=0;i<n;i++){
    if(a[i]<x)cout<<a[i]<< ' ';
  }
}
