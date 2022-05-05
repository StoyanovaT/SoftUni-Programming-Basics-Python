contribution = input()

bank_account_total = 0

while contribution != "NoMoreMoney":
    if float(contribution) > 0:
        print(f"Increase: {float(contribution):.2f}")
    if float(contribution) < 0:
        print("Invalid operation!")
        break
    bank_account_total += float(contribution)
    contribution = input()
print(f"Total: {bank_account_total:.2f}")

# Решение на лектора:
# # повтаряме:
# # 1. четем сума
# # 2. проверка < 0
# # 3. > 0 -> отпечатваме
# # 4. добавяме сумата към сметката
#
# # стоп: команда == "NoMoreMoney"
# # продължаваме: команда != "NoMoreMoney"
# total_amount = 0
# # команда => число под формата на текст('5.51') или "NoMoreMoney"
# command = input()
#
# while command != "NoMoreMoney":
#     #command = '5.51'
#     # число под формата на текст '5.51' -> число
#     sum = float(command) #сума за внасяне
#     if sum < 0:
#         print('Invalid operation!')
#         break
#
#     print(f"Increase: {sum:.2f}")
#     total_amount += sum
#     command = input()
#
# print(f"Total: {total_amount:.2f}")