from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()  # sort by year as the Guitar class coded
    display_guitars(guitars)


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


main()
