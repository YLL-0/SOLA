# Podan seznam
elementi = ["Audi", "BMW", "Saab", "Škoda", "Mercedes"]

# 6. Ustvarjanje novega seznama brez "Škoda"
novi_elementi = [x for x in elementi if x != "Škoda"]
print("6. Nov seznam brez 'Škoda':", novi_elementi)

# 7. Pretvorba seznama v velike črke
elementi_veliki = [x.upper() for x in elementi]
print("7. Seznam z velikimi črkami:", elementi_veliki)

# 8. Zamenjava "BMW" s "VW"
elementi[elementi.index("BMW")] = "VW"
print("8. Seznam z zamenjano znamko:", elementi)

# 9. Seznam v obratni smeri
elementi_obratno = elementi[::-1]
print("9. Seznam v obratni smeri:", elementi_obratno)

# 10. Razvrščanje seznama po abecedi
elementi_urejeni = sorted(elementi)
print("10. Razvrščen seznam:", elementi_urejeni)

# 11. Razvrščanje seznama po abecedi v nasprotni smeri
elementi_urejeni_obratno = sorted(elementi, reverse=True)
print("11. Obratno razvrščen seznam:", elementi_urejeni_obratno)

# 12. Preverjanje razvrščanja glede na velikost črk
elementi_test = ["Audi", "BMW", "saab", "Škoda", "mercedes"]
elementi_test_sorted = sorted(elementi_test)
print("12. Pri razvrščanju so najprej razvrščeni:", elementi_test_sorted)
print("    (Najprej so razvrščeni nizi z velikimi črkami)")

# Razvrščanje neodvisno od velikosti črk
elementi_test_case_insensitive = sorted(elementi_test, key=str.lower)
print("    Razvrščanje neodvisno od velikosti črk:", elementi_test_case_insensitive)

# 13. Razvrščanje števil glede na bližino številu 100
stev = [33, 133, 87, 11, 197, 98, 72, 125]
stev_blizina_100 = sorted(stev, key=lambda x: abs(x - 100))
print("13. Števila razvrščena po bližini številu 100:", stev_blizina_100)
