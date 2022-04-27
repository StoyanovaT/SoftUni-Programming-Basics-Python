text = input()
tot_sum = 0
for char in text:
    if char == "a":
        tot_sum += 1
    elif char == "e":
        tot_sum += 2
    elif char == "i":
        tot_sum += 3
    elif char == "o":
        tot_sum += 4
    elif char == "u":
        tot_sum += 5

print(tot_sum)