#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//일곱난쟁이
int num[9],result[7];
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  for(int i=0;i<9;i++) {
    cin >> num[i];
  }//입력 받아 저장완료
  for(int i=0;i<8;i++){
    int total=0;
    for(int j=i+1;j<9;j++){
      total=0;
      for(int k=0,l=0;k<9;k++){
        if(k!=i && k!=j){
          result[l++]=num[k];
        }
      }
      for(int i=0;i<7;i++) total+=result[i];
      if(total==100) break;
    }
    if(total==100) break;
    //cout << total<<" ";
  }
  
  
  //정렬은 완료
  sort(result,result+7);
  for(int i=0;i<7;i++){
      cout << result[i]<<"\n";
  }
  
}
