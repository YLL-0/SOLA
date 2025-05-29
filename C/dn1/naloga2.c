#include <stdio.h>

int main() {
    // Ker je velika stevilka uporabimo long
    long vnosSekund, preostaleSekunde;

    int dnevi, ure, minute, ostanekSekunde;

    // Vnos sekunbd
    printf("Vnesti sekude: ");
    scanf("%ld", &vnosSekund);

    // Racunanje:
    preostaleSekunde = vnosSekund;
    dnevi = preostaleSekunde / (24 * 60 * 60);
    preostaleSekunde %= (24 * 60 * 60);
    ure = preostaleSekunde / (60 * 60);
    preostaleSekunde %= (60 * 60);
    minute = preostaleSekunde / 60;
    ostanekSekunde = preostaleSekunde % 60;
    // Izpis
    printf("Vnesene sekunde %ld se lahko zpise kot %d dni,%d ur ,%d minut in "
           "%d sekund. \n",
           vnosSekund, dnevi, ure, minute, ostanekSekunde);

    return 0;
}
