from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", "1923", 10000)
other_guitar = Guitar("NoiseMaker4000", 2013, 10)

print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
print(f"{other_guitar.name} get_age() - Expected 10. Got {other_guitar.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{other_guitar.name} is_vintage() - Expected False. Got {other_guitar.is_vintage()}")
