niz = "adislavburgicthegreat"
niz2 = ""

for i in range(len(niz)):
    if i % 2 == 0:
        niz2 += niz[i].upper()
    else:
        niz2 += niz[i]
print(niz2)
