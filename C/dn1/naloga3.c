#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int i, glava = 0, stevilka = 0;
    // Inicializacija za generiranje randome stevil
    srand(time(NULL));

    for (i = 0; i < 1000; i++) {
        // Generiramo nakljucno stevilo in nato primerjamo
        int metKovanca = rand() % 2;
        if (metKovanca == 0) {
            glava++;
        } else {
            stevilka++;
        }
    }
    // Izpis
    printf("Po 1000 metih kovanca dobimo: \n");
    printf("Stevilka : %d\n", stevilka);
    printf("Glava : %d\n", glava);

    return 0;
}
