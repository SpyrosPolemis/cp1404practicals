from random import randint

out_file = open("temps_input.txt", "w")
for i in range(0, 15):
    print(randint(-200, 200), file=out_file)
