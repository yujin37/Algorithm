//휴대폰요금
#include <stdio.h>
int main(void){
    int N,phone[10000],Y=0,M=0;
    scanf("%d", &N);
    for(int i=0;i<N;i++) scanf("%d", &phone[i]);
    for(int i=0;i<N;i++) Y+=((phone[i]/30)+1)*10;
    for(int i=0;i<N;i++) M+=((phone[i]/60)+1)*15;
    if(Y>M) printf("M %d",M);
    else if(Y<M) printf("Y %d", Y);
    else if(Y==M) printf("Y M %d", Y);
    
    return 0;
}
