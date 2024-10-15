"""
Wimbledon
Estimate: 30 minutes
Actual:   40 minutes
"""

FILENAME = 'wimbledon.csv'


def main():
    print("Wimbledon Champions:")
    data = read_wimbledon_data()
    champion_wins = get_champion_wins(data)
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")
    print("These 12 countries have won Wimbledon:")
    countries = get_countries(data)
    print(", ".join(sorted(countries)))


def read_wimbledon_data():
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip the header
        for line in in_file:
            row = line.strip().split(",")
            data.append(row)
    return data


def get_champion_wins(data):
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return countries


main()
