//별찍기4
#include <stdio.h>
int main(void){
    int n;
    scanf("%d", &n);
    for(int i=0;i<n;i++){
        for(int j=n-i;j<n;j++){
            printf(" ");
        }
        for(int k=n-i-1;k>=0;k--){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
