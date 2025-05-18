# Naloga filter

# 1. Podan je seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Naloga 1: Podvojena vrednost za elemente večje od 5")
seznam1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for element in seznam1:
    if element > 5:
        print(element * 2)

print("\n")

# 2. Podan je seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5]
seznam2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5]

# a) izpišite vse podvojene vrednosti
print("Naloga 2a: Vse podvojene vrednosti")
for element in seznam2:
    print(element * 2)

print("\n")

# b) izpišite katere vrednosti so podvojene
print("Naloga 2b: Vrednosti, ki se pojavijo več kot enkrat")
pojavitve = {}

# Štetje pojavitev
for element in seznam2:
    if element in pojavitve:
        pojavitve[element] += 1
    else:
        pojavitve[element] = 1

# Izpis vrednosti, ki se pojavijo več kot enkrat
for element, stevilo in pojavitve.items():
    if stevilo > 1:
        print(f"Vrednost {element} se pojavi {stevilo}-krat")
