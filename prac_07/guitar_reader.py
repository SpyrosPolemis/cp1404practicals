"""
Guitar reader program - Reads guitar info from file, then makes Guitar object with each of them and prints them

Estimate: 30
Actual:
"""
from guitar import Guitar


def main():
    """"""
    guitars = load_guitars_from_file()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars_from_file():
    """Load guitars from file into Guitar objects in as a list."""
    guitars = []
    with open("guitars.csv") as in_file:
        for line in in_file:
            guitar = line.strip().split(",")
            guitar = Guitar(guitar[0], guitar[1], guitar[2])
            guitars.append(guitar)
    return guitars


if __name__ == '__main__':
    main()
