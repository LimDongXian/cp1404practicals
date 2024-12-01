from prac_09 import taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Loop for the taxi fare simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_price = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            try:
                choose_taxi = int(input("Choose taxi: "))
                if choose_taxi > len(taxis) - 1 or choose_taxi < 0:
                    print("Invalid taxi choice")
                else:
                    current_taxi = taxis[choose_taxi]
            except ValueError:
                print("Invalid input")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    if distance < 0:
                        print("Invalid distance")
                    else:
                        distance_travel = current_taxi.drive(distance)
                        trip_cost = current_taxi.get_fare()
                        total_price += trip_cost
                        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                        current_taxi.start_fare()  # to reset the fare, so it won't add up previous drive
                except ValueError:
                    print("Invalid input")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_price:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_price:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display a list of taxis with their details."""
    print("Taxi available: ")
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")


main()
