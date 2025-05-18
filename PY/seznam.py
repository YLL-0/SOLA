studenti = ["Tine", "Tone", "Jure", "Tone", "Meta"]

studenti1 = ["Adi", "Matic", "Erik", "Jaka", "Patrik"]
studenti.extend(studenti1)  
print("1. Razširjen seznam:", studenti)

najpogostejse_ime = max(studenti, key=studenti.count)
print("2. Najpogostejše ime:", najpogostejse_ime)

st_pojavitev = studenti.count(najpogostejse_ime)
print("3. Število pojavitev najpogostejšega imena:", st_pojavitev)

studenti.sort()
print("4. Urejen seznam:", studenti)

stevilke = [1, 2, 3, 4, 5]
dvakratniki_map = list(map(lambda x: x * 2, stevilke))
print("5. Seznam dvakratnikov (map):", dvakratniki_map)

dvakratniki_lambda = list(map(lambda x: x * 2, stevilke))
print("6. Seznam dvakratnikov (lambda):", dvakratniki_lambda)
