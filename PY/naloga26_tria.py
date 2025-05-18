tekmovalci = {
    "Ana": {"številka": 1, "plavanje": 30, "kolesarjenje": 90, "tek": 45},
    "Bine": {"številka": 2, "plavanje": 25, "kolesarjenje": 95, "tek": 50},
    "Cilka": {"številka": 3, "plavanje": 28, "kolesarjenje": 85, "tek": 48},
    "Domen": {"številka": 4, "plavanje": 33, "kolesarjenje": 88, "tek": 46},
    "Eva": {"številka": 5, "plavanje": 29, "kolesarjenje": 92, "tek": 47},
}
print("Seznam tekmovalcev:")
for ime, podatki in tekmovalci.items():
    print(
        f"{ime}: številka {podatki['številka']}, plavanje: {podatki['plavanje']} min, kolesarjenje: {podatki['kolesarjenje']} min, tek: {podatki['tek']} min"
    )

print()
# Prva naloga:
print("Prva naloga:")


def skupni_cas(podatki):
    return podatki["plavanje"] + podatki["kolesarjenje"] + podatki["tek"]


skupni_casi = {ime: skupni_cas(podatki) for ime, podatki in tekmovalci.items()}
zmagovalec = min(skupni_casi.items(), key=lambda x: x[1])

print(f"Zmagovalec: {zmagovalec[0]} s časom {zmagovalec[1]} minut")
print()
# Druga naloga:
print("Druga naloga:")

hitri_kolesarji1 = [
    ime for ime, podatki in tekmovalci.items() if podatki["kolesarjenje"] < 90
]
print("Tekmovalci s kolesarjenjem pod 90 minut:")
for ime in hitri_kolesarji1:
    print(f"{ime}: {tekmovalci[ime]['kolesarjenje']} minut")

# Z lambdo
print()
hitri_kolesarji = list(
    filter(lambda ime: tekmovalci[ime]["kolesarjenje"] < 90, tekmovalci.keys())
)

print("Tekmovalci s kolesarjenjem pod 90 minut:")
for ime in hitri_kolesarji:
    print(f"{ime}: {tekmovalci[ime]['kolesarjenje']} minut")

# Tretja naloga:
print()

slovar_plavalcev = {
    podatki_tekmovalca["številka"]: podatki_tekmovalca["plavanje"]
    for ime_tekmovalca, podatki_tekmovalca in tekmovalci.items()
}

print("Naloge 3:")
print(slovar_plavalcev)

# Za boljšo predstavo izpišimo podatke v berljivi obliki
print("\nPodatki v berljivi obliki:")
for stevilka_tekmovalca, cas_plavanja in slovar_plavalcev.items():
    print(f"Tekmovalec št. {stevilka_tekmovalca}: {cas_plavanja} minut plavanja")

# Cetrta naloga:
print()

urejeni_tekmovalci = sorted(tekmovalci.items(), key=lambda par: par[1]["tek"])

print("Seznam tekmovalcev po času teka od najhitrejšega do najpočasnejšega:")
for mesto, (ime_tekmovalca, podatki) in enumerate(urejeni_tekmovalci, 1):
    print(f"{mesto}. {ime_tekmovalca}: {podatki['tek']} minut")
