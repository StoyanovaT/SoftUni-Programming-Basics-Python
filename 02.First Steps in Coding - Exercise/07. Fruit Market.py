strawberries_price_lv = float(input())
bananas_quantity_kg = float(input())
oranges_quantity_kg = float(input())
raspberries_quantity_kg = float(input())
strawberries_quantity_kg = float(input())
raspberries_price_lv = strawberries_price_lv / 2
oranges_price_lv = raspberries_price_lv - (0.4 * raspberries_price_lv)
bananas_price_lv = raspberries_price_lv - (0.8 * raspberries_price_lv)
tot_raspberries_price = raspberries_price_lv * raspberries_quantity_kg
tot_oranges_price = oranges_price_lv * oranges_quantity_kg
tot_bananas_price = bananas_price_lv * bananas_quantity_kg
tot_strawberries_price = strawberries_price_lv * strawberries_quantity_kg
tot_money_spent = tot_strawberries_price + tot_bananas_price + tot_raspberries_price + tot_oranges_price
print(tot_money_spent)