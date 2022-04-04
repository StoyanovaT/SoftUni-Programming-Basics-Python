book_pages = int(input())
reading_pages_per_hour = int(input())
number_of_days = int(input())
hours_needed_for_book = book_pages / reading_pages_per_hour
hours_per_day = hours_needed_for_book / number_of_days
print(hours_per_day)
