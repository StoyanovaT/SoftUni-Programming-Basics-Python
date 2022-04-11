days = int(input())
room_type = str(input())
rating = str(input())
room_price = 0

if room_type == "room for one person":
    room_price = 18 * (days - 1)
    if rating == "positive":
        room_price += room_price * 0.25
    elif rating == "negative":
        room_price -= room_price * 0.10

elif room_type == "apartment":
    room_price = 25 * (days - 1)

    if days < 10 and rating == "positive":
        room_price -= room_price * 0.30
        room_price += room_price * 0.25
    elif days < 10 and rating == "negative":
        room_price -= room_price * 0.30
        room_price -= room_price * 0.10

    elif 10 <= days <= 15 and rating == "positive":
        room_price -= room_price * 0.35
        room_price += room_price * 0.25
    elif 10 <= days <= 15 and rating == "negative":
        room_price -= room_price * 0.35
        room_price -= room_price * 0.10

    elif days > 15 and rating == "positive":
        room_price -= room_price * 0.50
        room_price += room_price * 0.25
    elif days > 15 and rating == "negative":
        room_price -= room_price * 0.50
        room_price -= room_price * 0.10

elif room_type == "president apartment":
    room_price = 35 * (days - 1)

    if days < 10 and rating == "positive":
        room_price -= room_price * 0.10
        room_price += room_price * 0.25
    elif days < 10 and rating == "negative":
        room_price -= room_price * 0.10
        room_price -= room_price * 0.10

    elif 10 <= days <= 15 and rating == "positive":
        room_price -= room_price * 0.55
        room_price += room_price * 0.25
    elif 10 <= days <= 15 and rating == "negative":
        room_price -= room_price * 0.55
        room_price -= room_price * 0.10

    elif days > 15 and rating == "positive":
        room_price -= room_price * 0.20
        room_price += room_price * 0.25
    elif days > 15 and rating == "negative":
        room_price -= room_price * 0.20
        room_price -= room_price * 0.10

print(f"{room_price:.02f}")
