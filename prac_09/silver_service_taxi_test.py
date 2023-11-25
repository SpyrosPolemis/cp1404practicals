from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Cool taxi", 100, 2)
my_taxi.drive(18)
print(my_taxi, my_taxi.get_fare())
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi, my_taxi.get_fare())