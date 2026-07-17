def reverse_first_five_positions(items : list[int])->list[int]:
    return items[:5][::-1] + items[5:]






print(reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7,
8, 9, 10]))