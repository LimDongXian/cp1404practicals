class Band:
    """Band class for managing a group of musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a Musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician and their first instrument (or that they need one)."""
        players = []
        for musician in self.musicians:
            players.append(musician.play())
        return "\n".join(players)