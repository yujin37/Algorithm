//숫자
#include <stdio.h>
int main(void){
    long long n1, n2;
    scanf("%lld %lld",&n1, &n2);
    if(n1>n2){
        long long temp=n1;
        n1=n2;
        n2=temp;
    }
    if(n1==n2 || n2-n1==1) printf("0\n");
    else{
        printf("%lld\n",n2-n1-1);
        for(long long i=n1+1;i<n2;i++){
            printf("%lld\n",i);
        }
    }
    return 0;
}
