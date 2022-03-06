#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//최대값

int main(void){
  int num[9],max=0,record;
  ios::sync_with_stdio(0);
  cin.tie(0);
  for(int i=0;i<9;i++) {
    cin>>num[i];
    if(max<num[i]){
      max=num[i];
      record=(i+1);
    }
  }
  cout<<max<<"\n"<<record;
  
}
