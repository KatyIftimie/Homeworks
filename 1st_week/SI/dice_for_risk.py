import random


# for i in range(4):

attacker_input = input("How many dice you want to roll?(max 3) ")
while int(attacker_input) not in range(1, 4):
    print("Invalid input.")
    attacker_input = input("How many dice you want to roll?(max 3) ")

defender_input = input("How many dice you want to roll?(max 2) ")
while int(defender_input) not in range(1, 3):
    print("Invalid input.")
    defender_input = input("How many dice you want to roll?(max 2) ")
print("")
atta_list = []
def_list = []


counter = 0
counter_2 = 0

while counter < int(attacker_input):
    dice = random.randint(1, 6)
    atta_list.append(dice)
    counter += 1
atta_list = sorted(atta_list, reverse=True)
for i in atta_list:
    print(i, end=" ")
print("")

while counter_2 < int(defender_input):
    dice = random.randint(1, 6)
    def_list.append(dice)
    counter_2 += 1
def_list = sorted(def_list, reverse=True)
for i in def_list:
    print(i, end=" ")
print("")
print("")

if (len(atta_list) == 1) or (len(def_list) == 1):
    if atta_list[0] > def_list[0]:
        print("Defender lost 1 unit")
    else:
        print("Attacker lost 1 unit")

if (len(atta_list) > 1) and (len(def_list) > 1):
    atta_counter = 0
    def_counter = 0

    if atta_list[0] <= def_list[0]:
        atta_counter += 1
    if atta_list[1] <= def_list[1]:
        atta_counter += 1
    print("Attacker lost " + str(atta_counter) + " units")

    if atta_list[0] > def_list[0]:
        def_counter += 1
    if atta_list[1] > def_list[1]:
        def_counter += 1
#     print("Defender lost " + str(def_counter) + " units")
    print("Defender lost " + str(def_counter) + " units")
