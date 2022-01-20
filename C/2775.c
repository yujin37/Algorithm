//bronze1/다시 풀기
#include <stdio.h>
int main(void){
    int T, k, n;
    int arr[15][15]={0,};//층호수이므로 이차원 배열
    scanf("%d", &T);//테스트 갯수
    for(int i=1;i<15;i++){
        arr[0][i]=i;
    }//0층은 미리 만들어줌
    for(int i=1;i<15;i++){
        for(int j=1;j<15;j++){
            arr[i][j]=arr[i-1][j]+arr[i][j-1];
        }
    }
  /*이렇게 해주어야 하는 이유는 아래층을 자기 호수 아래까지 세줄 수 있지만 복잡하기에 자기 앞에 호수까지 더하고
  자기 바로 아래층 호수를 더해주면 되므로 이 방식을 선택하면 편리 */
    for(int i=0;i<T;i++){
        scanf("%d %d", &k, &n);//바로바로 나와야 하므로 층과 호수를 물으면
        printf("%d\n", arr[k][n]);//바로 출력을 시켜준다.
    }
    return 0;
}
