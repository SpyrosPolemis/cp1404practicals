# DISCOUNT_RATE = 0.1
#
# get number_of_items
# for number_of_items
#     get item_price
#     total_price += item_price
# if total_price > 100
#     total_price = total_price - total_price * discount_rate
# print total_price

DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for items in range(number_of_items):
    item_price = float(input(f"Price of item {items + 1}: "))  # The {items + 1} kinda smells
    total_price += item_price
if total_price > 100:
    total_price = total_price - total_price * DISCOUNT_RATE
print(f"The total price for {number_of_items} items is ${total_price:.2f}")
