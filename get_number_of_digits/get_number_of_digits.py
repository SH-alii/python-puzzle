def get_number_of_digits(number: int, total: int)-> int:
     
    number = abs(number)
    
    if(number + 0 == 0):
        return total
    else:
      if(number + 0 > 0):
          return get_number_of_digits(number // 10, total + 1)
          
          
total = 0         
print(get_number_of_digits(-123456, total))