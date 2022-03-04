//별찍기7
#include <stdio.h>
int main(void){
   int n;
   scanf("%d", &n);
   for(int i=1;i<=n-1;i++){
      for(int j=1;j<=n-i;j++) printf(" ");
      for(int k=1;k<=2*i-1;k++) printf("*");
      printf("\n");
   }
   for(int i=n;i>0;i--){
      for(int j=n-i;j>0;j--) printf(" ");
      for(int k=1;k<=2*i-1;k++) printf("*");
      printf("\n");
   }
}
