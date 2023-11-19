"""
UnreliableCar class
Prac09 CP1404
Estimated: 20 minutes
Actual: 35 minutes
"""
import random

from car import Car


class UnreliableCar(Car):
    """Represent an UnreliableCar object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car if it passes reliability threshold."""
        reliability_threshold = random.randint(1, 100)
        if self.reliability > reliability_threshold:
            super().drive(distance)
        else:
            return 0
