# Podani podatki o delavcih
delavci = [
    ("Tine", "Uš", (1990, 5, 6)),
    ("Tone", "Novak", (1990, 1, 16)),
    ("Anton", "Novak", (1980, 8, 26)),
    ("Anton", "Novak", (1982, 10, 16)),
    ("Tine", "Uš", (1990, 5, 6)),
]

delavci.sort(key=lambda delavec: (delavec[1], delavec[0], delavec[2]))

for delavec in delavci:
    print(delavec)

# brez lambda

print()


def urejevalni_kljuc(delavec):
    priimek = delavec[1]
    ime = delavec[0]
    datum_rojstva = delavec[2]
    return (priimek, ime, datum_rojstva)


delavci.sort(key=urejevalni_kljuc)


for delavec in delavci:
    print(delavec)
