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

void redirect() {
  printf("Redirect to article page\n");
}

void check_credentials() {
  printf("Check credentials in DB\n");
}

int main(int argc, char **argv) {
  struct data *d;
  struct selector *f;

  d = malloc(sizeof(struct data));
  f = malloc(sizeof(struct selector));
  f->selector = check_credentials;

  strcpy(d->name, argv[1]);

  f->selector();

  return 1;
}

