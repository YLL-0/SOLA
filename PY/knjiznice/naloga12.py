studenti = []
visine = []
# branje
with open("visine.txt", "r") as datoteka:
    for vrstica in datoteka:
        podatki = vrstica.strip().split()
        studenti.append(podatki[0])
        visine.append(int(podatki[1]))

# avg visina
print("Povprečna višina:", sum(visine) / len(visine))

# najvisji in najnizji
najvišji_indeks = visine.index(max(visine))
najnižji_indeks = visine.index(min(visine))

print("Najvišji je", studenti[najvišji_indeks], "z višino", max(visine), "cm")
print("Najnižji je", studenti[najnižji_indeks], "z višino", min(visine), "cm")

# podatki urejeni po velikosti
print("\n Urejeni podatki po višini:")
pari = list(zip(visine, studenti))
pari.sort()

for visina, student in pari:
    print(student, visina)
