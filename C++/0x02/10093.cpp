#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//숫자

int main(void){
  long long n1,n2;
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n1 >> n2;
  if(n1>n2) swap(n1,n2);
  if(n1==n2||n2-n1==1) cout << 0;
  else{
    cout << n2-n1-1<<"\n";
    for(long long i=n1+1;i<n2;i++){
        cout << i << " ";
    }
  }
}
