glasovi = ["Janez", "Miha", "Janez", "Ana", "Miha", "Janez", "Ana", "Ana"]

# Napišimo program, ki bo sprejel glasove in izračunal skupno
# število glasov za vsakega kandidata ter nato izpisal rezultate v obliki
# slovarja, kjer so ključi imena kandidatov, vrednosti pa skupno število
# prejetih glasov.
st_glasov = []

for glas in glasovi:
    st_glasov.append(glasovi.count(glas))
    print(glasovi.count(glas))

seznam = {}

i = 0
while i < len(glasovi):
    seznam[glasovi[i]] = st_glasov[i]
    i = i + 1
print(seznam)
