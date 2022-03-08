#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//개수세기

int main(void){
  int n,num[101]={},v,count=0;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>n;
  for(int i=0;i<n;i++) cin>>num[i];
  cin>>v;
  for(int i=0;i<n;i++){
    if(num[i]==v) count+=1;
  }
  cout<<count;
}
