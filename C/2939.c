//bronze1
#include <stdio.h>
int main(void){
    int N;
    int bag=0;
    scanf("%d", &N);
    while(N>=0){
        if(N%5==0){
            bag+=(N/5);
            break;
        }
        N-=3;
        bag++;
    }
    if(N<0){
        bag=-1;
    }
    printf("%d",bag);
    return 0;
}
