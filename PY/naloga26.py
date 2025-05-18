def Csv(niz):
    besede = []
    trenutna_beseda = ""
    
    for znak in niz:
        if znak.isspace():
            if trenutna_beseda:  
                besede.append(trenutna_beseda)
                trenutna_beseda = ""
        else:
            trenutna_beseda += znak
    
    if trenutna_beseda:
        besede.append(trenutna_beseda)
    
    rezultat = ";".join(besede)
    
    return rezultat

test_niz = "Ana  je beseda, ker  nima vmesnih presledkov! Zakaj  tako pišemo?"
rezultat = Csv(test_niz)
print(f"CSV format: '{rezultat}'")
