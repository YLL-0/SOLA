pretekli_mesec = {"avto", "kocke", "barbike", "zoga"}
ta_mesec = {"kocke", "zoga", "puzzle", "plisasti medvedek"}
print("Prejsni mesec: ", pretekli_mesec)
print("Ta mesec: ", ta_mesec)
#

# print(ta_mesec.symmetric_difference(pretekli_mesec))
print(pretekli_mesec - ta_mesec)
print(ta_mesec - pretekli_mesec)
ponavljajoce = pretekli_mesec.intersection(ta_mesec)
print(ponavljajoce)

skupno = ta_mesec.union(pretekli_mesec)
print(skupno)
count = 0
for i in skupno:
    count += 1
print(count)
