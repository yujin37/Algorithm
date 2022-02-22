//시험성적
#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용


int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int a;
  cin >> a;
  if(90<=a && a<=100) cout << 'A';
  else if(80<=a) cout << 'B';
  else if(70<=a) cout << 'C';
  else if(60<=a) cout << 'D';
  else cout <<'F';
}
