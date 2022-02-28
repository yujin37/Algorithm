#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//카드역배치
int num[21];
void reverse(int n1,int n2){
  for(int i=0;i<=(n2-n1-1)/2;i++){
    swap(num[n1+i],num[n2-i]);
  }
}
int main(void){
  int a,b;
  ios::sync_with_stdio(0);
  cin.tie(0);
  for(int i=1;i<=20;i++) num[i]=i;
  for(int i=1;i<=10;i++){
    cin >>a>>b;
    reverse(a,b);
  }
  for(int i=1;i<=20;i++) cout<<num[i]<<" ";
  
}
