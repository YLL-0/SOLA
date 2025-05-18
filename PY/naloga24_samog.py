nizi1 = ["Abrakadabra", "solo", "cerebellum", "evkaliptus", "motokultivator"]

samoglasniki = "AEIOUaeiou"


urejeni_nizi = sorted(
    nizi1, key=lambda niz: sum(1 for znak in niz if znak in samoglasniki)
)

print("Urejen seznam glede na število samoglasnikov:")
for niz in urejeni_nizi:
    print(niz)

# bre lambde
print()
nizi2 = ["Abrakadabra", "solo", "cerebellum", "evkaliptus", "motokultivator"]


def stetje_samopglasnikov(niz):
    return sum(1 for znak in niz if znak in samoglasniki)


urejeni_nizi_brez_lambde = sorted(nizi2, key=stetje_samopglasnikov)

for niz in urejeni_nizi_brez_lambde:
    print(niz)

# brez vsega
# zamenjamo elemente, če je število samoglasnikov večje v for
# kjer rocno uredis seznam gledse na stevil samoglasnikov
print()

stevilo_samoglasnikov = [(niz, stetje_samopglasnikov(niz)) for niz in nizi1]

for i in range(len(stevilo_samoglasnikov)):
    for j in range(i + 1, len(stevilo_samoglasnikov)):
        if stevilo_samoglasnikov[i][1] > stevilo_samoglasnikov[j][1]:
            stevilo_samoglasnikov[i], stevilo_samoglasnikov[j] = (
                stevilo_samoglasnikov[j],
                stevilo_samoglasnikov[i],
            )

for niz, stevilo in stevilo_samoglasnikov:
    print(niz)
