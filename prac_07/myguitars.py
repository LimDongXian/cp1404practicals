from prac_07.guitar import Guitar


def main():
    guitars = load_file()
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added.\n")
        name = input("Name: ")
    guitars.sort()  # sort by year as the Guitar class coded
    print("\n...snip...\n")
    print("These are my guitars:")
    display_guitars(guitars)


def load_file():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


main()
