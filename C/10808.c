#include <stdio.h>
#include <string.h>
int main(void){
    char S[101];
    int count[27]={0,};
    scanf("%s", S);
    for(int i=0;i<101;i++){
        for(int j=0;j<26;j++){
            if(S[i]==(j+97)){
                count[j]+=1;
            }
        }
        if(i==strlen(S)){
            break;
        }
        
    }
    for(int i=0;i<26;i++){
        printf("%d ", count[i]);
    }
    return 0;
}
