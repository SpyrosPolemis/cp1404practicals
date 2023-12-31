"""
Estimated: 50 minutes
Actual: 60 minutes
"""

from guitar import Guitar


def main():
    """"""
    guitars = get_guitars()
    print_guitars(guitars)


def print_guitars(guitars):
    """Print all user's guitars."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:,.2f}"
              f"{' (vintage)' if guitar.is_vintage() else ''}")


def get_guitars():
    """Get guitars from user until they enter blank string."""
    guitars = []
    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = input("Cost: ")
        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        guitar_name = input("Name: ")
    return guitars


def test_print_guitars(guitars):
    """Test print guitars function."""
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print_guitars(guitars)


# test_print_guitars([])
main()
