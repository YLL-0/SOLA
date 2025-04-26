#include <stdio.h>

int main() {
  int c;
  while ((c = getchar()) != EOF) {
    if (c == '\t')
      printf("\\t"); // Print \t literally
    else if (c == '\b')
      printf("\\b"); // Print \b literally
    else if (c == '\\')
      printf("\\\\"); // Print \\ literally
    else
      putchar(c); // Print normal character
  }
  return 0;
}
