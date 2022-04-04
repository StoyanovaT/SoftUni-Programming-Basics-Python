num_of_days = int(input())
num_of_bakers = int(input())
num_of_cakes = int(input())
num_of_waffles = int(input())
num_of_pancakes = int(input())
cake_price = 45
waffle_price = 5.80
pancake_price = 3.20
cakes = num_of_cakes * cake_price
waffles = num_of_waffles * waffle_price
pancakes = num_of_pancakes * pancake_price
sum_for_a_day = (cakes + waffles + pancakes) * num_of_bakers
tot_sum_gained = (sum_for_a_day * num_of_days) - ((sum_for_a_day * num_of_days) / 8)
print(tot_sum_gained)
