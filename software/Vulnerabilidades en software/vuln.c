#include <stdio.h>

int main(int argc, char **argv){
        char buffer[256];
        strcpy(buffer, argv[1]);
        printf(buffer);
        printf("\n");

        return 1;
}
