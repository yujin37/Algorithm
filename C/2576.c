//홀수
#include <stdio.h>
int main(void){
    int num, result=0,min=100;
    for(int i=0;i<7;i++){
        scanf("%d",&num);
        if(num%2!=0){
            result+=num;
            if(min>num) min=num;
        }
    }
    if(result!=0){
        printf("%d %d", result, min);
    }
    else{
        printf("-1");
    }
    return 0;
}
