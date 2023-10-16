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

from operator import itemgetter


def main():
    """Read match history from file and print winning players and countries."""
    filename = "wimbledon.csv"
    # filename = input("Enter filename: ")
    match_results = format_match_results(filename)
    winning_players = count_player_wins(match_results)
    winning_countries = derive_winning_countries(match_results)
    # Print winning players
    print("Wimbledon Champions:")
    for winning_player in winning_players:
        print(f"{winning_player[0]} {winning_player[1]}")
    # Print winning countries
    print("These twelve countries have won Wimbledon:")
    print(*winning_countries, sep=", ")


def derive_winning_countries(match_results):
    """Derive the winning countries from match history."""
    countries = []
    for match_result in match_results:
        countries.append(match_result[1])
    countries = set(countries)
    return countries


def count_player_wins(match_results):
    """Count how many times each player won the finals."""
    player_to_number_of_wins = {}
    for match_result in match_results:
        if match_result[2] in player_to_number_of_wins:
            player_to_number_of_wins[match_result[2]] += 1
        else:
            player_to_number_of_wins[match_result[2]] = 1
    winning_players = list(player_to_number_of_wins.items())
    winning_players.sort(key=itemgetter(1), reverse=True)
    return winning_players


def format_match_results(filename):
    """Format match results into a list of lists to improve utility of data."""
    match_results = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            match_results.append(parts)
            # line = line[5:line.find(',', line.find(',', line.find(',') + 1) + 1)]  # for future generations to see
    return match_results
    # returns in format: [["1968", "AUS", "Federer", etc.], ["1969", "FRA", "Spyros", etc.]]


main()
