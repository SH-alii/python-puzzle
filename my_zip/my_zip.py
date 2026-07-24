def my_zip(input_list_a: list[any], input_list_b: list[any])->list[any]:
    newlist = []
    smaller_array_length = len(input_list_a) if len(input_list_a) <= len(input_list_b) else len(input_list_b)     
    for i in range(0,smaller_array_length,1):
            newlist.append((input_list_a[i], input_list_b[i]))
          
    return newlist


def recursive_my_zip(input_list_a: list[any], input_list_b: list[any])->list[any]:
    smaller_array = input_list_a if len(input_list_a) <= len(input_list_b) else input_list_b
 
    
print(my_zip([1,4, 5],[2, 4]))  
            
             