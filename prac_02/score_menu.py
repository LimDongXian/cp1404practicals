MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            print(f"")
        elif choice == "P":
            print(f"")
        elif choice == "S":
            print(f"")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")



main()
