#include <stdio.h>

#define IN 1
#define OUT 0
// This is some text for a assigment i am doing -> 10 besed
// Modefiy is to it counts all spaces, newlines, tabs, words and how many
// times does a diget 1-10 appered
int main() {
  FILE *dat;
  int c;
  int space = 0, newlines = 0, tabs = 0;
  int words = 0;
  int state = OUT;
  // r pomeni read
  dat = fopen("text.txt", "r");

  while ((c = fgetc(dat)) != EOF) {

    if (c == ' ' || c == '\n' || c == '\t')
      state = OUT;
    else if (state == OUT) {
      state = IN;
      ++words;
    }
  }

  printf("The word count is: %d\n", words);
  rewind(dat);
  int wordLeinght[words];
  int numOfChar = 0, count;
  int inWord = 0;

  while ((c = fgetc(dat)) != EOF) {
    if (c == ' ' || c == '\n' || c == '\t') {
      if (inWord) {
        wordLeinght[count] = numOfChar;
        ++count;
        numOfChar = 0;
        inWord = 0;
      }
    } else {
      inWord = 1;
      ++numOfChar;
    }
  }
  if (inWord && numOfChar < words) {
    wordLeinght[count] = numOfChar;
    ++count;
  }

  for (int i = 0; i < words; i++) {
    printf("[%d]-> ", i);
    for (int j = 1; j <= wordLeinght[i]; j++) {
      printf("*");
    }
    printf("\n");
  }
  // make a character count and then print in histogram
  fclose(dat);
  return 0;
}
