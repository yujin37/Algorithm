//bronze3 하지만 난이도 좀 있음
#include <stdio.h>

int main(void){
    int x[5], y[5];
    for(int i=0;i<3;i++){
        scanf("%d %d", &x[i], &y[i]);
    }
    if(x[0]==x[1]){//수가 적으므로 노가다 하면 된다.
        x[3]=x[2];
    }
    else if(x[0]==x[2]){
        x[3]=x[1];
    }
    else{
        x[3]=x[0];
    }
    if(y[0]==y[1]){
        y[3]=y[2];
    }
    else if(y[0]==y[2]){
        y[3]=y[1];
    }
    else{
        y[3]=y[0];
    }
    printf("%d %d", x[3], y[3]);
    return 0;
}
