//bronze 2
#include <stdio.h>
#include <string.h>

int main(void){
    char sen[1000001];
    int count=1;
    fgets(sen,1000001,stdin);
    for(int i=0;i<strlen(sen);i++){
        if(sen[i]==' '&&sen[i-1]==' '){
            continue;
        }
        else if(sen[i]==' '){
            count++;
        }
    }
    if(sen[0]==' '){
        count--;
    }//처음 부분에 공백
    if(sen[strlen(sen)-2]==' '){
        count--;
    }//마지막 부분에 공백
    printf("%d", count);
    return 0;
}
