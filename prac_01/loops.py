for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
for stars in range(number_of_stars):
    print("*", end="")
print()

number_of_rows = int(input("Number of rows: "))
for row in range(number_of_rows):
    for i in range(row + 1):
        print("*", end="")
    print()
