def Izpis(**kwargs):
    masa = kwargs.get("masa", 0)
    visina = kwargs.get("visina", 0)
    barva = kwargs.get("barva_las", "")

    masaT = masa / 1000
    visinaM = visina / 100
    barvaV = barva.upper()

    print("masa = ", masa, "kg in ", masaT, "ton")
    print("visina = ", visina, "cm in ", visinaM, "m")
    print("barva las = ", barva, " in ", barvaV)

    return masaT, visinaM, barvaV


Izpis(masa=60, visina=170, barva_las="crni")
