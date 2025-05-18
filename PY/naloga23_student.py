studenti = {
    "Janez": {"višina": 1.88, "starost": 20},
    "Miha": {"višina": 1.91, "starost": 19},
    "Ana": {"višina": 1.65, "starost": 20},
    "Angela": {"višina": 1.77, "starost": 21},
    "Rozi": {"višina": 1.71, "starost": 20},
    "Matevž": {"višina": 1.75, "starost": 21},
    "Pepca": {"višina": 1.80, "starost": 19},
}

starosti = list(map(lambda student: student["starost"], studenti.values()))
povprecna_starost = sum(starosti) / len(starosti)

print(f"Povprečna starost študentov je: {povprecna_starost}")

# brez lambda funkcije:

vsota_starosti = 0
stevilo_studentov = 0

for student_info in studenti.values():
    vsota_starosti += student_info["starost"]
    stevilo_studentov += 1

povprecna_starost_brez_lambda = vsota_starosti / stevilo_studentov

print(f"Povprečna starost študentov je: {povprecna_starost_brez_lambda}")
