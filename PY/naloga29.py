def StejCrke(niz):
    besede = niz.split()
    dolzine = []
    
    for beseda in besede:
        ociscena = beseda.strip(',.!?:;\"\'()[]{}*&!@#$%^~+=-_')
        dolzine.append(str(len(ociscena)))
    
    print(' '.join(dolzine))

niz = 'danes je lep dan!'
StejCrke(niz)  
