#include <stdio.h>

int main() {

  char tab[20000], c;
  FILE *dat;
  dat = fopen("text.txt", "r");
  int count = 0;
  while ((c = fgetc(dat)) != EOF) {

    if (c != '\n') {
      tab[count] = c;
      ++count;
    } else if (c == '\n') {
      if (count >= 80) {
        printf("%s\n", tab);
      }
      for (int i = 0; i <= count; i++)
        tab[i] = ' ';
      count = 0;
    }
  }

  fclose(dat);

  return 0;
}
