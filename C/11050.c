#bronze 1
#include <stdio.h>
int main(void){
    int N, K;
    int result=0;
    int h=1,l=1;
    scanf("%d %d", &N, &K);
    //printf("%d %d\n", N, K);
    for(int i=0;i<N;i++){
        h*=(N-i);
    }
    for(int j=0;j<K;j++){
        l*=(K-j);
    }
    for(int k=0;k<(N-K);k++){
        l*=((N-K)-k);
    }
    result+=(h/l);
    printf("%d", result);
    return 0;
}
