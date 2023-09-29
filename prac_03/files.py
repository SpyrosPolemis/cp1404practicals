def question_1():
    name = input("Your name is: ")
    with open("name.txt", "w") as out_file:
        print(name, file=out_file)


def question_2():
    with open("name.txt") as in_file:
        name = in_file.read()
        print(f"Your name is {name}")


question_1()
question_2()
