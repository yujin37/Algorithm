//별찍기 6
#include <stdio.h>
int main(void){
   int n;
   scanf("%d", &n);
   for(int i=n;i>0;i--){
      for(int j=n-i;j>0;j--) printf(" ");
      for(int k=1;k<=2*i-1;k++) printf("*");
      printf("\n");
   }
}
