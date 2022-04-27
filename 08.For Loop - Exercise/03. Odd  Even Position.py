import sys

number_of_range = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, number_of_range + 1):
    current_number = float(input())
    if i % 2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number

print(f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize:
    odd_min = "No"
    print(f"OddMin={odd_min},")
else:
    print(f"OddMin={odd_min:.2f},")

if odd_max == -sys.maxsize:
    odd_max = "No"
    print(f"OddMax={odd_max},")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    even_min = "No"
    print(f"EvenMin={even_min},")
else:
    print(f"EvenMin={even_min:.2f},")

if even_max == -sys.maxsize:
    even_max = "No"
    print(f"EvenMax={even_max}")
else:
    print(f"EvenMax={even_max:.2f}")
