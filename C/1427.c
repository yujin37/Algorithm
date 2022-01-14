//정렬 silver 5
#include <stdio.h>
#include <string.h>

int main(void){
    char N[11];
    int len;
    scanf("%s", N);
    len=strlen(N);
    for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            if((N[i])>(N[j])){
                char temp=N[i];
                N[i]=N[j];
                N[j]=temp;
            }
        }
    }
    printf("%s", N);
    return 0;
}
