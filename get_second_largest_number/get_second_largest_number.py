def get_second_largest_number(list2: list[int])-> int | None:
    
    newList =  sorted(set(list2), reverse=True)
    
    if(len(newList) < 2):
        return None
    return newList[1]
    
    
    
print(get_second_largest_number([1]))