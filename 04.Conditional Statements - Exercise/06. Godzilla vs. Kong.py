budget_movie = float(input())
number_extras = int(input())
price_clothes_for_1 = float(input())
decor_price = budget_movie * 0.10
all_clothes_price = number_extras * price_clothes_for_1
if number_extras > 150:
    all_clothes_price = all_clothes_price * 0.90

total_expenses = all_clothes_price + decor_price

if budget_movie < total_expenses:
    money_short = total_expenses - budget_movie
    print(f"Not enough money!")
    print(f"Wingard needs {money_short:.2f} leva more.")
else:
    money_left = budget_movie - total_expenses
    print(f"Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
