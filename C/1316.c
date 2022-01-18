/*silver5/ 다시 풀기/ 길이를 재주는 것, 그리고 중복 여부를 세주는 w를 이용해 확인. 연속으로 나오면 !=w가 성립하지 않지만
따로 있는데 중복 될 경우에는 +=1이 되어 2가 되므로 중단되는 원리*/
#include <stdio.h>
#include <string.h> 
int main(void){
    int N;
    scanf("%d", &N);
    char word[100];
    int count=N;
    for(int i=0;i<N;i++){
        int alp[27]={0,};
        char w='0';
        scanf("%s", word);
        for(int j=0;j<strlen(word);j++){
            if(word[j]!=w){
                w=word[j];
                alp[word[j]-'a']+=1;
            }
            if(alp[word[j]-'a']==2){
                count-=1;
                break;
            }
        }
    }
    printf("%d", count);

    /*
    for(int i=0;i<N;i++){
        printf("%s\n", word[i]);
    }
    */
    return 0;
}
