import matplotlib.pyplot as plt

# Podatki o številu živali na kmetiji
zivali = ["mačke", "pujsi", "krave", "konji", "psi"]
stevilo = [3, 5, 4, 1, 2]  # Število posameznih živali

# Barve za posamezne kategorije (prilagojene podobno kot na vzorčni sliki)
barve = ["#3080c8", "#ff8b22", "#4ca62e", "#dd3333", "#a667bf"]

# Ustvarjanje tortnega diagrama
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    stevilo, labels=None, colors=barve, autopct="%1.1f%%", startangle=90
)

# Dodajanje naslova
plt.title("Število živali na kmetiji", fontsize=16, fontweight="bold")

# Dodajanje legende
plt.legend(
    wedges,
    [f"{z} - {s}" for z, s in zip(zivali, stevilo)],
    title="Živali na kmetiji",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
)

# Zagotovitev, da se tortni diagram izriše kot krog
plt.axis("equal")

# Prilagoditev postavitve, da bo dovolj prostora za legendo
plt.tight_layout()

# Prikaz diagrama
plt.show()
