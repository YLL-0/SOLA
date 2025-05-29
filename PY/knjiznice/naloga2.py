import matplotlib.pyplot as plt

vozila = [
    "motorna kolesa",
    "osebni avtomobil",
    "avtobus",
    "tovornjak",
    "traktor",
]
stevilo = [133000, 1313000, 3700, 124000, 114000]
barve = ["orange", "blue", "green", "red", "purple"]

plt.bar(vozila, stevilo, color=barve)

plt.xlabel("Vrsta vozila")
plt.ylabel("Število registriranih")
plt.title("Registrirana vozila v Sloveniji (2024)")
plt.xticks(rotation=15)
plt.show()
