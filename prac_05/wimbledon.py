"""
Game, set, match!
Estimated: 40 mins
Actual: Too long, too long.

get filename
with in_file
    read first line of in_file
    process_file_in_good_format
    find_champs
    find_countries
"""


def main():
    """ """
    filename = "wimbledon.csv"
    records = process_file(filename)
    print_champions(records)
    print_countries(records)


def print_countries(records):
    countries = []
    for record in records:
        countries.append(record[1])
    countries = set(countries)
    print("These twelve countries have won Wimbledon:")
    print(countries)


def print_champions(records):
    player_to_number_of_wins = {}
    for record in records:
        if record[2] in player_to_number_of_wins:
            player_to_number_of_wins[record[2]] += 1
        else:
            player_to_number_of_wins[record[2]] = 1
    print("Wimbledon Champions:")
    for player, number_of_wins in player_to_number_of_wins.items():
        print(f"{player} {number_of_wins}")


def process_file(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            # line = line[5:line.find(',', line.find(',', line.find(',') + 1) + 1)]  # for future generations to see
            records.append(line.split(","))
    return records


main()
