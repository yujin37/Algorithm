//bronze2/ 다시 풀기
#include <stdio.h>
int main(void){
    int N;
    int i=2,j=5;
    int count=2;
    scanf("%d", &N);
    if(N==1){
        printf("1");
        return 0;
    }
    while(1){
        if(i<=N&&i+j>=N){
            printf("%d",count);
            break;
        }
        i=i+j+1;
        j+=6;
        count++;
    }
    return 0;
}
