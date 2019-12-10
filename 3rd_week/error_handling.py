# ex 1.2 syntax errors
# myfunction(x, y):
#     return x + y
# else:
#     print("Hello!")
# if is missing

# if mark >= 50
#     print("You passed!")
#  : after 50 is missing

# if arriving:
#     print("Hi!")
# esle:
#     print("Bye!")
#  else is wrote wrong

# if flag:
# print("Flag is set!")
# missing the identation


# ex 1.2 runtime errors

# dividend = float(input("Please enter the dividend: "))
# divisor = float(input("Please enter the divisor: "))
# quotient = dividend / divisor
# quotient_rounded = math.round(quotient)
# (math. it's unnecessary in the code :
# quotient_rounded = round(quotient))


# ex 1.3 runtime errors

# for x in range(a, b):
#     print("(%f, %f, %f)" % my_list[x])
# a, b, my_list not defined


# ex 1.4 logic errors
# product = 0
# for i in range(10):
#     product *= i
# product * i remains 0

# sum_squares = 0
# for i in range(10):
#     i_sq = i**2
# sum_squares += i_sq
# it's adding only the last square because it's not indented in the loop


# nums = 0
# for num in range(10):
#     num += num
# wrong usage of variable
