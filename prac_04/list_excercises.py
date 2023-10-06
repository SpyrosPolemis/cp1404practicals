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

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access granted.")
else:
    print("Access denied")
