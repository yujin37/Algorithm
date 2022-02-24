//윷놀이
#include <stdio.h>
int main(void){
    int a,b,c,d,result;
    for(int i=0;i<3;i++){
        result=0;
        scanf("%d %d %d %d",&a,&b,&c,&d);
        result=a+b+c+d;
        if(result==1) printf("C");
        else if(result==2) printf("B");
        else if(result==3) printf("A");
        else if(result==4) printf("E");
        else if(result==0) printf("D");
        printf("\n");
    }

}
