#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//대표값
int num[5],total;
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  for(int i=0;i<5;i++) {
    cin >> num[i];
    total+=num[i];
  }
  cout << total/5 <<"\n";
  sort(num,num+5);
  cout << num[2];
  
}
