numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

minimum = numbers[0]
maximum = numbers[0]
sum_of_numbers = 0

for number in numbers:
    if minimum > number:
        minimum = number

for number in numbers:
    if maximum < number:
        maximum = number

for number in numbers:
    sum_of_numbers += number
average = sum_of_numbers // len(numbers)


print(minimum)
print(maximum)
print(average)
