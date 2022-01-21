//silver5, 구조를 잘못 만들어서 틀렸음. 반대로 생각함. flag라는 확인할 수 있는 것들을 넣어주자.
#include <stdio.h>
int main(void){
    int M, N;
    int min=0, sum=0;
    int flag;
    scanf("%d",&M);
    scanf("%d", &N);
    
    for(int i=M;i<=N;i++){
        flag=0;
        if(i==1){
            continue;
        }
        for(int j=2;j<i;j++){
            if(i%j==0){
                flag=1;
            }
        }
        if(flag==0){
            if(min==0){
                min+=i;
            }
            sum+=i;
        }
    }
    
    
    if(sum==0){
        printf("-1");
    }
    else{
        printf("%d %d", sum, min);
    }
    
    return 0;
}
