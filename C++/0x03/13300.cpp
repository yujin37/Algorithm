#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//방배정

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n,k,room=0;
  int std[2][7]={0,};//이거 안하면 오류 발생할 수 있으므로 만들어줌.
  cin>>n>>k;
  for(int i=0;i<n;i++){
    int s,y;//매번 갱신이 필요
    cin>>s>>y;
    std[s][y]++;
    //cout<<std[s][y]<<"\n";    
  }
  //cout<<room<<"\n";
  for(int i=0;i<2;++i){
    for(int j=1;j<=6;++j){
      room+=(std[i][j]/k);//일단 나누어서 그 값을 넣어주는데
      if(std[i][j]%k>0) room+=1;//만약 나머지가 있다면 room에 +1을 해주는 형태로 해준다.
      //cout<<room<<"\n";
    }
    
  }
  cout<<room<<"\n";
}
