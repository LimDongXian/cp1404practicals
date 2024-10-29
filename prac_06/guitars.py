from prac_06.guitar import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))  # for test purpose only
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))  # for test purpose only
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))  # for test purpose only

print("Mu guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "added.\n")
    name = input("Name: ")

print("\n...snip...\n")
print("These are my guitars:")

name_width = max(len(guitar.name) for guitar in guitars)
cost_width = max(len(str(guitar.cost)) for guitar in guitars) + 1  # Add one for the float .00

for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    print(
        f"Guitar {i}: {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:>{cost_width}.2f}{vintage_string}")
