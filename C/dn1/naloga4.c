#include <stdio.h>

int main() {
    int x, count = 0;
    int bit1, bit2, bit3, bit4;

    // Preverjanje vnosa
    do {
        printf("Vnesi x med 1 in 100: ");
        scanf("%d", &x);
    } while (x < 1 || x > 100);

    // Generiranje binarnih števil s pomočjo 4 gnezdenih zank
    for (bit1 = 0; bit1 <= 1 && count < x; bit1++) {
        for (bit2 = 0; bit2 <= 1 && count < x; bit2++) {
            for (bit3 = 0; bit3 <= 1 && count < x; bit3++) {
                for (bit4 = 0; bit4 <= 1 && count < x; bit4++) {
                    printf("%d%d%d%d\n", bit1, bit2, bit3, bit4);
                    count++;
                }
            }
        }
    }

    return 0;
}
