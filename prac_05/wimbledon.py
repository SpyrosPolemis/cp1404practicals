"""
Game, set, match!
Estimated: 40 mins
Actual: At least 18 minutes

for line in file
    we want tooo
    keep track of how many times each player appears (dict)
    each country (set)
"""


def main():
    # filename = input("Enter filename: ")
    filename = "wimbledon.csv"
    player_info = []
    player_to_number_of_wins = {}
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            # line.strip()  # not needed?
            parts = line.split(" ")
            player_info.append(parts)



main()
