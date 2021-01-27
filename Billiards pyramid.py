def pyramid(balls):
    return int(((8 * balls + 1) ** .5 - 1) // 2)


print(pyramid(20))