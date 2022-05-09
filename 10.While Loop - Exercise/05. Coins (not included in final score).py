money_back = int(float(input()) * 100)
coins = 0

while money_back > 0:
    coins += 1

    if money_back >= 200:
        money_back -= 200

    elif money_back >= 100:
        money_back -= 100

    elif money_back >= 50:
        money_back -= 50

    elif money_back >= 20:
        money_back -= 20

    elif money_back >= 10:
        money_back -= 10

    elif money_back >= 5:
        money_back -= 5

    elif money_back >= 2:
        money_back -= 2

    elif money_back <= 1:
        money_back -= 1

print(coins)