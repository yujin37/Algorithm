//대표값2
#include <stdio.h>
int main(void){
    int num[5]={0,}, total=0;
    for(int i=0;i<5;i++){
        scanf("%d", &num[i]);
        total+=num[i];
    }
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            if(num[i]>num[j]){
                int temp=num[i];
                num[i]=num[j];
                num[j]=temp;
            }
        }
    }
    printf("%d\n%d", total/5, num[2]);
    return 0;
}
