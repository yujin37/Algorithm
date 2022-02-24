#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용

//윤년 4의 배수, 100의 배수가 아닐때, 400의 배수일때
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int year;
  cin>>year;
  if(year%4==0){
    if(year%400==0) cout<<1;
    else if(year%100==0) cout<<0;
    else cout << 1;
  }
  else{
      cout <<0;
  }


}
