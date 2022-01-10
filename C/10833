//34점 풀이: 배열을 apple, std에 넣었음. 100점 풀이: 배열을 없애고 변수에 계속 넣어주는 식으로 바꿈. 아래는 100점풀이
#include <stdio.h>

int main(void){
    int N;
    int std,apple,total=0;
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        scanf("%d %d", &std, &apple);
        if(std<apple){
            total+=(apple%std);
        }
        else if(std>apple){
            total+=apple;
        }
    }
    printf("%d",total);
    return 0;
}
