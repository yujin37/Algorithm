#include <stdio.h>
int main(void){
    int n,p;
    int cute=0, not=0;
    scanf("%d", &n);
    for(int i=0;i<n;i++){
        scanf("%d", &p);
        if(p==1){
            cute+=1;
        }
        else if(p==0){
            not+=1;
        }
    }

    if(cute>not){
        printf("Junhee is cute!");
    }
    else if(cute<not){
        printf("Junhee is not cute!");
    }
    return 0;
}
