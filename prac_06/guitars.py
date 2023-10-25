"""
Estimated: 50 minutes
Actual:
"""

from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    guitar_name = "f"
    while guitar_name != "":
        guitar_name = input("Name: ")
        guitar_year = input("Year: ")
        guitar_cost = input("Cost: ")
        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")



main()
