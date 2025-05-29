# ne urejeni, neindeksirani i nni podvojenih vrednosti
kava = {"bela", "kratak", "dolga", "ledena"}
print(kava)
print(len(kava))

for i in kava:
    print(i)
kava.add("irska")

kava.remove("irska")
kava.discard("irksa")
x = kava.pop()

kava.clear()
del kava
