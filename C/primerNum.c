#include <stdio.h>

int isPrime(int num) {
  if (num < 2) {
    return 0;
  }
  for (int i = 2; i * i <= num; i++) {
    if (num % i == 0) {
      return 0;
    }
  }
  return 1;
}

int main() {
  int n, count = 0, num = 2;

  printf("Vnesi koliko primeniggerjev zelis: ");
  scanf("%d", &n);

  printf("Prvih %d primeniggerkjev je:\n", n);

  while (count < n) {
    if (isPrime(num)) {
      printf("%d ", num);
      count++;
    }
    num++;
  }

  printf("\n");
  return 0;
}
