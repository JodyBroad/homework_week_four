import random

lotto_numbers = []
# number_1 = random.randint(1, 50)
# print(number_1)
#
# lotto_numbers.append(number_1)
# print(lotto_numbers)

for i in range(0, 6):
    number = random.randint(1, 50)
    # to get rid of duplicates
    while number in lotto_numbers:
        number = random.randint(1, 50)
        # if it isn't already on the list, we now add it to the list with append
    lotto_numbers.append(number)
print(lotto_numbers)

#list numbers sorted
lotto_numbers_sorted = sorted(lotto_numbers)
print("This week's lottery numbers are: ", lotto_numbers_sorted)
