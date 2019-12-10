doors = [False] * 100
result = ""
for i in range(100):
    for j in range(i, 100, i+1):
        doors[j] = not doors[j]
    if doors[j]:
        result += (str(i+1) + ", ")
print("Folowing doors are open: " + result)
