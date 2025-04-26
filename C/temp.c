#include <stdio.h>
// Naredi program, ki izpise temeperaturo v farenhitih in v stopinjah
// Najprej naredi tako da ko vnesemo eno enoto nam vrne nazaj se drugo
// Formula je C=(5/9)*(F-32)

#define UPPER 20

int vStopinje(int x) {
  int y = 0;
  y = (5 / 9) * (x - 32);
  return y;
}

int main() {

  int a = 1;
  char c = getchar();
  putchar(c);
}
