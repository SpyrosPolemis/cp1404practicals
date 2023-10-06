"""
List-exercises program
"""

NUMBER_OF_NUMBERS = 5

numbers = []
for i in range(NUMBER_OF_NUMBERS):
    number = int(input("Number: "))
    numbers.append(number)
print(numbers[0])
print(numbers[-1])
print(min(numbers))
print(max(numbers))
print(sum(numbers) / NUMBER_OF_NUMBERS)
