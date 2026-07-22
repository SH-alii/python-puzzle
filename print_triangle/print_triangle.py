def print_triangle(symbol: str, level: int):
    shape = ''
    for i in range(1, level + 1):
        shape += ' ' * (level - i) + symbol * (2 * i - 1) + '\n'
    print(shape)

print_triangle("*", 5)
