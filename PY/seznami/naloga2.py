studenti = ["Tone", "Tine", "Jure", "Tone", "Meta"]

# 1 dodaj se 5 svojih k temu seznamu

seznam2 = ["Erik", "Semir", "Adi", "Patrik", "Nik"]
studenti = studenti + seznam2
print(studenti)

# 2 izpisi najpogostejse ime
najpogostejse = max(studenti)
print(najpogostejse)

# 3 kolikokrat se ponavlja najpogostejse ime
count = 0
for niz in studenti:
    if niz == najpogostejse:
        count += 1
print(count)

# 4 uredite seznam studenti po abecedi
studenti.sort()
print(studenti)

# 5 naredi sezna s 5 stevili nato pa map funkcijo ki vrne dvakratnike tega seznama

stevila = [11, 22, 6, 8, 3]


def Dvokratniki(x):
    return x * 2


print(stevila)
stevila_dvokratniki = list(map(Dvokratniki, stevila))
print(stevila_dvokratniki)


# ponovi to samo s lambda funkcijo

stevila_dvokratniki_lambda = list(map(lambda x: x * 2, stevila))
print(stevila_dvokratniki_lambda)
