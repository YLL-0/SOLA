niz = {"ana", "miha", "janez", "bob"}

for i in niz:
    if i[::-1] == i:
        print(f"{i} je polindrom")
