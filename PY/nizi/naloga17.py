niz = "zgodovina"
samoglasniki = "AEIOUaeiou"
count = 0
for i in niz:
    for j in samoglasniki:
        if i == j:
            count += 1

print(count)
