//bronze1, try again
#include <stdio.h>
#include <string.h>
int main(void){
    char word[1000000];
    int count[26]={0,};
    int alp,result=0,select=0;
    scanf("%s",word);
    for(int i='a';i<='z';i++){
        for(int j=0;j<strlen(word);j++){
            if(i==word[j]){
                count[i-'a']++;
            }
        }
    }
    for(int i='A';i<='Z';i++){
        for(int j=0;j<strlen(word);j++){
            if(i==word[j]){
                count[i-'A']++;
            }
        }
    }
    alp=count[0];
    for(int i=0;i<26;i++){
        if(alp<count[i]){
            alp=count[i];
            select=i;
        }
    }
    for(int i=0;i<25;i++){
        if(alp==count[i]){
            result++;
        }
    }
    if(result >1){
        printf("?\n");
    }
    else{
        printf("%c", select+'A');
    }
    return 0;
}
