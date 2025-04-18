#include <stdio.h>
// tabele!!!!!!!

void displayGrid() {
  int vrstniRed = 1;
  int tab[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      printf("%d", tab[i][j]);
    }
    printf("\n");
  }
}
int guess() {
  int g;
  scanf("%d", &g);
  return g;
}

void takingTurns(int x) {
  int count = 0;
  if (x < 10) {
  }
}

void game() {
  int bool = 0;
  int gue;
  while (bool == 0) {
    int gue = guess();
    if (gue != 0) {
      printf("NOT a 0");

    } else {
      printf("ITS 0");
    }
  }
}

int main() {
  game();

  return 0;
}
