//bronze2, fibonacci
#include <stdio.h>
int main(void){
    int n;
    scanf("%d", &n);
    int fibo[n+2];
    fibo[0]=0;
    fibo[1]=1;
    for(int i=2;i<n+1;i++){
        fibo[i]=fibo[i-2]+fibo[i-1];
    }
    printf("%d",fibo[n]);
    return 0;
}
