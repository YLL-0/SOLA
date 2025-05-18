#include <stdio.h>

void reverse(char s[]){ 
  int temp;
  int length = 0;

  while (s[length] != '\0') {
    length++;
  }
  for (int i = 0, j = length - 1; i < j; i++, j--) {
    temp = s[i];
    s[i] = s[j];
    s[j] = temp;
  }
}

 int main() {
  char tab[14000], c;
  FILE *dat;
  
  dat = fopen("text.txt", "r");
  if (dat == NULL) {
    printf("Error opening file\n");
    return 1;
  }
  
  int count = 0;
  
  while ((c = fgetc(dat)) != EOF) {
    if (c != '\n') {
      tab[count] = c;
      ++count;
    } else {
      tab[count] = '\0'; // Add null terminator
      reverse(tab);
      printf("%s\n", tab);
      count = 0;
    }
  }
  
  // Process the last line if it doesn't end with a newline
  if (count > 0) {
    tab[count] = '\0';
    reverse(tab);
    printf("%s\n", tab);
  }
  
  fclose(dat);
  return 0;
}
