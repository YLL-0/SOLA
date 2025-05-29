studenti = ("Tine", "Tone", "Jure", "Meta")
ocena = (9, 8, 7, 6)
rezultati = list(zip(studenti, ocena))
print(rezultati)

studenti, ocene = zip(*rezultati)
print("Studenti: ", studenti)
print("Ocene: ", ocena)
