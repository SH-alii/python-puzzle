def my_zip(input_list_a: list[any], input_list_b: list[any])->list[any]:
    newlist = []
    if len(input_list_a) <= len(input_list_b):
        for i in range(0,len(input_list_a),1):
            newlist.append((input_list_a[i], input_list_b[i]))
    else: 
        for i in range(0,len(input_list_b),1):
            newlist.append((input_list_a[i], input_list_b[i]))        
    return newlist


print(my_zip([1,2,3,4],[5,6]))  
            
            