user_number = int(input("Enter an arabic number(1 - 3999):  "))


roman_converter = dict(M=1000, CM=900, D=500, CD=400, C=100, XC=90,
                          L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)


def roman_num(user_number):
    result = ""
    # global user_number
    base_sorted_numbers = sorted(roman_converter.items(), key=lambda x: x[1], reverse=True)
    for rnumber, number in base_sorted_numbers:
        count = int(user_number / number)
        result += rnumber * count
        user_number -= count * number
    return result


def main():
    if (user_number > 0) and (user_number <= 3999):
        print(roman_num(user_number))
    else:
        raise ValueError('Your number is out of range. ')


if __name__ == "__main__":
    main()
