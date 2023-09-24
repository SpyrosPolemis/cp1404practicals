""""""

from score import evaluate_score

MENU = """(G)et
(P)rint
(S)how
(Q)uit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()  # Could use a function but eh
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"{score} is {evaluate_score(score)}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice.")
        choice = input(">>> ").upper()


def get_valid_score():
    score = int(input("Enter a score (1-100): "))
    while score < 1 or score > 100:
        print("Invalid score.")
        score = int(input("Enter a score (1-100): "))
    return score


main()
