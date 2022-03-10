#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//애너그램만들기
/*
이 문제를 풀기위해서는 문제를 먼저 이해해야 한다. 여기서 배열을 바꿔서 같은지 확인하기는 쉽지 않다.
그래서 방법은 알파벳 배열에 같은 것이 있다면 1씩 더해주어서 확인하는 것이다. 그리고 빼줘서 abs 절대값 문법으로 더해주게 되면 된다.
다른 것이 몇개 있는지 체크를 해주는 것이다.
*/
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  string word1,word2;
  int arr[2][26]={0,},res=0;
  cin>>word1>>word2;
  for(char c:word1)//이렇게 for문을 활용해서
    arr[0][c-'a']++;//arr에 숫자에 대응하게 해주고
  for(char c:word2)//여기도 마찬가지
    arr[1][c-'a']++;
  for(int i=0;i<26;i++){
    res+=abs(arr[0][i]-arr[1][i]);//abs는 절대값이고 값이 있다면 빼주게 되므로 다른 것의 개수를 셀수 있다.
  }
  cout<<res;//그리고 출력
}
