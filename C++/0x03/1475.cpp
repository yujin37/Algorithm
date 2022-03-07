#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//방번호

int main(void){
  int a,num[10]={0,},ans=1;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>a;
  while(a){
    num[a%10]++;
    a/=10;
  }
  for(int i=0;i<10;i++){
    if(i==6 || i==9) continue;
    ans=max(ans,num[i]);//1,4
  }//ans=4
  ans=max(ans,(num[6]+num[9]+1)/2);//4,2
  cout<<ans;
  
}
