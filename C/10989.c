//silver5
//정렬방식이 특이함
#include <stdio.h>
int main(void){
    int N;
    scanf("%d", &N);
    int num[10001]={0,};
    int number;
    for(int i=0;i<N;i++){
        scanf("%d", &number);//숫자를 입력받고
        num[number]++;//똑같은 숫자가 있으면 몇번 반복할 것인지
    }
    for(int i=1;i<=10000;i++){//이것은 제한 걸려있는 전체 수
        for(int j=0;j<num[i];j++){//몇번 반복할 것인지
            printf("%d\n",i);//그 숫자를 계속 출력
        }
    }
    return 0;
}
