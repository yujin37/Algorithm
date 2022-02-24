#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//주사위3개
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int a,b,c;
  cin>>a>>b>>c;
  if(a==b&&b==c) cout<<10000+a*1000;
  else if(a==b || a==c) cout<<1000+a*100;
  else if(b==c) cout<<1000+b*100;
  else{
    cout<< max({a,b,c})*100;
  }

}
