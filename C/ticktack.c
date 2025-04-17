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
void game(int x) {
  int bool = 0;

  while (bool == 0) {
  }
}

int main() {
  guess();
  return 0;
}
