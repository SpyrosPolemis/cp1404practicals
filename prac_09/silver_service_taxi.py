"""
SilverServiceTaxi subclass of Taxi
Prac09 CP1404
Estimated: 35 mins
Actual:
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes increased fare costs."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return string representation of SilverServiceTaxi object."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"
