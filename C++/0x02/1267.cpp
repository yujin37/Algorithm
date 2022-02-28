#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//핸드폰 요금

int main(void){
  int N,phone[10000],Y=0,M=0;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  for(int i=0;i<N;i++) cin >> phone[i]; //입력을 받고
  for(int i=0;i<N;i++) Y+=((phone[i]/30)+1)*10;
  for(int i=0;i<N;i++) M+=((phone[i]/60)+1)*15;

  if(Y<M) cout<<"Y "<< Y;
  else if(Y>M) cout<< "M "<<M;
  else if(Y==M) cout<<"Y M "<< Y;
  
}
