"""
Game, set, match!
Estimated: 40 mins
Actual: Too long, tooo long. (2 hours? I was being silly)

get filename
with in_file
    read first line of in_file
    process_file_in_good_format
    find_champs
    find_countries
"""


def main():
    """"""
    # filename = "wimbledon.csv"
    filename = input("Enter filename: ")
    match_results = format_match_results(filename)
    player_to_number_of_wins = count_player_wins(match_results)
    country_wins = derive_winning_countries(match_results)
    # Print winning players
    print("Wimbledon Champions:")
    for player, number_of_wins in player_to_number_of_wins.items():
        print(f"{player} {number_of_wins}")
    # Print winning countries
    print("These twelve countries have won Wimbledon:")
    print(*country_wins, sep=", ")


def derive_winning_countries(match_results):
    """"""
    countries = []
    for match_result in match_results:
        countries.append(match_result[1])
    countries = set(countries)
    return countries


def count_player_wins(match_results):
    """"""
    player_to_number_of_wins = {}
    for match_result in match_results:
        if match_result[2] in player_to_number_of_wins:
            player_to_number_of_wins[match_result[2]] += 1
        else:
            player_to_number_of_wins[match_result[2]] = 1
    return player_to_number_of_wins


def format_match_results(filename):
    """"""
    match_results = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            match_results.append(parts)
            # line = line[5:line.find(',', line.find(',', line.find(',') + 1) + 1)]  # for future generations to see
    return match_results


main()
