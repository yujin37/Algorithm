//bronze1/다시 풀기
#include <stdio.h>
int main(void){
    int X, count=0;
    int num1=0, num2=1, flag=-1;//flag는 홀짝 현재는 짝수
    scanf("%d", &X); //입력받고
    while(num1<X){//만약 num1이 x보다 작다면
        num1+=num2;//num2만큼 더해준다.
        num2+=1;//이렇게 해줘야 가능
        flag*=-1;//홀짝을 변환
    }
    num1=num1-(num2-1);//이건 잘 모르겠음
    if(flag>0){//홀수라면
        printf("%d/%d\n", num2+num1-X, X-num1);//num1+num2해서 입력만큼 빼준다. 이건 바뀌는 순간 자리를 봐주는 것으로 추정. 
    }
    else{
        printf("%d/%d\n", X-num1, num2+num1-X);//마찬가지. 꺾이는 부분을 x만큼 빼줌으로서 계산
    }
    return 0;
}
