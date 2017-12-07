import decimal

def math_func(base, multiplier, rolls):
    reverse_rolls = 1
    print("Roll #1: ", base)
    while rolls > 0:
        increase = base * multiplier
        base = base + increase
        rolls -= 1
        reverse_rolls += 1
        print("Roll #{}: ".format(reverse_rolls), base)


base = decimal.Decimal(input("Enter the base bet: "))
multiplier = decimal.Decimal(input("Enter the multiplier: "))
rolls = int(input("Enter the amount of rolls: "))

math_func(base, multiplier, rolls)
