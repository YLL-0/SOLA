#include <stdio.h>

// program prebere preslede in si zapomne ali je prejsni
// bil presledek in ce je ne izpise outputa

int main() {
  int c, blanks = 0;

  while ((c = getchar()) != EOF) {
    if (c != ' ') {
      printf("%c", c);
      blanks = 0;

    } else {
      ++blanks;
      if (blanks < 2) {
        printf("%c", c);
      }
    }
  }
  return 0;
}
