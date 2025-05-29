def word_count(niz):
    x = 0
    for i in niz.split():
        x += 1
    return x


niz1 = "danes je lep dan "
print(niz1.split())
print(word_count(niz1))
