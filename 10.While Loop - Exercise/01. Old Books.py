searched_book = input()
checked_books = 0
book = input()

while book != "No More Books":
    if searched_book == book:
        print(f"You checked {checked_books} books and found it.")
        break
    checked_books += 1
    book = input()

else:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")

# Решение на лектора:
# wanted_book = input()
# books_counter = 0
#
# while True:
#     current_name_of_book = input()
#
#     if current_name_of_book == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {books_counter} books.")
#         break
#
#     elif current_name_of_book == wanted_book:
#         print(f"You checked {books_counter} books and found it.")
#         break
#
#     books_counter += 1