"""Program to write evaluation of random scores to text file"""

from score import evaluate_score
from random import randint


def main():
    """"""
    number_of_scores = int(input("How many scores? "))
    out_file = open("results.txt", "w")
    for i in range(number_of_scores):
        random_score = randint(1, 100)
        print(f"{random_score} is {evaluate_score(random_score)}", file=out_file)
    out_file.close()


main()
