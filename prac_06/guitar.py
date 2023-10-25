"""Guitar class for cp1404 prac_06"""


class Guitar:
    """Represent a guitar object"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}) : ${self.cost:,}"

