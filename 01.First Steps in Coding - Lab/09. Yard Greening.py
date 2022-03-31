square_meters = float(input())
price_before_discout = square_meters * 7.61
discount = price_before_discout * 0.18
price_after_discount = price_before_discout - discount
print(f"The final price is: {price_after_discount} lv.")
print(f"The discount is: {discount} lv.")