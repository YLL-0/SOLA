
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n, i;
    char medpomnilnik[3000]; // Začasni medpomnilnik za branje nizov
    char *nizi[1000];        // Tabela kazalcev na nize
    int skupnoZnakov = 0;

    // Preverjanje vnosa
    do {
        printf("Vnesi n izmed 1 in 10000: ");
        scanf("%d", &n);
        getchar(); // Porabi znak za novo vrstico
    } while (n < 1 || n > 1000);

    // Preberi n nizov
    printf("Vnesi %d nizov (skupna dolzina < 3000 znakov):\n", n);
    for (i = 0; i < n; i++) {
        printf("Niz %d: ", i + 1);
        fgets(medpomnilnik, sizeof(medpomnilnik), stdin);

        // Odstrani znak za novo vrstico, če je prisoten
        int dolzina = strlen(medpomnilnik);
        if (medpomnilnik[dolzina - 1] == '\n') {
            medpomnilnik[dolzina - 1] = '\0';
            dolzina--;
        }

        // Dodeli pomnilnik za ta niz in kopiraj iz medpomnilnika
        nizi[i] = (char *)malloc((dolzina + 1) * sizeof(char));
        strcpy(nizi[i], medpomnilnik);

        skupnoZnakov += dolzina;

        // Preveri, ali skupno število znakov presega omejitev
        if (skupnoZnakov >= 3000) {
            printf("Skupno stevilo znakov presega 3000. Ustavljanje vnosa.\n");
            n = i + 1; // Prilagodi n na dejansko število prebranih nizov
            break;
        }
    }

    // Izpiši vse nize
    printf("\nVsi nizi:\n");
    for (i = 0; i < n; i++) {
        printf("%s\n", nizi[i]);
    }

    // Sprosti dodeljen pomnilnik
    for (i = 0; i < n; i++) {
        free(nizi[i]);
    }

    return 0;
}
