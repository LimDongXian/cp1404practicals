from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
guitar = Guitar(name, year, cost)
print(guitar)
print(guitar.get_age())  # Expected  102 got 102
print(guitar.is_vintage())  # Expected True got True

name = "Another_Guitar"
year = 2000
cost = 12345.67
guitar = Guitar(name, year, cost)
print(guitar)
print(guitar.get_age())  # Expected  24 got 24
print(guitar.is_vintage())  # Expected False got False
