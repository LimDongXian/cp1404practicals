from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            print("Choose")
        elif choice == "d":
            print("Drive")
        else:
            print("Invalid option")
        print(MENU)  # loop start here for every choice done
        choice = input(">>> ").lower()

    print("Total trip cost: $682.60")
    print("Taxis are now:")

main()