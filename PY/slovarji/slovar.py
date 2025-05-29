avto = {
    "znamka": "BMW",
    "model": "M5",
    "leto": "2015",
    "barva": ["crna", "bela", "rumena"],
}
print(len(avto))

x = avto["znamka"]
y = avto.get("znamka")
print(x, y)

z = avto.keys()
print(z)
avto["oblika"] = "limuzina"
print(avto.keys())

print(avto.values())
