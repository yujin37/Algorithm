//bronze1, while문으로 풀면 time over, 시간 빠르게 하려면 if문처럼 딱 끝나야 함.
#include <stdio.h>
int main(void){
    int A,B,V,i;

    scanf("%d %d %d", &A, &B, &V);
    i=(V-B)/(A-B);//빠르게 하기 위해 이방식 선택. 이미 미끄러졌을 수도 있기 때문에 이를 빼주는 것을 v에 반영. A-B는 하루에 나아갈 수 있는 움직임
    if((V-B)%(A-B)!=0){//이것은 예외사항. 나누어떨어지지 않으면 다음날에 한번더 이동해야 하는 것을 고려해줌.
        i+=1;
    }
    printf("%d", i);
    return 0;
}
