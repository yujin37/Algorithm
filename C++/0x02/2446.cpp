#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//별찍기9

int main(void){
  int a;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>a;
  for(int i=1;i<=a-1;i++){
    for(int k=1;k<i;k++) cout<<" ";
    for(int j=1;j<=(2*(a-i)+1);j++) cout << "*";
    cout << "\n";
  }
  for(int i=a;i>0;i--){
    for(int k=i-1;k>0;k--) cout<<" ";
    for(int j=(2*(a-i)+1);j>0;j--) cout << "*";
    cout <<"\n";
  }
  
}
