# Kvadrat: p = a*a, o 4*a
# Trikotnik: p = (b * h)/2, o = a + b + c
# Krog: p = pi*r^2, o = 2*pi*r
# Pravokotnik: a*b, o = 2 (a + b)
import math
from types import prepare_class


def Kvadrat(a):
    p = a * a
    o = 4 * a
    return p, o


def Trikotnik(a):
    p = (a * a * math.sqrt(3)) / 4
    o = 3 * a
    return p, o


def Krog(r):
    p = math.pi * r**2
    o = 2 * math.pi * r
    return p, o


def Pravokotnik(a, b):
    p = a * b
    o = 2 * (a + b)
    return p, o


def Izracun(niz, x, y):
    if niz == "Kvadrat":
        print(Kvadrat(x))
    elif niz == "Trikotnik":
        print(Trikotnik(x))
    elif niz == "Krog":
        print(Krog(x))
    elif niz == "Pravokotnik":
        print(Pravokotnik(x, y))
    else:
        print("Napacen vnos")


#
# print(Kvadrat(4))
# print(Trikotnik(2))
# print(Krog(3))
# print(Pravokotnik(2, 3))

Izracun("Kvadrat", 4, 0)
