"""
Game, set, match!
Estimated: 40 mins
Actual:

for line in file
    we want tooo
    keep track of how many times each player appears (dict)
    each country (set)
"""


def main():
    # filename = input("Enter filename: ")
    filename = "wimbledon.csv"
    player_to_number_of_wins = {}
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        player_information = in_file.readlines()
        print(player_information)

main()
