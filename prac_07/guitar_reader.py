"""
Guitar reader program - Reads guitar info from file, then makes Guitar object with each of them and prints them

Estimate: 30
Actual:
"""
from guitar import Guitar


def main():
    """Get guitars from file, ask user for their guitars then print guitars and save them to file."""
    guitars = load_guitars_from_file()
    add_user_guitars(guitars)
    print_guitars(guitars)
    save_guitars_to_file(guitars)


def load_guitars_from_file():
    """Load guitars from file into Guitar objects in as a list sorted by year."""
    guitars = []
    with open("guitars.csv") as in_file:
        for line in in_file:
            guitar = line.strip().split(",")
            guitar = Guitar(guitar[0], guitar[1], guitar[2])
            guitars.append(guitar)
        guitars.sort()
    return guitars


def add_user_guitars(guitars):
    """Add user's guitars to guitars list."""
    print("Add your guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = input("Cost: ")
        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        guitar_name = input("Name: ")


def print_guitars(guitars):
    """Print all guitars."""
    for guitar in guitars:
        print(guitar)


def save_guitars_to_file(guitars):
    """Save list of guitars to file."""
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(repr(guitar), file=out_file)


if __name__ == '__main__':
    main()
