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
    years = process_file(filename)
    print(years)


def process_file(filename):
    years = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            # line = line[5:line.find(',', line.find(',', line.find(',') + 1) + 1)]  # for future generations to see
            years.append(line.split(","))
    return years


main()
