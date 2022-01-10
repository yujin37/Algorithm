//N%H==0일때의 처리가 매우 중요
#include <stdio.h>
int main(void){
    int T,H,W,N;
    int room;
    scanf("%d", &T);//테스트데이터개수
    for(int i=0;i<T;i++){
        room=0;
        scanf("%d %d %d", &H, &W, &N);
        if(N%H==0){
            room+=(H*100+(N/H));
        }
        else{
            room+=((N%H)*100+(N/H+1));
        }
        printf("%d\n", room);
    }
    return 0;
}
