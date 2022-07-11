number = int(input())

sum_numbers = 0

while number != sum_numbers:
    if number <= sum_numbers:
        break
    new_number = int(input())
    sum_numbers += new_number

print(sum_numbers)

# max_sum = int(input())
#
# # повтаряме: четене на цяло число, добавяме към сумата
# # стоп: сума >= max_sum
# # продължаваме: сума < max_sum
#
# sum = 0 # сумата на числата
#
# while sum < max_sum:
#     number = int(input())
#     sum += number
# # sum >= max_sum
# print(sum)