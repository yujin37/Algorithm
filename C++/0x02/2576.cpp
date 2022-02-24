//홀수
#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int result=0,num,now=100;
  for(int i=0;i<7;i++){
    cin >>num;
    if(num%2!=0){
      if(now>num) now=num;
      result+=num;
    }
  }
  
  
if(result!=0){
  cout << result<<"\n"<< now;
}
else cout << "-1";
  
}
