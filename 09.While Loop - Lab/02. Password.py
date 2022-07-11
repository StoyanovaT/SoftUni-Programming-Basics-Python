username = input()
password = input()
data = input()

while data != password:
    data = input()
print(f"Welcome {username}!")

# Друго решение на лектора:
# username = input()
# password = input()
#
# # повтаряме: въвеждаме парола
# # стоп: въведаната парола == password
# # продължавам: въведената парола != password
#
# while True:
#     entered_password = input()
#     if entered_password == password:
#         print(f"Welcome {username}!")
#         break


# Друго решение на лектора:
# username = input()
# password = input()
#
# # повтаряме: въвеждаме парола
# # стоп: въведаната парола == password
# # продължавам: въведената парола != password
#
# entered_password = input()
# while entered_password != password:
#     entered_password = input()
# else: # entered_password == password
#     print(f"Welcome {username}!")

