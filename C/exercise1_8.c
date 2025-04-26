#include <stdio.h>

int main() {

  int tabs = 0, newlines = 0, blanks = 0;
  int c;

  while ((c = getchar()) != EOF) {
    if (c == ' ')
      ++blanks;
    else if (c == '\t')
      ++tabs;
    else if (c == '\n')
      ++newlines;
  }
  printf("%d\n%d\n%d", blanks, tabs, newlines);

  return 0;
}
