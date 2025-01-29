#include <string.h>
#include <stdio.h>

void main(int argc, char *argv[]) {
	copy(argv[1]);
}

int copy(char *str) {
	char buffer[100];
	strcpy(buffer, str);
}
