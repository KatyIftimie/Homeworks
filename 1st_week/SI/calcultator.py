def verify():
    if operator == "+":
        result = int(number_1) + int(number_2)
    elif operator == "-":
        result = int(number_1) - int(number_2)
    elif operator == "*":
        result = int(number_1) * int(number_2)
    elif operator == "/":
        result = int(number_1) / int(number_2)
    return result


while True:
    number_1 = input("Enter first number: ")
    while str(number_1) not in ("0123456789"):
        print("Wrong input.")
        number_1 = input("Enter first number: ")

    operator = input("Please choose an operation : + , - , * , /  ")
    while operator not in ("+-*/"):
        print("Wrong input.")
        operator = input("Please choose an operation : + , - , * , /  ")

    number_2 = input("Enter second number: ")
    while str(number_2) not in ("0123456789"):
        print("Wrong input.")
        number_2 = input("Enter second number: ")
    print(verify())
