//마지막 계산 방식을 : ? 방식으로도 풀수 있을 것으로 예상됨
#include <stdio.h>
int main(void){
    int x,y,w,h;//0,0 을 계산
    int x1, y1;//w,h를 기준으로 계산
    scanf("%d %d %d %d", &x, &y, &w, &h);
    x1=x;
    y1=y;
    x1-=w;
    y1-=h;
    if(x1<0){
        x1*=-1;
    }
    if(y1<0){
        y1*=-1;
    }
    if(x>x1){
        x=x1;
    }
    if(y>y1){
        y=y1;
    }
    if(x<y){
        printf("%d",x);
    }
    else{
        printf("%d", y);
    }
    return 0;
}
