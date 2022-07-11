trip_price = float(input())
quantity_saws = int(input())
quantity_dolls = int(input())
quantity_teddy_bears = int(input())
quantity_minions = int(input())
quantity_trucks = int(input())
sum_of_order = quantity_saws * 2.60 + quantity_dolls * 3 + quantity_teddy_bears * 4.10 + quantity_minions * 8.20 + \
               quantity_trucks * 2
quantity_of_toys_ordered = quantity_saws + quantity_dolls + quantity_teddy_bears + quantity_minions + quantity_trucks
if quantity_of_toys_ordered >= 50:
    discount = sum_of_order * 0.25
else:
    discount = 0
total_order_lv = sum_of_order - discount
rent = total_order_lv * 0.10
profit = total_order_lv - rent
if profit >= trip_price:
    money_left = profit - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    short_money = trip_price - profit
    print(f"Not enough money! {short_money:.2f} lv needed.")
