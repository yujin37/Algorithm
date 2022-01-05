#include <stdio.h>
int main(void){
    int N, F,result[3]={0,};
    scanf("%d", &N);
    scanf("%d", &F);
    N-=(N%100);
    for(int i=0;i<100;i++){
        if(N%F==0){
            break;
        }
        N+=1;
    }
    if((N%100)<10){
        result[1]+=(N%100);
    }
    else{
        result[0]+=((N%100)/10);
        result[1]+=((N%100)%10);
    }
    for(int i=0;i<2;i++){
        printf("%d", result[i]);
    }
    return 0;
}
