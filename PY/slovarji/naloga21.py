ime = ["Janez", "Miha", "Ana", "Angela", "Rozi", "Matevz", "Pepec"]
visina = [1.88, 1.91, 1.65, 1.77, 1.71, 1.75, 1.80]
starost = [22, 23, 20, 21, 20, 21, 19]

i = 0
seznam = {}
while i < len(ime):
    seznam[ime[i]] = visina[i], starost[i]
    i = i + 1
print(seznam.values())
studenti = {
    "Janez": {"visina": 1.88, "starost": 22},
    "Miha": {"visina": 1.91, "starost": 23},
    "Ana": {"visina": 1.65, "starost": 20},
    "Angela": {"visina": 1.77, "starost": 21},
    "Rozi": {"visina": 1.71, "starost": 20},
    "Matevž": {"visina": 1.75, "starost": 21},
    "Pepca": {"visina": 1.80, "starost": 19},
}

for vis in studenti.values():
    print(vis["visina"])
