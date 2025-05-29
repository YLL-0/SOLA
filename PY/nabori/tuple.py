sani = ("lesene", "pvc", "kovinske")
(prva, druga, tretja) = sani
print(prva)
print(*druga)

nove = sani * 2
print(nove)

dict = {1: "ena", 2: "dva"}
nabor1 = tuple(dict)
print(nabor1)

list1 = [1, 2, 3, 4, 5]
nabor2 = tuple(list1)
print(nabor2)

niz = "danes je lep dan"
nabor3 = tuple(niz)
print(nabor3)

# COUNT izpise kolikokrat se elemnent (x) ponovi
ocene = (1, 2, 3, 2, 3, 4, 1, 3, 5)
print(ocene.count(3))

# INDEX od 3 v naboru
print(ocene.index(3))

student = ("Joze", 1.91, 21)
ime, visina, starost = student
print(ime, visina, student)
