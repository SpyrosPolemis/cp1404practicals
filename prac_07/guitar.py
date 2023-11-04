"""Guitar class for cp1404 prac_06"""

CURRENT_YEAR = 2023


class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Return string representation of Guitar object."""
        return f"{self.name}, ({self.year}) : ${self.cost:,}"

    def __repr__(self):
        """Return string representation of object that can be used to recreate it."""
        return f"{self.name},{self.year},{self.cost}"

    def __lt__(self, other):
        """Compare if a guitar is less than another using its year."""
        return self.year < other.year

    def get_age(self):
        """Get age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True or False based on weather guitar is vitange (50 years)."""
        return self.get_age() > 50
