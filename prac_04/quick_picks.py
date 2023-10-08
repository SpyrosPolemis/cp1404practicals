"""

"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))
quick_pick = []  # doesn't really sound like a list but random_numbers etc. also feels wrong
for i in range(number_of_quick_picks):
    for j in range(NUMBERS_PER_LINE):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in quick_pick:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(random_number)
    quick_pick.sort()
    for number in quick_pick:
        print(f"{number:2}", end=" ")
    print()
    quick_pick = []
