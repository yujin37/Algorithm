/*
이 문제는 단순하게 풀면 안됨
이중 for문으로 풀게 되면 시간 초과가 되게 됨. 너무 많이 돌아야해서.
그러므로 일반 for문에서 x에서 num[i]를 빼주고 그것이 true일때만 count가 가능
*/
#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//두수의 합
int n,num[100001]={};
bool occur[2000001];
int x;
int main(void){
  int count=0;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin>>n;
  for(int i=0;i<n;i++) cin>>num[i];
  cin>>x;
  for(int i=0;i<n;i++){
    if(x-num[i]>0 && occur[x-num[i]]) count++;
    occur[num[i]]=true;
  }
  cout<<count;
}
