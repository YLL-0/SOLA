
#include <stdio.h>

// Rekurzivna funkcija za iskanje NSD dveh števil z Evklidovim algoritmom
int GCD(int a, int b) { return b == 0 ? a : GCD(b, a % b); }

// Funkcija za iskanje NSD več števil
int iskanjeGCD(int stevila[], int n) {
    int rezultat = stevila[0];
    for (int i = 1; i < n; i++) {
        rezultat = GCD(rezultat, stevila[i]);
    }
    return rezultat;
}

int main() {
    int n, i;
    int stevila[100000]; // Največja velikost tabele je 100000 po navodilih

    // Preverjanje vnosa
    do {
        printf("Vnesi n (2 <= n <= 100000): ");
        scanf("%d", &n);
    } while (n < 2 || n > 100000);

    // Vnos n števil
    printf("Vnesi %d naravnih stevil:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &stevila[i]);
    }

    // Izračun in izpis NSD
    int rezultat = iskanjeGCD(stevila, n);
    printf("Najvecji skupni delitelj: %d\n", rezultat);

    return 0;
}
