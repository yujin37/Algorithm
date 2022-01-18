#silver5/ 이문제에서 조건에 만약 크로아티아 문자가 없다면 하나로 세줘야 한다했으므로 +하는 것보다 전체길이를 계산해 빼주는게 빠르다.
#include <stdio.h>
#include <string.h>

int main(void){
    char word[100];
    scanf("%s", word);
    int count=strlen(word);
    for(int i=0;i<strlen(word);i++){
        if(word[i]== '='){
            if(word[i-1]== 'c'){
                count-=1;
            }
            else if(word[i-1]== 'z'){
                if(word[i-2]== 'd'){
                    count-=2;
                }
                else{
                    count-=1;
                }
            }
            else if(word[i-1]== 's'){
                count-=1;
            }
        }
        else if(word[i]=='-'){
            if(word[i-1]=='c'){
                count-=1;
            }
            else if(word[i-1]=='d'){
                count-=1;
            }
        }
        else if(word[i]=='j'){
            if(word[i-1]== 'l'){
                count-=1;
            }
            else if(word[i-1]== 'n'){
                count-=1;
            }
        }
    }
    printf("%d", count);
    //printf("%s", word);
    return 0;
}
