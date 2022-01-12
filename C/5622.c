#bronze 2
#include <stdio.h>
#include <string.h>
int main(void){
    char call[16];
    int time=0;
    scanf("%s",call);
    for(int i=0;i<strlen(call);i++){
        if(call[i]=='A'||call[i]=='B'||call[i]=='C'){
            time+=3;
        }
        else if(call[i]=='D'||call[i]=='E'||call[i]=='F'){
            time+=4;
        }
        else if(call[i]=='G'||call[i]=='H'||call[i]=='I'){
            time+=5;
        }
        else if(call[i]=='J'||call[i]=='K'||call[i]=='L'){
            time+=6;
        }
        else if(call[i]=='M'||call[i]=='N'||call[i]=='O'){
            time+=7;
        }
        else if(call[i]=='P'||call[i]=='Q'||call[i]=='R'||call[i]=='S'){
            time+=8;
        }
        else if(call[i]=='T'||call[i]=='U'||call[i]=='V'){
            time+=9;
        }
        else if(call[i]=='W'||call[i]=='X'||call[i]=='Y'||call[i]=='Z'){
            time+=10;
        }
    }
    printf("%d", time);
    return 0;
}
