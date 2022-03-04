//별찍기 9
#include <stdio.h>
int main(void){
   int n;
   scanf("%d", &n);
   for(int i=1;i<=n-1;i++){
    for(int k=1;k<i;k++) printf(" ");
    for(int j=1;j<=(2*(n-i)+1);j++) printf("*");
    printf("\n");
  }
  for(int i=n;i>0;i--){
    for(int k=i-1;k>0;k--) printf(" ");
    for(int j=(2*(n-i)+1);j>0;j--) printf("*");
    printf("\n");
  }
}
