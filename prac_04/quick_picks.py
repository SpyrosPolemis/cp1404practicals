"""

"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
random_numbers = []
for i in range(number_of_quick_picks):
    for j in range(6):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in random_numbers:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        random_numbers.append(random_number)
    random_numbers.sort()
    for number in random_numbers:
        print(number, end=" ")
    print()
    random_numbers = []
