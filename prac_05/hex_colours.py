name_to_code = {"Aqua": "#00ffff", "Bittersweet": "#fe6f5e", "Canary": "#ffff99", "Denim": "#1560bd", "Emerald": "#50c878",
                "Feldgrau": "#4d5d53", "Ginger": "#b06500", "Heliotrope": "#df73ff", "Iceberg": "#71a6d2", "Jasmine": "#f8de7e", }




colour_name = input("Enter name of the colour: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", name_to_code[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter name of the colour: ").title()