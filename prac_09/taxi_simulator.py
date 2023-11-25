"""
Taxi simulator program for CP1404
Estimated: 60 minutes
Actual: 35 minutes
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program that lets users drive with different taxis and calculates their bill."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0
    print("Lets drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            print_taxis(taxis)
            selected_taxi_index = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[selected_taxi_index]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                total_bill = drive_taxi(current_taxi, total_bill)
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now: ")
    print_taxis(taxis)


def drive_taxi(current_taxi, total_bill):
    current_taxi.start_fare()
    distance_to_drive = float(input("Drive how far? "))
    current_taxi.drive(distance_to_drive)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    total_bill += trip_cost
    return total_bill


def print_taxis(taxis):
    """Print taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
