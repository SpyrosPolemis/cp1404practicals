def question_1():
    name = input("Your name is: ")
    with open("name.txt", "w") as out_file:
        print(name, file=out_file)

question_1()
