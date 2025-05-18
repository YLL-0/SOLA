#include <stdio.h>
// Naredi program, ki izpise temeperaturo v farenhitih in v stopinjah
// Najprej naredi tako da ko vnesemo eno enoto nam vrne nazaj se drugo
// Formula je C=(5/9)*(F-32)

int stopnje_v_farehnite(int y) {
  double x = (5 / 9) * (y - 32);

  return x;
}

int main() { return 0; }
