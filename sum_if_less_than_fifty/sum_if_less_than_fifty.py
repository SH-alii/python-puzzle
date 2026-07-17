



def sum_if_less_than_fifty(input_1: int, input_2: int )-> int | None:
    total = input_1 + input_2
    if(total < 50):
        return total
    else:
        return None
    
    
print(sum_if_less_than_fifty(30, 10))

print(sum_if_less_than_fifty(40, 10))