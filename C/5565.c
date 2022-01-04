#include <stdio.h>
int main(void){
    int book[11];
    int total;
    scanf("%d", &total);
    for(int i=0;i<9;i++){
        scanf("%d", &book[i]);
        total-=book[i];
    }
    printf("%d", total);
    return 0;
}
