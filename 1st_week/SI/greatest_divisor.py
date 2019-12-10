num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
list_num1 = []
list_num2 = []
divisors = []

for i in range(1, num1+1):
    if num1 % i == 0:
        list_num1.append(i)

for i in range(1, num2+1):
    if num2 % i == 0:
        list_num2.append(i)

print(list_num1)
print(list_num2)

for i in list_num1:
    for j in list_num2:
        if i == j:
            divisors.append(i)
print(divisors[-1:])
