


def filter_strings_containing_a(input_str: list[str])-> list[str]:
    sorted_array = []
    for value in input_str:
        if("a" in value):
            sorted_array.append(value)
            
    return sorted_array
            
            
            
print(filter_strings_containing_a(['apple', 'banna', 'cherry', 'date']))
            
print(filter_strings_containing_a(['pple', 'right', 'cherry', 'dte']))      
