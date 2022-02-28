#include <stdio.h>
int num[21];
void reverse(int n1, int n2){
    for(int i=0;i<((n2-n1)/2)+1;i++){
        int temp=num[n1+i];
        num[n1+i]=num[n2-i];
        num[n2-i]=temp;
        
    }
}
int main(void){
    for(int i=1;i<=20;i++) num[i]=i;
    for(int i=1;i<=10;i++){
        int a, b;
        scanf("%d %d", &a, &b);
        reverse(a,b);
        //for(int i=1;i<=20;i++) printf("%d ",num[i]);
        //printf("\n");
    }
    for(int i=1;i<=20;i++) printf("%d ",num[i]);
    return 0;
}
