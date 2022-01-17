#include <stdio.h>
#include <stdlib.h>
typedef struct Map{
    int x;
    int y;
}Map;

int compare(const void *a, const void *b){
    Map A=*(Map *)a;
    Map B=*(Map *)b;

    if(A.x >B.x){
        return 1;//바꿔줌
    }
    else if(A.x==B.x){
        if(A.y>B.y){
            return 1;//바꿔줌
        }
        else{
            return -1;//바꾸어주지 않음
        }
    }
    return -1;//해당하지 않으므로 바꿔주지 않음
}
int main(void){
    int N;
    scanf("%d", &N);
    Map *map;
    map=(Map*)malloc(sizeof(Map)*N);
    for(int i=0;i<N;i++){
        scanf("%d %d", &map[i].x, &map[i].y);
    }
    qsort(map,N,sizeof(Map),compare);//정렬할 배열, 요소 개수, 요소 크기, 비교 함수를 넣어줌
    for(int i=0;i<N;i++){
        printf("%d %d\n", map[i].x, map[i].y);
    }
    free(map);
    return 0;
}
