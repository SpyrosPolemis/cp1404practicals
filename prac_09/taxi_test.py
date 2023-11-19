"""
Prac 09 CP1404
Test for taxi class
Estimate: 25 mins
Actual: 20 minutes
"""

from taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
my_taxi.drive(40)
print(my_taxi, my_taxi.get_fare())
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi, my_taxi.get_fare())