def math_func(base, multiplier, rolls):
    reverse_rolls = 0
    while rolls > 0:
        increase = base * multiplier
        base = base + increase
        rolls -= 1
        reverse_rolls += 1
        print("Roll #{}: ".format(reverse_rolls), base)

math_func(0.000014, 3.04615, 15)
