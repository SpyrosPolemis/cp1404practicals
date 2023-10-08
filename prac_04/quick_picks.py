"""

"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))
random_numbers = []
for i in range(number_of_quick_picks):
    for j in range(NUMBERS_PER_LINE):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in random_numbers:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        random_numbers.append(random_number)
    random_numbers.sort()
    for number in random_numbers:
        print(f"{number:2}", end=" ")
    print()
    random_numbers = []
