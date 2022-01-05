#include <stdio.h>
#include <string.h>
int main(void){
    char C[3];
    scanf("%s", C);
    if(!strcmp(C, "A+")){
        printf("4.3");
    }
    else if(!strcmp(C, "A0")){
        printf("4.0");
    }
    else if(!strcmp(C, "A-")){
        printf("3.7");
    }
    else if(!strcmp(C, "B+")){
        printf("3.3");
    }
    else if(!strcmp(C, "B0")){
        printf("3.0");
    }
    else if(!strcmp(C, "B-")){
        printf("2.7");
    }
    else if(!strcmp(C, "C+")){
        printf("2.3");
    }
    else if(!strcmp(C, "C0")){
        printf("2.0");
    }
    else if(!strcmp(C, "C-")){
        printf("1.7");
    }
    else if(!strcmp(C, "D+")){
        printf("1.3");
    }
    else if(!strcmp(C, "D0")){
        printf("1.0");
    }
    else if(!strcmp(C, "D-")){
        printf("0.7");
    }
    else if(!strcmp(C, "F")){
        printf("0.0");
    }
    return 0;
}
