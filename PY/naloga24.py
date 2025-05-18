def Prvi(n, s):
    return s[:n]

def Zadnji(n, s):
    return s[-n:]

test_niz = "Danes je lep dan"
n = 5
print(f"Prvih {n} znakov: {Prvi(n, test_niz)}")
print(f"Zadnjih {n} znakov: {Zadnji(n, test_niz)}")
