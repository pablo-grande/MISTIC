#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>


struct data {
 char name[64];
};

struct selector {
 int (*selector)();
};

void secret() {
 printf("secret area\n");
}

void regular() {
 printf("normal execution\n");
}

int main(int argc, char **argv) {
 struct data *d;
 struct selector *f;

 d = malloc(sizeof(struct data));
 f = malloc(sizeof(struct selector));
 f->selector = regular;

 printf("data is at %p, selector is at %p\n", d, f);

 strcpy(d->name, argv[1]);

 f->selector();
 
 return 1;
}

