leap_normal = input()
holidays = int(input())
weekends = int(input())

number_of_games = ((48-weekends) * 3/4) + weekends + (holidays * 2/3)
if leap_normal == "leap":
    number_of_games += number_of_games * 0.15

print(int(number_of_games))
