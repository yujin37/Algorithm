//silver 4, greedy algorithm
//why use long long type in total and now? because if we sum length*liter, int's range is over. so we need to use long long type
#include <stdio.h>

int main(void){
    int N;
    long long total=0;
    scanf("%d", &N);//도시의 개수
    int length[N+1];
    int liter[N+1];
    long now;
    for(int i=1;i<N;i++){
        scanf("%d",&length[i]);
    }
    for(int i=0;i<N;i++){
        scanf("%d", &liter[i]);
    }
    now=liter[0];
    total+=(now*length[1]);

    //printf("%d", total);
    for(int i=1;i<N-1;i++){
        if(now<liter[i]){
            total+=(now*length[i+1]);
        }
        else{
            now=liter[i];
            total+=(now*length[i+1]);
        }
    }
    printf("%lld", total);
    return 0;
}
