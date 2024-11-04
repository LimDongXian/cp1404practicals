CURRENT_YEAR = 2024


class Guitar:
    """
    Represents a guitar with specific attributes, including its name, year of manufacture,
    and cost.
    """
    def __init__(self, name="", year=0, cost=0):
        """Initializes a new instance of the Guitar class."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of the guitar, showing its name, year, and cost."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Returns true if the guitar is less than the other guitar."""
        return self.year < other.year

    def get_age(self):
        """Calculates the age of the guitar based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines if the guitar is considered vintage (older than 50 years)."""
        return Guitar.get_age(self) > 50
