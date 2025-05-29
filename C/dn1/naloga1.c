#include <stdio.h>

int main() {

    int x, i;
    int tabela[100];
    int zadnji;

    // vnos stevila

    do {
        printf("Vnesi stevilo med 1 in 100: ");
        scanf("%d", &x);
    } while (x <= 1 || x > 100);

    printf("Vnesi %d stevil :\n", x);
    for (i = 0; i < x; i++) {
        scanf("%d", &tabela[i]);
    }

    // Shranimo zadnji element preden ga uporabimo:
    zadnji = tabela[x - 1];

    // Zamaknemo desno za eno mesto, zacnemo desno da ne overwritamo vrednosti
    for (i = x - 1; i > 0; i--) {
        tabela[i] = tabela[i - 1];
    }
    tabela[0] = zadnji;

    printf("Obrnjeana tabela :\n");
    for (i = 0; i < x; i++) {
        printf("%d ", tabela[i]);
    }
    printf("\n");

    return 0;
}
