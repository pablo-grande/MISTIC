#include <stdio.h>
#include <string.h>

char s[6];

int main() {
  puts("Whats my name?");

  do
    fgets(s, sizeof(s), stdin);
  while(strcmp(s, "mrmtg"));  

  puts("You got it!");

  return 0;
}
