//bronze1
#include <stdio.h>
int main(void){
    int N,num[1001];
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        scanf("%d", &num[i]);
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(num[i]<num[j]){
                int temp=num[i];
                num[i]=num[j];
                num[j]=temp;
            }
        }
    }
    for(int i=0;i<N;i++){
        printf("%d\n", num[i]);
    }
    return 0;
}
