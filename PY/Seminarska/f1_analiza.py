def nalozi_podatke(datoteka):
    rezultati = []
    with open(datoteka, 'r', encoding='utf-8') as f:
        # bere prvo vrstico
        glava = f.readline().strip().split(',')
        
        # bere ostale vrstice
        for vrstica in f:
            podatki = vrstica.strip().split(',')
            slovar = {}
            # spremeni stevilke v int
            for i, polje in enumerate(glava):
                if polje in ['Startna_pozicija', 'Koncna_pozicija', 'Tocke']:
                    try:
                        slovar[polje] = int(podatki[i])
                    except ValueError:
                        slovar[polje] = 0  
                else:
                    slovar[polje] = podatki[i]
            rezultati.append(slovar)
    
    print(f"Nalozenih {len(rezultati)} rezultatov dirk.")
    return rezultati


def ekipe_in_dirkaci(rezultati):
    ekipe = set()  
    # mnozica ekip
    dirkaci_po_ekipah = {}  
    
    # gre preko vseh rezultatov
    for zapis in rezultati:
        ekipa = zapis['Ekipa']
        ekipe.add(ekipa)  
        
        # ce ekipa se ne obstaja jo dodaj
        if ekipa not in dirkaci_po_ekipah:
            dirkaci_po_ekipah[ekipa] = set()
        
        # dodaj dirkaca
        dirkaci_po_ekipah[ekipa].add(zapis['Dirkac'])
    
    # spremeni v sortirane sezname
    for ekipa in dirkaci_po_ekipah:
        dirkaci_po_ekipah[ekipa] = sorted(list(dirkaci_po_ekipah[ekipa]))
    
    return ekipe, dirkaci_po_ekipah


def dirke_po_uspesnosti(rezultati):
    dirke = {}  
    # slovar za dirke
    
    # zbere pozicije za vsako dirko
    for zapis in rezultati:
        dirka = zapis['Dirka']
        koncna_pozicija = zapis['Koncna_pozicija']
        
        # samo ce je koncal dirko
        if koncna_pozicija > 0:
            if dirka not in dirke:
                dirke[dirka] = {'pozicije': [], 'tocke': []}
            
            # dodaj pozicijo
            dirke[dirka]['pozicije'].append(koncna_pozicija)
    
    # izracunaj povprecje
    povprecne_pozicije = []
    for dirka, podatki in dirke.items():
        povprecna_pozicija = sum(podatki['pozicije']) / len(podatki['pozicije'])
        povprecne_pozicije.append((dirka, round(povprecna_pozicija, 2)))
    
    # sortiraj po uspesnosti
    povprecne_pozicije.sort(key=lambda x: x[1])
    
    return povprecne_pozicije


def najboljsi_dirkaci(rezultati):
    dirkaci = {}  
    # slovar za dirkace
    
    # greje preko vseh rezultatov
    for zapis in rezultati:
        dirkac = zapis['Dirkac']
        koncna_pozicija = zapis['Koncna_pozicija']
        tocke = zapis['Tocke']
        
        # dodaj dirkaca ce ga ni
        if dirkac not in dirkaci:
            dirkaci[dirkac] = {'pozicije': [], 'skupne_tocke': 0}
        
        # dodaj podatke samo za koncane dirke
        if koncna_pozicija > 0:
            dirkaci[dirkac]['pozicije'].append(koncna_pozicija)
        # sestej tocke
        dirkaci[dirkac]['skupne_tocke'] += tocke
    
    # naredi seznam statistik
    dirkaci_statistika = []
    for dirkac, podatki in dirkaci.items():
        if len(podatki['pozicije']) > 0:  
            # samo ce je koncal vsaj eno dirko
            povprecna_pozicija = sum(podatki['pozicije']) / len(podatki['pozicije'])
            # terka (dirkac, povprecna_pozicija, skupne_tocke)
            dirkaci_statistika.append((dirkac, round(povprecna_pozicija, 2), podatki['skupne_tocke']))
    
    # sortiraj po tockah
    dirkaci_statistika.sort(key=lambda x: x[2], reverse=True)
    
    return dirkaci_statistika


def analiza_napredovanja(rezultati):
    dirkaci = {}  
    # slovar za napredovanja
    
    # gre preko vseh dirk
    for zapis in rezultati:
        dirkac = zapis['Dirkac']
        startna_pozicija = zapis['Startna_pozicija']
        koncna_pozicija = zapis['Koncna_pozicija']
        
        # samo tisti ki so startali in koncali
        if startna_pozicija > 0 and koncna_pozicija > 0:
            # pozitivno = napredoval, negativno = nazadoval
            napredovanje = startna_pozicija - koncna_pozicija
            
            # dodaj dirkaca ce ga ni
            if dirkac not in dirkaci:
                dirkaci[dirkac] = {'napredovanja': [], 'st_dirk': 0}
            
            # dodaj napredovanje
            dirkaci[dirkac]['napredovanja'].append(napredovanje)
            dirkaci[dirkac]['st_dirk'] += 1
    
    # izracunaj povprecno napredovanje
    napredovanja = []
    for dirkac, podatki in dirkaci.items():
        povprecno_napredovanje = sum(podatki['napredovanja']) / len(podatki['napredovanja'])
        # terka (dirkac, povprecno_napredovanje, stevilo_dirk)
        napredovanja.append((dirkac, round(povprecno_napredovanje, 2), podatki['st_dirk']))
    
    # sortiraj po napredovanju
    napredovanja.sort(key=lambda x: x[1], reverse=True)
    
    return napredovanja


def tockovanje_konstruktorjev(rezultati):
    ekipe = {} 
    # slovar za ekipe
    
    # gre preko vseh rezultatov
    for zapis in rezultati:
        ekipa = zapis['Ekipa']
        tocke = zapis['Tocke']
        najhitrejsi_krog = zapis['Najhitrejsi_krog']
        
        # dodaj ekipo ce je ni
        if ekipa not in ekipe:
            ekipe[ekipa] = {
                'tocke': 0,
                'najhitrejsi_krogi': 0,
                'zmage': 0,
                'stopnicke': 0,
                'dirke': set()  
                # mnozica za dirke
            }
        
        # sestej tocke
        ekipe[ekipa]['tocke'] += tocke
        
        # preveri najhitrejsi krog
        if najhitrejsi_krog == 'Da':
            ekipe[ekipa]['najhitrejsi_krogi'] += 1
        
        # preveri zmago
        if zapis['Koncna_pozicija'] == 1:
            ekipe[ekipa]['zmage'] += 1
        
        # preveri stopnicke
        if 1 <= zapis['Koncna_pozicija'] <= 3:
            ekipe[ekipa]['stopnicke'] += 1
        
        # dodaj dirko
        ekipe[ekipa]['dirke'].add(zapis['Dirka'])
    
    # spremeni mnozico dirk v stevilo
    for ekipa in ekipe:
        ekipe[ekipa]['st_dirk'] = len(ekipe[ekipa]['dirke'])
        del ekipe[ekipa]['dirke']  
        # odstrani mnozico
    
    return ekipe


def main():
    try:
        # 1. nalozi podatke
        rezultati = nalozi_podatke('formula1_2024.csv')
        
        # 2. analiza ekip in dirkacov
        ekipe, dirkaci_po_ekipah = ekipe_in_dirkaci(rezultati)
        print("\nEkipe v sezoni 2024:")
        for i, ekipa in enumerate(sorted(ekipe), 1):
            print(f"{i}. {ekipa}: {', '.join(dirkaci_po_ekipah[ekipa])}")
        
        # 3. analiza dirk po uspesnosti
        povprecne_pozicije = dirke_po_uspesnosti(rezultati)
        print("\nDirke razvrscene po povprecni uvrstitvi:")
        for dirka, povp in povprecne_pozicije:
            print(f"Dirka: {dirka}, Povprecna uvrstitev: {povp}")
        
        # 4. najboljsi dirkaci
        dirkaci_statistika = najboljsi_dirkaci(rezultati)
        print("\nDirkaci po stevilu tock:")
        for i, (dirkac, povp_poz, tocke) in enumerate(dirkaci_statistika, 1):
            print(f"{i}. {dirkac}: {tocke} tock (povprecna pozicija: {povp_poz})")
        
        # 5. analiza napredovanja
        napredovanja = analiza_napredovanja(rezultati)
        print("\nDirkaci po povprecnem napredovanju:")
        for dirkac, napredovanje, st_dirk in napredovanja:
            if napredovanje > 0:
                smer = "napredoval za"
            elif napredovanje < 0:
                smer = "nazadoval za"
                napredovanje = abs(napredovanje)
            else:
                smer = "ohranil pozicijo"
                napredovanje = ""
            
            print(f"{dirkac} je povprecno {smer} {napredovanje} mest ({st_dirk} dirk)")
        
        # 6. konstruktorsko prvenstvo
        ekipe_tocke = tockovanje_konstruktorjev(rezultati)
        print("\nKonstruktorsko prvenstvo:")
        for ekipa, statistika in sorted(ekipe_tocke.items(), key=lambda x: x[1]['tocke'], reverse=True):
            print(f"{ekipa}: {statistika['tocke']} tock, "
                  f"{statistika['zmage']} zmag, "
                  f"{statistika['stopnicke']} uvrstitev na stopnicke, "
                  f"{statistika['najhitrejsi_krogi']} najhitrejsih krogov")
    
    except FileNotFoundError:
        print("NAPAKA: Datoteka 'formula1_2024.csv' ne obstaja!")
    except Exception as e:
        print(f"NAPAKA: {e}")


if __name__ == "__main__":
    main()
