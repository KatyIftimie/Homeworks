user_input = input("Enter your name ")


def verifing_input():
    greeting = ""
    if user_input == "":
        greeting = "Hello word!"
    else:
        greeting = "Hello " + user_input
    return greeting


print(verifing_input())
