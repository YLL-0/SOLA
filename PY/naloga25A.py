def Pali_razsirjen(niz):
    ocisceni_niz = niz.lower().replace(" ", "")
    
    je_palindrom = True
    dolzina = len(ocisceni_niz)
    
    for i in range(dolzina // 2):
        znak_levo = ocisceni_niz[i]
        znak_desno = ocisceni_niz[dolzina - 1 - i]
        
        if znak_levo != znak_desno:
            je_palindrom = False
            print(f"Znaka '{znak_levo}' in '{znak_desno}' na pozicijah {i} in {dolzina - 1 - i} se ne ujemata.")
    
    if je_palindrom:
        print(f"niz '{niz}' je palindrom.")
        return True
    else:
        print(f"niz '{niz}' ni palindrom.")
        return False

test_niz = "arara"
Pali_razsirjen(test_niz)
