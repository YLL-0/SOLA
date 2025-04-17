#include <stdio.h>
#include <stdlib.h>

void izpisPolja(int stevilo, int polje[]) {
  printf("Elementi v polju so: ");
  for (int i = 0; i < stevilo; i++) {
    printf("%d\n", polje[i]);
  }
}

int maxElement(int stevilo, int polje[]) {
  int max = polje[0];
  int i;
  for (i = 1; i < stevilo; i++) {
    if (max < polje[i]) {
      max = polje[i];
    }
  }
  return max;
}

void pozMaxElementa(int stevilo, int polje[], int max) {
  int pozicija = 0;
  int maxElem = max;
  int i;
  for (int i = 0; i < stevilo; i++) {
    if (polje[i] == maxElem) {
      pozicija = i;
    }
  }
  printf("%d\n", pozicija);
};

int main() {
  int a[] = {25, 50, 75, 100, 23, 65, 123, 91, 2, 82};
  int st = 10;

  izpisPolja(st, a);
  printf("\n");
  int max = maxElement(st, a);
  printf("%d\n", max);

  pozMaxElementa(st, a, max);
}
