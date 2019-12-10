i = 0
j = 1
k = 0
fib = 0
user_input = int(input("Enter how many fibonacci numbers do you want to print: "))


def fibonacci_sequence(i, j, k, fib, user_input):
    while i < user_input:
        fib = j + k
        j = k
        k = fib
        i += 1
        print(i, " " * (20 - len(str(i)) - len(str(fib))), fib)


fibonacci_sequence(i, j, k, fib, user_input)
