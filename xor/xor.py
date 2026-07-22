def xor(input_a: str, input_b: str)-> str:
    dict = {
        ('0', '0'): '0',
        ('0', '1'): '1',
        ('1', '0'): '1',
        ('1', '1'): '0'
        
    }
    new_string = ''
    
    for input_1, input_2 in zip(input_a, input_b):
            new_string += dict[(input_1, input_2)]

    
    return new_string
   
    

    
print(xor("1111","0000000"))