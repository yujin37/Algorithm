//세수정렬
#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용


int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int a, b, c;
  cin >> a >> b >> c;
  int d, e, f;
  d=min({a,b,c});
  e=max({a,b,c});
  f=a+b+c-d-e;
  cout<< d << ' ' << f << ' ' << e;

}
