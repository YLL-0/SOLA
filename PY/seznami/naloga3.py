elementi = ["Audi", "BMW", "Saab", "Skoda", "Mercedes"]
# 1 ustvari novega ki NE vsebuje SKoda:
seznam_brez_skode = []

for elm in elementi:
    if elm != "Skoda":
        seznam_brez_skode.append(elm)
print(seznam_brez_skode)

# 2 vse z veliki mickrami:
seznam_velike_crke = []


def VelikeCrke(niz):
    return niz.upper()


seznam_velike_crke = list(map(VelikeCrke, elementi))
seznam_velike_crke_lambda = list(map(lambda x: x.upper(), elementi))

print(seznam_velike_crke)
print(seznam_velike_crke_lambda)

# 3 zamenjaj BMW z VW:
elementi[elementi.index("BMW")] = "VW"
print(elementi)

# 4 elemenit v obratni smeri
elemenit_obratno = elementi[::-1]
print(elemenit_obratno)

# 5 razvrsti po abeceddi


elemenit_po_abecedi = sorted(elementi)
print(elemenit_po_abecedi)


# 6 razvrsti elemenit obratno

elemenit_po_abecedi_obratno = sorted(elementi, reverse=True)
print(elemenit_po_abecedi_obratno)

# 7 razvrsceno neglede na velikost crk


elemenit_po_abecedi_neglede = sorted(elementi, key=str.lower)
print(elemenit_po_abecedi_neglede)

# 8 razvrsti na tko koliko so blizu 100

sezname = [33, 133, 87, 11, 197, 98, 72, 125]

seznam_blizu100 = sorted(sezname, key=lambda x: abs(x - 100))
print(seznam_blizu100)


# 9 5 stevil v tabelo ter izpisi njiho vsoto in povprecno vrednost
stevila = [30, 5, 11, 67, 53]


def vsotaInAvg(x):
    vsota = 0
    avg = 0
    count = 0
    for i in x:
        count += 1
        vsota += i
    avg = vsota / count
    return vsota, avg


print(vsotaInAvg(stevila))

# 10 v tabeli 10 stevil poisci najvecjo in najmanjso vrednost

stevinla2 = [123, 8, 23, 48, 987, 2, 482, 99, 366, 100]


def MaxSt(x):
    max = 0
    for i in x:
        if i > max:
            max = i
    return max


def MinSt(x):
    min = 0
    for i in x:
        if i < min:
            min = i
    return min


print(MinSt(stevinla2), MaxSt(stevinla2))
