def question_1():
    name = input("Your name is: ")
    with open("name.txt", "w") as out_file:
        print(name, file=out_file)


def question_2():
    with open("name.txt") as in_file:
        name = in_file.read()
        print(f"Your name is {name}")


def question_3():
    with open("numbers.txt") as in_file:
        (first_number) = in_file.readline().strip()
        (second_number) = in_file.readline().strip()
        total = int(first_number) + int(second_number)
        print(total)


def question_4():
    total = 0
    with open("numbers.txt") as in_file:
        for line in in_file:
            number = int(line)
            total += number
        print(total)

question_1()
question_2()
question_3()
question_4()
