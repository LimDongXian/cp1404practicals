class ProgrammingLanguage:
    """Represents a programming language with specific attributes, including
    its name, typing system, reflection capability, and year of introduction."""
    def __init__(self, name, typing, reflection, year):
        """Initializes a new instance of the ProgrammingLanguage class."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Checks if the programming language uses dynamic typing."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string representation of the programming language"""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}")
