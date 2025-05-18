import math

def Izracun(lik, **kwargs):
    if lik == "kvadrat":
        a = kwargs.get("a", 0)
        obseg = 4 * a
        ploscina = a ** 2
        
    elif lik == "trikotnik":
        a = kwargs.get("a", 0)
        obseg = 3 * a
        ploscina = (math.sqrt(3) / 4) * (a ** 2)
        
    elif lik == "krog":
        r = kwargs.get("r", 0)
        obseg = 2 * math.pi * r
        ploscina = math.pi * (r ** 2)
        
    elif lik == "pravokotnik":
        a = kwargs.get("a", 0)
        b = kwargs.get("b", 0)
        obseg = 2 * (a + b)
        ploscina = a * b
        
    else:
        return None, None
            
    return obseg, ploscina

def Izpis(lik, **kwargs):
    if lik == "kvadrat":
        print(lik + ":", "a =", kwargs.get('a'))
    elif lik == "trikotnik":
        print(lik + ":", "a =", kwargs.get('a'))
    elif lik == "krog":
        print(lik + ":", "r =", kwargs.get('r'))
    elif lik == "pravokotnik":
        print(lik + ":", "a =", kwargs.get('a'), ", b =", kwargs.get('b'))
            
    obseg, ploscina = Izracun(lik, **kwargs)
    print("obseg =", obseg)
    print("ploscina =", ploscina)
    
    return obseg, ploscina

print("Test za kvadrat:")
Izpis("kvadrat", a=4)
print()

print("Test za trikotnik:")
Izpis("trikotnik", a=2)
print()

print("Test za krog:")
Izpis("krog", r=3)
print()

print("Test za pravokotnik:")
Izpis("pravokotnik", a=2, b=3)
print()
