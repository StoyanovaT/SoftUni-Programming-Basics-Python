meters = float(input())
unit_input = str(input())
unit_output = str(input())

if unit_input == 'm':
    number = meters
elif unit_input == 'cm':
    number = meters / 100
elif unit_input == 'mm':
    number = meters / 1000

if unit_output == 'm':
    number_output = number
elif unit_output == 'cm':
    number_output = number * 100
elif unit_output == 'mm':
    number_output = number * 1000

print(f"{number_output:.3f}")