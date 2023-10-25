"""ProgrammingLanguage class for CP1404 prac week_06"""


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"
