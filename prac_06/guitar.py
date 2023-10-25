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
        return f"{self.name}, ({self.year}) : ${self.cost:,}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() > 50
