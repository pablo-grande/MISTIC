// https://medium.com/@jhjaksimsam2/what-is-format-string-attack-how-to-prevent-this-attack-59b480ce9989
#include <stdio.h>
#include <string.h>

int main(){
  int i =0;
  char buf[64];
  memset(buf, 0, 64);
  read(0, buf, 64);
  printf(buf);
  return 1;
}
