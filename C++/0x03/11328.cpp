//이 문제는 특이한 문법이라 보고 작성
#include <bits/stdc++.h>//자주 사용 라이브러리 전부 컴파일
using namespace std;//std 네임 스페이스를 사용
//strfry

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin>>n;
  while(n--){
    int a[26]={0,};
    string s1, s2;
    cin>>s1>>s2;

    for(auto c:s1) a[c-'a']++;//s1의 문자를 차례대로 a만큼 값을 빼서 더해주게 된다.
    for(auto c:s2) a[c-'a']--;//그리고 s2에서는 반대로 빼준다.
    //만약 모두 같다면 다시 0이 될 것이고 같지 않다면 0아닌 양수가 나올 것이다.
    bool isPossible=true;//true, false를 보여주기 위해 bool 변수를 활용하고
    for(int i:a){//a배열에 담겨있는 값을 i에 넣어서
      if(i!=0) isPossible=false;//0이 아닌 경우에는 ispossible이 불가능이 될 것이다. 같지 않은 것이 있으므로
    }

    if(isPossible) cout << "Possible\n";//그렇다면 이렇게 각각 출력이 가능하다.
    else cout <<"Impossible\n";
  }
}
