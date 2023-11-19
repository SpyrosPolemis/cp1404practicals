"""
Band class for CP1404
Estimated: 30 mins
Actual:
"""


class Band:
    """Represent band object."""

    def __init__(self, name: str):
        """Initialise band object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of band object."""
        return f"{self.name} {', '.join(str(musician) for musician in self.musicians)}"

    def add(self, musician):
        """Add musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Play a song for each musician in band."""
        for musician in self.musicians:
            print(musician.play())
