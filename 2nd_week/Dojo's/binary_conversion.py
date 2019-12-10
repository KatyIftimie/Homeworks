number, base = input("Enter a number and the base separated by a single space: ").split()


def converter(number, base):
    if base == 10:
        binary = ""
        while number > 0:
            x = number // 2
            binary += str(number % 2)
            number = x
        # print(binary[::-1])
        binary = ("0" * (16 - int(len(binary))) + binary[::-1])
        return binary
    elif base == 2:
        power = 0
        power_list = []
        len_number = len(str(number))
        i = 0
        while i < len_number:
            power_list.append(2**power)
            power += 1
            i += 1
        power_list.reverse()
        decimals_list = list(str(number))
        decimal = 0
        counter = 0
        while counter < len(decimals_list):
            if decimals_list[counter] == "1":
                decimal += power_list[counter]
            counter += 1
        return decimal
    

print(converter(int(number), int(base)))
