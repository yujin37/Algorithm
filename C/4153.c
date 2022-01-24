//bronze3
#include <stdio.h>
int main(void){
    int d1, d2, d3;
    int temp;
    while(1){
        scanf("%d %d %d", &d1, &d2, &d3);
        if(d1==0&&d2==0&&d3==0){
            return 0;
        }
        if(d1<d2){
            temp=d1;
            d1=d2;
            d2=temp;
            if(d1<d3){
                temp=d1;
                d1=d3;
                d3=temp;
            }   
        }
        else{
            if(d1<d3){
                temp=d1;
                d1=d3;
                d3=temp;
            }
        }
        //여기까지는 큰 수 판정
        int result=d1*d1-d2*d2-d3*d3;
        if(result==0){
            printf("right\n");
        }
        else{
            printf("wrong\n");
        }
        
    }//여기는 계산해서 판단
}
