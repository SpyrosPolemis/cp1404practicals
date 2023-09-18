"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.10
        # bonus = 0.1 * sales
    else:
        bonus_rate = 0.15
    bonus = sales * bonus_rate
    print(f"The bonus for ${sales:.2f} in sales is ${bonus:.2f}.")
    sales = float(input("Enter sales: $"))


# sales = float(input("Enter sales: $"))
# number_of_sales = 0
# total_bonus = 0
# while sales >= 0:
#
#     # Calculate bonus rate
#     if sales < 1000:
#         bonus_rate = 0.10
#     else:
#         bonus_rate = 0.15
#     bonus = sales * bonus_rate
#
#     # Track total bonus and number of sales
#     total_bonus += bonus
#     number_of_sales += 1
#
#     print(f"The bonus for ${sales:.2f} in sales is ${bonus:.2f}.")
#     sales = float(input("Enter sales: $"))
#
# print(f"The total bonus for your {number_of_sales} sales is {total_bonus}")
