vsota = 0
for i in range(0, 31, 2):
    vsota += i
print(vsota)

count = 0
for i in range(100, 1000):
    x = str(i)
    x1 = int(x[0])
    x2 = int(x[1])
    x3 = int(x[2])
    count = x1 + x2 + x3
    if count < 11:
        print(f"{i}: {count}")
    if count % 2 != 0:
        print(f"Liha: {i}: {count}")
    count = 0

for i in range(100, 200, 17):
    count += i
print(count)
