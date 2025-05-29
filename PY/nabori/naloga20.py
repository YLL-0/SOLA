seznam = [
    ("moka", 2.11),
    ("jajca", 2.42),
    ("kruh", 2.81),
    ("caj", 3.12),
    ("solata", 2.92),
    ("donat", 2.74),
]
print(seznam)
samo_artikli = []
samo_cema = []
for i, j in seznam:
    samo_artikli.append(i)
    samo_cema.append(j)
print(samo_artikli, samo_cema)

kolicina_kosov = [2, 2, 1, 3, 1, 6]

znesek = 0
for x, element in enumerate(samo_cema):
    znesek = znesek + (element * kolicina_kosov[x])


print("Znesek je: ", znesek)
