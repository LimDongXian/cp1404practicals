NAME_TO_CODE = {"Aqua": "#00ffff", "Bittersweet": "#fe6f5e", "Canary": "#ffff99", "Denim": "#1560bd", "Emerald": "#50c878",
                "Feldgrau": "#4d5d53", "Ginger": "#b06500", "Heliotrope": "#df73ff", "Iceberg": "#71a6d2", "Jasmine": "#f8de7e", }

for name, code in NAME_TO_CODE.items():
    print(f"{name:11} is {code}")


colour_name = input("Enter name of the colour: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter name of the colour: ").title()