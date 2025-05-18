def Izpis(**izpis):
    
    masa = izpis.get("masa", 0)
    visina = izpis.get("visina", 0)
    barvaLas = izpis.get("barvaLas", "")
    
    tona = masa / 1000
    metri = visina / 100
    barvaVeliko = barvaLas.upper()
    
    print("masa =", masa, "kg =", tona, "T")
    print("visina =", visina, "cm =", metri, "m")
    print("barvaLas =", barvaLas, "=", barvaVeliko)
    
    return masa, visina, barvaLas

Izpis(masa=66.5, visina=170, barvaLas="črni")
