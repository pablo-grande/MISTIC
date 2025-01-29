#include <stdio.h>
#include <string.h>


void main(int argc, char *argv[]) {
  copy(argv[1]);
}

void copy(char *str) {
  char buffer[100];
  strcpy(buffer, str);
}
