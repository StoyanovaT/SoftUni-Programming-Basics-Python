lenght_sm = int(input())
width_sm = int(input())
height_sm = int(input())
percent_non_usable_volume = float(input())
volume_sm3 = lenght_sm * width_sm * height_sm
volume_dm3_litre = volume_sm3 / 1000
percent_non_usable_volume = percent_non_usable_volume * 0.01
actual_litres_in_tank = volume_dm3_litre * (1-percent_non_usable_volume)
print(actual_litres_in_tank)