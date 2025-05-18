def Palindrom(niz):
    ocisceni_niz = niz.lower().replace(" ", "")
    
    if ocisceni_niz == ocisceni_niz[::-1]:
        print(f"niz '{niz}' je palindrom.")
        return True
    else:
        print(f"niz '{niz}' ni palindrom.")
        return False

test_niz1 = "Ana"
test_niz2 = "Danes je lep dan"
Palindrom(test_niz1)
Palindrom(test_niz2)
