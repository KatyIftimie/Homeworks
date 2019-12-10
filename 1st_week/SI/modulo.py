result = []

for multiple in range(100, 1000):
    if multiple % 7 == 0 or multiple % 9 == 0:
        result.append(multiple)

for i in result[-25:]:
    print(i)
