niz = "Ana     je beseda ,   kar    nima vmesnigh   presledkov!"


def Csv(niz1):

    niz1 = niz1.replace(",", "")
    split = niz1.split()
    niz2 = ""
    for beseda in split:
        niz2 = niz2 + beseda + ";"
    print(niz2)


Csv(niz)
