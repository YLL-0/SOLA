def Prvi(n, s):
    count = 1
    for c in s:
        if count <= n:
            print(c)
            count += 1


def Zadnji(n, s):
    s = s[::-1]
    count = 1
    for c in s:
        if count <= n:
            print(c)
            count += 1


Prvi(20, "danes je lep dan")
Zadnji(4, "danes je lep dan")
