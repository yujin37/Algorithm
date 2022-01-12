//bronze 2
#include <stdio.h>
#include <stdlib.h>
int main(void){
    char A[4], B[4];
    scanf("%s %s", A, B);
    char temp=A[0];
    A[0]=A[2];
    A[2]=temp;

    char temp1=B[0];
    B[0]=B[2];
    B[2]=temp1;

    if(atoi(A)>atoi(B)){
        printf("%s", A);
    }
    else{
        printf("%s", B);
    }
    return 0;
}
