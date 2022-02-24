#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//윷놀이
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  string play="DCBAE";
  int result, input;
  for(int i=0;i<3;i++){
    result=0;
    for(int j=0;j<4;j++){
      cin >> input;
      result+=input;
    }
    cout << play[result]<<'\n';
  }
}
