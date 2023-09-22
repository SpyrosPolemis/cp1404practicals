"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    print(f"{score} is {evaluate_score(score)}")
    random_score = randint(1, 100)
    print(f"Random score {random_score} is {evaluate_score(random_score)}")


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
