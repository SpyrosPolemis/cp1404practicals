"""Project class for CP1404 prac_07"""

class Project:
    """Represent a project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)


    def __str__(self):
        """Return string representation of Project instance."""
        return f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"




