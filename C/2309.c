//bronze 2
#include <stdio.h>
int main(void){
    int N[10]; //난쟁이 키 입력받는 변수
    int sum=0,sum1;
    int out1=0, out2=0;
    for(int i=0;i<9;i++){
        scanf("%d", &N[i]);//저장
        sum+=N[i];
    }
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            sum1=sum;
            sum1=sum1-(N[i]+N[j]);
            if(sum1==100){
                if(out1==0 && out2==0){
                    out1+=i;
                    out2+=j;
                    break;
                }
            }
        }
    }
    int h1=N[out1];
    int h2=N[out2];
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            if(N[i]<N[j]){
                int temp=N[i];
                N[i]=N[j];
                N[j]=temp;
            }
        }
    }
    for(int i=0;i<9;i++){
        if(N[i]!=h1 && N[i]!=h2){
            printf("%d\n", N[i]);
        }
    }
    return 0;
}
