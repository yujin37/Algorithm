#include <stdio.h>

int main(void){
    int n1, n2;
    for(int i=0;i<10000;i++){
        scanf("%d %d", &n1, &n2);
        if(n1==0 && n2==0)
            break;
        if(n2%n1==0){
            printf("factor\n");
        }
        else if(n1%n2==0){
            printf("multiple\n");
        }
        else{
            printf("neither\n");
        }
    }
    return 0;
}
